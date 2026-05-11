#!/usr/bin/env python3
"""Grid-based tenure-clear screening for NWT gold follow-up.

This deliberately avoids pretending to perform legal parcel subtraction. It
classifies 0.10 x 0.05 degree cells as tenure-clear only when no active claim,
lease, or prospecting-permit polygon intersects the cell using local geometry
tests on the official ArcGIS REST geometries.
"""

from __future__ import annotations

import csv
import glob
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

WINDOWS = {
    "South Rae / Hearne margin south of MacKay": {
        "code": "sr",
        "bbox": (-113.0, 61.3, -108.0, 63.5),
        "belt_weight": 10,
    },
    "East Slave Lac de Gras-MacKay-McCrea": {
        "code": "es",
        "bbox": (-112.0, 63.2, -107.5, 65.2),
        "belt_weight": 8,
    },
    "Central Slave Indin-Colomac-Courageous": {
        "code": "cs",
        "bbox": (-116.5, 63.8, -112.0, 65.8),
        "belt_weight": 8,
    },
}

KNOWN_CORES = [
    ("Colomac", -115.0878, 64.3992),
    ("Tundra", -111.1744, 64.0400),
    ("Salmita", -111.2411, 64.0750),
    ("Courageous Lake showing", -111.3600, 64.2544),
]


def load_json(path: Path) -> dict:
    with path.open() as f:
        return json.load(f)


def ring_bbox(ring: list[list[float]]) -> tuple[float, float, float, float]:
    xs = [p[0] for p in ring]
    ys = [p[1] for p in ring]
    return min(xs), min(ys), max(xs), max(ys)


def bbox_overlap(a, b) -> bool:
    return not (a[2] < b[0] or a[0] > b[2] or a[3] < b[1] or a[1] > b[3])


def point_in_ring(x: float, y: float, ring: list[list[float]]) -> bool:
    inside = False
    j = len(ring) - 1
    for i in range(len(ring)):
        xi, yi = ring[i]
        xj, yj = ring[j]
        if (yi > y) != (yj > y):
            x_intersect = (xj - xi) * (y - yi) / ((yj - yi) or 1e-12) + xi
            if x < x_intersect:
                inside = not inside
        j = i
    return inside


def ccw(a, b, c) -> bool:
    return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])


def segments_intersect(a, b, c, d) -> bool:
    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)


def ring_intersects_cell(ring: list[list[float]], cell_bbox) -> bool:
    if not bbox_overlap(ring_bbox(ring), cell_bbox):
        return False
    minx, miny, maxx, maxy = cell_bbox
    corners = [(minx, miny), (minx, maxy), (maxx, miny), (maxx, maxy)]
    if any(point_in_ring(x, y, ring) for x, y in corners):
        return True
    if any(minx <= x <= maxx and miny <= y <= maxy for x, y in ring):
        return True
    edges = [
        ((minx, miny), (maxx, miny)),
        ((maxx, miny), (maxx, maxy)),
        ((maxx, maxy), (minx, maxy)),
        ((minx, maxy), (minx, miny)),
    ]
    for i in range(len(ring) - 1):
        seg = (tuple(ring[i]), tuple(ring[i + 1]))
        if any(segments_intersect(seg[0], seg[1], edge[0], edge[1]) for edge in edges):
            return True
    return False


def point_in_polygon_rings(x: float, y: float, rings: list[list[list[float]]]) -> bool:
    return any(point_in_ring(x, y, ring) for ring in rings)


def haversine_km(lon1, lat1, lon2, lat2) -> float:
    r = 6371.0088
    p1 = math.radians(lat1)
    p2 = math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def cell_area_km2(minx, miny, maxx, maxy) -> float:
    mid_lat = math.radians((miny + maxy) / 2)
    km_per_deg_lat = 111.32
    km_per_deg_lon = 111.32 * math.cos(mid_lat)
    return abs((maxx - minx) * km_per_deg_lon * (maxy - miny) * km_per_deg_lat)


def load_tenure(code: str):
    rings = []
    counts = {}
    for layer in ("claims", "leases", "permits"):
        data = load_json(RAW / f"{code}_{layer}.json")
        features = data.get("features", [])
        counts[layer] = len(features)
        for ft in features:
            geom = ft.get("geometry") or {}
            for ring in geom.get("rings", []):
                if len(ring) >= 4:
                    rings.append({"layer": layer, "ring": ring, "bbox": ring_bbox(ring)})
    return rings, counts


def webmerc_to_lonlat(x, y):
    r = 6378137.0
    lon = x / r * 180 / math.pi
    lat = (2 * math.atan(math.exp(y / r)) - math.pi / 2) * 180 / math.pi
    return lon, lat


def load_gold_showings():
    rows = []
    for path in [RAW / "nwt_gold_showings_0.json", RAW / "nwt_gold_showings_1000.json"]:
        for ft in load_json(path).get("features", []):
            a = ft.get("attributes", {})
            try:
                lon = float(a.get("LONGITUDE"))
                lat = float(a.get("LATITUDE"))
            except (TypeError, ValueError):
                continue
            stage = a.get("DEV_STAGE") or ""
            rows.append(
                {
                    "lon": lon,
                    "lat": lat,
                    "name": a.get("NAME") or "",
                    "stage": stage,
                    "showing_id": a.get("SHOWING_ID") or "",
                    "drilled": "drill" in stage.lower(),
                    "advanced": "advanced" in stage.lower(),
                    "producer": "producer" in stage.lower(),
                }
            )
    return rows


def load_till_au_ppb():
    rows = []
    for path in sorted(RAW.glob("nwt_till_au_*.json")):
        for ft in load_json(path).get("features", []):
            a = ft.get("attributes", {})
            if (a.get("C_ELEMENT1") or "").lower() != "ppb":
                continue
            try:
                value = float(a.get("C_ELEMENT_"))
            except (TypeError, ValueError):
                continue
            geom = ft.get("geometry") or {}
            if "x" not in geom or "y" not in geom:
                continue
            lon, lat = webmerc_to_lonlat(geom["x"], geom["y"])
            rows.append(
                {
                    "lon": lon,
                    "lat": lat,
                    "au_ppb": value,
                    "sample": a.get("C_SAMPLE") or "",
                    "report": a.get("C_REPORT_I") or "",
                }
            )
    return rows


def in_bbox(point, bbox) -> bool:
    lon, lat = point
    return bbox[0] <= lon <= bbox[2] and bbox[1] <= lat <= bbox[3]


def nearest_distance(lon, lat, rows):
    if not rows:
        return None
    return min(haversine_km(lon, lat, row["lon"], row["lat"]) for row in rows)


def score_cell(metrics, window_weight):
    if not metrics["tenure_clear"]:
        return 0
    score = window_weight
    max_au = metrics["max_au_ppb"] or 0
    if max_au >= 1000:
        score += 35
    elif max_au >= 300:
        score += 30
    elif max_au >= 100:
        score += 24
    elif max_au >= 40:
        score += 18
    elif max_au >= 15:
        score += 10
    elif max_au >= 5:
        score += 4

    high_au_km = metrics["nearest_high_au_km"]
    if high_au_km is not None:
        if high_au_km <= 5:
            score += 20
        elif high_au_km <= 10:
            score += 14
        elif high_au_km <= 20:
            score += 7

    drilled_km = metrics["nearest_drilled_or_advanced_km"]
    if drilled_km is not None:
        if drilled_km <= 5:
            score += 14
        elif drilled_km <= 10:
            score += 9
        elif drilled_km <= 20:
            score += 5

    score += min(10, metrics["gold_showings_in_cell"] * 3)
    score += min(8, metrics["au_sample_count"] // 2)
    if metrics["near_known_core_km"] is not None and metrics["near_known_core_km"] < 5:
        score -= 20
    return max(0, min(100, score))


def main():
    showings = load_gold_showings()
    till = load_till_au_ppb()
    high_au = [row for row in till if row["au_ppb"] >= 110]
    drilled_or_advanced = [row for row in showings if row["drilled"] or row["advanced"] or row["producer"]]

    summaries = []
    candidate_rows = []
    geojson_features = []
    anomaly_rows = []

    dx, dy = 0.10, 0.05
    for window_name, cfg in WINDOWS.items():
        code = cfg["code"]
        bbox = cfg["bbox"]
        rings, counts = load_tenure(code)
        cells_total = cells_clear = 0
        area_total = area_clear = 0.0

        lon = bbox[0]
        while lon < bbox[2] - 1e-9:
            lat = bbox[1]
            while lat < bbox[3] - 1e-9:
                cell = (lon, lat, min(lon + dx, bbox[2]), min(lat + dy, bbox[3]))
                center = ((cell[0] + cell[2]) / 2, (cell[1] + cell[3]) / 2)
                area = cell_area_km2(*cell)
                intersects = any(ring_intersects_cell(r["ring"], cell) for r in rings)

                au_in = [row for row in till if in_bbox((row["lon"], row["lat"]), cell)]
                show_in = [row for row in showings if in_bbox((row["lon"], row["lat"]), cell)]
                core_dist = nearest_distance(center[0], center[1], [{"lon": c[1], "lat": c[2]} for c in KNOWN_CORES])
                metrics = {
                    "tenure_clear": not intersects,
                    "max_au_ppb": max([row["au_ppb"] for row in au_in], default=None),
                    "au_sample_count": len(au_in),
                    "gold_showings_in_cell": len(show_in),
                    "drilled_showings_in_cell": sum(1 for row in show_in if row["drilled"]),
                    "advanced_showings_in_cell": sum(1 for row in show_in if row["advanced"]),
                    "nearest_high_au_km": nearest_distance(center[0], center[1], high_au),
                    "nearest_drilled_or_advanced_km": nearest_distance(center[0], center[1], drilled_or_advanced),
                    "near_known_core_km": core_dist,
                }
                score = score_cell(metrics, cfg["belt_weight"])
                cells_total += 1
                area_total += area
                if not intersects:
                    cells_clear += 1
                    area_clear += area
                if not intersects and score >= 25:
                    row = {
                        "window": window_name,
                        "cell_id": f"{code}_{cell[0]:.2f}_{cell[1]:.2f}",
                        "min_lon": round(cell[0], 5),
                        "min_lat": round(cell[1], 5),
                        "max_lon": round(cell[2], 5),
                        "max_lat": round(cell[3], 5),
                        "center_lon": round(center[0], 5),
                        "center_lat": round(center[1], 5),
                        "area_km2": round(area, 2),
                        "score": score,
                        **{
                            k: (round(v, 2) if isinstance(v, float) else v)
                            for k, v in metrics.items()
                        },
                    }
                    candidate_rows.append(row)
                    polygon = [
                        [cell[0], cell[1]],
                        [cell[2], cell[1]],
                        [cell[2], cell[3]],
                        [cell[0], cell[3]],
                        [cell[0], cell[1]],
                    ]
                    geojson_features.append(
                        {
                            "type": "Feature",
                            "properties": row,
                            "geometry": {"type": "Polygon", "coordinates": [polygon]},
                        }
                    )
                lat += dy
            lon += dx

        summaries.append(
            {
                "window": window_name,
                "bbox_wgs84": ",".join(map(str, bbox)),
                "active_claims": counts["claims"],
                "active_leases": counts["leases"],
                "active_permits": counts["permits"],
                "grid_cells_total": cells_total,
                "tenure_clear_cells": cells_clear,
                "tenure_clear_cell_pct": round(cells_clear / cells_total * 100, 1),
                "approx_window_area_km2": round(area_total, 1),
                "approx_tenure_clear_grid_area_km2": round(area_clear, 1),
            }
        )

        for row in sorted([r for r in till if in_bbox((r["lon"], r["lat"]), bbox)], key=lambda r: r["au_ppb"], reverse=True)[:20]:
            inside_tenure = any(point_in_polygon_rings(row["lon"], row["lat"], [r["ring"]]) for r in rings)
            nearest_open = None
            for cand in candidate_rows:
                if cand["window"] != window_name:
                    continue
                dist = haversine_km(row["lon"], row["lat"], cand["center_lon"], cand["center_lat"])
                nearest_open = dist if nearest_open is None else min(nearest_open, dist)
            anomaly_rows.append(
                {
                    "window": window_name,
                    "sample": row["sample"],
                    "report": row["report"],
                    "au_ppb": row["au_ppb"],
                    "lon": round(row["lon"], 5),
                    "lat": round(row["lat"], 5),
                    "inside_active_tenure_polygon": inside_tenure,
                    "nearest_ranked_tenure_clear_cell_km": None if nearest_open is None else round(nearest_open, 2),
                }
            )

    candidate_rows.sort(key=lambda r: r["score"], reverse=True)
    geojson_features.sort(key=lambda f: f["properties"]["score"], reverse=True)
    geojson_features = geojson_features[:250]

    with (OUT / "window_tenure_grid_summary.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(summaries[0].keys()))
        writer.writeheader()
        writer.writerows(summaries)

    with (OUT / "top_candidate_cells.csv").open("w", newline="") as f:
        fieldnames = list(candidate_rows[0].keys()) if candidate_rows else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(candidate_rows[:250])

    with (OUT / "ranked_open_cells.geojson").open("w") as f:
        json.dump({"type": "FeatureCollection", "features": geojson_features}, f, indent=2)

    with (OUT / "anomaly_tenure_trace.csv").open("w", newline="") as f:
        fieldnames = list(anomaly_rows[0].keys()) if anomaly_rows else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(anomaly_rows)

    print("summaries", len(summaries))
    print("candidate_rows", len(candidate_rows))
    print("geojson_features", len(geojson_features))
    print("anomaly_rows", len(anomaly_rows))


if __name__ == "__main__":
    main()
