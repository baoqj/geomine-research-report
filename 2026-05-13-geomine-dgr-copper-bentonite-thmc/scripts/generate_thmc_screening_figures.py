#!/usr/bin/env python3
"""Generate screening THMC calculations and SVG figures for the DGR paper.

The calculations are deliberately low-order. They turn literature-derived
parameter ranges into transparent screening envelopes; they are not a calibrated
repository safety assessment.
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
R = 8.314462618
F = 96485.33212

PALETTE = {
    "ink": "#172026",
    "muted": "#52616a",
    "grid": "#d7e0e5",
    "blue": "#1f6f9f",
    "teal": "#249186",
    "green": "#5d8f3a",
    "amber": "#d08b2f",
    "red": "#c94f44",
    "purple": "#6f5aa7",
    "sand": "#d8bf84",
    "rock": "#9aa6ad",
    "bentonite": "#c9a85d",
    "copper": "#b86b2f",
    "water": "#5aa6c8",
}


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
        "text{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;"
        "fill:#172026} .small{font-size:12px;fill:#52616a}"
        ".label{font-size:14px}.title{font-size:18px;font-weight:700}"
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


def polyline(points: list[tuple[float, float]], stroke: str, sw: float = 2.0) -> str:
    data = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<polyline points="{data}" fill="none" stroke="{stroke}" stroke-width="{sw}"/>'


def circle(cx: float, cy: float, r: float, fill: str, stroke: str = "#172026") -> str:
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}"/>'


def arrow_defs() -> str:
    return (
        "<defs><marker id='arrow' markerWidth='9' markerHeight='9' refX='8' refY='4.5' "
        "orient='auto'><path d='M0,0 L9,4.5 L0,9 z' fill='#172026'/></marker></defs>"
    )


def water_viscosity_pa_s(temp_c: float) -> float:
    temp_k = temp_c + 273.15
    return 2.414e-5 * 10 ** (247.8 / (temp_k - 140.0))


def heat_power_per_m(t_year: float) -> float:
    q0 = 120.0
    terms = [(0.62, 35.0), (0.28, 250.0), (0.10, 3000.0)]
    return q0 * sum(weight * math.exp(-t_year / tau) for weight, tau in terms)


def delta_t_radial(q_per_m: float, conductivity: float = 1.5,
                   r_canister: float = 0.55, r_far: float = 10.0) -> float:
    return q_per_m / (2.0 * math.pi * conductivity) * math.log(r_far / r_canister)


def osmotic_pressure_mpa(mol_l: float, temp_k: float = 298.15) -> float:
    return 2.0 * R * temp_k * (mol_l * 1000.0) / 1e6


def copper_depth_mm(conc_hs_umol_l: float, diffusion_m2_s: float,
                    years: float = 100_000.0, buffer_m: float = 0.35) -> float:
    conc_mol_m3 = conc_hs_umol_l * 1e-3
    flux = diffusion_m2_s * conc_mol_m3 / buffer_m
    molar_mass_cu = 0.063546
    density_cu = 8960.0
    stoich_cu_per_s = 2.0
    rate_m_s = stoich_cu_per_s * molar_mass_cu / density_cu * flux
    return rate_m_s * YEAR_S * years * 1000.0


def h2_pressure_rate_mpa_yr(current_uamp_m2: float, area_m2: float = 10.0,
                            gas_volume_m3: float = 0.01, temp_k: float = 300.0) -> float:
    current_a_m2 = current_uamp_m2 * 1e-6
    mol_s = area_m2 * current_a_m2 / (2.0 * F)
    return (R * temp_k / gas_volume_m3) * mol_s * YEAR_S / 1e6


def retardation(kd_m3_kg: float, bulk_density_kg_m3: float = 1700.0,
                porosity: float = 0.35) -> float:
    return 1.0 + bulk_density_kg_m3 * kd_m3_kg / porosity


def diffusion_time_years(kd_m3_kg: float, temp_c: float = 25.0,
                         length_m: float = 0.35, de25_m2_s: float = 1e-10) -> float:
    mu25 = water_viscosity_pa_s(25.0)
    mu_t = water_viscosity_pa_s(temp_c)
    d_ratio = (temp_c + 273.15) / 298.15 * mu25 / mu_t
    rd = retardation(kd_m3_kg)
    return length_m * length_m * rd / (de25_m2_s * d_ratio) / YEAR_S


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    fieldnames: list[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def chart_axes(x: int, y: int, w: int, h: int, title: str, xlab: str, ylab: str) -> str:
    parts = [text(x, y - 18, title, size=18, weight="700", cls="title")]
    parts.append(line(x, y + h, x + w, y + h, sw=1.2))
    parts.append(line(x, y, x, y + h, sw=1.2))
    parts.append(text(x + w / 2, y + h + 42, xlab, size=13, anchor="middle", cls="small"))
    parts.append(text(x - 48, y + h / 2, ylab, size=13, anchor="middle", cls="small"))
    return "\n".join(parts)


def figure_1_concept() -> None:
    body = [arrow_defs(), text(44, 34, "Near-field THMC system", size=20, weight="700")]
    body.append(rect(70, 80, 560, 210, "#f3f6f8", PALETTE["rock"], sw=2, rx=10))
    body.append(text(350, 306, "fractured crystalline rock / groundwater boundary", anchor="middle", cls="small"))
    body.append(rect(140, 115, 420, 140, "#d9c17b", "#9d7d2d", sw=2, rx=10))
    body.append(text(350, 274, "compacted bentonite buffer", anchor="middle", cls="small"))
    body.append(rect(265, 135, 170, 100, "#c57a3a", "#7b3f1f", sw=2, rx=12))
    body.append(text(350, 190, "Cu-coated UFC", anchor="middle", fill="white", weight="700"))
    body.append(rect(250, 120, 200, 130, "none", "#4b3f2e", sw=2.5, rx=14))
    body.append(text(350, 116, "gap / interface", anchor="middle", cls="small"))
    body.append(line(352, 78, 352, 132, PALETTE["red"], 2.5, marker=True))
    body.append(text(362, 74, "decay heat Q(t)", fill=PALETTE["red"], weight="700"))
    body.append(line(625, 160, 455, 160, PALETTE["water"], 3, marker=True))
    body.append(text(633, 154, "saline fracture water", fill=PALETTE["water"], weight="700"))
    body.append(line(622, 210, 455, 210, PALETTE["purple"], 2.5, marker=True))
    body.append(text(633, 216, "HS-, SO4, pH/Eh", fill=PALETTE["purple"], weight="700"))
    body.append(line(292, 238, 210, 315, PALETTE["green"], 2.5, marker=True))
    body.append(text(70, 333, "swelling / self-sealing", fill=PALETTE["green"], weight="700"))
    body.append(line(408, 238, 515, 318, PALETTE["amber"], 2.5, marker=True))
    body.append(text(520, 333, "H2 gas pressure", fill=PALETTE["amber"], weight="700"))
    body.append(line(350, 235, 350, 330, PALETTE["blue"], 2.5, marker=True))
    body.append(text(214, 356, "radionuclide diffusion + sorption", fill=PALETTE["blue"], weight="700"))
    (FIG_DIR / "fig1_nearfield_concept.svg").write_text(svg(700, 390, "\n".join(body)), encoding="utf-8")


def figure_2_coupling_matrix() -> list[dict[str, object]]:
    labels = ["T", "H", "M", "C"]
    matrix = [
        [0, 3, 2, 4],
        [2, 0, 4, 5],
        [1, 5, 0, 3],
        [1, 3, 3, 0],
    ]
    notes = {
        ("T", "C"): "temperature-dependent diffusion/reactions",
        ("H", "C"): "sulfide and radionuclide transport",
        ("M", "H"): "swelling/fracture aperture controls permeability",
        ("H", "M"): "pore pressure and saturation control swelling stress",
    }
    colors = ["#f5f7f8", "#dbe9ef", "#a9d0db", "#6ba9bd", "#247892", "#0f4d61"]
    body = [text(36, 34, "THMC coupling intensity matrix", size=20, weight="700")]
    x0, y0, cell = 130, 70, 78
    for i, label in enumerate(labels):
        body.append(text(x0 + i * cell + cell / 2, y0 - 18, f"to {label}", anchor="middle", weight="700"))
        body.append(text(x0 - 20, y0 + i * cell + cell / 2 + 5, f"from {label}", anchor="end", weight="700"))
    rows: list[dict[str, object]] = []
    for r, src in enumerate(labels):
        for c, dst in enumerate(labels):
            score = matrix[r][c]
            body.append(rect(x0 + c * cell, y0 + r * cell, cell - 4, cell - 4, colors[score], "#ffffff", sw=1, rx=3))
            body.append(text(x0 + c * cell + cell / 2 - 2, y0 + r * cell + cell / 2 + 6, "-" if score == 0 else str(score), anchor="middle", size=18, weight="700"))
            rows.append({"from": src, "to": dst, "coupling_score_0_5": score, "note": notes.get((src, dst), "")})
    body.append(text(492, 116, "0 none", cls="small"))
    body.append(text(492, 146, "3 material feedback", cls="small"))
    body.append(text(492, 176, "5 first-order control", cls="small"))
    (FIG_DIR / "fig2_coupling_matrix.svg").write_text(svg(660, 430, "\n".join(body)), encoding="utf-8")
    return rows


def figure_3_thermal() -> list[dict[str, object]]:
    times = [0, 1, 5, 10, 25, 50, 75, 100, 200, 500, 1000, 5000, 10000]
    rows: list[dict[str, object]] = []
    for t in times:
        q = heat_power_per_m(t)
        dt = delta_t_radial(q)
        surface = 20.0 + dt
        d_ratio = (surface + 273.15) / 298.15 * water_viscosity_pa_s(25.0) / water_viscosity_pa_s(surface)
        rows.append({
            "time_year": t,
            "heat_power_w_per_m": round(q, 4),
            "radial_delta_t_c": round(dt, 4),
            "canister_surface_temp_c": round(surface, 4),
            "free_water_diffusion_ratio_vs_25c": round(d_ratio, 4),
        })
    x, y, w, h = 75, 72, 520, 270
    body = [chart_axes(x, y, w, h, "Heat decay and screening canister temperature", "time after closure (yr, log scale)", "temperature / heat")]
    for frac in [0, 0.25, 0.5, 0.75, 1.0]:
        yy = y + h * frac
        body.append(line(x, yy, x + w, yy, "#d7e0e5", 1))
    def px(t: float) -> float:
        return x + (math.log10(t + 1.0) / math.log10(10001.0)) * w
    def py_temp(temp: float) -> float:
        return y + h - ((temp - 20.0) / 50.0) * h
    def py_q(q: float) -> float:
        return y + h - (q / 130.0) * h
    temp_points = [(px(r["time_year"]), py_temp(r["canister_surface_temp_c"])) for r in rows]
    q_points = [(px(r["time_year"]), py_q(r["heat_power_w_per_m"])) for r in rows]
    body.append(polyline(q_points, PALETTE["red"], 2.5))
    body.append(polyline(temp_points, PALETTE["blue"], 2.5))
    for tick in [0, 10, 100, 1000, 10000]:
        xx = px(tick)
        body.append(line(xx, y + h, xx, y + h + 5))
        body.append(text(xx, y + h + 22, str(tick), anchor="middle", size=11, cls="small"))
    for temp in [20, 40, 60]:
        yy = py_temp(temp)
        body.append(text(x - 8, yy + 4, f"{temp} C", anchor="end", size=11, cls="small"))
    body.append(text(402, 96, "red: Q' W/m", fill=PALETTE["red"], weight="700"))
    body.append(text(402, 118, "blue: T surface C", fill=PALETTE["blue"], weight="700"))
    body.append(line(x, py_temp(100), x + w, py_temp(100), PALETTE["amber"], 1.5, dash="5 4"))
    body.append(text(424, 82, "NWMO design FAQ: surface <100 C", fill=PALETTE["amber"], size=12))
    (FIG_DIR / "fig3_thermal_decay_temperature.svg").write_text(svg(670, 410, "\n".join(body)), encoding="utf-8")
    return rows


def figure_4_salinity() -> list[dict[str, object]]:
    concentrations = [0.0, 0.01, 0.1, 0.3, 1.0]
    max_factor = [1.0, 0.90, 0.65, 0.45, 0.30]
    final_factor = [1.0, 0.85, 0.55, 0.30, 0.10]
    rho_d, rho_s = 1700.0, 2700.0
    e = rho_s / rho_d - 1.0
    k_di = 1e-13 * e ** 3.74 / (1.0 + e)
    k_brine = 1e-9 * e ** 11.86
    rows: list[dict[str, object]] = []
    for c, m, f in zip(concentrations, max_factor, final_factor):
        rows.append({
            "nacl_mol_l": c,
            "osmotic_pressure_mpa": round(osmotic_pressure_mpa(c), 4),
            "swelling_pressure_max_factor": m,
            "swelling_pressure_long_term_factor": f,
            "mx80_di_k_m_s_at_e_0_588": f"{k_di:.3e}",
            "mx80_brine_k_m_s_at_e_0_588": f"{k_brine:.3e}",
            "brine_to_di_k_ratio": round(k_brine / k_di, 1),
        })
    x, y, w, h = 75, 70, 520, 270
    body = [chart_axes(x, y, w, h, "Salinity weakens swelling and raises permeability envelope", "NaCl concentration (mol/L)", "normalized swelling pressure")]
    for frac in [0, 0.25, 0.5, 0.75, 1.0]:
        yy = y + h * frac
        body.append(line(x, yy, x + w, yy, "#d7e0e5", 1))
        body.append(text(x - 8, yy + 4, f"{1 - frac:.2f}", anchor="end", size=11, cls="small"))
    def px(c: float) -> float:
        return x + (math.log10(c + 0.01) - math.log10(0.01)) / (math.log10(1.01) - math.log10(0.01)) * w
    def py(v: float) -> float:
        return y + h - v * h
    max_points = [(px(c), py(v)) for c, v in zip(concentrations, max_factor)]
    final_points = [(px(c), py(v)) for c, v in zip(concentrations, final_factor)]
    body.append(polyline(max_points, PALETTE["teal"], 2.5))
    body.append(polyline(final_points, PALETTE["red"], 2.5))
    for c, m, f in zip(concentrations, max_factor, final_factor):
        body.append(circle(px(c), py(m), 4.5, PALETTE["teal"], "white"))
        body.append(circle(px(c), py(f), 4.5, PALETTE["red"], "white"))
    for tick in [0, 0.01, 0.1, 1.0]:
        xx = px(tick)
        body.append(line(xx, y + h, xx, y + h + 5))
        body.append(text(xx, y + h + 22, str(tick), anchor="middle", size=11, cls="small"))
    body.append(text(365, 100, "early maximum", fill=PALETTE["teal"], weight="700"))
    body.append(text(365, 122, "long-term brine state", fill=PALETTE["red"], weight="700"))
    body.append(text(330, 316, f"MX-80 brine k / DI k at e=0.588: {k_brine / k_di:.0f}x", size=12, cls="small"))
    (FIG_DIR / "fig4_salinity_swelling_permeability.svg").write_text(svg(680, 410, "\n".join(body)), encoding="utf-8")
    return rows


def figure_5_corrosion() -> list[dict[str, object]]:
    concentrations = [1, 3, 10, 30, 100, 120]
    diffusions = [1e-12, 1e-11, 1e-10, 3e-10]
    colors = [PALETTE["green"], PALETTE["blue"], PALETTE["red"], PALETTE["purple"]]
    rows: list[dict[str, object]] = []
    for d in diffusions:
        for c in concentrations:
            rows.append({
                "hs_umol_l": c,
                "effective_diffusion_m2_s": f"{d:.1e}",
                "cu_depth_mm_100kyr": round(copper_depth_mm(c, d), 5),
            })
    x, y, w, h = 82, 70, 520, 270
    body = [chart_axes(x, y, w, h, "Sulfide transport-limited copper corrosion envelope", "HS- concentration (umol/L, log scale)", "Cu penetration over 100 kyr (mm, log scale)")]
    ymin, ymax = 0.0005, 30.0
    def px(c: float) -> float:
        return x + (math.log10(c) - math.log10(1.0)) / (math.log10(120.0) - math.log10(1.0)) * w
    def py(v: float) -> float:
        return y + h - (math.log10(v) - math.log10(ymin)) / (math.log10(ymax) - math.log10(ymin)) * h
    for val in [0.001, 0.01, 0.1, 1, 3, 10]:
        yy = py(val)
        body.append(line(x, yy, x + w, yy, "#d7e0e5", 1))
        body.append(text(x - 8, yy + 4, str(val), anchor="end", size=10, cls="small"))
    for d, color in zip(diffusions, colors):
        pts = [(px(c), py(max(copper_depth_mm(c, d), ymin))) for c in concentrations]
        body.append(polyline(pts, color, 2.5))
        body.append(text(430, py(copper_depth_mm(40, d)) - 4, f"De={d:.0e}", fill=color, weight="700", size=12))
    threshold_y = py(3.0)
    body.append(line(x, threshold_y, x + w, threshold_y, PALETTE["amber"], 1.5, dash="6 4"))
    body.append(text(385, threshold_y - 7, "3 mm coating reference", fill=PALETTE["amber"], size=12))
    for tick in [1, 10, 100, 120]:
        xx = px(tick)
        body.append(line(xx, y + h, xx, y + h + 5))
        body.append(text(xx, y + h + 22, str(tick), anchor="middle", size=11, cls="small"))
    (FIG_DIR / "fig5_sulfide_copper_corrosion.svg").write_text(svg(700, 410, "\n".join(body)), encoding="utf-8")
    return rows


def figure_6_h2() -> list[dict[str, object]]:
    currents = [0.1, 1.0, 10.0]
    colors = [PALETTE["green"], PALETTE["blue"], PALETTE["red"]]
    times = [0, 100, 250, 500, 1000, 2000, 5000]
    rows: list[dict[str, object]] = []
    for cur in currents:
        rate = h2_pressure_rate_mpa_yr(cur)
        for t in times:
            rows.append({
                "corrosion_current_uA_m2": cur,
                "no_loss_pressure_mpa": round(rate * t, 4),
                "time_year": t,
                "pressure_rate_mpa_yr": round(rate, 7),
            })
    x, y, w, h = 75, 70, 520, 270
    body = [chart_axes(x, y, w, h, "No-loss H2 pressure envelope from corrosion current", "time (yr)", "gas pressure (MPa)")]
    pmax = 5.0
    for val in [0, 1, 2, 3, 4, 5]:
        yy = y + h - val / pmax * h
        body.append(line(x, yy, x + w, yy, "#d7e0e5", 1))
        body.append(text(x - 8, yy + 4, str(val), anchor="end", size=11, cls="small"))
    def px(t: float) -> float:
        return x + t / 5000.0 * w
    def py(p: float) -> float:
        return y + h - min(p, pmax) / pmax * h
    for cur, color in zip(currents, colors):
        rate = h2_pressure_rate_mpa_yr(cur)
        pts = [(px(t), py(rate * t)) for t in times]
        body.append(polyline(pts, color, 2.5))
        body.append(text(430, py(rate * 3000) - 5, f"{cur:g} uA/m2", fill=color, weight="700", size=12))
    threshold_y = py(2.0)
    body.append(line(x, threshold_y, x + w, threshold_y, PALETTE["amber"], 1.5, dash="6 4"))
    body.append(text(395, threshold_y - 7, "example gas-entry threshold", fill=PALETTE["amber"], size=12))
    for tick in [0, 1000, 2000, 5000]:
        xx = px(tick)
        body.append(line(xx, y + h, xx, y + h + 5))
        body.append(text(xx, y + h + 22, str(tick), anchor="middle", size=11, cls="small"))
    body.append(text(116, 103, "upper bound: no dissolution, diffusion, or microbial consumption", size=12, cls="small"))
    (FIG_DIR / "fig6_h2_pressure_envelope.svg").write_text(svg(700, 410, "\n".join(body)), encoding="utf-8")
    return rows


def figure_7_radionuclides() -> list[dict[str, object]]:
    groups = [
        ("I-129 / TcO4", 0.0),
        ("Sr / Cs", 0.01),
        ("U / Np", 0.03),
        ("Pu / Am", 0.10),
    ]
    rows: list[dict[str, object]] = []
    for name, kd in groups:
        rows.append({
            "radionuclide_group": name,
            "kd_m3_kg": kd,
            "retardation_factor": round(retardation(kd), 2),
            "diffusion_time_year_25c": round(diffusion_time_years(kd, 25.0), 1),
            "diffusion_time_year_80c": round(diffusion_time_years(kd, 80.0), 1),
        })
    x, y, w, h = 120, 60, 500, 280
    body = [chart_axes(x, y, w, h, "Buffer diffusion times with temperature effect", "diffusion time (yr, log scale)", "radionuclide group")]
    xmin, xmax = 10.0, 100000.0
    def px(v: float) -> float:
        return x + (math.log10(v) - math.log10(xmin)) / (math.log10(xmax) - math.log10(xmin)) * w
    for tick in [10, 100, 1000, 10000, 100000]:
        xx = px(tick)
        body.append(line(xx, y, xx, y + h, "#d7e0e5", 1))
        body.append(text(xx, y + h + 22, str(tick), anchor="middle", size=11, cls="small"))
    bar_h = 23
    for i, row in enumerate(rows):
        yy = y + 42 + i * 58
        body.append(text(x - 10, yy + 17, row["radionuclide_group"], anchor="end", size=12))
        body.append(rect(x, yy, px(row["diffusion_time_year_25c"]) - x, bar_h, PALETTE["blue"], "none", rx=2))
        body.append(rect(x, yy + 25, px(row["diffusion_time_year_80c"]) - x, bar_h, PALETTE["red"], "none", rx=2))
        body.append(text(px(row["diffusion_time_year_25c"]) + 5, yy + 17, f"{row['diffusion_time_year_25c']:.0f}", size=11, cls="small"))
    body.append(text(440, 92, "25 C", fill=PALETTE["blue"], weight="700"))
    body.append(text(440, 114, "80 C", fill=PALETTE["red"], weight="700"))
    (FIG_DIR / "fig7_radionuclide_diffusion_times.svg").write_text(svg(720, 410, "\n".join(body)), encoding="utf-8")
    return rows


def figure_8_scenarios() -> list[dict[str, object]]:
    rows_labels = ["high salinity", "sulfide pulse", "H2 build-up", "thermal peak", "glacial boundary"]
    cols = ["swelling", "Cu corrosion", "gas", "nuclide flux", "fracture flow"]
    scores = [
        [5, 2, 1, 3, 2],
        [1, 5, 3, 2, 2],
        [2, 2, 5, 2, 4],
        [3, 3, 2, 4, 2],
        [3, 3, 2, 4, 5],
    ]
    colors = ["#f5f7f8", "#e0eff1", "#b9dbdf", "#8ac1c7", "#e2b968", "#c94f44"]
    x0, y0, cell_w, cell_h = 152, 82, 92, 48
    body = [text(38, 34, "Scenario-to-performance indicator matrix", size=20, weight="700")]
    for c, col in enumerate(cols):
        body.append(text(x0 + c * cell_w + cell_w / 2, y0 - 16, col, anchor="middle", size=12, weight="700"))
    out: list[dict[str, object]] = []
    for r, label in enumerate(rows_labels):
        body.append(text(x0 - 10, y0 + r * cell_h + 31, label, anchor="end", size=12))
        for c, col in enumerate(cols):
            score = scores[r][c]
            body.append(rect(x0 + c * cell_w, y0 + r * cell_h, cell_w - 4, cell_h - 4, colors[score], "#ffffff", rx=3))
            body.append(text(x0 + c * cell_w + cell_w / 2 - 2, y0 + r * cell_h + 30, str(score), anchor="middle", weight="700"))
            out.append({"scenario": label, "indicator": col, "screening_score_1_5": score})
    body.append(text(142, 365, "1 low direct leverage; 5 first-order sensitivity under screening assumptions", cls="small"))
    (FIG_DIR / "fig8_scenario_matrix.svg").write_text(svg(700, 400, "\n".join(body)), encoding="utf-8")
    return out


def write_parameter_sources() -> None:
    rows = [
        {
            "source_id": "S1",
            "parameter_or_claim": "DGR near-field review focus",
            "value_used": "canister-bentonite interaction; corrosion; self-sealing; H2; THMC",
            "source_url": "https://doi.org/10.1016/j.jenvrad.2025.107750",
            "use_in_model": "scenario classification and evidence matrix",
        },
        {
            "source_id": "S2",
            "parameter_or_claim": "NWMO multiple barrier system and <100 C container surface design statement",
            "value_used": "engineered plus natural barriers; design avoids container surface temperatures above 100 C",
            "source_url": "https://www.nwmo.ca/Canadas-Plan/Multiple-barrier-system",
            "use_in_model": "Canadian DGR context and thermal reference line",
        },
        {
            "source_id": "S3",
            "parameter_or_claim": "MX-80 brine swelling pressure reduction",
            "value_used": "highly concentrated brine peak about 30% of DI; final about one order smaller",
            "source_url": "https://link.springer.com/article/10.1007/s11440-019-00762-5",
            "use_in_model": "normalized salinity-swelling screening curve",
        },
        {
            "source_id": "S4",
            "parameter_or_claim": "MX-80 hydraulic conductivity relationships",
            "value_used": "DI k=1e-13 e^3.74/(1+e); brine k=1e-9 e^11.86",
            "source_url": "https://link.springer.com/article/10.1007/s11440-019-00762-5",
            "use_in_model": "DI/brine permeability contrast at e=0.588",
        },
        {
            "source_id": "S5",
            "parameter_or_claim": "sulphide transport control of copper corrosion",
            "value_used": "transport-limited HS- supply to copper surface",
            "source_url": "https://doi.org/10.1080/1478422X.2017.1300363",
            "use_in_model": "sulfide diffusion-limited corrosion envelope",
        },
        {
            "source_id": "S6",
            "parameter_or_claim": "Forsmark sulphide concentration range for SR-Site",
            "value_used": "screening range 1-120 umol/L HS-",
            "source_url": "https://skb.com/publication/2155543",
            "use_in_model": "sulfide concentration sensitivity range; not Canadian site data",
        },
        {
            "source_id": "S7",
            "parameter_or_claim": "H2 production/consumption and HS- feedback in Canadian DGR model",
            "value_used": "H2 dynamics depend on MIC, HS- supply, transport, and consumption",
            "source_url": "https://doi.org/10.1016/j.rineng.2025.106008",
            "use_in_model": "H2 pressure envelope caveat and process coupling",
        },
        {
            "source_id": "S8",
            "parameter_or_claim": "GeoMine THMC MCP local smoke tests",
            "value_used": "geomine_thmc mock: 20 tools ok; geomine_thmc_data mock: 13 tools ok",
            "source_url": "local:plugins/Code/geo-mining-research/scripts/test_thmc_mcp_tools.py",
            "use_in_model": "MCP workflow provenance only; not scientific measured data",
        },
    ]
    write_csv(DATA_DIR / "thmc_parameter_sources.csv", rows)


def main() -> None:
    ensure_dirs()
    write_parameter_sources()
    figure_1_concept()
    coupling_rows = figure_2_coupling_matrix()
    thermal_rows = figure_3_thermal()
    salinity_rows = figure_4_salinity()
    corrosion_rows = figure_5_corrosion()
    h2_rows = figure_6_h2()
    radionuclide_rows = figure_7_radionuclides()
    scenario_rows = figure_8_scenarios()

    all_rows: list[dict[str, object]] = []
    for name, rows in [
        ("coupling_matrix", coupling_rows),
        ("thermal_decay", thermal_rows),
        ("salinity_swelling", salinity_rows),
        ("sulfide_corrosion", corrosion_rows),
        ("h2_pressure", h2_rows),
        ("radionuclide_diffusion", radionuclide_rows),
        ("scenario_matrix", scenario_rows),
    ]:
        for row in rows:
            out = {"dataset": name}
            out.update(row)
            all_rows.append(out)
    write_csv(DATA_DIR / "thmc_screening_results.csv", all_rows)

    summary = {
        "status": "screening_calculations_not_site_calibration",
        "generated_figures": sorted(path.name for path in FIG_DIR.glob("fig*.svg")),
        "key_results": {
            "thermal_initial_delta_t_c": thermal_rows[0]["radial_delta_t_c"],
            "thermal_initial_surface_temp_c": thermal_rows[0]["canister_surface_temp_c"],
            "mx80_brine_to_di_k_ratio_e_0_588": salinity_rows[-1]["brine_to_di_k_ratio"],
            "cu_depth_100kyr_mm_at_10uM_De1e_11": round(copper_depth_mm(10.0, 1e-11), 5),
            "cu_depth_100kyr_mm_at_120uM_De1e_10": round(copper_depth_mm(120.0, 1e-10), 5),
            "cu_depth_100kyr_mm_at_120uM_De3e_10": round(copper_depth_mm(120.0, 3e-10), 5),
            "h2_pressure_rate_mpa_yr_at_1uA_m2": round(h2_pressure_rate_mpa_yr(1.0), 7),
            "iodine_diffusion_time_year_25c": radionuclide_rows[0]["diffusion_time_year_25c"],
            "pu_am_diffusion_time_year_25c": radionuclide_rows[-1]["diffusion_time_year_25c"],
            "diffusion_time_reduction_factor_25_to_80c_free_water": round(
                diffusion_time_years(0.0, 25.0) / diffusion_time_years(0.0, 80.0), 3
            ),
        },
        "limitations": [
            "No site-specific Canadian DGR groundwater sample, borehole, fracture, or canister heat inventory was ingested.",
            "Salinity-swelling points are normalized from literature statements and should be replaced by test data before calibration.",
            "Corrosion envelopes assume sulfide transport control and immediate Cu2S formation.",
            "H2 pressure curves are no-loss upper bounds; dissolution, diffusion, consumption, and two-phase escape must be added.",
        ],
    }
    (DATA_DIR / "thmc_screening_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
