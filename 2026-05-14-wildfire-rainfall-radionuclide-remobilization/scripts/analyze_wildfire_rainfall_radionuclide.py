#!/usr/bin/env python3
"""Reproducible screening analysis for wildfire/rainfall radionuclide remobilization.

The script intentionally avoids non-standard GIS/plotting dependencies so that the
paper package remains runnable in a minimal Python environment. Spatial operations
are screening-grade: fire polygons are not clipped to the AOI, and distances are
approximated from polygon rings after an explicit point-in-polygon check.
"""

from __future__ import annotations

import csv
import json
import math
import re
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "figures"
MODELS = ROOT / "models"

AOI = {
    "name": "Athabasca Basin uranium mining district screening AOI",
    "west": -107.0,
    "east": -102.0,
    "south": 56.5,
    "north": 59.0,
    "crs": "EPSG:4326",
}

R_EARTH_KM = 6371.0088
SVG_NS = "http://www.w3.org/2000/svg"


def ensure_dirs() -> None:
    for path in (PROCESSED, FIGURES, MODELS):
        path.mkdir(parents=True, exist_ok=True)


def parse_float(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value).strip()
    if not s or s.upper() in {"NA", "N/A", "NRM | NRS", "ND", "NULL"}:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def parse_date(value: Any) -> date | None:
    if not value:
        return None
    s = str(value).replace("Z", "").strip()
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(s[:19] if " " in s else s[:10], fmt).date()
        except ValueError:
            continue
    return None


def haversine_km(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = phi2 - phi1
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R_EARTH_KM * math.asin(math.sqrt(a))


def flatten_rings(geometry: dict[str, Any]) -> list[list[list[float]]]:
    if not geometry:
        return []
    gtype = geometry.get("type")
    coords = geometry.get("coordinates", [])
    if gtype == "Polygon":
        return coords
    if gtype == "MultiPolygon":
        rings: list[list[list[float]]] = []
        for polygon in coords:
            rings.extend(polygon)
        return rings
    return []


def ring_bbox(ring: list[list[float]]) -> tuple[float, float, float, float]:
    xs = [p[0] for p in ring]
    ys = [p[1] for p in ring]
    return min(xs), min(ys), max(xs), max(ys)


def point_in_ring(lon: float, lat: float, ring: list[list[float]]) -> bool:
    inside = False
    n = len(ring)
    if n < 3:
        return False
    j = n - 1
    for i in range(n):
        xi, yi = ring[i][0], ring[i][1]
        xj, yj = ring[j][0], ring[j][1]
        if (yi > lat) != (yj > lat):
            x_intersect = (xj - xi) * (lat - yi) / ((yj - yi) or 1e-12) + xi
            if lon < x_intersect:
                inside = not inside
        j = i
    return inside


def point_in_geometry(lon: float, lat: float, rings: list[list[list[float]]]) -> bool:
    # Screening rule: exterior-ring hit is enough for proximity analysis. Holes
    # are not material for mine-to-fire distance screening at this scale.
    for ring in rings:
        west, south, east, north = ring_bbox(ring)
        if west <= lon <= east and south <= lat <= north and point_in_ring(lon, lat, ring):
            return True
    return False


def point_to_geometry_distance_km(lon: float, lat: float, rings: list[list[list[float]]]) -> float:
    if not rings:
        return float("nan")
    if point_in_geometry(lon, lat, rings):
        return 0.0
    best = float("inf")
    for ring in rings:
        if not ring:
            continue
        step = max(1, len(ring) // 500)
        for x, y, *_ in ring[::step]:
            d = haversine_km(lon, lat, x, y)
            if d < best:
                best = d
    return best


def coord_to_xy(lon: float, lat: float, width: int, height: int, margin: int = 52) -> tuple[float, float]:
    x = margin + (lon - AOI["west"]) / (AOI["east"] - AOI["west"]) * (width - 2 * margin)
    y = height - margin - (lat - AOI["south"]) / (AOI["north"] - AOI["south"]) * (height - 2 * margin)
    return x, y


def svg_text(x: float, y: float, text: str, size: int = 12, anchor: str = "start", weight: str = "400", fill: str = "#222") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{escape(text)}</text>'
    )


def escape(text: Any) -> str:
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def save_svg(path: Path, width: int, height: int, body: list[str]) -> None:
    content = [
        f'<svg xmlns="{SVG_NS}" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        *body,
        "</svg>",
    ]
    path.write_text("\n".join(content), encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    if fieldnames is None:
        keys: list[str] = []
        for row in rows:
            for key in row:
                if key not in keys:
                    keys.append(key)
        fieldnames = keys
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def read_geojson(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def read_xlsx_first_sheet(path: Path) -> list[dict[str, str]]:
    ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

    def col_index(cell_ref: str) -> int:
        letters = re.match(r"[A-Z]+", cell_ref).group(0)  # type: ignore[union-attr]
        n = 0
        for ch in letters:
            n = n * 26 + ord(ch) - 64
        return n - 1

    with ZipFile(path) as z:
        strings: list[str] = []
        if "xl/sharedStrings.xml" in z.namelist():
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            for si in root.findall("a:si", ns):
                strings.append("".join(t.text or "" for t in si.findall(".//a:t", ns)))

        root = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
        raw_rows: list[dict[int, str]] = []
        for row in root.findall(".//a:row", ns):
            vals: dict[int, str] = {}
            for cell in row.findall("a:c", ns):
                v = cell.find("a:v", ns)
                val = "" if v is None else (v.text or "")
                if cell.attrib.get("t") == "s" and val:
                    val = strings[int(val)]
                vals[col_index(cell.attrib["r"])] = val
            if vals:
                raw_rows.append(vals)

    headers = [raw_rows[0].get(i, "") for i in range(max(raw_rows[0]) + 1)]
    rows: list[dict[str, str]] = []
    for raw in raw_rows[1:]:
        row = {headers[i]: raw.get(i, "") for i in range(len(headers))}
        rows.append(row)
    return rows


def load_cnsc_releases() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    path = RAW / "cnsc_uranium_mines_mills_radionuclide_loadings.xlsx"
    records = read_xlsx_first_sheet(path)
    out: list[dict[str, Any]] = []
    facilities: dict[str, dict[str, Any]] = {}
    for rec in records:
        year = int(rec["Year | Année"])
        facility = rec["Facility Name | Nom de l'installation"]
        lat = parse_float(rec["Latitude | Latitude"])
        lon = parse_float(rec["Longitude | Longitude"])
        substance = rec["Substance Name (English) | Nom de substance (Anglais)"]
        units = rec["Units | Unités"]
        direct = parse_float(rec["Direct Discharge | Évacuations directes"])
        stack = parse_float(rec["Stack Emissions | Émissions de cheminées"])
        row = {
            "year": year,
            "npri_id": rec["NPRI ID | ID INRP"],
            "company": rec["Company Name | Raison Sociale"],
            "facility": facility,
            "province": rec["Province | Province"],
            "latitude": lat,
            "longitude": lon,
            "substance": substance,
            "units": units,
            "stack_emissions": stack,
            "direct_discharge": direct,
        }
        out.append(row)
        if facility not in facilities and lat is not None and lon is not None:
            facilities[facility] = {
                "facility": facility,
                "company": row["company"],
                "latitude": lat,
                "longitude": lon,
                "npri_id": row["npri_id"],
            }
    return out, list(sorted(facilities.values(), key=lambda r: r["facility"]))


def load_nbac() -> list[dict[str, Any]]:
    data = read_geojson(RAW / "nbac_athabasca_bbox_1986_2024.geojson")
    fires: list[dict[str, Any]] = []
    for feature in data["features"]:
        p = feature["properties"]
        rings = flatten_rings(feature.get("geometry") or {})
        fire = {
            "gid": p.get("__gid") or f"{p.get('year')}_{p.get('nfireid')}",
            "year": int(p["year"]),
            "nfireid": p.get("nfireid"),
            "cause": p.get("firecaus"),
            "mapping_source": p.get("firemaps"),
            "poly_ha": float(p.get("poly_ha") or 0),
            "adj_ha": float(p.get("adj_ha") or 0),
            "start_date": parse_date(p.get("hs_sdate") or p.get("ag_sdate")),
            "end_date": parse_date(p.get("hs_edate") or p.get("ag_edate")),
            "version": p.get("version"),
            "rings": rings,
        }
        fires.append(fire)
    return fires


def load_climate() -> dict[date, dict[str, Any]]:
    data = read_geojson(RAW / "eccc_key_lake_daily_2020_2024.geojson")
    by_day: dict[date, dict[str, Any]] = {}
    station_ids = set()
    for feature in data["features"]:
        p = feature["properties"]
        day = parse_date(p.get("LOCAL_DATE"))
        if not day:
            continue
        station_ids.add(p.get("CLIMATE_IDENTIFIER"))
        precip = parse_float(p.get("TOTAL_PRECIPITATION"))
        rain = parse_float(p.get("TOTAL_RAIN"))
        temp = parse_float(p.get("MEAN_TEMPERATURE"))
        current = by_day.setdefault(
            day,
            {
                "date": day,
                "station_name": p.get("STATION_NAME"),
                "station_ids": set(),
                "precip_mm": None,
                "rain_mm": None,
                "mean_temperature_c": None,
            },
        )
        current["station_ids"].add(p.get("CLIMATE_IDENTIFIER"))
        # Co-located KEY LAKE station IDs are merged by using the higher daily
        # precipitation value, a conservative first-flush screening choice.
        if precip is not None:
            current["precip_mm"] = max(current["precip_mm"] or 0.0, precip)
        if rain is not None:
            current["rain_mm"] = max(current["rain_mm"] or 0.0, rain)
        if temp is not None:
            current["mean_temperature_c"] = temp if current["mean_temperature_c"] is None else (current["mean_temperature_c"] + temp) / 2
    for row in by_day.values():
        row["station_ids"] = ",".join(sorted(str(s) for s in row["station_ids"] if s))
    return by_day


def load_hydro() -> dict[date, dict[str, Any]]:
    data = read_geojson(RAW / "wsc_06DA004_daily_2020_2024.geojson")
    by_day: dict[date, dict[str, Any]] = {}
    for feature in data["features"]:
        p = feature["properties"]
        day = parse_date(p.get("DATE"))
        if not day:
            continue
        by_day[day] = {
            "date": day,
            "station_number": p.get("STATION_NUMBER"),
            "station_name": p.get("STATION_NAME"),
            "level_m": parse_float(p.get("LEVEL")),
            "discharge_m3_s": parse_float(p.get("DISCHARGE")),
            "discharge_symbol": p.get("DISCHARGE_SYMBOL_EN"),
            "longitude": feature["geometry"]["coordinates"][0],
            "latitude": feature["geometry"]["coordinates"][1],
        }
    return by_day


def load_hydro_stations() -> list[dict[str, Any]]:
    data = read_geojson(RAW / "wsc_hydrometric_stations_aoi.geojson")
    rows = []
    for feature in data["features"]:
        p = feature["properties"]
        rows.append(
            {
                "station_number": p.get("STATION_NUMBER"),
                "station_name": p.get("STATION_NAME"),
                "status": p.get("STATUS_EN"),
                "real_time": p.get("REAL_TIME"),
                "rhbn": p.get("RHBN"),
                "longitude": feature["geometry"]["coordinates"][0],
                "latitude": feature["geometry"]["coordinates"][1],
            }
        )
    return rows


def rolling_sum(values: dict[date, dict[str, Any]], start: date, days: int, field: str) -> float:
    total = 0.0
    for i in range(days):
        row = values.get(start + timedelta(days=i))
        if row and row.get(field) is not None:
            total += float(row[field])
    return total


def window_mean(values: dict[date, dict[str, Any]], start: date, days: int, field: str) -> float | None:
    xs: list[float] = []
    for i in range(days):
        row = values.get(start + timedelta(days=i))
        if row and row.get(field) is not None:
            xs.append(float(row[field]))
    return sum(xs) / len(xs) if xs else None


def max_in_window(values: dict[date, dict[str, Any]], start: date, days: int, field: str) -> float | None:
    xs: list[float] = []
    for i in range(days):
        row = values.get(start + timedelta(days=i))
        if row and row.get(field) is not None:
            xs.append(float(row[field]))
    return max(xs) if xs else None


def first_threshold_day(values: dict[date, dict[str, Any]], start: date, days: int, field: str, threshold: float) -> int | None:
    for i in range(days):
        row = values.get(start + timedelta(days=i))
        if row and row.get(field) is not None and float(row[field]) >= threshold:
            return i
    return None


def normalize_log(value: float | None, max_value: float | None) -> float:
    if value is None or max_value is None or max_value <= 0:
        return 0.0
    return math.log1p(max(value, 0.0)) / math.log1p(max_value)


def analyze() -> dict[str, Any]:
    ensure_dirs()
    releases, facilities = load_cnsc_releases()
    fires = load_nbac()
    climate = load_climate()
    hydro = load_hydro()
    hydro_stations = load_hydro_stations()

    write_csv(PROCESSED / "cnsc_releases_long.csv", releases)
    write_csv(PROCESSED / "facilities.csv", facilities)
    write_csv(PROCESSED / "wsc_hydrometric_stations_aoi.csv", hydro_stations)

    annual_fire: dict[int, dict[str, Any]] = defaultdict(lambda: {"year": None, "fire_count": 0, "total_poly_ha": 0.0, "natural_count": 0, "human_count": 0})
    for fire in fires:
        y = fire["year"]
        annual_fire[y]["year"] = y
        annual_fire[y]["fire_count"] += 1
        annual_fire[y]["total_poly_ha"] += fire["poly_ha"]
        cause = (fire.get("cause") or "").lower()
        if "natural" in cause:
            annual_fire[y]["natural_count"] += 1
        elif "human" in cause:
            annual_fire[y]["human_count"] += 1
    annual_rows = [annual_fire[y] for y in sorted(annual_fire)]
    write_csv(PROCESSED / "nbac_annual_summary.csv", annual_rows)

    climate_annual: list[dict[str, Any]] = []
    for y in sorted({d.year for d in climate}):
        year_days = [d for d in climate if d.year == y]
        precip = [climate[d]["precip_mm"] or 0.0 for d in year_days]
        station_ids = sorted({sid for d in year_days for sid in str(climate[d]["station_ids"]).split(",") if sid})
        climate_annual.append(
            {
                "year": y,
                "days": len(year_days),
                "total_precip_mm": round(sum(precip), 2),
                "max_daily_precip_mm": round(max(precip) if precip else 0.0, 2),
                "days_precip_ge_10mm": sum(1 for p in precip if p >= 10),
                "station_ids_merged": ",".join(station_ids),
            }
        )
    write_csv(PROCESSED / "eccc_key_lake_annual_precip_summary.csv", climate_annual)

    hydro_annual: list[dict[str, Any]] = []
    for y in sorted({d.year for d in hydro}):
        year_days = [d for d in hydro if d.year == y]
        q = [hydro[d]["discharge_m3_s"] for d in year_days if hydro[d]["discharge_m3_s"] is not None]
        hydro_annual.append(
            {
                "year": y,
                "days": len(year_days),
                "mean_discharge_m3_s": round(sum(q) / len(q), 3) if q else None,
                "max_discharge_m3_s": round(max(q), 3) if q else None,
                "ice_condition_days": sum(1 for d in year_days if hydro[d].get("discharge_symbol")),
            }
        )
    write_csv(PROCESSED / "wsc_06DA004_annual_discharge_summary.csv", hydro_annual)

    fire_exposures: list[dict[str, Any]] = []
    event_metrics: list[dict[str, Any]] = []
    for facility in facilities:
        lon = float(facility["longitude"])
        lat = float(facility["latitude"])
        best_by_year: dict[int, dict[str, Any]] = {}
        for fire in fires:
            dist = point_to_geometry_distance_km(lon, lat, fire["rings"])
            row = {
                "facility": facility["facility"],
                "year": fire["year"],
                "fire_gid": fire["gid"],
                "fire_start": fire["start_date"].isoformat() if fire["start_date"] else "",
                "fire_end": fire["end_date"].isoformat() if fire["end_date"] else "",
                "fire_poly_ha": round(fire["poly_ha"], 3),
                "distance_km": round(dist, 3),
                "fire_cause": fire["cause"],
            }
            current = best_by_year.get(fire["year"])
            if current is None or dist < current["distance_km"]:
                best_by_year[fire["year"]] = row
        fire_exposures.extend(best_by_year[y] for y in sorted(best_by_year))

    recent_exposures = [r for r in fire_exposures if int(r["year"]) >= 2020]
    max_recent_area = max((float(r["fire_poly_ha"]) for r in recent_exposures), default=1.0)

    for row in recent_exposures:
        start = parse_date(row["fire_start"])
        if not start:
            continue
        pre_q = window_mean(hydro, start - timedelta(days=7), 7, "discharge_m3_s")
        post_q = window_mean(hydro, start, 7, "discharge_m3_s")
        q_ratio = None
        if pre_q and post_q is not None:
            q_ratio = post_q / pre_q
        metric = {
            **row,
            "post_fire_p1_mm": round(rolling_sum(climate, start, 1, "precip_mm"), 2),
            "post_fire_p7_mm": round(rolling_sum(climate, start, 7, "precip_mm"), 2),
            "post_fire_p30_mm": round(rolling_sum(climate, start, 30, "precip_mm"), 2),
            "post_fire_max_daily_p30_mm": round(max_in_window(climate, start, 30, "precip_mm") or 0.0, 2),
            "first_day_ge_5mm_after_fire": first_threshold_day(climate, start, 30, "precip_mm", 5.0),
            "pre_fire_q7_m3_s": round(pre_q, 3) if pre_q is not None else None,
            "post_fire_q7_m3_s": round(post_q, 3) if post_q is not None else None,
            "post_pre_q7_ratio": round(q_ratio, 3) if q_ratio is not None else None,
        }
        event_metrics.append(metric)

    write_csv(PROCESSED / "facility_fire_exposure_by_year.csv", fire_exposures)
    write_csv(PROCESSED / "post_fire_event_metrics_2020_2024.csv", event_metrics)

    release_2024 = [r for r in releases if r["year"] == 2024]
    fac_substance_rows: list[dict[str, Any]] = []
    by_facility_2024: dict[str, dict[str, Any]] = defaultdict(dict)
    for r in release_2024:
        fac = r["facility"]
        substance = r["substance"]
        direct = r["direct_discharge"] or 0.0
        fac_substance_rows.append(
            {
                "facility": fac,
                "substance": substance,
                "units": r["units"],
                "direct_discharge": direct,
                "stack_emissions": r["stack_emissions"],
            }
        )
        by_facility_2024[fac][substance] = direct
    write_csv(PROCESSED / "cnsc_2024_facility_substance_summary.csv", fac_substance_rows)

    max_u = max((by_facility_2024[f].get("Uranium", 0.0) for f in by_facility_2024), default=0.0)
    max_activity = max(
        (
            sum(v for k, v in by_facility_2024[f].items() if k != "Uranium")
            for f in by_facility_2024
        ),
        default=0.0,
    )

    best_recent_event_by_fac: dict[str, dict[str, Any]] = {}
    for metric in event_metrics:
        fac = metric["facility"]
        dist = float(metric["distance_km"])
        current = best_recent_event_by_fac.get(fac)
        if current is None or dist < float(current["distance_km"]):
            best_recent_event_by_fac[fac] = metric

    risk_rows: list[dict[str, Any]] = []
    for facility in facilities:
        fac = facility["facility"]
        rels = by_facility_2024.get(fac, {})
        u_score = normalize_log(rels.get("Uranium", 0.0), max_u)
        activity_sum = sum(v for k, v in rels.items() if k != "Uranium")
        activity_score = normalize_log(activity_sum, max_activity)
        source_score = 0.4 * u_score + 0.6 * activity_score
        event = best_recent_event_by_fac.get(fac)
        if event:
            dist = float(event["distance_km"])
            area = float(event["fire_poly_ha"])
            fire_score = math.exp(-dist / 25.0) * normalize_log(area, max_recent_area)
            rain_score = min(1.0, 0.55 * (float(event["post_fire_p7_mm"]) / 30.0) + 0.45 * (float(event["post_fire_p30_mm"]) / 90.0))
            q_ratio = parse_float(event.get("post_pre_q7_ratio"))
            hydro_score = min(1.0, (q_ratio or 0.0) / 2.0)
            nearest_fire_year = event["year"]
            nearest_fire_distance = dist
        else:
            fire_score = rain_score = hydro_score = 0.0
            nearest_fire_year = ""
            nearest_fire_distance = None
        climate_trigger = 0.45 * fire_score + 0.35 * rain_score + 0.20 * hydro_score
        screening_index = source_score * climate_trigger
        risk_rows.append(
            {
                "facility": fac,
                "source_score": round(source_score, 3),
                "fire_score": round(fire_score, 3),
                "rain_score": round(rain_score, 3),
                "hydro_score": round(hydro_score, 3),
                "climate_trigger_score": round(climate_trigger, 3),
                "screening_index": round(screening_index, 3),
                "nearest_recent_fire_year": nearest_fire_year,
                "nearest_recent_fire_distance_km": round(nearest_fire_distance, 3) if nearest_fire_distance is not None else "",
                "uranium_direct_discharge_kg_2024": rels.get("Uranium", 0.0),
                "activity_direct_discharge_mbq_sum_2024": round(activity_sum, 3),
            }
        )
    risk_rows.sort(key=lambda r: r["screening_index"], reverse=True)
    write_csv(PROCESSED / "screening_risk_index.csv", risk_rows)

    model_spec = {
        "research_type": "radionuclide_transport",
        "scenario": "uranium_mine_surface_water_post_wildfire",
        "coupling_level": "HC",
        "active_processes": {
            "thermal": "indirect via fire severity and ash generation; no heat-transport equation solved",
            "hydrological": True,
            "mechanical": "erosion/sediment resuspension represented as empirical source terms",
            "chemical": True,
        },
        "aoi": AOI,
        "datasets": [
            "CWFIS NBAC fire polygons through version 20250506, WFS public:nbac",
            "ECCC climate-daily observations, KEY LAKE station IDs 4063753 and 4063757",
            "Water Survey of Canada HYDAT daily means, station 06DA004",
            "CNSC/Open Canada radionuclide releases, uranium mines and mills, NPRI format",
        ],
        "limitations": [
            "NBAC polygons are used as intersecting fires, not clipped fire area inside the AOI.",
            "Fire severity raster, DEM flow routing, water chemistry, sediment chemistry and site boundaries are not yet downloaded.",
            "The screening index is for research prioritization and sampling design only; it is not a dose calculation or regulatory risk finding.",
        ],
    }
    (PROCESSED / "model_spec.json").write_text(json.dumps(model_spec, ensure_ascii=False, indent=2), encoding="utf-8")

    make_figures(fires, annual_rows, climate, hydro, facilities, hydro_stations, fac_substance_rows, risk_rows, event_metrics)
    write_phreeqc_template()

    summary = {
        "facility_count": len(facilities),
        "nbac_fire_feature_count": len(fires),
        "nbac_year_min": min(f["year"] for f in fires),
        "nbac_year_max": max(f["year"] for f in fires),
        "key_lake_daily_records_after_merge": len(climate),
        "wsc_daily_records": len(hydro),
        "hydrometric_station_count": len(hydro_stations),
        "release_record_count": len(releases),
        "top_screening_facility": risk_rows[0]["facility"] if risk_rows else None,
        "top_screening_index": risk_rows[0]["screening_index"] if risk_rows else None,
    }
    (PROCESSED / "analysis_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def scale(value: float, minv: float, maxv: float, start: float, end: float) -> float:
    if maxv == minv:
        return (start + end) / 2
    return start + (value - minv) / (maxv - minv) * (end - start)


def make_figures(
    fires: list[dict[str, Any]],
    annual_rows: list[dict[str, Any]],
    climate: dict[date, dict[str, Any]],
    hydro: dict[date, dict[str, Any]],
    facilities: list[dict[str, Any]],
    hydro_stations: list[dict[str, Any]],
    fac_substance_rows: list[dict[str, Any]],
    risk_rows: list[dict[str, Any]],
    event_metrics: list[dict[str, Any]],
) -> None:
    make_study_area_map(fires, facilities, hydro_stations)
    make_annual_burned_area(annual_rows)
    make_fire_rainfall_discharge(climate, hydro, event_metrics)
    make_release_heatmap(fac_substance_rows)
    make_risk_index_chart(risk_rows)
    make_mechanism_diagram()
    make_theoretical_sensitivity()


def make_study_area_map(fires: list[dict[str, Any]], facilities: list[dict[str, Any]], hydro_stations: list[dict[str, Any]]) -> None:
    width, height = 980, 620
    body = [
        svg_text(30, 34, "Figure 1. Athabasca Basin uranium facilities and NBAC wildfire polygons", 18, weight="700"),
        svg_text(30, 56, "Screening AOI: lon -107 to -102, lat 56.5 to 59.0; fires shown for 2020-2024, source CWFIS WFS public:nbac.", 12, fill="#555"),
        '<rect x="52" y="72" width="876" height="496" fill="#f7fbff" stroke="#1f2933" stroke-width="1.2"/>',
    ]
    colors = {2020: "#f4a261", 2021: "#e76f51", 2022: "#d62828", 2023: "#8d0801", 2024: "#6a040f"}
    recent = [f for f in fires if 2020 <= f["year"] <= 2024]
    recent.sort(key=lambda f: f["poly_ha"], reverse=True)
    for fire in recent[:140]:
        color = colors.get(fire["year"], "#999")
        for ring in fire["rings"][:5]:
            if not ring:
                continue
            step = max(1, len(ring) // 180)
            points = []
            for lon, lat, *_ in ring[::step]:
                x, y = coord_to_xy(lon, lat, width, height)
                points.append(f"{x:.1f},{y:.1f}")
            if len(points) > 2:
                body.append(f'<polygon points="{" ".join(points)}" fill="{color}" fill-opacity="0.12" stroke="{color}" stroke-width="0.65" stroke-opacity="0.65"/>')

    for station in hydro_stations:
        x, y = coord_to_xy(float(station["longitude"]), float(station["latitude"]), width, height)
        body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.0" fill="#2563eb" stroke="#ffffff" stroke-width="1"/>')
    for facility in facilities:
        x, y = coord_to_xy(float(facility["longitude"]), float(facility["latitude"]), width, height)
        body.append(f'<path d="M{x:.1f},{y-8:.1f} L{x+7:.1f},{y+6:.1f} L{x-7:.1f},{y+6:.1f} Z" fill="#5b21b6" stroke="#ffffff" stroke-width="1.2"/>')
        body.append(svg_text(x + 9, y + 4, facility["facility"], 11, fill="#111827"))

    for lon in range(int(AOI["west"]), int(AOI["east"]) + 1):
        x, _ = coord_to_xy(lon, AOI["south"], width, height)
        body.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="72" y2="568" stroke="#cbd5e1" stroke-width="0.4"/>')
        body.append(svg_text(x, 588, f"{lon}°", 10, anchor="middle", fill="#475569"))
    for lat_i in [56.5, 57.0, 57.5, 58.0, 58.5, 59.0]:
        _, y = coord_to_xy(AOI["west"], lat_i, width, height)
        body.append(f'<line x1="52" x2="928" y1="{y:.1f}" y2="{y:.1f}" stroke="#cbd5e1" stroke-width="0.4"/>')
        body.append(svg_text(38, y + 4, f"{lat_i:g}°", 10, anchor="end", fill="#475569"))

    lx, ly = 732, 98
    body.append('<rect x="716" y="78" width="204" height="116" fill="#ffffff" stroke="#cbd5e1" rx="4"/>')
    body.append(svg_text(lx, ly, "Legend", 12, weight="700"))
    body.append('<path d="M733,116 L743,134 L723,134 Z" fill="#5b21b6"/>')
    body.append(svg_text(752, 130, "Uranium mine/mill facility", 11))
    body.append('<circle cx="733" cy="153" r="4" fill="#2563eb"/>')
    body.append(svg_text(752, 157, "WSC hydrometric station", 11))
    body.append('<rect x="724" y="170" width="18" height="12" fill="#e76f51" fill-opacity="0.28" stroke="#e76f51"/>')
    body.append(svg_text(752, 181, "NBAC fire polygon", 11))
    save_svg(FIGURES / "fig01_study_area_fire_facilities.svg", width, height, body)


def make_annual_burned_area(annual_rows: list[dict[str, Any]]) -> None:
    width, height = 980, 520
    margin = 70
    years = [int(r["year"]) for r in annual_rows]
    area = [float(r["total_poly_ha"]) for r in annual_rows]
    counts = [int(r["fire_count"]) for r in annual_rows]
    max_area = max(area) if area else 1
    max_count = max(counts) if counts else 1
    body = [
        svg_text(30, 34, "Figure 2. Annual NBAC fire exposure in the Athabasca screening AOI", 18, weight="700"),
        svg_text(30, 56, "Bars show total full-polygon area of fires intersecting the AOI; line shows feature count. Areas are not clipped to the AOI.", 12, fill="#555"),
        f'<line x1="{margin}" x2="{width-margin}" y1="{height-margin}" y2="{height-margin}" stroke="#111827"/>',
        f'<line x1="{margin}" x2="{margin}" y1="{margin}" y2="{height-margin}" stroke="#111827"/>',
    ]
    n = len(years)
    bar_w = (width - 2 * margin) / max(n, 1) * 0.72
    for i, (y, a, c) in enumerate(zip(years, area, counts)):
        x = margin + (i + 0.5) * (width - 2 * margin) / n
        bh = scale(a, 0, max_area, 0, height - 2 * margin)
        color = "#e76f51" if y >= 2020 else "#f4a261"
        body.append(f'<rect x="{x-bar_w/2:.1f}" y="{height-margin-bh:.1f}" width="{bar_w:.1f}" height="{bh:.1f}" fill="{color}" fill-opacity="0.75"/>')
        if y % 5 == 0 or y >= 2020:
            body.append(svg_text(x, height - margin + 18, str(y), 9, anchor="middle", fill="#374151"))
        cx = x
        cy = height - margin - scale(c, 0, max_count, 0, height - 2 * margin)
        body.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="2.8" fill="#111827"/>')
        if i > 0:
            px = margin + (i - 0.5) * (width - 2 * margin) / n
            pc = counts[i - 1]
            py = height - margin - scale(pc, 0, max_count, 0, height - 2 * margin)
            body.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{cx:.1f}" y2="{cy:.1f}" stroke="#111827" stroke-width="1.2"/>')
    for frac in [0, 0.25, 0.5, 0.75, 1.0]:
        y = height - margin - frac * (height - 2 * margin)
        val = max_area * frac / 1000
        body.append(f'<line x1="{margin-4}" x2="{width-margin}" y1="{y:.1f}" y2="{y:.1f}" stroke="#e5e7eb"/>')
        body.append(svg_text(margin - 8, y + 4, f"{val:,.0f}k ha", 10, anchor="end", fill="#374151"))
    body.append(svg_text(width - margin, margin - 18, "Fire count line", 11, anchor="end", fill="#111827"))
    body.append(svg_text(margin, height - 22, "Year", 11, fill="#374151"))
    save_svg(FIGURES / "fig02_annual_burned_area.svg", width, height, body)


def make_fire_rainfall_discharge(climate: dict[date, dict[str, Any]], hydro: dict[date, dict[str, Any]], event_metrics: list[dict[str, Any]]) -> None:
    width, height = 980, 540
    margin = 78
    start = date(2024, 6, 1)
    end = date(2024, 10, 1)
    days = [start + timedelta(days=i) for i in range((end - start).days + 1)]
    precip = [climate.get(d, {}).get("precip_mm") or 0.0 for d in days]
    discharge = [hydro.get(d, {}).get("discharge_m3_s") for d in days]
    q_vals = [q for q in discharge if q is not None]
    max_p = max(precip) if precip else 1.0
    max_q = max(q_vals) if q_vals else 1.0
    min_q = min(q_vals) if q_vals else 0.0
    body = [
        svg_text(30, 34, "Figure 3. Fire-rainfall-discharge timing, 2024 fire season", 18, weight="700"),
        svg_text(30, 56, "Key Lake daily precipitation is merged from station IDs 4063753/4063757; discharge is WSC 06DA004.", 12, fill="#555"),
        f'<line x1="{margin}" x2="{width-margin}" y1="{height-margin}" y2="{height-margin}" stroke="#111827"/>',
        f'<line x1="{margin}" x2="{margin}" y1="{margin}" y2="{height-margin}" stroke="#111827"/>',
        f'<line x1="{width-margin}" x2="{width-margin}" y1="{margin}" y2="{height-margin}" stroke="#111827"/>',
    ]
    plot_w = width - 2 * margin
    plot_h = height - 2 * margin
    for i, d in enumerate(days):
        x = margin + i / (len(days) - 1) * plot_w
        p = precip[i]
        bh = (p / max(max_p, 1.0)) * plot_h * 0.45
        if p > 0:
            body.append(f'<rect x="{x-2:.1f}" y="{height-margin-bh:.1f}" width="4" height="{bh:.1f}" fill="#38bdf8" fill-opacity="0.72"/>')
    q_points = []
    for i, d in enumerate(days):
        q = discharge[i]
        if q is None:
            continue
        x = margin + i / (len(days) - 1) * plot_w
        y = height - margin - scale(q, min_q, max_q, 0, plot_h * 0.88)
        q_points.append((x, y))
    for (x1, y1), (x2, y2) in zip(q_points, q_points[1:]):
        body.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#2563eb" stroke-width="2"/>')
    selected = [m for m in event_metrics if str(m["year"]) == "2024" and float(m["distance_km"]) <= 80]
    for m in selected[:10]:
        d = parse_date(m["fire_start"])
        if not d or not (start <= d <= end):
            continue
        x = margin + (d - start).days / (len(days) - 1) * plot_w
        body.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{margin}" y2="{height-margin}" stroke="#dc2626" stroke-width="1.1" stroke-dasharray="4 4"/>')
    for m in range(6, 11):
        d = date(2024, m, 1)
        x = margin + (d - start).days / (len(days) - 1) * plot_w
        body.append(svg_text(x, height - margin + 22, d.strftime("%b"), 10, anchor="middle", fill="#374151"))
    body.append(svg_text(30, margin + 10, f"Precip. max {max_p:.1f} mm d^-1", 11, fill="#0369a1"))
    body.append(svg_text(width - 30, margin + 10, f"Discharge {min_q:.1f}-{max_q:.1f} m3 s^-1", 11, anchor="end", fill="#1d4ed8"))
    body.append(svg_text(width - 30, margin + 30, "Red dashed lines: nearby 2024 fire start dates", 11, anchor="end", fill="#991b1b"))
    save_svg(FIGURES / "fig03_fire_rainfall_discharge_coupling.svg", width, height, body)


def make_release_heatmap(rows: list[dict[str, Any]]) -> None:
    facilities = sorted({r["facility"] for r in rows})
    substances = ["Uranium", "Thorium-230", "Radium-226", "Lead-210", "Polonium-210"]
    values: dict[tuple[str, str], float] = {}
    units: dict[str, str] = {}
    for r in rows:
        values[(r["facility"], r["substance"])] = float(r["direct_discharge"] or 0.0)
        units[r["substance"]] = r["units"]
    width, height = 980, 450
    left, top = 180, 86
    cell_w, cell_h = 128, 48
    max_by_sub = {s: max(values.get((f, s), 0.0) for f in facilities) for s in substances}
    body = [
        svg_text(30, 34, "Figure 4. 2024 CNSC direct-discharge source-term matrix", 18, weight="700"),
        svg_text(30, 56, "Values are normalized by substance for color; U is kg, decay-series radionuclides are MBq.", 12, fill="#555"),
    ]
    for j, s in enumerate(substances):
        body.append(svg_text(left + j * cell_w + cell_w / 2, top - 18, s.replace("-", "\n"), 11, anchor="middle", weight="700"))
        body.append(svg_text(left + j * cell_w + cell_w / 2, top - 4, units.get(s, ""), 10, anchor="middle", fill="#6b7280"))
    for i, f in enumerate(facilities):
        y = top + i * cell_h
        body.append(svg_text(left - 14, y + 30, f, 12, anchor="end", weight="700"))
        for j, s in enumerate(substances):
            x = left + j * cell_w
            v = values.get((f, s), 0.0)
            frac = normalize_log(v, max_by_sub.get(s, 0.0))
            red = int(255 - 70 * frac)
            green = int(245 - 170 * frac)
            blue = int(235 - 205 * frac)
            fill = f"rgb({red},{green},{blue})"
            body.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell_w-4}" height="{cell_h-4}" fill="{fill}" stroke="#ffffff"/>')
            label = f"{v:g}"
            body.append(svg_text(x + cell_w / 2 - 2, y + 29, label, 11, anchor="middle", fill="#111827"))
    save_svg(FIGURES / "fig04_cnsc_release_heatmap.svg", width, height, body)


def make_risk_index_chart(rows: list[dict[str, Any]]) -> None:
    width, height = 980, 460
    margin = 76
    max_idx = max(float(r["screening_index"]) for r in rows) if rows else 1
    body = [
        svg_text(30, 34, "Figure 5. Multi-source remobilization screening index", 18, weight="700"),
        svg_text(30, 56, "Index = source score x climate-trigger score; designed for research prioritization, not dose or compliance assessment.", 12, fill="#555"),
    ]
    chart_w = width - 2 * margin
    bar_h = 34
    for i, r in enumerate(rows):
        y = 92 + i * 60
        idx = float(r["screening_index"])
        w = (idx / max(max_idx, 1e-9)) * chart_w
        body.append(svg_text(margin - 14, y + 23, r["facility"], 12, anchor="end", weight="700"))
        body.append(f'<rect x="{margin}" y="{y}" width="{chart_w}" height="{bar_h}" fill="#f1f5f9"/>')
        body.append(f'<rect x="{margin}" y="{y}" width="{w:.1f}" height="{bar_h}" fill="#7c3aed" fill-opacity="0.82"/>')
        body.append(svg_text(margin + w + 8, y + 23, f"{idx:.3f}", 12, fill="#111827"))
        components = f"S={r['source_score']:.3f} F={r['fire_score']:.3f} P={r['rain_score']:.3f} H={r['hydro_score']:.3f}; nearest recent fire {r['nearest_recent_fire_distance_km']} km"
        body.append(svg_text(margin, y + 50, components, 10, fill="#64748b"))
    save_svg(FIGURES / "fig05_screening_risk_index.svg", width, height, body)


def make_mechanism_diagram() -> None:
    width, height = 1100, 620
    boxes = [
        ("Wildfire", 60, 120, "#ef4444", "vegetation loss\\nash generation\\nsoil heating"),
        ("Ash and soil source", 260, 120, "#f97316", "U-Th-Ra-Pb-Po-Cs\\nfine particles\\nDOC/alkalinity shift"),
        ("Extreme rainfall", 60, 330, "#0ea5e9", "first flush\\nrunoff pulse\\nTSS increase"),
        ("Hydrological transport", 260, 330, "#2563eb", "overland flow\\nstream/lake routing\\ndilution"),
        ("Geochemical partitioning", 520, 220, "#16a34a", "carbonate complexation\\nsorption/desorption\\nbarite/coprecipitation"),
        ("Exposure interface", 810, 220, "#7c3aed", "water intake\\nfish/wild foods\\nsediment/aerosol"),
    ]
    body = [
        svg_text(30, 36, "Figure 6. Mechanistic model for wildfire-rainfall radionuclide remobilization", 18, weight="700"),
        svg_text(30, 58, "The causal chain separates physical mobilization from geochemical speciation and exposure; each arrow maps to a measurable variable.", 12, fill="#555"),
    ]
    for title, x, y, color, text in boxes:
        body.append(f'<rect x="{x}" y="{y}" width="210" height="116" rx="6" fill="{color}" fill-opacity="0.11" stroke="{color}" stroke-width="2"/>')
        body.append(svg_text(x + 16, y + 28, title, 14, weight="700", fill="#111827"))
        for k, line in enumerate(text.split("\\n")):
            body.append(svg_text(x + 16, y + 55 + 19 * k, line, 12, fill="#374151"))
    arrows = [
        (270, 178, 260, 178),
        (165, 236, 165, 330),
        (270, 388, 260, 388),
        (470, 388, 520, 300),
        (470, 178, 520, 260),
        (730, 278, 810, 278),
    ]
    for x1, y1, x2, y2 in arrows:
        body.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#334155" stroke-width="2.2" marker-end="url(#arrow)"/>')
    body.insert(
        1,
        '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#334155"/></marker></defs>',
    )
    eqs = [
        "Event load: L_k = integral Q(t)[C_d,k(t)+TSS(t)C_p,k(t)]dt",
        "Retardation: R_k = 1 + rho_b K_d,k / theta",
        "U-carbonate fraction: alpha_j = beta_j a_CO3^j / (1 + sum beta_m a_CO3^m)",
    ]
    body.append('<rect x="70" y="500" width="960" height="78" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>')
    for i, eq in enumerate(eqs):
        body.append(svg_text(92, 526 + i * 19, eq, 12, fill="#111827"))
    save_svg(FIGURES / "fig06_mechanism_reactive_transport.svg", width, height, body)


def make_theoretical_sensitivity() -> None:
    width, height = 980, 520
    margin = 78
    body = [
        svg_text(30, 34, "Figure 7. Theoretical controls on dissolved versus particle-facilitated mobility", 18, weight="700"),
        svg_text(30, 56, "Curves are dimensionless theory plots, not calibrated field results. They show how Kd and suspended solids alter first-flush transport.", 12, fill="#555"),
        f'<line x1="{margin}" x2="{width-margin}" y1="{height-margin}" y2="{height-margin}" stroke="#111827"/>',
        f'<line x1="{margin}" x2="{margin}" y1="{margin}" y2="{height-margin}" stroke="#111827"/>',
    ]
    plot_w = width - 2 * margin
    plot_h = height - 2 * margin
    theta = 0.35
    rho_b = 1500.0  # kg m-3
    kd_values = [10 ** (-4 + i * 0.08) for i in range(76)]  # m3 kg-1
    colors = [("#2563eb", 0.05), ("#16a34a", 0.2), ("#dc2626", 1.0)]  # kg m-3 TSS
    for color, tss in colors:
        pts = []
        for kd in kd_values:
            mobile_fraction = (1 + kd * tss) / (1 + rho_b * kd / theta)
            x = margin + (math.log10(kd) + 4) / 6 * plot_w
            y = height - margin - scale(mobile_fraction, 0, 1.02, 0, plot_h)
            pts.append((x, y))
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            body.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="2"/>')
        body.append(svg_text(pts[-1][0] - 80, pts[-1][1] - 6, f"TSS={tss:g} kg m^-3", 11, fill=color))
    for log_kd in range(-4, 3):
        x = margin + (log_kd + 4) / 6 * plot_w
        body.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{margin}" y2="{height-margin}" stroke="#e5e7eb"/>')
        body.append(svg_text(x, height - margin + 20, f"1e{log_kd}", 10, anchor="middle", fill="#374151"))
    for frac in [0, 0.25, 0.5, 0.75, 1.0]:
        y = height - margin - frac * plot_h
        body.append(f'<line x1="{margin}" x2="{width-margin}" y1="{y:.1f}" y2="{y:.1f}" stroke="#e5e7eb"/>')
        body.append(svg_text(margin - 10, y + 4, f"{frac:.2f}", 10, anchor="end", fill="#374151"))
    body.append(svg_text(width / 2, height - 22, "Distribution coefficient Kd (m3 kg^-1)", 12, anchor="middle"))
    body.append(svg_text(18, height / 2, "Relative mobile load fraction", 12, anchor="middle"))
    save_svg(FIGURES / "fig07_theoretical_sensitivity.svg", width, height, body)


def write_phreeqc_template() -> None:
    text = """TITLE Wildfire ash leachate and stream-water mixing screen for uranium-mine settings
# Database recommendation: llnl.dat or minteq.v4.dat for uranium trace species,
# after verifying thermodynamic coverage and surface-complexation constants.
# This is a template: measured chemistry is required before execution is treated
# as evidence.

SOLUTION 1 Stream_water_baseline
    temp      <temperature_C>
    pH        <stream_pH>
    pe        <stream_pe_or_Eh_converted>
    units     mg/L
    Alkalinity <alkalinity_as_CaCO3_mg_L>
    Ca        <Ca_mg_L>
    Mg        <Mg_mg_L>
    Na        <Na_mg_L>
    K         <K_mg_L>
    S(6)      <SO4_mg_L> as SO4
    C(4)      <DIC_mg_L> as HCO3
    U         <U_ug_L> ug/L
END

SOLUTION 2 Ash_leachate_or_tailings_runoff
    temp      <temperature_C>
    pH        <ash_leachate_pH>
    pe        <ash_leachate_pe_or_Eh_converted>
    units     mg/L
    Alkalinity <ash_alkalinity_as_CaCO3_mg_L>
    Ca        <Ca_mg_L>
    Mg        <Mg_mg_L>
    Na        <Na_mg_L>
    K         <K_mg_L>
    S(6)      <SO4_mg_L> as SO4
    C(4)      <DIC_mg_L> as HCO3
    U         <U_ug_L> ug/L
    Ra        <Ra_Bq_L_or_mol_basis> # verify database species and units
END

MIX 10 First_flush_mixing_series
    1 0.95
    2 0.05
SAVE solution 10
END

MIX 11 First_flush_mixing_series
    1 0.75
    2 0.25
SAVE solution 11
END

MIX 12 First_flush_mixing_series
    1 0.50
    2 0.50
SAVE solution 12
END

SELECTED_OUTPUT
    -file wildfire_ash_mixing_selected.tsv
    -reset false
    -pH true
    -pe true
    -alkalinity true
    -ionic_strength true
    -totals U Ra S(6) C(4) Ca Ba Sr Fe Mn
    -saturation_indices Calcite Gypsum Barite Uraninite
END
"""
    (MODELS / "phreeqc_wildfire_ash_stream_mixing_template.phr").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    result = analyze()
    print(json.dumps(result, ensure_ascii=False, indent=2))
