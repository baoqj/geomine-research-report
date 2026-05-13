#!/usr/bin/env python3
"""Generate screening calculations and SVG figures for fractured-rock RN transport.

The dataset is a transparent, literature-guided screening model. It is designed
to test relative hypotheses about adsorption, matrix diffusion, and
colloid-facilitated transport. It is not a calibrated safety assessment.
"""

from __future__ import annotations

import csv
import html
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
YEAR_S = 365.25 * 24 * 3600

PAL = {
    "ink": "#172026",
    "muted": "#52616a",
    "grid": "#d7e0e5",
    "blue": "#1f6f9f",
    "teal": "#249186",
    "green": "#5d8f3a",
    "amber": "#d08b2f",
    "red": "#c94f44",
    "purple": "#6f5aa7",
    "rock": "#9aa6ad",
    "calcite": "#d8d2ba",
    "oxide": "#8f5146",
    "clay": "#c8a45d",
    "water": "#5aa6c8",
}


NUCLIDES = [
    {
        "name": "I-129",
        "group": "high-mobility anion",
        "dominant_forms_oxidizing": "I-, IO3-",
        "dominant_forms_reducing": "I-",
        "kd_oxidizing_m3_kg": 1e-5,
        "kd_reducing_m3_kg": 1e-5,
        "colloid_k_l_kg": 1e2,
        "redox_sensitive": 1,
        "mineral_affinity": "low; organic matter may matter",
    },
    {
        "name": "Tc-99",
        "group": "redox-sensitive anion",
        "dominant_forms_oxidizing": "TcO4-",
        "dominant_forms_reducing": "Tc(IV) solids/complexes",
        "kd_oxidizing_m3_kg": 1e-5,
        "kd_reducing_m3_kg": 5e-2,
        "colloid_k_l_kg": 1e4,
        "redox_sensitive": 5,
        "mineral_affinity": "Fe oxides, reducing phases",
    },
    {
        "name": "Se-79",
        "group": "mobile anion",
        "dominant_forms_oxidizing": "SeO4--/SeO3--",
        "dominant_forms_reducing": "Se(0)/Se(-II) controls",
        "kd_oxidizing_m3_kg": 1e-4,
        "kd_reducing_m3_kg": 1e-2,
        "colloid_k_l_kg": 1e3,
        "redox_sensitive": 4,
        "mineral_affinity": "Fe oxides, sulfides",
    },
    {
        "name": "Sr-90",
        "group": "fission product cation",
        "dominant_forms_oxidizing": "Sr++",
        "dominant_forms_reducing": "Sr++",
        "kd_oxidizing_m3_kg": 1e-3,
        "kd_reducing_m3_kg": 1e-3,
        "colloid_k_l_kg": 1e3,
        "redox_sensitive": 1,
        "mineral_affinity": "calcite, clays, ion exchange",
    },
    {
        "name": "Cs-137",
        "group": "fission product cation",
        "dominant_forms_oxidizing": "Cs+",
        "dominant_forms_reducing": "Cs+",
        "kd_oxidizing_m3_kg": 2e-2,
        "kd_reducing_m3_kg": 2e-2,
        "colloid_k_l_kg": 5e4,
        "redox_sensitive": 1,
        "mineral_affinity": "biotite, illite/frayed-edge sites",
    },
    {
        "name": "Ra-226",
        "group": "decay-series cation",
        "dominant_forms_oxidizing": "Ra++",
        "dominant_forms_reducing": "Ra++",
        "kd_oxidizing_m3_kg": 1e-2,
        "kd_reducing_m3_kg": 1e-2,
        "colloid_k_l_kg": 1e3,
        "redox_sensitive": 1,
        "mineral_affinity": "barite/calcite co-precipitation, clays",
    },
    {
        "name": "U",
        "group": "actinide / decay-series",
        "dominant_forms_oxidizing": "U(VI)-carbonate",
        "dominant_forms_reducing": "U(IV)",
        "kd_oxidizing_m3_kg": 1e-3,
        "kd_reducing_m3_kg": 1e-1,
        "colloid_k_l_kg": 1e5,
        "redox_sensitive": 5,
        "mineral_affinity": "Fe oxides, chlorite, clay, organic colloids",
    },
    {
        "name": "Np",
        "group": "actinide",
        "dominant_forms_oxidizing": "Np(V)",
        "dominant_forms_reducing": "Np(IV)",
        "kd_oxidizing_m3_kg": 1e-3,
        "kd_reducing_m3_kg": 5e-2,
        "colloid_k_l_kg": 5e4,
        "redox_sensitive": 5,
        "mineral_affinity": "hematite, montmorillonite, altered minerals",
    },
    {
        "name": "Pu",
        "group": "actinide",
        "dominant_forms_oxidizing": "Pu(IV/V/VI), hydrolysis",
        "dominant_forms_reducing": "Pu(III/IV)",
        "kd_oxidizing_m3_kg": 1e-1,
        "kd_reducing_m3_kg": 1.0,
        "colloid_k_l_kg": 1e6,
        "redox_sensitive": 5,
        "mineral_affinity": "Fe-Mn oxides, clays, organic colloids",
    },
    {
        "name": "Am",
        "group": "trivalent actinide",
        "dominant_forms_oxidizing": "Am(III)",
        "dominant_forms_reducing": "Am(III)",
        "kd_oxidizing_m3_kg": 2e-1,
        "kd_reducing_m3_kg": 1.0,
        "colloid_k_l_kg": 1e6,
        "redox_sensitive": 2,
        "mineral_affinity": "clays, Fe oxides, organic colloids",
    },
    {
        "name": "Th",
        "group": "tetravalent actinide",
        "dominant_forms_oxidizing": "Th(IV)",
        "dominant_forms_reducing": "Th(IV)",
        "kd_oxidizing_m3_kg": 1.0,
        "kd_reducing_m3_kg": 5.0,
        "colloid_k_l_kg": 1e6,
        "redox_sensitive": 1,
        "mineral_affinity": "Fe oxides, clay, organic colloids",
    },
]

SCENARIOS = [
    ("reducing low-colloid", "low Eh, stable matrix diffusion", 0.01, 0.03, "reducing"),
    ("oxidizing carbonate", "U/Np/Tc mobilized by oxidized carbonate water", 0.01, 0.03, "oxidizing"),
    ("colloid pulse", "bentonite / Fe-Mn / organic colloids remain mobile", 1.0, 0.01, "reducing"),
    ("filtered colloids", "colloids attach or are strained in narrow apertures", 1.0, 0.05, "reducing"),
]


def ensure_dirs() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    FIG_DIR.mkdir(exist_ok=True)


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def svg(width: int, height: int, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img">\n'
        "<style>"
        "text{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;fill:#172026}"
        ".small{font-size:12px;fill:#52616a}.title{font-size:18px;font-weight:700}"
        ".axis{stroke:#172026;stroke-width:1.1}.grid{stroke:#d7e0e5;stroke-width:1}"
        "</style>\n"
        f"{body}\n</svg>\n"
    )


def text(x: float, y: float, content: str, size: int = 13, anchor: str = "start",
         fill: str = "#172026", weight: str = "400", cls: str = "") -> str:
    class_attr = f' class="{cls}"' if cls else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
        f'fill="{fill}" font-weight="{weight}"{class_attr}>{esc(content)}</text>'
    )


def rect(x: float, y: float, w: float, h: float, fill: str, stroke: str = "#172026",
         sw: float = 1.0, rx: float = 4.0, opacity: float = 1.0) -> str:
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx:.1f}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>'
    )


def line(x1: float, y1: float, x2: float, y2: float, stroke: str = "#172026",
         sw: float = 1.0, dash: str | None = None, marker: bool = False) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    marker_attr = ' marker-end="url(#arrow)"' if marker else ""
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{stroke}" stroke-width="{sw}"{dash_attr}{marker_attr}/>'
    )


def polyline(points: list[tuple[float, float]], stroke: str, sw: float = 2.0,
             dash: str | None = None) -> str:
    data = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<polyline points="{data}" fill="none" stroke="{stroke}" stroke-width="{sw}"{dash_attr}/>'


def circle(cx: float, cy: float, r: float, fill: str, stroke: str = "#172026") -> str:
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}"/>'


def arrow_defs() -> str:
    return (
        "<defs><marker id='arrow' markerWidth='9' markerHeight='9' refX='8' refY='4.5' "
        "orient='auto'><path d='M0,0 L9,4.5 L0,9 z' fill='#172026'/></marker></defs>"
    )


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def chart_axes(x: int, y: int, w: int, h: int, title: str, xlab: str, ylab: str) -> str:
    parts = [text(x, y - 18, title, size=18, weight="700", cls="title")]
    parts.append(line(x, y + h, x + w, y + h, sw=1.2))
    parts.append(line(x, y, x, y + h, sw=1.2))
    parts.append(text(x + w / 2, y + h + 42, xlab, size=13, anchor="middle", cls="small"))
    parts.append(text(x - 54, y + h / 2, ylab, size=13, anchor="middle", cls="small"))
    return "\n".join(parts)


def retardation(kd_m3_kg: float, porosity: float = 0.01, bulk_density: float = 2650.0) -> float:
    return 1.0 + bulk_density * kd_m3_kg / porosity


def diffusion_penetration_m(kd_m3_kg: float, years: float, de_m2_s: float = 1e-12,
                            porosity: float = 0.01, bulk_density: float = 2650.0) -> float:
    r = retardation(kd_m3_kg, porosity, bulk_density)
    return math.sqrt(de_m2_s * years * YEAR_S / r)


def matrix_storage_m(kd_m3_kg: float, years: float, de_m2_s: float = 1e-12,
                     porosity: float = 0.01, bulk_density: float = 2650.0) -> float:
    r = retardation(kd_m3_kg, porosity, bulk_density)
    return 2.0 * porosity * math.sqrt(r * de_m2_s * years * YEAR_S / math.pi)


def colloid_fraction(k_l_kg: float, colloid_mg_l: float) -> float:
    m_kg_l = colloid_mg_l * 1e-6
    x = k_l_kg * m_kg_l
    return x / (1.0 + x)


def colloid_survival(distance_m: float, filtration_m_inv: float) -> float:
    return math.exp(-filtration_m_inv * distance_m)


def mobility_index(kd_m3_kg: float, k_l_kg: float, colloid_mg_l: float = 1.0,
                   filtration_m_inv: float = 0.01, distance_m: float = 100.0,
                   porosity: float = 0.01, bulk_density: float = 2650.0) -> float:
    aq = 1.0 / retardation(kd_m3_kg, porosity, bulk_density)
    col = colloid_fraction(k_l_kg, colloid_mg_l) * colloid_survival(distance_m, filtration_m_inv)
    return min(1.0, aq + col)


def figure_1_concept() -> None:
    body = [arrow_defs(), text(38, 34, "Fracture-flow / matrix-diffusion / colloid-facilitated transport", size=19, weight="700")]
    body.append(rect(55, 82, 590, 260, "#f3f6f8", PAL["rock"], sw=2, rx=8))
    body.append(rect(82, 180, 536, 48, PAL["water"], "#2f7896", sw=2, rx=6))
    body.append(text(350, 211, "advective water-conducting fracture", anchor="middle", fill="white", weight="700"))
    for i, x in enumerate([118, 180, 244, 500, 560]):
        body.append(circle(x, 202 + (i % 2) * 8, 7, PAL["purple"], "white"))
    body.append(text(505, 178, "mobile colloids", fill=PAL["purple"], weight="700"))
    body.append(line(615, 204, 668, 204, PAL["water"], 3, marker=True))
    body.append(text(628, 192, "flow", fill=PAL["water"], weight="700"))
    for x in [95, 170, 255, 335, 420, 510, 600]:
        body.append(line(x, 180, x - 24, 118, PAL["green"], 2, marker=True))
        body.append(line(x, 228, x + 26, 295, PAL["green"], 2, marker=True))
    body.append(text(75, 111, "matrix diffusion + sorption", fill=PAL["green"], weight="700"))
    body.append(text(365, 305, "altered fracture rim / grain-boundary pores", fill=PAL["green"], weight="700"))
    minerals = [
        (112, 142, "biotite", PAL["clay"]),
        (235, 138, "chlorite", "#6d8f59"),
        (365, 137, "Fe-Mn oxides", PAL["oxide"]),
        (515, 140, "calcite", PAL["calcite"]),
        (205, 276, "clay", PAL["clay"]),
        (432, 276, "magnetite", "#596167"),
    ]
    for mx, my, label, color in minerals:
        body.append(rect(mx - 42, my - 16, 84, 32, color, "#53616a", rx=12))
        body.append(text(mx, my + 5, label, anchor="middle", size=11, weight="700"))
    body.append(line(194, 201, 194, 148, PAL["red"], 2.2, marker=True))
    body.append(text(204, 153, "surface sorption", fill=PAL["red"], weight="700"))
    body.append(line(518, 201, 518, 250, PAL["amber"], 2.2, marker=True))
    body.append(text(528, 258, "colloid attachment / filtration", fill=PAL["amber"], weight="700"))
    (FIG_DIR / "fig1_fractured_rock_concept.svg").write_text(svg(700, 390, "\n".join(body)), encoding="utf-8")


def figure_2_multiscale_matrix() -> list[dict[str, object]]:
    rows = [
        ("fracture cm-m", "advection + dispersion", "I, Tc(VII), Se(VI)", 5, 3, 2, 4),
        ("rim mm-cm", "surface sorption + alteration", "U, Np, Cs, Sr", 4, 5, 3, 3),
        ("matrix um-mm", "matrix diffusion + storage", "Cs, Sr, Np", 3, 4, 4, 2),
        ("colloid nm-um", "mobile carrier + filtration", "Pu, Am, Th, U, Cs", 4, 4, 2, 5),
    ]
    x0, y0 = 52, 72
    col_w = [120, 182, 142, 68, 68, 68, 68]
    headers = ["scale", "dominant process", "sensitive RN", "H", "C", "M", "colloid"]
    colors = ["#f5f7f8", "#dbe9ef", "#a9d0db", "#6ba9bd", "#247892", "#0f4d61"]
    body = [text(40, 34, "Multiscale process relevance matrix", size=20, weight="700")]
    x = x0
    for w, h in zip(col_w, headers):
        body.append(text(x + w / 2, y0 - 12, h, anchor="middle", weight="700", size=12))
        x += w
    out: list[dict[str, object]] = []
    for r, row in enumerate(rows):
        y = y0 + r * 58
        vals = row[:3]
        scores = row[3:]
        x = x0
        for i, val in enumerate(vals):
            body.append(rect(x, y, col_w[i] - 4, 48, "#eef3f5", "#ffffff", rx=3))
            body.append(text(x + 6, y + 28, str(val), size=11))
            x += col_w[i]
        for score in scores:
            body.append(rect(x, y, 64, 48, colors[score], "#ffffff", rx=3))
            body.append(text(x + 32, y + 30, str(score), anchor="middle", weight="700"))
            x += 68
        out.append({
            "scale": row[0],
            "dominant_process": row[1],
            "sensitive_radionuclides": row[2],
            "hydrological_score": row[3],
            "chemical_score": row[4],
            "mechanical_score": row[5],
            "colloid_score": row[6],
        })
    body.append(text(62, 346, "score 1-5: screening importance for long-term far-field migration", cls="small"))
    (FIG_DIR / "fig2_multiscale_process_matrix.svg").write_text(svg(720, 380, "\n".join(body)), encoding="utf-8")
    return out


def figure_3_kd_retardation() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for item in NUCLIDES:
        rox = retardation(item["kd_oxidizing_m3_kg"])
        rred = retardation(item["kd_reducing_m3_kg"])
        rows.append({
            "nuclide": item["name"],
            "kd_oxidizing_m3_kg": item["kd_oxidizing_m3_kg"],
            "kd_reducing_m3_kg": item["kd_reducing_m3_kg"],
            "retardation_oxidizing": round(rox, 2),
            "retardation_reducing": round(rred, 2),
        })
    x, y, w, h = 108, 62, 520, 305
    body = [chart_axes(x, y, w, h, "Sorption Kd translated to matrix retardation factor", "retardation factor R, log scale", "radionuclide")]
    xmin, xmax = 1.0, 2_000_000.0
    def px(v: float) -> float:
        return x + (math.log10(max(v, xmin)) - math.log10(xmin)) / (math.log10(xmax) - math.log10(xmin)) * w
    for tick in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        xx = px(tick)
        body.append(line(xx, y, xx, y + h, PAL["grid"], 1))
        body.append(text(xx, y + h + 20, f"{tick:g}", anchor="middle", size=10, cls="small"))
    for i, row in enumerate(rows):
        yy = y + 14 + i * 25
        body.append(text(x - 8, yy + 9, row["nuclide"], anchor="end", size=11))
        body.append(rect(x, yy, px(row["retardation_oxidizing"]) - x, 9, PAL["red"], "none", rx=1))
        body.append(rect(x, yy + 11, px(row["retardation_reducing"]) - x, 9, PAL["blue"], "none", rx=1))
    body.append(text(480, 88, "oxidizing", fill=PAL["red"], weight="700"))
    body.append(text(480, 108, "reducing", fill=PAL["blue"], weight="700"))
    body.append(text(130, 386, "R = 1 + rho_b Kd / phi; phi=0.01, rho_b=2650 kg/m3", cls="small"))
    (FIG_DIR / "fig3_kd_retardation.svg").write_text(svg(710, 430, "\n".join(body)), encoding="utf-8")
    return rows


def figure_4_matrix_diffusion() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    years = 100.0
    for item in NUCLIDES:
        kd = item["kd_oxidizing_m3_kg"]
        pen = diffusion_penetration_m(kd, years)
        store = matrix_storage_m(kd, years)
        rows.append({
            "nuclide": item["name"],
            "kd_for_screening_m3_kg": kd,
            "penetration_depth_m_100yr": round(pen, 6),
            "matrix_storage_m_100yr_per_unit_concentration": round(store, 6),
        })
    cs_dapp = (0.05 ** 2) / (5.0 * YEAR_S)
    np_dapp = (0.02 ** 2) / (5.0 * YEAR_S)
    x, y, w, h = 100, 62, 520, 300
    body = [chart_axes(x, y, w, h, "Matrix diffusion depth: model envelope and Grimsel LTD targets", "penetration depth (m, log scale)", "radionuclide")]
    xmin, xmax = 1e-4, 0.2
    def px(v: float) -> float:
        return x + (math.log10(max(v, xmin)) - math.log10(xmin)) / (math.log10(xmax) - math.log10(xmin)) * w
    for tick in [1e-4, 1e-3, 1e-2, 0.05, 0.1]:
        xx = px(tick)
        body.append(line(xx, y, xx, y + h, PAL["grid"], 1))
        body.append(text(xx, y + h + 20, f"{tick:g}", anchor="middle", size=10, cls="small"))
    for i, row in enumerate(rows):
        yy = y + 12 + i * 24
        color = PAL["red"] if row["nuclide"] in {"I-129", "Tc-99", "Se-79"} else PAL["blue"]
        body.append(text(x - 8, yy + 9, row["nuclide"], anchor="end", size=11))
        body.append(rect(x, yy, px(row["penetration_depth_m_100yr"]) - x, 14, color, "none", rx=2))
    body.append(line(px(0.05), y, px(0.05), y + h, PAL["green"], 2, dash="6 4"))
    body.append(line(px(0.02), y, px(0.02), y + h, PAL["amber"], 2, dash="6 4"))
    body.append(text(px(0.05) + 5, y + 18, "GTS Cs-137 up to 5 cm", fill=PAL["green"], size=12))
    body.append(text(px(0.02) + 5, y + 38, "GTS Np-237 up to 2 cm", fill=PAL["amber"], size=12))
    body.append(text(122, 392, f"Implied Dapp over 5 yr: Cs {cs_dapp:.2e} m2/s, Np {np_dapp:.2e} m2/s", cls="small"))
    (FIG_DIR / "fig4_matrix_diffusion_depth.svg").write_text(svg(710, 430, "\n".join(body)), encoding="utf-8")
    rows.append({"nuclide": "GTS Cs-137 target", "penetration_depth_m_5yr": 0.05, "implied_dapp_m2_s": f"{cs_dapp:.3e}"})
    rows.append({"nuclide": "GTS Np-237 target", "penetration_depth_m_5yr": 0.02, "implied_dapp_m2_s": f"{np_dapp:.3e}"})
    return rows


def figure_5_colloid_association() -> list[dict[str, object]]:
    concentrations = [0.001, 0.01, 0.1, 1, 10, 100]
    k_values = [1e2, 1e4, 1e6]
    colors = [PAL["green"], PAL["blue"], PAL["red"]]
    rows: list[dict[str, object]] = []
    for k in k_values:
        for c in concentrations:
            rows.append({"colloid_k_l_kg": k, "colloid_mg_l": c, "mobile_colloid_fraction": round(colloid_fraction(k, c), 6)})
    x, y, w, h = 78, 65, 520, 285
    body = [chart_axes(x, y, w, h, "Fraction of RN associated with mobile colloids", "colloid concentration (mg/L, log scale)", "mobile colloid-associated fraction")]
    def px(c: float) -> float:
        return x + (math.log10(c) - math.log10(0.001)) / (math.log10(100) - math.log10(0.001)) * w
    def py(f: float) -> float:
        return y + h - f * h
    for frac in [0, 0.25, 0.5, 0.75, 1.0]:
        yy = py(frac)
        body.append(line(x, yy, x + w, yy, PAL["grid"], 1))
        body.append(text(x - 8, yy + 4, f"{frac:.2f}", anchor="end", size=10, cls="small"))
    for k, color in zip(k_values, colors):
        pts = [(px(c), py(colloid_fraction(k, c))) for c in concentrations]
        body.append(polyline(pts, color, 2.5))
        body.append(text(410, py(colloid_fraction(k, 3.0)) - 4, f"Kcol={k:.0e} L/kg", fill=color, weight="700", size=12))
    for tick in concentrations:
        xx = px(tick)
        body.append(line(xx, y + h, xx, y + h + 5))
        body.append(text(xx, y + h + 22, f"{tick:g}", anchor="middle", size=10, cls="small"))
    (FIG_DIR / "fig5_colloid_association.svg").write_text(svg(690, 420, "\n".join(body)), encoding="utf-8")
    return rows


def figure_6_colloid_filtration() -> list[dict[str, object]]:
    distances = [0, 10, 25, 50, 100, 200, 500]
    lambdas = [0.001, 0.01, 0.05]
    colors = [PAL["green"], PAL["blue"], PAL["red"]]
    rows: list[dict[str, object]] = []
    for lam in lambdas:
        for d in distances:
            rows.append({"filtration_m_inv": lam, "distance_m": d, "survival_fraction": round(colloid_survival(d, lam), 6)})
    x, y, w, h = 78, 65, 520, 285
    body = [chart_axes(x, y, w, h, "Colloid filtration controls whether facilitation persists", "distance along fracture (m)", "colloid survival fraction")]
    def px(d: float) -> float:
        return x + d / 500.0 * w
    def py(s: float) -> float:
        return y + h - s * h
    for frac in [0, 0.25, 0.5, 0.75, 1.0]:
        yy = py(frac)
        body.append(line(x, yy, x + w, yy, PAL["grid"], 1))
        body.append(text(x - 8, yy + 4, f"{frac:.2f}", anchor="end", size=10, cls="small"))
    for lam, color in zip(lambdas, colors):
        pts = [(px(d), py(colloid_survival(d, lam))) for d in distances]
        body.append(polyline(pts, color, 2.5))
        body.append(text(420, py(colloid_survival(330, lam)) - 4, f"lambda={lam:g} m-1", fill=color, weight="700", size=12))
    for tick in [0, 100, 200, 500]:
        xx = px(tick)
        body.append(line(xx, y + h, xx, y + h + 5))
        body.append(text(xx, y + h + 22, str(tick), anchor="middle", size=10, cls="small"))
    (FIG_DIR / "fig6_colloid_filtration.svg").write_text(svg(690, 420, "\n".join(body)), encoding="utf-8")
    return rows


def figure_7_mobility_index() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for item in NUCLIDES:
        ox = mobility_index(item["kd_oxidizing_m3_kg"], item["colloid_k_l_kg"], 1.0, 0.01, 100.0)
        red = mobility_index(item["kd_reducing_m3_kg"], item["colloid_k_l_kg"], 1.0, 0.01, 100.0)
        no_col = 1.0 / retardation(item["kd_oxidizing_m3_kg"])
        rows.append({
            "nuclide": item["name"],
            "aqueous_only_oxidizing_index": round(no_col, 8),
            "with_colloid_oxidizing_index": round(ox, 8),
            "with_colloid_reducing_index": round(red, 8),
        })
    x, y, w, h = 115, 62, 520, 305
    body = [chart_axes(x, y, w, h, "Relative mobility index: aqueous retardation vs colloid facilitation", "mobility index, log scale", "radionuclide")]
    xmin, xmax = 1e-7, 1.0
    def px(v: float) -> float:
        return x + (math.log10(max(v, xmin)) - math.log10(xmin)) / (math.log10(xmax) - math.log10(xmin)) * w
    for tick in [1e-7, 1e-5, 1e-3, 1e-1, 1.0]:
        xx = px(tick)
        body.append(line(xx, y, xx, y + h, PAL["grid"], 1))
        body.append(text(xx, y + h + 20, f"{tick:g}", anchor="middle", size=10, cls="small"))
    for i, row in enumerate(rows):
        yy = y + 13 + i * 25
        body.append(text(x - 8, yy + 9, row["nuclide"], anchor="end", size=11))
        body.append(rect(x, yy, px(row["aqueous_only_oxidizing_index"]) - x, 7, PAL["green"], "none", rx=1))
        body.append(rect(x, yy + 9, px(row["with_colloid_oxidizing_index"]) - x, 7, PAL["red"], "none", rx=1))
        body.append(rect(x, yy + 18, px(row["with_colloid_reducing_index"]) - x, 7, PAL["blue"], "none", rx=1))
    body.append(text(430, 86, "aq only ox.", fill=PAL["green"], weight="700"))
    body.append(text(430, 106, "with colloids ox.", fill=PAL["red"], weight="700"))
    body.append(text(430, 126, "with colloids red.", fill=PAL["blue"], weight="700"))
    body.append(text(130, 390, "Assumption: 1 mg/L colloids, Kcol by RN, filtration lambda=0.01 m-1 over 100 m", cls="small"))
    (FIG_DIR / "fig7_mobility_index.svg").write_text(svg(730, 430, "\n".join(body)), encoding="utf-8")
    return rows


def figure_8_scenario_matrix() -> list[dict[str, object]]:
    indicators = ["weak anions", "redox RN", "strong actinides", "Cs/Sr", "biosphere flux"]
    scenario_scores = {
        "reducing low-colloid": [2, 2, 1, 2, 2],
        "oxidizing carbonate": [5, 5, 3, 2, 5],
        "colloid pulse": [3, 4, 5, 4, 4],
        "filtered colloids": [3, 3, 2, 3, 3],
    }
    colors = ["#f5f7f8", "#e0eff1", "#b9dbdf", "#8ac1c7", "#e2b968", "#c94f44"]
    x0, y0, cw, ch = 165, 82, 94, 50
    body = [text(36, 34, "Scenario-to-risk indicator matrix", size=20, weight="700")]
    for c, ind in enumerate(indicators):
        body.append(text(x0 + c * cw + cw / 2, y0 - 16, ind, anchor="middle", size=11, weight="700"))
    out: list[dict[str, object]] = []
    for r, (scenario, scores) in enumerate(scenario_scores.items()):
        body.append(text(x0 - 10, y0 + r * ch + 31, scenario, anchor="end", size=11))
        for c, score in enumerate(scores):
            body.append(rect(x0 + c * cw, y0 + r * ch, cw - 4, ch - 4, colors[score], "#ffffff", rx=3))
            body.append(text(x0 + c * cw + cw / 2 - 2, y0 + r * ch + 31, str(score), anchor="middle", weight="700"))
            out.append({"scenario": scenario, "indicator": indicators[c], "risk_score_1_5": score})
    body.append(text(120, 332, "1 low under screening assumptions; 5 first-order migration concern", cls="small"))
    (FIG_DIR / "fig8_scenario_risk_matrix.svg").write_text(svg(720, 360, "\n".join(body)), encoding="utf-8")
    return out


def source_rows() -> list[dict[str, object]]:
    return [
        {
            "source_id": "S1",
            "source": "EGU26-5127",
            "url": "https://doi.org/10.5194/egusphere-egu26-5127",
            "data_or_claim": "I, Np, Tc sorption depends on redox, ionic strength, pH, complexing ions, microorganisms; high ionic strength, high temperature, organic ligands and microorganisms are knowledge gaps",
            "use": "problem framing and uncertainty matrix",
        },
        {
            "source_id": "S2",
            "source": "SKB TR-10-50",
            "url": "https://www.skb.com/publication/2166831",
            "data_or_claim": "SR-Site radionuclide transport report for crystalline-rock safety assessment",
            "use": "far-field transport concepts and parameter-data lane",
        },
        {
            "source_id": "S3",
            "source": "SKB R-10-48",
            "url": "https://skb.com/publication/2192981",
            "data_or_claim": "Bedrock Kd data and uncertainty assessment for SR-Site geosphere transport calculations",
            "use": "order-of-magnitude Kd grouping; replace with table extraction for calibration",
        },
        {
            "source_id": "S4",
            "source": "Grimsel LTD",
            "url": "https://www.grimsel.com/gts-projects/ltd/ltd-diffusion-processes-study",
            "data_or_claim": "Cs-137 observed up to 5 cm into matrix; Np-237 up to 2 cm from shear zone",
            "use": "matrix diffusion calibration targets and figure markers",
        },
        {
            "source_id": "S5",
            "source": "Grimsel CRR experiment",
            "url": "https://doi.org/10.1016/S0927-7757(02)00556-3",
            "data_or_claim": "bentonite colloids influence in situ retardation of tri- and tetravalent actinides in fractured rock",
            "use": "colloid-facilitated transport scenario",
        },
        {
            "source_id": "S6",
            "source": "RES3T",
            "url": "https://www.re3data.org/repository/r3d100010241",
            "data_or_claim": "mineral-specific SCM database with surface areas, site data, and surface complexation reactions",
            "use": "future surface-complexation parameter source",
        },
        {
            "source_id": "S7",
            "source": "NEA Sorption Project",
            "url": "https://www.oecd-nea.org/jcms/pl_27447/sorption-project",
            "data_or_claim": "benchmark systems include Np-hematite, Se-goethite, U-quartz, Ni-clays, Np-montmorillonite",
            "use": "model validation cases for mineral-specific sorption",
        },
        {
            "source_id": "S8",
            "source": "ThermoChimie",
            "url": "https://www.thermochimie-tdb.com/",
            "data_or_claim": "radionuclide thermodynamic database for pH 6-14, below 80 C, Eh -0.5 to +0.5 V; compatible with PHREEQC and PFLOTRAN",
            "use": "speciation and solubility database route",
        },
    ]


def nuclide_parameter_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for item in NUCLIDES:
        row = {key: value for key, value in item.items()}
        row["retardation_oxidizing_phi_0_01"] = round(retardation(item["kd_oxidizing_m3_kg"]), 2)
        row["retardation_reducing_phi_0_01"] = round(retardation(item["kd_reducing_m3_kg"]), 2)
        row["colloid_fraction_1mg_l"] = round(colloid_fraction(item["colloid_k_l_kg"], 1.0), 6)
        row["mobility_index_oxidizing_1mg_l_lambda_0_01_100m"] = round(
            mobility_index(item["kd_oxidizing_m3_kg"], item["colloid_k_l_kg"]), 8
        )
        rows.append(row)
    return rows


def main() -> None:
    ensure_dirs()
    write_csv(DATA_DIR / "fracture_colloid_parameter_sources.csv", source_rows())
    write_csv(DATA_DIR / "fracture_colloid_nuclide_parameters.csv", nuclide_parameter_rows())

    figure_1_concept()
    multiscale = figure_2_multiscale_matrix()
    kd_rows = figure_3_kd_retardation()
    diffusion_rows = figure_4_matrix_diffusion()
    assoc_rows = figure_5_colloid_association()
    filter_rows = figure_6_colloid_filtration()
    mobility_rows = figure_7_mobility_index()
    scenario_rows = figure_8_scenario_matrix()

    combined: list[dict[str, object]] = []
    for name, rows in [
        ("multiscale_process_matrix", multiscale),
        ("kd_retardation", kd_rows),
        ("matrix_diffusion", diffusion_rows),
        ("colloid_association", assoc_rows),
        ("colloid_filtration", filter_rows),
        ("mobility_index", mobility_rows),
        ("scenario_matrix", scenario_rows),
    ]:
        for row in rows:
            out = {"dataset": name}
            out.update(row)
            combined.append(out)
    write_csv(DATA_DIR / "fracture_colloid_screening_results.csv", combined)

    cs_dapp = (0.05 ** 2) / (5.0 * YEAR_S)
    np_dapp = (0.02 ** 2) / (5.0 * YEAR_S)
    key = {
        "i129_retardation": round(retardation(1e-5), 2),
        "tc99_retardation_oxidizing": round(retardation(1e-5), 2),
        "tc99_retardation_reducing": round(retardation(5e-2), 2),
        "cs137_retardation": round(retardation(2e-2), 2),
        "pu_retardation_reducing": round(retardation(1.0), 2),
        "grimsel_cs137_implied_dapp_m2_s": f"{cs_dapp:.3e}",
        "grimsel_np237_implied_dapp_m2_s": f"{np_dapp:.3e}",
        "colloid_fraction_k1e6_1mg_l": round(colloid_fraction(1e6, 1.0), 4),
        "colloid_survival_100m_lambda_0_01": round(colloid_survival(100.0, 0.01), 4),
        "pu_mobility_index_with_1mg_l_colloid": round(mobility_index(1e-1, 1e6), 6),
    }
    summary = {
        "status": "screening_calculations_not_site_calibration",
        "router": {
            "scenario": ["radionuclide_transport", "fractured_rock_contaminant_transport", "long_term_environmental_risk"],
            "core_coupling_level": "HC",
            "thmc_extensions": ["temperature-dependent speciation/diffusion", "fracture aperture/filtering evolution", "mineral alteration and colloid generation"],
        },
        "generated_figures": sorted(p.name for p in FIG_DIR.glob("fig*.svg")),
        "key_results": key,
        "limitations": [
            "Kd values are illustrative grouped screening values; replace with site- and mineral-specific tables before safety assessment.",
            "The mobility index is a dimensionless ranking metric, not a breakthrough-curve prediction.",
            "Grimsel LTD depths are field targets from public project description and are not full raw concentration profiles.",
            "Colloid facilitation requires stable mobile colloids and weak filtration; strong filtration collapses the effect.",
        ],
    }
    (DATA_DIR / "fracture_colloid_screening_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
