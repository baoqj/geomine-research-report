#!/usr/bin/env python3
"""Generate a PHREEQC screening package and flat SVG figures for U-Ra-SO4-CO3 groundwater.

The input waters in this script are synthetic end-member and mixing scenarios
for workflow testing. They are not field measurements and must not be used as
site compliance evidence.
"""

from __future__ import annotations

import csv
import html
import json
import math
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
MODEL_DIR = ROOT / "models" / "phreeqc"
PHREEQC = Path("/Users/aibao/.local/bin/phreeqc")
DATABASE = Path("/Users/aibao/.local/phreeqc/phreeqc-3.5.0-14000/database/llnl.dat")

AVOGADRO = 6.02214076e23
RA226_HALF_LIFE_S = 1600.0 * 365.25 * 24.0 * 3600.0
RA226_LAMBDA = math.log(2.0) / RA226_HALF_LIFE_S

COLORS = {
    "ink": "#172026",
    "muted": "#52616a",
    "grid": "#d7e0e5",
    "blue": "#1f6f9f",
    "teal": "#249186",
    "green": "#5d8f3a",
    "amber": "#d08b2f",
    "red": "#c94f44",
    "purple": "#6f5aa7",
    "bg": "#f7faf9",
}


def ra226_bq_l_to_mg_l(bq_l: float) -> float:
    mol_l = bq_l / (RA226_LAMBDA * AVOGADRO)
    return mol_l * 226.025 * 1000.0


BASE_WATERS = [
    {
        "sample_id": "OX-CARB-01",
        "scenario": "shallow oxidizing carbonate groundwater",
        "type": "oxidizing carbonate",
        "temperature_c": 10.0,
        "pH": 7.85,
        "pe": 8.0,
        "alkalinity_mg_l_as_caco3": 245.0,
        "Ca_mg_l": 72.0,
        "Mg_mg_l": 24.0,
        "Na_mg_l": 58.0,
        "K_mg_l": 3.2,
        "Cl_mg_l": 34.0,
        "SO4_mg_l": 42.0,
        "Ba_mg_l": 0.025,
        "Sr_mg_l": 0.42,
        "Fe_mg_l": 0.015,
        "Mn_mg_l": 0.008,
        "U_mg_l": 0.085,
        "Ra226_Bq_l": 0.08,
    },
    {
        "sample_id": "RED-BRINE-01",
        "scenario": "deep reducing saline fracture groundwater",
        "type": "reducing brine",
        "temperature_c": 18.0,
        "pH": 7.25,
        "pe": -3.0,
        "alkalinity_mg_l_as_caco3": 155.0,
        "Ca_mg_l": 185.0,
        "Mg_mg_l": 78.0,
        "Na_mg_l": 820.0,
        "K_mg_l": 18.0,
        "Cl_mg_l": 1450.0,
        "SO4_mg_l": 8.0,
        "Ba_mg_l": 0.18,
        "Sr_mg_l": 3.8,
        "Fe_mg_l": 1.6,
        "Mn_mg_l": 0.42,
        "U_mg_l": 0.0015,
        "Ra226_Bq_l": 0.95,
    },
    {
        "sample_id": "TAIL-SO4-01",
        "scenario": "tailings-influenced high-sulfate seepage",
        "type": "tailings sulfate",
        "temperature_c": 12.0,
        "pH": 6.75,
        "pe": 4.2,
        "alkalinity_mg_l_as_caco3": 88.0,
        "Ca_mg_l": 285.0,
        "Mg_mg_l": 112.0,
        "Na_mg_l": 135.0,
        "K_mg_l": 8.4,
        "Cl_mg_l": 165.0,
        "SO4_mg_l": 1040.0,
        "Ba_mg_l": 0.018,
        "Sr_mg_l": 2.6,
        "Fe_mg_l": 0.34,
        "Mn_mg_l": 0.23,
        "U_mg_l": 0.044,
        "Ra226_Bq_l": 0.32,
    },
]


NUMERIC_KEYS = [
    "temperature_c",
    "pH",
    "pe",
    "alkalinity_mg_l_as_caco3",
    "Ca_mg_l",
    "Mg_mg_l",
    "Na_mg_l",
    "K_mg_l",
    "Cl_mg_l",
    "SO4_mg_l",
    "Ba_mg_l",
    "Sr_mg_l",
    "Fe_mg_l",
    "Mn_mg_l",
    "U_mg_l",
    "Ra226_Bq_l",
]


def mix(row_a: dict[str, object], row_b: dict[str, object], fraction_b: float, sample_id: str) -> dict[str, object]:
    row: dict[str, object] = {
        "sample_id": sample_id,
        "scenario": f"{row_a['type']} mixed with {row_b['type']} ({fraction_b:.0%} second end-member)",
        "type": "mixing path",
    }
    for key in NUMERIC_KEYS:
        row[key] = (1.0 - fraction_b) * float(row_a[key]) + fraction_b * float(row_b[key])
    return row


def build_dataset() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = [dict(row) for row in BASE_WATERS]
    ox, red, tail = BASE_WATERS
    for idx, frac in enumerate([0.1, 0.25, 0.5, 0.75, 0.9], start=1):
        rows.append(mix(ox, tail, frac, f"MIX-TAIL-{idx:02d}"))
    for idx, frac in enumerate([0.1, 0.25, 0.5, 0.75, 0.9], start=1):
        rows.append(mix(ox, red, frac, f"MIX-RED-{idx:02d}"))
    for row in rows:
        row["Ra_mg_l"] = ra226_bq_l_to_mg_l(float(row["Ra226_Bq_l"]))
        row["ionic_strength_proxy"] = (
            float(row["Ca_mg_l"]) + float(row["Mg_mg_l"]) + float(row["Na_mg_l"]) + float(row["Cl_mg_l"]) + float(row["SO4_mg_l"])
        ) / 1000.0
        row["tailings_signature_score"] = log_norm(float(row["SO4_mg_l"]), 8.0, 1040.0) * 0.45 + log_norm(
            float(row["Cl_mg_l"]), 34.0, 1450.0
        ) * 0.25 + log_norm(float(row["Fe_mg_l"]) + float(row["Mn_mg_l"]), 0.023, 2.02) * 0.30
        row["u_carbonate_redox_score"] = clamp(
            0.55 * norm(float(row["alkalinity_mg_l_as_caco3"]), 88.0, 245.0)
            + 0.35 * norm(float(row["pe"]), -3.0, 8.0)
            + 0.10 * norm(float(row["pH"]), 6.75, 7.85)
        )
        row["ra_sulfate_ba_sr_score"] = clamp(
            0.45 * log_norm(float(row["SO4_mg_l"]), 8.0, 1040.0)
            + 0.30 * log_norm(float(row["Sr_mg_l"]), 0.42, 3.8)
            + 0.25 * log_norm(float(row["Ba_mg_l"]), 0.018, 0.18)
        )
    return rows


def norm(value: float, low: float, high: float) -> float:
    if high == low:
        return 0.0
    return clamp((value - low) / (high - low))


def log_norm(value: float, low: float, high: float) -> float:
    return norm(math.log10(max(value, 1e-30)), math.log10(max(low, 1e-30)), math.log10(max(high, 1e-30)))


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    keys = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def build_phreeqc_input(rows: list[dict[str, object]]) -> str:
    lines = [
        "TITLE U-Ra-SO4-CO3 groundwater screening package",
        "SELECTED_OUTPUT 1",
        "  -file selected_output.tsv",
        "  -reset false",
        "  -simulation true",
        "  -solution true",
        "  -state true",
        "  -pH true",
        "  -pe true",
        "  -temperature true",
        "  -alkalinity true",
        "  -ionic_strength true",
        "  -charge_balance true",
        "  -percent_error true",
        "  -water true",
        "  -totals U Ra Ba Sr Ca Mg Na K Cl S C Fe Mn",
        "  -saturation_indices Calcite Dolomite Barite Celestite Gypsum Uraninite Coffinite Goethite Manganite Pyrolusite RaSO4",
        "  -molalities UO2+2 UO2CO3 UO2(CO3)2-2 UO2(CO3)3-4 Ra+2 Ba+2 Sr+2 SO4-2 HCO3-",
        "END",
    ]
    for index, row in enumerate(rows, start=1):
        lines.extend(
            [
                f"SOLUTION {index} {row['sample_id']}",
                f"  temp {float(row['temperature_c']):.4g}",
                "  units mg/L",
                f"  pH {float(row['pH']):.4g}",
                f"  pe {float(row['pe']):.4g}",
                f"  Alkalinity {float(row['alkalinity_mg_l_as_caco3']):.8g} as CaCO3",
                f"  Ca {float(row['Ca_mg_l']):.8g}",
                f"  Mg {float(row['Mg_mg_l']):.8g}",
                f"  Na {float(row['Na_mg_l']):.8g}",
                f"  K {float(row['K_mg_l']):.8g}",
                f"  Cl {float(row['Cl_mg_l']):.8g}",
                f"  S(6) {float(row['SO4_mg_l']):.8g} as SO4",
                f"  Ba {float(row['Ba_mg_l']):.8g}",
                f"  Sr {float(row['Sr_mg_l']):.8g}",
                f"  Fe {float(row['Fe_mg_l']):.8g}",
                f"  Mn {float(row['Mn_mg_l']):.8g}",
                f"  U {float(row['U_mg_l']):.8g}",
                f"  Ra {float(row['Ra_mg_l']):.12g}",
                "END",
            ]
        )
    return "\n".join(lines) + "\n"


def run_phreeqc(input_path: Path, output_path: Path) -> dict[str, object]:
    if not PHREEQC.exists() or not DATABASE.exists():
        return {
            "ran": False,
            "reason": "PHREEQC executable or llnl.dat database not found",
            "phreeqc": str(PHREEQC),
            "database": str(DATABASE),
        }
    result = subprocess.run(
        [str(PHREEQC), str(input_path.name), str(output_path.name), str(DATABASE)],
        cwd=MODEL_DIR,
        text=True,
        capture_output=True,
        timeout=60,
        check=False,
    )
    return {
        "ran": result.returncode == 0,
        "returncode": result.returncode,
        "stdout": result.stdout[-4000:],
        "stderr": result.stderr[-4000:],
        "phreeqc": str(PHREEQC),
        "database": str(DATABASE),
    }


def parse_selected(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    lines = [line.rstrip("\n") for line in path.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip()]
    if not lines:
        return []
    header = lines[0].split()
    rows = []
    for line in lines[1:]:
        parts = line.split()
        row: dict[str, object] = {}
        for key, value in zip(header, parts):
            row[key] = maybe_float(value)
        rows.append(row)
    return rows


def maybe_float(value: str) -> object:
    try:
        return float(value)
    except ValueError:
        return value


def merge_results(inputs: list[dict[str, object]], selected: list[dict[str, object]]) -> list[dict[str, object]]:
    merged = []
    for idx, row in enumerate(inputs):
        out = dict(row)
        if idx < len(selected):
            for key, value in selected[idx].items():
                out[f"phreeqc_{key}"] = value
        merged.append(out)
    return merged


def pearson(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    if n < 2:
        return 0.0
    mx = sum(xs) / n
    my = sum(ys) / n
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx <= 0 or vy <= 0:
        return 0.0
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / math.sqrt(vx * vy)


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def svg(width: int, height: int, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">\n'
        "<style>"
        "text{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;fill:#172026}"
        ".small{font-size:12px;fill:#52616a}.title{font-size:18px;font-weight:700}.axis{stroke:#172026;stroke-width:1}"
        ".grid{stroke:#d7e0e5;stroke-width:1}.label{font-size:13px;fill:#172026}.legend{font-size:12px;fill:#52616a}"
        "</style>\n"
        f"{body}\n</svg>\n"
    )


def text(x: float, y: float, value: object, size: int = 13, anchor: str = "start", weight: str = "400", cls: str = "") -> str:
    class_attr = f' class="{cls}"' if cls else ""
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}"{class_attr}>{esc(value)}</text>'


def rect(x: float, y: float, w: float, h: float, fill: str, stroke: str = "none", opacity: float = 1.0) -> str:
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" stroke="{stroke}" opacity="{opacity:.3g}"/>'


def line(x1: float, y1: float, x2: float, y2: float, stroke: str = "#172026", sw: float = 1.0, dash: str = "") -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw:.1f}"{dash_attr}/>'


def circle(x: float, y: float, r: float, fill: str, stroke: str = "#172026") -> str:
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="0.8"/>'


def color_for(row: dict[str, object]) -> str:
    typ = str(row["type"])
    if typ == "oxidizing carbonate":
        return COLORS["blue"]
    if typ == "reducing brine":
        return COLORS["purple"]
    if typ == "tailings sulfate":
        return COLORS["red"]
    return COLORS["teal"]


def plot_xy(rows: list[dict[str, object]], xkey: str, ykey: str, xlabel: str, ylabel: str, title: str, path: Path, logx: bool = False, logy: bool = False) -> None:
    vals = []
    for row in rows:
        x = float(row[xkey])
        y = float(row[ykey])
        vals.append((math.log10(x) if logx else x, math.log10(y) if logy else y, row))
    xs = [v[0] for v in vals]
    ys = [v[1] for v in vals]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    if xmin == xmax:
        xmax += 1
    if ymin == ymax:
        ymax += 1
    xpad = (xmax - xmin) * 0.08
    ypad = (ymax - ymin) * 0.08
    xmin -= xpad
    xmax += xpad
    ymin -= ypad
    ymax += ypad
    w, h = 920, 600
    left, right, top, bottom = 95, 35, 70, 92
    pw, ph = w - left - right, h - top - bottom

    def sx(x: float) -> float:
        return left + (x - xmin) / (xmax - xmin) * pw

    def sy(y: float) -> float:
        return top + ph - (y - ymin) / (ymax - ymin) * ph

    body = [rect(0, 0, w, h, "#ffffff"), text(26, 34, title, 18, weight="700", cls="title")]
    for i in range(6):
        x = left + i / 5 * pw
        y = top + i / 5 * ph
        body.append(line(x, top, x, top + ph, COLORS["grid"]))
        body.append(line(left, y, left + pw, y, COLORS["grid"]))
    body.append(line(left, top + ph, left + pw, top + ph, COLORS["ink"], 1.2))
    body.append(line(left, top, left, top + ph, COLORS["ink"], 1.2))
    body.append(text(left + pw / 2, h - 32, xlabel + (" (log10)" if logx else ""), 13, anchor="middle"))
    body.append(text(22, top + ph / 2, ylabel + (" (log10)" if logy else ""), 13, anchor="middle"))
    r = pearson([float(row[xkey]) for row in rows], [float(row[ykey]) for row in rows])
    body.append(text(w - 260, 34, f"Pearson r = {r:+.2f} (synthetic scenarios)", 12, cls="small"))
    for x, y, row in vals:
        body.append(circle(sx(x), sy(y), 6.5, color_for(row)))
        if str(row["sample_id"]).endswith("01"):
            body.append(text(sx(x) + 9, sy(y) - 8, row["sample_id"], 11, cls="small"))
    legend_x = 610
    for idx, (name, col) in enumerate(
        [
            ("oxidizing carbonate", COLORS["blue"]),
            ("reducing brine", COLORS["purple"]),
            ("tailings sulfate", COLORS["red"]),
            ("mixing path", COLORS["teal"]),
        ]
    ):
        y = 532 + idx * 17
        body.append(circle(legend_x, y - 4, 5, col))
        body.append(text(legend_x + 12, y, name, 12, cls="legend"))
    path.write_text(svg(w, h, "\n".join(body)), encoding="utf-8")


def plot_correlation_heatmap(rows: list[dict[str, object]], path: Path) -> None:
    variables = [
        ("pH", "pH"),
        ("pe", "pe"),
        ("Alk", "alkalinity_mg_l_as_caco3"),
        ("SO4", "SO4_mg_l"),
        ("Ba", "Ba_mg_l"),
        ("Sr", "Sr_mg_l"),
        ("U", "U_mg_l"),
        ("Ra226", "Ra226_Bq_l"),
        ("U score", "u_carbonate_redox_score"),
        ("Ra score", "ra_sulfate_ba_sr_score"),
    ]
    w, h = 860, 820
    margin = 150
    cell = 58
    body = [rect(0, 0, w, h, "#ffffff"), text(28, 36, "Figure 1. Correlation matrix for PHREEQC screening inputs and mechanism scores", 18, weight="700")]
    for i, (label_i, key_i) in enumerate(variables):
        body.append(text(margin - 12, margin + i * cell + 35, label_i, 12, anchor="end"))
        body.append(text(margin + i * cell + 29, margin - 16, label_i, 12, anchor="middle"))
        for j, (_, key_j) in enumerate(variables):
            r = pearson([float(row[key_i]) for row in rows], [float(row[key_j]) for row in rows])
            fill = corr_color(r)
            body.append(rect(margin + j * cell, margin + i * cell, cell - 2, cell - 2, fill, "#ffffff"))
            body.append(text(margin + j * cell + cell / 2, margin + i * cell + 35, f"{r:+.2f}", 10, anchor="middle"))
    body.append(text(28, 756, "Note: scenarios are synthetic end-members and mixtures for workflow testing; correlations are not field evidence.", 12, cls="small"))
    path.write_text(svg(w, h, "\n".join(body)), encoding="utf-8")


def corr_color(r: float) -> str:
    r = max(-1.0, min(1.0, r))
    if r >= 0:
        base = (31, 111, 159)
        alpha = r
    else:
        base = (201, 79, 68)
        alpha = -r
    bg = (248, 250, 249)
    rgb = tuple(int(bg[i] * (1 - alpha) + base[i] * alpha) for i in range(3))
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def plot_score_bars(rows: list[dict[str, object]], path: Path) -> None:
    picked = [row for row in rows if str(row["sample_id"]) in {"OX-CARB-01", "RED-BRINE-01", "TAIL-SO4-01", "MIX-TAIL-03", "MIX-RED-03"}]
    w, h = 940, 560
    left, top = 190, 82
    bar_h, gap = 24, 26
    scale_w = 590
    body = [rect(0, 0, w, h, "#ffffff"), text(28, 36, "Figure 4. Mechanism-score decomposition for representative waters", 18, weight="700")]
    for idx, row in enumerate(picked):
        y0 = top + idx * (bar_h * 3 + gap)
        body.append(text(left - 16, y0 + 16, row["sample_id"], 12, anchor="end"))
        for j, (label, key, col) in enumerate(
            [
                ("U carbonate/redox", "u_carbonate_redox_score", COLORS["blue"]),
                ("Ra sulfate-Ba/Sr", "ra_sulfate_ba_sr_score", COLORS["purple"]),
                ("tailings signature", "tailings_signature_score", COLORS["red"]),
            ]
        ):
            y = y0 + j * (bar_h + 3)
            body.append(rect(left, y, scale_w, bar_h, "#eef4f5", "#d7e0e5"))
            width = float(row[key]) * scale_w
            body.append(rect(left, y, width, bar_h, col))
            body.append(text(left + 8, y + 16, label, 11, cls="small"))
            body.append(text(left + scale_w + 10, y + 16, f"{float(row[key]):.2f}", 11, cls="small"))
    body.append(text(28, 525, "Scores are transparent screening indices derived from input chemistry; they are not calibrated risk probabilities.", 12, cls="small"))
    path.write_text(svg(w, h, "\n".join(body)), encoding="utf-8")


def plot_si_heatmap(rows: list[dict[str, object]], path: Path) -> None:
    phases = [
        ("Calcite", "si_Calcite"),
        ("Barite", "si_Barite"),
        ("Celestite", "si_Celestite"),
        ("Gypsum", "si_Gypsum"),
        ("Uraninite", "si_Uraninite"),
        ("Coffinite", "si_Coffinite"),
        ("RaSO4", "si_RaSO4"),
    ]
    picked = [row for row in rows if str(row["sample_id"]) in {"OX-CARB-01", "RED-BRINE-01", "TAIL-SO4-01", "MIX-TAIL-03", "MIX-RED-03"}]
    w, h = 930, 560
    left, top, cell_w, cell_h = 170, 96, 98, 58
    body = [rect(0, 0, w, h, "#ffffff"), text(28, 36, "Figure 5. Saturation-index heatmap from PHREEQC selected output", 18, weight="700")]
    for j, (label, _) in enumerate(phases):
        body.append(text(left + j * cell_w + cell_w / 2, top - 16, label, 12, anchor="middle"))
    for i, row in enumerate(picked):
        body.append(text(left - 14, top + i * cell_h + 36, row["sample_id"], 12, anchor="end"))
        for j, (_, key) in enumerate(phases):
            val = float(row.get(key, 0.0))
            body.append(rect(left + j * cell_w, top + i * cell_h, cell_w - 2, cell_h - 2, si_color(val), "#ffffff"))
            body.append(text(left + j * cell_w + cell_w / 2, top + i * cell_h + 35, f"{val:+.2f}", 11, anchor="middle"))
    body.append(text(28, 510, "Warm colors indicate supersaturation tendency; blue colors indicate undersaturation. Interpretation depends on database coverage and equilibrium assumptions.", 12, cls="small"))
    path.write_text(svg(w, h, "\n".join(body)), encoding="utf-8")


def si_color(value: float) -> str:
    value = max(-5.0, min(5.0, value))
    if value >= 0:
        alpha = value / 5.0
        base = (201, 79, 68)
    else:
        alpha = -value / 5.0
        base = (31, 111, 159)
    bg = (248, 250, 249)
    rgb = tuple(int(bg[i] * (1 - alpha) + base[i] * alpha) for i in range(3))
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def add_si_aliases(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    aliases = {
        "si_Calcite": ["phreeqc_si_Calcite", "phreeqc_Calcite"],
        "si_Barite": ["phreeqc_si_Barite", "phreeqc_Barite"],
        "si_Celestite": ["phreeqc_si_Celestite", "phreeqc_Celestite"],
        "si_Gypsum": ["phreeqc_si_Gypsum", "phreeqc_Gypsum"],
        "si_Uraninite": ["phreeqc_si_Uraninite", "phreeqc_Uraninite"],
        "si_Coffinite": ["phreeqc_si_Coffinite", "phreeqc_Coffinite"],
        "si_RaSO4": ["phreeqc_si_RaSO4", "phreeqc_RaSO4"],
    }
    for row in rows:
        for target, candidates in aliases.items():
            row[target] = 0.0
            for candidate in candidates:
                if candidate in row:
                    row[target] = row[candidate]
                    break
    return rows


def write_manifest(status: dict[str, object], rows: list[dict[str, object]]) -> None:
    manifest = {
        "title": "U-Ra-SO4-CO3 PHREEQC screening package",
        "generated_by": "GeoMine Research local workflow",
        "input_type": "synthetic end-member and mixing scenarios for skill testing",
        "phreeqc_status": status,
        "sample_count": len(rows),
        "figures": [
            "fig1_correlation_matrix.svg",
            "fig2_u_vs_alkalinity.svg",
            "fig3_ra_vs_sulfate.svg",
            "fig4_mechanism_scores.svg",
            "fig5_saturation_index_heatmap.svg",
            "fig6_u_vs_ra_decoupling.svg",
        ],
        "limitations": [
            "Synthetic values are not field measurements.",
            "PHREEQC selected output is a screening calculation, not field validation.",
            "Ra-226 activity was converted to elemental Ra mass for PHREEQC input for workflow testing.",
            "Database coverage and mineral equilibrium assumptions must be audited before real-site interpretation.",
        ],
    }
    (ROOT / "workflow_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    DATA_DIR.mkdir(exist_ok=True)
    FIG_DIR.mkdir(exist_ok=True)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    rows = build_dataset()
    write_csv(DATA_DIR / "synthetic_groundwater_endmembers.csv", rows)

    input_text = build_phreeqc_input(rows)
    input_path = MODEL_DIR / "u_ra_so4_co3_screening.phr"
    output_path = MODEL_DIR / "u_ra_so4_co3_screening.out"
    input_path.write_text(input_text, encoding="utf-8")

    status = run_phreeqc(input_path, output_path)
    selected = parse_selected(MODEL_DIR / "selected_output.tsv")
    merged = add_si_aliases(merge_results(rows, selected))
    write_csv(DATA_DIR / "screening_results.csv", merged)
    write_manifest(status, merged)

    plot_correlation_heatmap(merged, FIG_DIR / "fig1_correlation_matrix.svg")
    plot_xy(
        merged,
        "alkalinity_mg_l_as_caco3",
        "U_mg_l",
        "Alkalinity, mg/L as CaCO3",
        "U, mg/L",
        "Figure 2. U concentration tracks carbonate alkalinity in oxidizing scenarios",
        FIG_DIR / "fig2_u_vs_alkalinity.svg",
        logy=True,
    )
    plot_xy(
        merged,
        "SO4_mg_l",
        "Ra226_Bq_l",
        "SO4, mg/L",
        "Ra-226, Bq/L",
        "Figure 3. Ra does not increase monotonically with sulfate because Ba/Sr and mixing state also matter",
        FIG_DIR / "fig3_ra_vs_sulfate.svg",
        logx=True,
        logy=True,
    )
    plot_score_bars(merged, FIG_DIR / "fig4_mechanism_scores.svg")
    plot_si_heatmap(merged, FIG_DIR / "fig5_saturation_index_heatmap.svg")
    plot_xy(
        merged,
        "U_mg_l",
        "Ra226_Bq_l",
        "U, mg/L",
        "Ra-226, Bq/L",
        "Figure 6. Synthetic U-Ra decoupling across carbonate, reducing, and sulfate-rich waters",
        FIG_DIR / "fig6_u_vs_ra_decoupling.svg",
        logx=True,
        logy=True,
    )

    if shutil.which("python3"):
        print(json.dumps({"ok": True, "phreeqc_ran": status.get("ran"), "samples": len(merged)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
