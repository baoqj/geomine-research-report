#!/usr/bin/env python3
"""Build ArcGIS GeometryServer payloads and summarize exact tenure difference outputs."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

WINDOWS = {
    "sr": ("South Rae / Hearne margin south of MacKay", (-113.0, 61.3, -108.0, 63.5)),
    "es": ("East Slave Lac de Gras-MacKay-McCrea", (-112.0, 63.2, -107.5, 65.2)),
    "cs": ("Central Slave Indin-Colomac-Courageous", (-116.5, 63.8, -112.0, 65.8)),
}


def load(path: Path) -> dict:
    with path.open() as f:
        return json.load(f)


def bbox_polygon(bbox):
    minx, miny, maxx, maxy = bbox
    return {
        "rings": [
            [
                [minx, miny],
                [maxx, miny],
                [maxx, maxy],
                [minx, maxy],
                [minx, miny],
            ]
        ]
    }


def write_payloads():
    for code, (_, bbox) in WINDOWS.items():
        geoms = []
        for layer in ("claims", "leases", "permits"):
            data = load(RAW / f"{code}_{layer}.json")
            for ft in data.get("features", []):
                rings = (ft.get("geometry") or {}).get("rings")
                if rings:
                    geoms.append({"rings": rings})
        with (OUT / f"{code}_active_tenure_union_input.json").open("w") as f:
            json.dump({"geometryType": "esriGeometryPolygon", "geometries": geoms}, f)
        with (OUT / f"{code}_bbox_geometry_input.json").open("w") as f:
            json.dump({"geometryType": "esriGeometryPolygon", "geometries": [bbox_polygon(bbox)]}, f)


def build_difference_params():
    for code in WINDOWS:
        union_path = OUT / f"{code}_active_tenure_union.json"
        if not union_path.exists():
            continue
        data = load(union_path)
        geom = data.get("geometry")
        if geom:
            with (OUT / f"{code}_active_tenure_union_param.json").open("w") as f:
                json.dump({"geometryType": "esriGeometryPolygon", "geometry": geom}, f)


def signed_area_km2(ring, lat0):
    r = 6371.0088
    pts = []
    for lon, lat in ring:
        x = math.radians(lon) * r * math.cos(math.radians(lat0))
        y = math.radians(lat) * r
        pts.append((x, y))
    total = 0.0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        total += x1 * y2 - x2 * y1
    return total / 2.0


def polygon_area_km2(geom, lat0):
    return abs(sum(signed_area_km2(ring, lat0) for ring in geom.get("rings", [])))


def summarize():
    rows = []
    for code, (name, bbox) in WINDOWS.items():
        lat0 = (bbox[1] + bbox[3]) / 2
        bbox_area = polygon_area_km2(bbox_polygon(bbox), lat0)
        union_path = OUT / f"{code}_active_tenure_union.json"
        diff_path = OUT / f"{code}_open_ground_difference.json"
        union_area = None
        open_area = None
        open_parts = None
        if union_path.exists():
            union_area = polygon_area_km2(load(union_path).get("geometry", {}), lat0)
        if diff_path.exists():
            diff = load(diff_path)
            geoms = diff.get("geometries", [])
            open_parts = sum(len(g.get("rings", [])) for g in geoms)
            open_area = sum(polygon_area_km2(g, lat0) for g in geoms)
        rows.append(
            {
                "code": code,
                "window": name,
                "bbox_wgs84": ",".join(map(str, bbox)),
                "bbox_area_km2_approx": round(bbox_area, 1),
                "active_tenure_union_area_intersecting_bbox_km2_approx": None if union_area is None else round(union_area, 1),
                "open_ground_area_km2_approx": None if open_area is None else round(open_area, 1),
                "active_tenure_area_inside_bbox_km2_approx": None if open_area is None else round(bbox_area - open_area, 1),
                "open_ground_pct_approx": None if open_area is None else round(open_area / bbox_area * 100, 1),
                "open_polygon_ring_parts": open_parts,
            }
        )
    with (OUT / "exact_tenure_difference_summary.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print("wrote", OUT / "exact_tenure_difference_summary.csv")


if __name__ == "__main__":
    write_payloads()
    build_difference_params()
    summarize()
