#!/usr/bin/env python3
"""
Generate reproducible method/screening figures for the GeoMine PFLOTRAN
tailings-acid seepage paper.

The numeric data generated here are dimensionless screening values and
illustrative parameter sweeps. They are not PFLOTRAN simulation outputs and
must not be interpreted as measured or calibrated site results.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path
import struct
import zlib


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
DATA_DIR = ROOT / "data"


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


class Canvas:
    def __init__(self, width: int, height: int, bg: tuple[int, int, int] = (255, 255, 255)) -> None:
        self.width = width
        self.height = height
        self.px = [bg] * (width * height)

    def set(self, x: int, y: int, color: tuple[int, int, int]) -> None:
        if 0 <= x < self.width and 0 <= y < self.height:
            self.px[y * self.width + x] = color

    def rect(self, x: int, y: int, w: int, h: int, color: tuple[int, int, int]) -> None:
        for yy in range(max(0, y), min(self.height, y + h)):
            offset = yy * self.width
            for xx in range(max(0, x), min(self.width, x + w)):
                self.px[offset + xx] = color

    def line(self, x1: int, y1: int, x2: int, y2: int, color: tuple[int, int, int], width: int = 1) -> None:
        dx = abs(x2 - x1)
        sx = 1 if x1 < x2 else -1
        dy = -abs(y2 - y1)
        sy = 1 if y1 < y2 else -1
        err = dx + dy
        x, y = x1, y1
        while True:
            for oy in range(-(width // 2), width // 2 + 1):
                for ox in range(-(width // 2), width // 2 + 1):
                    self.set(x + ox, y + oy, color)
            if x == x2 and y == y2:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x += sx
            if e2 <= dx:
                err += dx
                y += sy

    def circle(self, cx: int, cy: int, r: int, color: tuple[int, int, int]) -> None:
        rr = r * r
        for y in range(cy - r, cy + r + 1):
            for x in range(cx - r, cx + r + 1):
                if (x - cx) * (x - cx) + (y - cy) * (y - cy) <= rr:
                    self.set(x, y, color)

    def polyline(self, points: list[tuple[int, int]], color: tuple[int, int, int], width: int = 2) -> None:
        for p1, p2 in zip(points, points[1:]):
            self.line(p1[0], p1[1], p2[0], p2[1], color, width)

    def save_png(self, path: Path) -> None:
        raw = bytearray()
        for y in range(self.height):
            raw.append(0)
            for x in range(self.width):
                raw.extend(self.px[y * self.width + x])

        def chunk(name: bytes, data: bytes) -> bytes:
            return (
                struct.pack(">I", len(data))
                + name
                + data
                + struct.pack(">I", zlib.crc32(name + data) & 0xFFFFFFFF)
            )

        png = b"\x89PNG\r\n\x1a\n"
        png += chunk(b"IHDR", struct.pack(">IIBBBBB", self.width, self.height, 8, 2, 0, 0, 0))
        png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        png += chunk(b"IEND", b"")
        path.write_bytes(png)


def svg(width: int, height: int, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    text {{ font-family: Arial, Helvetica, sans-serif; fill: #17202a; }}
    .small {{ font-size: 13px; }}
    .label {{ font-size: 15px; font-weight: 600; }}
    .title {{ font-size: 19px; font-weight: 700; }}
    .caveat {{ font-size: 12px; fill: #5f6b72; }}
  </style>
{body}
</svg>
"""


def fig01_conceptual_cross_section() -> None:
    body = """
  <rect x="0" y="0" width="1100" height="620" fill="#f7fbff"/>
  <text x="40" y="45" class="title">Conceptual model: sulfide-bearing uranium tailings seepage to shallow aquifer</text>
  <rect x="70" y="105" width="300" height="110" fill="#b7b0a6" stroke="#5b5147" stroke-width="2"/>
  <text x="105" y="150" class="label">Tailings source zone</text>
  <text x="105" y="176" class="small">pyrite + U-bearing phases</text>
  <path d="M80 215 C230 260 420 260 575 255 C745 248 890 255 1050 238 L1050 325 C830 348 630 337 430 330 C260 326 150 305 80 300 Z" fill="#d8c99b" stroke="#9c874e" stroke-width="2"/>
  <text x="455" y="302" class="label">Vadose / seepage pathway</text>
  <path d="M30 342 C250 335 420 360 630 350 C820 342 970 345 1080 360 L1080 495 L30 495 Z" fill="#cce7f6" stroke="#4a90ad" stroke-width="2"/>
  <text x="610" y="395" class="label">Shallow aquifer</text>
  <rect x="30" y="495" width="1050" height="75" fill="#8f8f8f" stroke="#555" stroke-width="2"/>
  <text x="690" y="540" class="label" fill="#fff">Low-permeability base layer</text>
  <path d="M240 210 C280 260 340 305 445 350" fill="none" stroke="#c0392b" stroke-width="5" stroke-dasharray="10 8" marker-end="url(#arrow-red)"/>
  <path d="M420 367 C560 367 705 370 900 392" fill="none" stroke="#2f80b7" stroke-width="5" marker-end="url(#arrow-blue)"/>
  <path d="M445 350 C560 330 690 325 840 318" fill="none" stroke="#d35400" stroke-width="4" stroke-dasharray="7 6" marker-end="url(#arrow-orange)"/>
  <circle cx="520" cy="380" r="9" fill="#4a90ad"/><text x="535" y="385" class="small">MW-1</text>
  <circle cx="720" cy="385" r="9" fill="#4a90ad"/><text x="735" y="390" class="small">MW-2</text>
  <circle cx="930" cy="405" r="9" fill="#4a90ad"/><text x="945" y="410" class="small">MW-3 / receptor</text>
  <rect x="115" y="235" width="190" height="70" fill="#fff7e6" stroke="#d35400" stroke-width="1.5"/>
  <text x="132" y="262" class="small">Acid + sulfate source</text>
  <text x="132" y="286" class="small">metals + U-series release</text>
  <rect x="540" y="255" width="250" height="70" fill="#eef8ef" stroke="#3a8b4f" stroke-width="1.5"/>
  <text x="560" y="283" class="small">Carbonate neutralization</text>
  <text x="560" y="307" class="small">Fe/Al hydroxide precipitation</text>
  <defs>
    <marker id="arrow-red" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c0392b"/></marker>
    <marker id="arrow-blue" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2f80b7"/></marker>
    <marker id="arrow-orange" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#d35400"/></marker>
  </defs>
  <text x="40" y="600" class="caveat">Schematic only. Geometry, gradients, concentrations, and mineral quantities require site measurements before PFLOTRAN execution.</text>
"""
    write(FIG_DIR / "fig01_conceptual_cross_section.svg", svg(1100, 620, body))


def fig02_reaction_network() -> None:
    nodes = [
        ("Sulfide oxidation", 60, 100, "#f6c6bd"),
        ("Acid + sulfate", 310, 100, "#ffd99a"),
        ("Carbonate buffering", 560, 100, "#d5efc2"),
        ("Fe/Al hydroxides", 810, 100, "#d7d7d7"),
        ("U(VI) carbonate", 205, 300, "#d7c5f0"),
        ("Ra sulfate/barite", 455, 300, "#c8e7f7"),
        ("Fe-Mn oxide sorption", 705, 300, "#dce5c2"),
        ("Downgradient plumes", 455, 480, "#f3f3f3"),
    ]
    body = ['  <rect x="0" y="0" width="1050" height="620" fill="#fbfcfd"/>']
    body.append('  <text x="40" y="45" class="title">Geochemical reaction-network design for PHREEQC prototype and PFLOTRAN transfer</text>')
    for label, x, y, color in nodes:
        body.append(f'  <rect x="{x}" y="{y}" rx="8" ry="8" width="190" height="82" fill="{color}" stroke="#50616b" stroke-width="1.6"/>')
        body.append(f'  <text x="{x+18}" y="{y+38}" class="label">{label}</text>')
    arrows = [
        (250, 141, 310, 141, "#c0392b"),
        (500, 141, 560, 141, "#d35400"),
        (750, 141, 810, 141, "#7f8c8d"),
        (405, 183, 300, 300, "#8e44ad"),
        (455, 183, 520, 300, "#2980b9"),
        (850, 183, 785, 300, "#4d7f35"),
        (300, 382, 500, 480, "#8e44ad"),
        (550, 382, 560, 480, "#2980b9"),
        (790, 382, 650, 480, "#4d7f35"),
    ]
    body.append('  <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#50616b"/></marker></defs>')
    for x1, y1, x2, y2, color in arrows:
        body.append(f'  <path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{color}" stroke-width="3" marker-end="url(#arrow)"/>')
    body.append('  <text x="52" y="590" class="caveat">Constants for kinetics, thermodynamics, surface complexation, and ion exchange are placeholders until database/lab calibration is supplied.</text>')
    write(FIG_DIR / "fig02_reaction_network.svg", svg(1050, 620, "\n".join(body)))


def fig03_domain_boundary_conditions() -> None:
    body = """
  <rect x="0" y="0" width="1050" height="620" fill="#ffffff"/>
  <text x="40" y="45" class="title">PFLOTRAN 2D cross-section model domain and boundary-condition plan</text>
  <rect x="120" y="100" width="780" height="390" fill="#f8fbfd" stroke="#1f2d3d" stroke-width="2.4"/>
  <rect x="120" y="100" width="220" height="90" fill="#b7b0a6" stroke="#5b5147" stroke-width="1.5"/>
  <text x="155" y="154" class="label">Tailings layer</text>
  <rect x="120" y="190" width="780" height="105" fill="#d8c99b" stroke="#9c874e" stroke-width="1.5"/>
  <text x="455" y="250" class="label">Vadose / transition zone</text>
  <rect x="120" y="295" width="780" height="140" fill="#cce7f6" stroke="#4a90ad" stroke-width="1.5"/>
  <text x="460" y="370" class="label">Shallow saturated aquifer</text>
  <rect x="120" y="435" width="780" height="55" fill="#8f8f8f" stroke="#555" stroke-width="1.5"/>
  <text x="455" y="468" class="label">Low-K base</text>
  <path d="M90 118 L120 118" stroke="#2f80b7" stroke-width="4" marker-end="url(#arrow)"/>
  <text x="25" y="123" class="small">infiltration</text>
  <path d="M900 362 L960 362" stroke="#2f80b7" stroke-width="4" marker-end="url(#arrow)"/>
  <text x="965" y="368" class="small">head / outflow</text>
  <path d="M120 360 L70 360" stroke="#5f6b72" stroke-width="3" stroke-dasharray="7 5"/>
  <text x="23" y="345" class="small">upgradient</text>
  <text x="25" y="365" class="small">head/flux</text>
  <text x="342" y="95" class="small">top atmospheric/recharge boundary</text>
  <text x="388" y="515" class="small">no-flow or specified leakage base</text>
  <circle cx="430" cy="360" r="7" fill="#1f77b4"/><text x="444" y="365" class="small">OBS-1</text>
  <circle cx="610" cy="365" r="7" fill="#1f77b4"/><text x="624" y="370" class="small">OBS-2</text>
  <circle cx="780" cy="374" r="7" fill="#1f77b4"/><text x="794" y="379" class="small">OBS-3</text>
  <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2f80b7"/></marker></defs>
  <text x="52" y="585" class="caveat">Recommended first executable geometry: 2D cross-section. 1D column is for screening; 3D requires measured topography, hydrostratigraphy, and monitoring layout.</text>
"""
    write(FIG_DIR / "fig03_domain_boundary_conditions.svg", svg(1050, 620, body))


def color_for(value: float, min_v: float, max_v: float) -> str:
    t = (value - min_v) / (max_v - min_v)
    t = max(0.0, min(1.0, t))
    r = int(248 * (1 - t) + 153 * t)
    g = int(248 * (1 - t) + 45 * t)
    b = int(241 * (1 - t) + 34 * t)
    return f"#{r:02x}{g:02x}{b:02x}"


def fig04_acid_buffer_heatmap() -> None:
    reactivity = [0.1, 0.3, 1.0, 3.0, 10.0]
    buffer = [0.1, 0.3, 1.0, 3.0, 10.0]
    rows = []
    for b in buffer:
        for r in reactivity:
            index = r / b
            rows.append({"sulfide_reactivity_norm": r, "carbonate_buffer_norm": b, "acid_buffer_index": index})
    with (DATA_DIR / "screening_parameter_sweep.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    cell = 78
    x0, y0 = 235, 100
    body = ['  <rect x="0" y="0" width="900" height="620" fill="#ffffff"/>']
    body.append('  <text x="40" y="45" class="title">Dimensionless acid-buffer screening index</text>')
    body.append('  <text x="252" y="560" class="label">Normalized sulfide oxidation / seepage forcing</text>')
    body.append('  <text x="35" y="310" class="label" transform="rotate(-90 35,310)">Normalized carbonate buffering capacity</text>')
    values = [row["acid_buffer_index"] for row in rows]
    min_v, max_v = min(values), max(values)
    for j, b in enumerate(reversed(buffer)):
        body.append(f'  <text x="{x0-60}" y="{y0 + j*cell + 48}" class="small">{b:g}</text>')
        for i, r in enumerate(reactivity):
            v = r / b
            fill = color_for(math.log10(v), math.log10(min_v), math.log10(max_v))
            x = x0 + i * cell
            y = y0 + j * cell
            body.append(f'  <rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{fill}" stroke="#ffffff" stroke-width="2"/>')
            body.append(f'  <text x="{x+20}" y="{y+45}" class="small">{v:.2g}</text>')
    for i, r in enumerate(reactivity):
        body.append(f'  <text x="{x0 + i*cell + 30}" y="{y0 + 5*cell + 28}" class="small">{r:g}</text>')
    body.append('  <text x="660" y="135" class="small">Index &gt; 1:</text>')
    body.append('  <text x="660" y="158" class="small">acid forcing exceeds</text>')
    body.append('  <text x="660" y="181" class="small">buffer capacity</text>')
    body.append('  <text x="660" y="235" class="small">Index &lt; 1:</text>')
    body.append('  <text x="660" y="258" class="small">buffer-dominated</text>')
    body.append('  <text x="40" y="590" class="caveat">Computed from dimensionless screening groups only; not calibrated acid generation or neutralization potential.</text>')
    write(FIG_DIR / "fig04_acid_buffer_index_heatmap.svg", svg(900, 620, "\n".join(body)))


def fig05_retardation_curves() -> None:
    scenarios = [
        ("Conservative tracer", 1.0, "#2f80b7"),
        ("Weak sorption", 2.0, "#3a8b4f"),
        ("Moderate sorption", 5.0, "#d35400"),
        ("Strong sorption", 15.0, "#8e44ad"),
    ]
    xs = [i / 25 for i in range(0, 101)]
    with (DATA_DIR / "retardation_scenarios.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["pore_volumes", "scenario", "retardation_factor", "normalized_concentration"])
        for name, r, _ in scenarios:
            for x in xs:
                c = 1.0 / (1.0 + math.exp(-(x - r) * 5.0))
                writer.writerow([f"{x:.3f}", name, r, f"{c:.6f}"])

    width, height = 950, 620
    x0, y0, w, h = 110, 90, 700, 410
    body = [f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>']
    body.append('  <text x="40" y="45" class="title">Breakthrough-screening curves under assumed retardation factors</text>')
    body.append(f'  <rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#f8fbfd" stroke="#34495e" stroke-width="1.8"/>')
    for gy in [0.25, 0.5, 0.75]:
        y = y0 + h * (1 - gy)
        body.append(f'  <line x1="{x0}" y1="{y}" x2="{x0+w}" y2="{y}" stroke="#d7dee2" stroke-width="1"/>')
        body.append(f'  <text x="{x0-45}" y="{y+5}" class="small">{gy:g}</text>')
    for gx in [1, 2, 3, 4]:
        x = x0 + w * (gx / 4)
        body.append(f'  <line x1="{x}" y1="{y0}" x2="{x}" y2="{y0+h}" stroke="#d7dee2" stroke-width="1"/>')
        body.append(f'  <text x="{x-5}" y="{y0+h+28}" class="small">{gx}</text>')
    body.append(f'  <text x="{x0 + 245}" y="{y0+h+65}" class="label">Pore volumes / conservative travel-time units</text>')
    body.append(f'  <text x="40" y="{y0+250}" class="label" transform="rotate(-90 40,{y0+250})">Normalized concentration</text>')
    for name, r, color in scenarios:
        pts = []
        for xval in xs:
            c = 1.0 / (1.0 + math.exp(-(xval - r) * 5.0))
            px = x0 + w * (xval / 4.0)
            py = y0 + h * (1.0 - c)
            pts.append(f"{px:.1f},{py:.1f}")
        body.append(f'  <polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="3"/>')
    for idx, (name, r, color) in enumerate(scenarios):
        y = 125 + idx * 34
        body.append(f'  <line x1="835" y1="{y}" x2="885" y2="{y}" stroke="{color}" stroke-width="4"/>')
        body.append(f'  <text x="895" y="{y+5}" class="small">{name} R={r:g}</text>')
    body.append('  <text x="40" y="590" class="caveat">Curves are analytic screening functions showing how retardation delays fronts; they are not PFLOTRAN observations or fitted well data.</text>')
    write(FIG_DIR / "fig05_retardation_screening_curves.svg", svg(width, height, "\n".join(body)))


def fig06_sensitivity_tornado() -> None:
    factors = [
        ("Pyrite oxidation rate", 0.95),
        ("Carbonate neutralization capacity", 0.82),
        ("Seepage flux / hydraulic gradient", 0.78),
        ("Fe-Mn oxide sorption capacity", 0.66),
        ("Dispersivity", 0.48),
        ("Redox boundary location", 0.44),
        ("Barite/Ra thermodynamic support", 0.39),
        ("Permeability anisotropy", 0.33),
    ]
    with (DATA_DIR / "sensitivity_screening_rank.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["factor", "relative_priority_score"])
        writer.writerows(factors)

    body = ['  <rect x="0" y="0" width="1000" height="620" fill="#ffffff"/>']
    body.append('  <text x="40" y="45" class="title">Prioritized sensitivity-analysis design for first PFLOTRAN runs</text>')
    x0, y0, max_w = 380, 105, 470
    for idx, (name, score) in enumerate(factors):
        y = y0 + idx * 52
        w = max_w * score
        color = "#c0392b" if idx < 3 else "#2f80b7"
        body.append(f'  <text x="60" y="{y+25}" class="small">{name}</text>')
        body.append(f'  <rect x="{x0}" y="{y}" width="{w:.1f}" height="30" fill="{color}" opacity="0.82"/>')
        body.append(f'  <text x="{x0+w+12:.1f}" y="{y+22}" class="small">{score:.2f}</text>')
    body.append('  <line x1="380" y1="535" x2="850" y2="535" stroke="#34495e" stroke-width="1.5"/>')
    body.append('  <text x="515" y="570" class="label">Relative priority score for uncertainty reduction</text>')
    body.append('  <text x="40" y="602" class="caveat">Ranking is an expert design aid derived from mechanism criticality, not a variance-based result from executed simulations.</text>')
    write(FIG_DIR / "fig06_sensitivity_tornado.svg", svg(1000, 620, "\n".join(body)))


def raster_figures() -> None:
    blue = (47, 128, 183)
    red = (192, 57, 43)
    orange = (211, 84, 0)
    green = (58, 139, 79)
    purple = (142, 68, 173)
    gray = (143, 143, 143)
    tan = (216, 201, 155)
    aquifer = (204, 231, 246)

    c = Canvas(1100, 620, (247, 251, 255))
    c.rect(70, 105, 300, 110, (183, 176, 166))
    c.rect(80, 215, 970, 110, tan)
    c.rect(30, 340, 1050, 155, aquifer)
    c.rect(30, 495, 1050, 75, gray)
    c.line(240, 210, 445, 350, red, 8)
    c.line(420, 367, 900, 392, blue, 8)
    c.line(445, 350, 840, 318, orange, 6)
    for x, y in [(520, 380), (720, 385), (930, 405)]:
        c.circle(x, y, 11, blue)
    c.save_png(FIG_DIR / "fig01_conceptual_cross_section.png")

    c = Canvas(1050, 620, (251, 252, 253))
    boxes = [
        (60, 100, red),
        (310, 100, orange),
        (560, 100, green),
        (810, 100, gray),
        (205, 300, purple),
        (455, 300, blue),
        (705, 300, green),
        (455, 480, (243, 243, 243)),
    ]
    for x, y, col in boxes:
        c.rect(x, y, 190, 82, col)
    for x1, y1, x2, y2, col in [
        (250, 141, 310, 141, red),
        (500, 141, 560, 141, orange),
        (750, 141, 810, 141, gray),
        (405, 183, 300, 300, purple),
        (455, 183, 520, 300, blue),
        (850, 183, 785, 300, green),
        (300, 382, 500, 480, purple),
        (550, 382, 560, 480, blue),
        (790, 382, 650, 480, green),
    ]:
        c.line(x1, y1, x2, y2, col, 6)
    c.save_png(FIG_DIR / "fig02_reaction_network.png")

    c = Canvas(1050, 620)
    c.rect(120, 100, 780, 390, (248, 251, 253))
    c.rect(120, 100, 220, 90, (183, 176, 166))
    c.rect(120, 190, 780, 105, tan)
    c.rect(120, 295, 780, 140, aquifer)
    c.rect(120, 435, 780, 55, gray)
    c.line(90, 118, 120, 118, blue, 8)
    c.line(900, 362, 960, 362, blue, 8)
    c.line(120, 360, 70, 360, gray, 5)
    for x, y in [(430, 360), (610, 365), (780, 374)]:
        c.circle(x, y, 10, blue)
    c.save_png(FIG_DIR / "fig03_domain_boundary_conditions.png")

    reactivity = [0.1, 0.3, 1.0, 3.0, 10.0]
    buffer = [0.1, 0.3, 1.0, 3.0, 10.0]
    c = Canvas(900, 620)
    cell = 78
    x0, y0 = 235, 100
    vals = [r / b for b in buffer for r in reactivity]
    min_v, max_v = math.log10(min(vals)), math.log10(max(vals))
    for j, b in enumerate(reversed(buffer)):
        for i, r in enumerate(reactivity):
            fill = color_for(math.log10(r / b), min_v, max_v)
            col = tuple(int(fill[k : k + 2], 16) for k in (1, 3, 5))
            c.rect(x0 + i * cell, y0 + j * cell, cell - 2, cell - 2, col)
    c.save_png(FIG_DIR / "fig04_acid_buffer_index_heatmap.png")

    c = Canvas(950, 620)
    x0, y0, w, h = 110, 90, 700, 410
    c.rect(x0, y0, w, h, (248, 251, 253))
    for gy in [0.25, 0.5, 0.75]:
        y = int(y0 + h * (1 - gy))
        c.line(x0, y, x0 + w, y, (215, 222, 226), 2)
    for gx in [1, 2, 3, 4]:
        x = int(x0 + w * (gx / 4))
        c.line(x, y0, x, y0 + h, (215, 222, 226), 2)
    for r, col in [(1.0, blue), (2.0, green), (5.0, orange), (15.0, purple)]:
        pts = []
        for i in range(101):
            xv = i / 25
            yy = 1.0 / (1.0 + math.exp(-(xv - r) * 5.0))
            pts.append((int(x0 + w * (xv / 4.0)), int(y0 + h * (1.0 - yy))))
        c.polyline(pts, col, 4)
    c.save_png(FIG_DIR / "fig05_retardation_screening_curves.png")

    c = Canvas(1000, 620)
    factors = [0.95, 0.82, 0.78, 0.66, 0.48, 0.44, 0.39, 0.33]
    for idx, score in enumerate(factors):
        y = 105 + idx * 52
        col = red if idx < 3 else blue
        c.rect(380, y, int(470 * score), 30, col)
    c.line(380, 535, 850, 535, (52, 73, 94), 3)
    c.save_png(FIG_DIR / "fig06_sensitivity_tornado.png")


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    fig01_conceptual_cross_section()
    fig02_reaction_network()
    fig03_domain_boundary_conditions()
    fig04_acid_buffer_heatmap()
    fig05_retardation_curves()
    fig06_sensitivity_tornado()
    raster_figures()


if __name__ == "__main__":
    main()
