#!/usr/bin/env python3
"""Phase-2 integrated wildfire-water-chemistry-sediment risk analysis.

This script extends the first-pass open-data screening package with the
Eastern Athabasca Regional Monitoring Program (EARMP), source-layer readiness,
post-fire water-chemistry controls, phase partitioning, and long-term sediment
secondary-source sensitivity figures.

The outputs are screening/research-design artifacts. They are not regulatory
findings, dose estimates, or validated site models.
"""

from __future__ import annotations

import csv
import json
import math
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
CATALOG = RAW / "catalog"
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "figures"
MODELS = ROOT / "models"

SVG_NS = "http://www.w3.org/2000/svg"
R_EARTH_KM = 6371.0088

MAP_EXTENT = {
    "west": -110.0,
    "east": -101.0,
    "south": 56.5,
    "north": 60.0,
}


def ensure_dirs() -> None:
    for path in (PROCESSED, FIGURES, MODELS):
        path.mkdir(parents=True, exist_ok=True)


def escape(value: Any) -> str:
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def svg_text(
    x: float,
    y: float,
    text: Any,
    size: int = 12,
    anchor: str = "start",
    weight: str = "400",
    fill: str = "#222",
) -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{escape(text)}</text>'
    )


def save_svg(path: Path, width: int, height: int, body: list[str]) -> None:
    path.write_text(
        "\n".join(
            [
                f'<svg xmlns="{SVG_NS}" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
                '<rect width="100%" height="100%" fill="#ffffff"/>',
                *body,
                "</svg>",
            ]
        ),
        encoding="utf-8",
    )


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


def quantile(values: list[float], q: float) -> float | None:
    if not values:
        return None
    xs = sorted(values)
    pos = (len(xs) - 1) * q
    lo = math.floor(pos)
    hi = math.ceil(pos)
    if lo == hi:
        return xs[lo]
    return xs[lo] * (hi - pos) + xs[hi] * (pos - lo)


def fmt(value: float | None, ndigits: int = 3) -> str:
    if value is None or math.isnan(value):
        return ""
    return f"{value:.{ndigits}f}".rstrip("0").rstrip(".")


def date_from_epoch_ms(value: Any) -> str:
    if value is None:
        return ""
    try:
        return datetime.fromtimestamp(float(value) / 1000.0, UTC).date().isoformat()
    except Exception:
        return ""


def year_from_epoch_ms(value: Any) -> int | None:
    text = date_from_epoch_ms(value)
    return int(text[:4]) if text else None


def normalize_community(name: str | None) -> str:
    if not name:
        return ""
    if name.lower() == "fond du lac":
        return "Fond du Lac"
    return name


def read_earmp_features() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(RAW.glob("earmp_layer0_features_*.geojson")):
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        for feature in data.get("features", []):
            prop = dict(feature.get("properties") or {})
            geom = feature.get("geometry") or {}
            coords = geom.get("coordinates") or []
            if len(coords) >= 2:
                prop["geom_lon"] = coords[0]
                prop["geom_lat"] = coords[1]
            prop["Community"] = normalize_community(prop.get("Community"))
            prop["sample_date"] = date_from_epoch_ms(prop.get("Sample_Date"))
            prop["sample_year"] = year_from_epoch_ms(prop.get("Sample_Date"))
            rows.append(prop)
    return rows


def summarize_earmp(rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    surface = [r for r in rows if r.get("Sample_Media") == "Surface Water"]
    records: list[dict[str, Any]] = []
    for r in surface:
        records.append(
            {
                "sample_date": r.get("sample_date"),
                "sample_year": r.get("sample_year"),
                "community": r.get("Community"),
                "latitude": r.get("Latitude"),
                "longitude": r.get("Longitude"),
                "substance": r.get("Substance_Name"),
                "flag": r.get("F_") or "",
                "result": r.get("Result"),
                "units": r.get("Units"),
                "basis": r.get("Basis"),
            }
        )

    grouped: dict[tuple[Any, Any, Any, Any], list[dict[str, Any]]] = defaultdict(list)
    for r in records:
        grouped[(r["community"], r["sample_year"], r["substance"], r["units"])].append(r)

    summary: list[dict[str, Any]] = []
    for (community, year, substance, units), group in sorted(grouped.items(), key=lambda item: tuple(str(v) for v in item[0])):
        values = [float(g["result"]) for g in group if isinstance(g.get("result"), (int, float))]
        censored = sum(1 for g in group if g.get("flag") == "<")
        summary.append(
            {
                "community": community,
                "year": year,
                "substance": substance,
                "units": units,
                "n": len(group),
                "censored_n": censored,
                "min": fmt(min(values), 6) if values else "",
                "median": fmt(quantile(values, 0.5), 6),
                "p90": fmt(quantile(values, 0.9), 6),
                "max": fmt(max(values), 6) if values else "",
            }
        )

    latest_year = max(r["sample_year"] for r in records if r.get("sample_year"))
    latest = [r for r in records if r.get("sample_year") == latest_year]
    return records, summary, latest


def open_data_inventory() -> list[dict[str, Any]]:
    rows = [
        {
            "data_layer": "NBAC burned-area/fire perimeter",
            "status": "downloaded_parsed",
            "evidence": "CWFIS GeoServer WFS public:nbac",
            "role": "fire exposure, year, fire cause, facility proximity",
            "limitation": "polygons are not clipped to AOI; burn severity is not included",
            "readiness_score": 3,
        },
        {
            "data_layer": "Fire burn severity",
            "status": "gap_for_northern_saskatchewan",
            "evidence": "Open Canada query found BC same-year burn severity but no national layer in this run",
            "role": "severity-weighted runoff and ash source term",
            "limitation": "derive dNBR/RdNBR from Sentinel-2/Landsat or locate a regional product before mapping",
            "readiness_score": 1,
        },
        {
            "data_layer": "MRDEM/CDEM elevation",
            "status": "metadata_queried",
            "evidence": "Open Canada MRDEM package and STAC bbox search saved",
            "role": "flow direction, slope, wetland/lake routing, watershed delineation",
            "limitation": "raster not downloaded or hydrologically conditioned in this run",
            "readiness_score": 2,
        },
        {
            "data_layer": "CHN hydrography",
            "status": "metadata_queried_limited_coverage",
            "evidence": "CHN MapServer metadata saved; current service extent did not cover AOI",
            "role": "flowline and waterbody routing where CHN work units exist",
            "limitation": "use NHN prepackaged work units for current northern Saskatchewan coverage",
            "readiness_score": 2,
        },
        {
            "data_layer": "NHN hydrography",
            "status": "catalog_queried",
            "evidence": "NHN Open Canada package metadata saved",
            "role": "rivers, lakes, drainage network and receptor connectivity",
            "limitation": "work-unit GPKG/SHP not downloaded or spatially joined in this run",
            "readiness_score": 2,
        },
        {
            "data_layer": "WSC hydrometric stations and discharge",
            "status": "downloaded_parsed",
            "evidence": "ECCC/WSC OGC API daily mean and station inventory",
            "role": "regional post-fire hydrologic response proxy",
            "limitation": "06DA004 is not a site-specific runoff gauge for each facility",
            "readiness_score": 3,
        },
        {
            "data_layer": "ECCC climate daily precipitation",
            "status": "downloaded_parsed",
            "evidence": "ECCC climate-daily OGC API, Key Lake stations",
            "role": "post-fire 7-day and 30-day rainfall trigger",
            "limitation": "single station proxy; event intensity and radar gridded precipitation still needed",
            "readiness_score": 3,
        },
        {
            "data_layer": "CNSC uranium mine radionuclide releases",
            "status": "downloaded_parsed",
            "evidence": "Open Canada CNSC radionuclide release workbook",
            "role": "facility source-term intensity for U, Th-230, Ra-226, Pb-210, Po-210",
            "limitation": "annual release table is not a spatially resolved tailings/waste-rock source map",
            "readiness_score": 3,
        },
        {
            "data_layer": "EARMP surface water and country-food chemistry",
            "status": "downloaded_parsed",
            "evidence": "CNSC Eastern Athabasca Regional Monitoring Program MapServer and XLSX",
            "role": "regional receptor chemistry, U/Ra/pH background and late-season post-fire checks",
            "limitation": "no alkalinity, major ions, Eh, TSS, Pb-210, Po-210, sediment cores, or first-flush event samples",
            "readiness_score": 3,
        },
        {
            "data_layer": "Indigenous community infrastructure",
            "status": "metadata_queried",
            "evidence": "Open Canada/ISC package metadata saved",
            "role": "community receptor context and water-system screening",
            "limitation": "exact intake points may be absent, sensitive, generalized, or require community-specific validation",
            "readiness_score": 2,
        },
        {
            "data_layer": "Lake/wetland sediment cores",
            "status": "field_data_required",
            "evidence": "not available in public data pulled in this run",
            "role": "secondary source inventory, burial, resuspension, Fe-Mn/organic matter binding",
            "limitation": "must be sampled and dated before long-term source terms can be calibrated",
            "readiness_score": 0,
        },
    ]
    return rows


def coord_to_xy(lon: float, lat: float, width: int, height: int, margin: int = 52) -> tuple[float, float]:
    x = margin + (lon - MAP_EXTENT["west"]) / (MAP_EXTENT["east"] - MAP_EXTENT["west"]) * (width - 2 * margin)
    y = height - margin - (lat - MAP_EXTENT["south"]) / (MAP_EXTENT["north"] - MAP_EXTENT["south"]) * (height - 2 * margin)
    return x, y


def haversine_km(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = phi2 - phi1
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R_EARTH_KM * math.asin(math.sqrt(a))


def plot_polyline(points: list[tuple[float, float]], stroke: str, width: float = 2.0, fill: str = "none") -> str:
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<polyline points="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"/>'


def fig_workflow() -> None:
    width, height = 1180, 520
    body: list[str] = [
        svg_text(40, 42, "Integrated causal workflow: screening -> first flush chemistry -> long-term secondary source", 20, weight="700"),
        svg_text(40, 68, "The present water-chemistry state is the bridge variable used to predict longer-term sediment and wetland risk.", 12, fill="#555"),
    ]
    boxes = [
        (60, 120, 285, 190, "#e8f2ff", "#1f5f99", "Analysis I", "Open-data disturbance screening", ["NBAC + burn severity", "DEM + NHN/CHN routing", "source term + receptor proximity"]),
        (445, 120, 285, 190, "#fff3dd", "#9a5b00", "Analysis II", "Post-fire first flush chemistry", ["ash/soil/runoff/water/TSS", "U-Ra-Pb-Po phase split", "PHREEQC speciation and SI"]),
        (830, 120, 285, 190, "#eaf7e9", "#23733a", "Analysis III", "Lake/wetland secondary source", ["sediment cores + grain size", "Fe-Mn/organic binding", "resuspension + burial"]),
    ]
    for x, y, w, h, fill, stroke, label, title, bullets in boxes:
        body.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        body.append(svg_text(x + 18, y + 32, label, 15, weight="700", fill=stroke))
        body.append(svg_text(x + 18, y + 58, title, 17, weight="700"))
        for j, bullet in enumerate(bullets):
            body.append(svg_text(x + 28, y + 92 + j * 28, f"- {bullet}", 13, fill="#333"))
    for x1, x2 in [(345, 445), (730, 830)]:
        body.append(f'<line x1="{x1}" y1="215" x2="{x2}" y2="215" stroke="#333" stroke-width="2.2" marker-end="url(#arrow)"/>')
    body.append(
        '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto" markerUnits="strokeWidth">'
        '<path d="M0,0 L0,6 L8,3 z" fill="#333"/></marker></defs>'
    )
    body.append('<rect x="190" y="365" width="800" height="80" rx="8" fill="#f7f7f7" stroke="#999"/>')
    body.append(svg_text(590, 392, "Prediction merge", 15, anchor="middle", weight="700"))
    body.append(svg_text(590, 418, "Current post-fire water chemistry constrains dissolved mobility; sediment inventory constrains chronic resuspension.", 13, anchor="middle", fill="#333"))
    body.append(f'<path d="M972,310 C990,350 980,365 925,365" fill="none" stroke="#23733a" stroke-width="2" marker-end="url(#arrow)"/>')
    body.append(f'<path d="M590,365 C555,330 555,315 590,310" fill="none" stroke="#555" stroke-width="2" marker-end="url(#arrow)"/>')
    save_svg(FIGURES / "fig08_integrated_causal_workflow.svg", width, height, body)


def fig_open_data_readiness(rows: list[dict[str, Any]]) -> None:
    width, height = 1180, 650
    body = [
        svg_text(40, 42, "Open-data layer readiness for northern uranium-mining wildfire risk screening", 20, weight="700"),
        svg_text(40, 68, "Score: 3 downloaded/parsed, 2 metadata/catalog queried, 1 identified gap, 0 field data required.", 12, fill="#555"),
    ]
    x0, y0 = 370, 110
    bar_w = 560
    row_h = 42
    for score in range(4):
        x = x0 + score / 3 * bar_w
        body.append(f'<line x1="{x:.1f}" y1="{y0-22}" x2="{x:.1f}" y2="{y0+row_h*len(rows)+5}" stroke="#e0e0e0"/>')
        body.append(svg_text(x, y0 - 30, score, 11, anchor="middle", fill="#666"))
    colors = {0: "#bdbdbd", 1: "#f2b35d", 2: "#77aadd", 3: "#4c956c"}
    for i, row in enumerate(rows):
        y = y0 + i * row_h
        score = int(row["readiness_score"])
        body.append(svg_text(40, y + 17, row["data_layer"], 12, fill="#222"))
        body.append(f'<rect x="{x0}" y="{y}" width="{bar_w}" height="18" fill="#f3f3f3" stroke="#ddd"/>')
        body.append(f'<rect x="{x0}" y="{y}" width="{score/3*bar_w:.1f}" height="18" fill="{colors[score]}"/>')
        body.append(svg_text(x0 + bar_w + 16, y + 14, row["status"], 11, fill="#333"))
    body.append(svg_text(40, height - 45, "Main design implication: burn severity, receptor intake points, and sediment cores are the limiting layers for moving from screening to prediction.", 12, fill="#555"))
    save_svg(FIGURES / "fig09_open_data_layer_readiness.svg", width, height, body)


def build_yearly_series(summary: list[dict[str, Any]], substance: str, field: str) -> dict[int, float]:
    grouped: dict[int, list[float]] = defaultdict(list)
    for row in summary:
        if row.get("substance") != substance:
            continue
        try:
            year = int(row["year"])
            value = float(row[field])
        except Exception:
            continue
        grouped[year].append(value)
    return {year: quantile(values, 0.5) or 0.0 for year, values in grouped.items()}


def fig_earmp_surface_water(summary: list[dict[str, Any]]) -> None:
    width, height = 1180, 760
    years = list(range(2011, 2024))
    panels = [
        ("pH", "median", 5.2, 8.3, "Surface-water pH", "#3d7ea6"),
        ("Uranium", "max", 0.0, 3.8, "U max, ug/L", "#7a4ea3"),
        ("Radium-226", "max", 0.0, 0.012, "Ra-226 max, Bq/L", "#a64242"),
    ]
    body = [
        svg_text(40, 42, "EARMP surface-water chemistry, 2011-2023", 20, weight="700"),
        svg_text(40, 68, "Late-season regional monitoring provides current/recent water-chemistry bounds, but not first-flush event chemistry.", 12, fill="#555"),
    ]
    left, top = 72, 115
    panel_w, panel_h = 1020, 170
    gap = 62
    for idx, (substance, field, ymin, ymax, title, color) in enumerate(panels):
        ybase = top + idx * (panel_h + gap)
        series = build_yearly_series(summary, substance, field)
        body.append(svg_text(left, ybase - 18, title, 15, weight="700"))
        body.append(f'<rect x="{left}" y="{ybase}" width="{panel_w}" height="{panel_h}" fill="#fbfbfb" stroke="#ddd"/>')
        for t in range(5):
            gy = ybase + panel_h - t / 4 * panel_h
            val = ymin + t / 4 * (ymax - ymin)
            body.append(f'<line x1="{left}" y1="{gy:.1f}" x2="{left+panel_w}" y2="{gy:.1f}" stroke="#e8e8e8"/>')
            body.append(svg_text(left - 8, gy + 4, fmt(val, 3), 10, anchor="end", fill="#666"))
        points: list[tuple[float, float]] = []
        for year in years:
            x = left + (year - years[0]) / (years[-1] - years[0]) * panel_w
            if year in series:
                y = ybase + panel_h - (series[year] - ymin) / (ymax - ymin) * panel_h
                points.append((x, y))
                body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2" fill="{color}" stroke="#fff"/>')
            if year in {2011, 2014, 2017, 2020, 2023}:
                body.append(svg_text(x, ybase + panel_h + 18, year, 10, anchor="middle", fill="#666"))
        if len(points) > 1:
            body.append(plot_polyline(points, color, 2.2))
    body.append(svg_text(72, height - 42, "Censoring note: many U and Ra observations are reported at or below detection limits; values are treated as reported upper-bound screen values.", 12, fill="#555"))
    save_svg(FIGURES / "fig10_earmp_surface_water_chemistry.svg", width, height, body)


def fig_phase_partitioning() -> None:
    width, height = 1100, 680
    body = [
        svg_text(46, 42, "First-flush dissolved-particle partitioning sensitivity", 20, weight="700"),
        svg_text(46, 68, "Particle-bound fraction increases with Kd and TSS; this is the key bridge from water chemistry to sediment loading.", 12, fill="#555"),
    ]
    left, top, plot_w, plot_h = 86, 116, 860, 430
    body.append(f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="#fbfbfb" stroke="#ddd"/>')
    for i in range(6):
        y = top + plot_h - i / 5 * plot_h
        body.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left+plot_w}" y2="{y:.1f}" stroke="#e8e8e8"/>')
        body.append(svg_text(left - 10, y + 4, f"{i/5:.1f}", 10, anchor="end", fill="#666"))
    for i, label in enumerate([1, 3, 10, 30, 100, 300, 1000]):
        x = left + (math.log10(label) - 0) / 3 * plot_w
        body.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top+plot_h}" stroke="#f0f0f0"/>')
        body.append(svg_text(x, top + plot_h + 18, label, 10, anchor="middle", fill="#666"))
    kd_values = [(1, "#377eb8", "Kd=1 m3/kg"), (10, "#4daf4a", "Kd=10"), (100, "#984ea3", "Kd=100"), (1000, "#e41a1c", "Kd=1000")]
    for kd, color, label in kd_values:
        points: list[tuple[float, float]] = []
        for n in range(100):
            tss_mg_l = 10 ** (0 + 3 * n / 99)
            tss_kg_m3 = tss_mg_l / 1000.0
            frac = kd * tss_kg_m3 / (1.0 + kd * tss_kg_m3)
            x = left + math.log10(tss_mg_l) / 3 * plot_w
            y = top + plot_h - frac * plot_h
            points.append((x, y))
        body.append(plot_polyline(points, color, 2.4))
        body.append(svg_text(points[-1][0] + 8, points[-1][1] + 4, label, 11, fill=color))
    body.append(svg_text(left + plot_w / 2, top + plot_h + 48, "TSS during first flush (mg/L, log scale)", 13, anchor="middle"))
    body.append(svg_text(24, top + plot_h / 2, "Particle-bound fraction", 13, anchor="middle"))
    body.append('<rect x="820" y="118" width="220" height="118" rx="8" fill="#fff" stroke="#ddd"/>')
    labels = [("U", "carbonate/DOC-sensitive"), ("Ra", "sulfate/Ba/Sr-sensitive"), ("Pb-Po-Th", "particle/sediment-sensitive")]
    for i, (a, b) in enumerate(labels):
        body.append(svg_text(838, 146 + i * 30, a, 13, weight="700"))
        body.append(svg_text(890, 146 + i * 30, b, 12, fill="#444"))
    save_svg(FIGURES / "fig11_first_flush_phase_partitioning.svg", width, height, body)


def fig_sediment_secondary_source() -> list[dict[str, Any]]:
    width, height = 1120, 680
    body = [
        svg_text(46, 42, "Lake/wetland sediment secondary-source sensitivity", 20, weight="700"),
        svg_text(46, 68, "Long-term risk depends on how much first-flush load is retained, buried, or resuspended.", 12, fill="#555"),
    ]
    left, top, plot_w, plot_h = 86, 118, 820, 420
    body.append(f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="#fbfbfb" stroke="#ddd"/>')
    scenarios = [
        ("low retention", 0.20, 0.020, 0.015, "#377eb8"),
        ("moderate retention", 0.55, 0.035, 0.025, "#4daf4a"),
        ("high retention", 0.85, 0.060, 0.040, "#e41a1c"),
    ]
    rows: list[dict[str, Any]] = []
    max_flux = 0.0
    curves: list[tuple[str, str, list[tuple[float, float]], float]] = []
    for label, retention, k_resusp, k_burial, color in scenarios:
        values = []
        for n in range(121):
            years = 20 * n / 120
            sediment_inventory = retention * math.exp(-(k_burial + k_resusp) * years)
            resuspension_flux = k_resusp * sediment_inventory
            values.append((years, resuspension_flux))
            rows.append(
                {
                    "scenario": label,
                    "years_after_fire": fmt(years, 3),
                    "retention_fraction": retention,
                    "k_resusp_per_year": k_resusp,
                    "k_burial_per_year": k_burial,
                    "relative_sediment_inventory": fmt(sediment_inventory, 6),
                    "relative_resuspension_flux": fmt(resuspension_flux, 6),
                }
            )
            max_flux = max(max_flux, resuspension_flux)
        curves.append((label, color, values, retention))
    for i in range(6):
        y = top + plot_h - i / 5 * plot_h
        body.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left+plot_w}" y2="{y:.1f}" stroke="#e8e8e8"/>')
        body.append(svg_text(left - 10, y + 4, fmt(max_flux * i / 5, 3), 10, anchor="end", fill="#666"))
    for i in range(5):
        x = left + i / 4 * plot_w
        body.append(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{top+plot_h}" stroke="#f0f0f0"/>')
        body.append(svg_text(x, top + plot_h + 18, int(i / 4 * 20), 10, anchor="middle", fill="#666"))
    for label, color, values, retention in curves:
        points = [(left + years / 20 * plot_w, top + plot_h - flux / max_flux * plot_h) for years, flux in values]
        body.append(plot_polyline(points, color, 2.5))
        body.append(svg_text(points[42][0] + 8, points[42][1] - 5, f"{label}, R={retention:.2f}", 11, fill=color))
    body.append(svg_text(left + plot_w / 2, top + plot_h + 48, "Years after post-fire first-flush event", 13, anchor="middle"))
    body.append(svg_text(22, top + plot_h / 2, "Relative resuspension flux", 13, anchor="middle"))
    body.append('<rect x="825" y="120" width="240" height="172" rx="8" fill="#fff" stroke="#ddd"/>')
    body.append(svg_text(845, 150, "Calibration needs", 13, weight="700"))
    for i, item in enumerate(["sediment-core activity", "grain-size fractions", "organic matter", "Fe-Mn oxide extraction", "storm TSS and flow"]):
        body.append(svg_text(850, 178 + i * 23, f"- {item}", 12, fill="#444"))
    save_svg(FIGURES / "fig12_sediment_secondary_source_risk.svg", width, height, body)
    return rows


def fig_receptor_network_map(earmp_records: list[dict[str, Any]]) -> None:
    width, height = 1080, 650
    body = [
        svg_text(42, 42, "Facilities, EARMP receptor communities, and recent fire centroids", 20, weight="700"),
        svg_text(42, 68, "Map is screening-grade and uses point locations, not facility boundaries or intake coordinates.", 12, fill="#555"),
    ]
    left, top = 70, 105
    map_w, map_h = 880, 470
    body.append(f'<rect x="{left}" y="{top}" width="{map_w}" height="{map_h}" fill="#f7fbff" stroke="#ccc"/>')
    for lon in range(-110, -100):
        x, _ = coord_to_xy(lon, MAP_EXTENT["south"], map_w, map_h, 0)
        body.append(f'<line x1="{left+x:.1f}" y1="{top}" x2="{left+x:.1f}" y2="{top+map_h}" stroke="#e5edf5"/>')
    for lat_i in range(57, 61):
        _, y = coord_to_xy(MAP_EXTENT["west"], lat_i, map_w, map_h, 0)
        body.append(f'<line x1="{left}" y1="{top+y:.1f}" x2="{left+map_w}" y2="{top+y:.1f}" stroke="#e5edf5"/>')
    fires_path = RAW / "nbac_athabasca_bbox_1986_2024.geojson"
    if fires_path.exists():
        with fires_path.open("r", encoding="utf-8") as f:
            fires = json.load(f).get("features", [])
        for feat in fires:
            prop = feat.get("properties") or {}
            if int(prop.get("year") or 0) < 2020:
                continue
            coords = feat.get("geometry", {}).get("coordinates") or []
            ring: list[Any] = []
            if feat.get("geometry", {}).get("type") == "Polygon" and coords:
                ring = coords[0]
            elif feat.get("geometry", {}).get("type") == "MultiPolygon" and coords and coords[0]:
                ring = coords[0][0]
            if not ring:
                continue
            step = max(1, len(ring) // 150)
            xs = [p[0] for p in ring[::step]]
            ys = [p[1] for p in ring[::step]]
            lon, lat = sum(xs) / len(xs), sum(ys) / len(ys)
            if not (MAP_EXTENT["west"] <= lon <= MAP_EXTENT["east"] and MAP_EXTENT["south"] <= lat <= MAP_EXTENT["north"]):
                continue
            x, y = coord_to_xy(lon, lat, map_w, map_h, 0)
            radius = max(2.0, min(15.0, math.sqrt(float(prop.get("poly_ha") or 0.0)) / 65.0))
            body.append(f'<circle cx="{left+x:.1f}" cy="{top+y:.1f}" r="{radius:.1f}" fill="#e6550d" opacity="0.18" stroke="#e6550d" stroke-width="0.5"/>')
    facilities_path = PROCESSED / "facilities.csv"
    if facilities_path.exists():
        with facilities_path.open("r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                lon, lat = float(row["longitude"]), float(row["latitude"])
                x, y = coord_to_xy(lon, lat, map_w, map_h, 0)
                body.append(f'<polygon points="{left+x:.1f},{top+y-8:.1f} {left+x-7:.1f},{top+y+6:.1f} {left+x+7:.1f},{top+y+6:.1f}" fill="#6a3d9a" stroke="#fff"/>')
                body.append(svg_text(left + x + 7, top + y - 7, row["facility"], 10, fill="#333"))
    latest_by_community: dict[str, dict[str, Any]] = {}
    for row in earmp_records:
        community = row["community"]
        if community and community not in latest_by_community:
            latest_by_community[community] = row
    for community, row in sorted(latest_by_community.items()):
        lon, lat = float(row["longitude"]), float(row["latitude"])
        x, y = coord_to_xy(lon, lat, map_w, map_h, 0)
        body.append(f'<circle cx="{left+x:.1f}" cy="{top+y:.1f}" r="5.2" fill="#1f78b4" stroke="#fff" stroke-width="1.5"/>')
        body.append(svg_text(left + x + 7, top + y + 4, community, 10, fill="#1f4e79"))
    body.append('<rect x="780" y="500" width="240" height="86" rx="6" fill="#fff" stroke="#ccc"/>')
    body.append(f'<circle cx="800" cy="523" r="7" fill="#e6550d" opacity="0.25" stroke="#e6550d"/>')
    body.append(svg_text(818, 527, "2020-2024 NBAC fire centroid", 11))
    body.append('<polygon points="795,546 788,560 802,560" fill="#6a3d9a"/>')
    body.append(svg_text(818, 558, "CNSC mine/mill facility", 11))
    body.append('<circle cx="800" cy="578" r="5.2" fill="#1f78b4"/>')
    body.append(svg_text(818, 582, "EARMP receptor community", 11))
    save_svg(FIGURES / "fig13_receptor_network_screening_map.svg", width, height, body)


def write_phreeqc_input(summary: list[dict[str, Any]]) -> Path:
    path = MODELS / "phreeqc_postfire_water_sensitivity_llnl.phr"
    # Reported 2023 EARMP upper-bound screen values: U commonly <0.1 ug/L and
    # Ra-226 commonly <0.005 Bq/L. Convert Ra-226 activity to mass using
    # 1 Bq Ra-226 ~= 2.70e-11 g; 0.005 Bq/L ~= 1.35e-10 mg/L.
    content = """TITLE Post-fire water chemistry sensitivity screen for EARMP-like surface water
# Purpose: illustrative PHREEQC sensitivity setup, not calibrated field evidence.
# Database used in the run manifest: llnl.dat.
# Measured anchors from EARMP 2023 surface water: pH range 5.43-7.08,
# U mostly <=0.1 ug/L, Ra-226 mostly <=0.005 Bq/L.
# Missing measured inputs: alkalinity, Ca, Mg, Na, K, Cl, sulfate, DOC, Eh/pe,
# TSS, Pb-210, Po-210, Fe/Mn, dissolved oxygen and charge balance.

SOLUTION 1 EARMP_2023_low_alkalinity_upper_bound
    units mg/L
    temp 10
    pH 6.59
    pe 4
    Alkalinity 5 as CaCO3
    Ca 2
    Mg 1
    Na 2
    K 0.5
    Cl 2
    S(6) 2 as SO4
    U(6) 0.0001
    Ra 1.35e-10
    Pb 0.0001

SOLUTION 2 Ash_alkalinity_pulse_upper_bound
    units mg/L
    temp 10
    pH 8.20
    pe 4
    Alkalinity 50 as CaCO3
    Ca 20
    Mg 3
    Na 5
    K 3
    Cl 3
    S(6) 5 as SO4
    U(6) 0.0001
    Ra 1.35e-10
    Pb 0.0001

SELECTED_OUTPUT 1
    -file phreeqc_postfire_water_sensitivity_llnl.sel
    -reset false
    -simulation true
    -state true
    -solution true
    -pH true
    -pe true
    -ionic_strength true
    -charge_balance true
    -alkalinity true
    -totals C Ca S(6) U Ra Pb
    -saturation_indices Calcite Gypsum Barite RaSO4 UO2CO3 UO2(OH)2(beta) UO2(am) Cerussite Anglesite
    -molalities UO2+2 UO2CO3 UO2(CO3)2-2 UO2(CO3)3-4 Ra+2 RaSO4 Pb+2 PbCO3 Pb(CO3)2-2
END
"""
    path.write_text(content, encoding="utf-8")
    return path


def main() -> None:
    ensure_dirs()
    earmp_rows = read_earmp_features()
    records, summary, latest = summarize_earmp(earmp_rows)
    inventory = open_data_inventory()
    sediment_rows = fig_sediment_secondary_source()

    write_csv(PROCESSED / "earmp_surface_water_records.csv", records)
    write_csv(PROCESSED / "earmp_surface_water_yearly_summary.csv", summary)
    write_csv(PROCESSED / "earmp_surface_water_latest_year.csv", latest)
    write_csv(PROCESSED / "open_data_layer_inventory_phase2.csv", inventory)
    write_csv(PROCESSED / "long_term_sediment_secondary_source_scenarios.csv", sediment_rows)

    fig_workflow()
    fig_open_data_readiness(inventory)
    fig_earmp_surface_water(summary)
    fig_phase_partitioning()
    fig_receptor_network_map(records)
    phreeqc_path = write_phreeqc_input(summary)

    surface = [r for r in earmp_rows if r.get("Sample_Media") == "Surface Water"]
    summary_json = {
        "earmp_total_records": len(earmp_rows),
        "earmp_surface_water_records": len(surface),
        "earmp_surface_water_substance_records": len(records),
        "earmp_surface_water_years": sorted({r["sample_year"] for r in records if r.get("sample_year")}),
        "earmp_surface_water_communities": sorted({r["community"] for r in records if r.get("community")}),
        "open_data_layers": len(inventory),
        "downloaded_or_parsed_layers": sum(1 for r in inventory if r["readiness_score"] == 3),
        "metadata_or_catalog_layers": sum(1 for r in inventory if r["readiness_score"] == 2),
        "critical_gaps": [r["data_layer"] for r in inventory if r["readiness_score"] <= 1],
        "phreeqc_input": str(phreeqc_path.relative_to(ROOT)),
        "figures_added": [
            "fig08_integrated_causal_workflow.svg",
            "fig09_open_data_layer_readiness.svg",
            "fig10_earmp_surface_water_chemistry.svg",
            "fig11_first_flush_phase_partitioning.svg",
            "fig12_sediment_secondary_source_risk.svg",
            "fig13_receptor_network_screening_map.svg",
        ],
    }
    (PROCESSED / "phase2_analysis_summary.json").write_text(json.dumps(summary_json, indent=2), encoding="utf-8")
    print(json.dumps(summary_json, indent=2))


if __name__ == "__main__":
    main()
