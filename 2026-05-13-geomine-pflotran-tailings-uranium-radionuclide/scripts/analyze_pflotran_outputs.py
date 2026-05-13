#!/usr/bin/env python3
"""
Parse the executed PFLOTRAN screening runs and generate paper-ready summaries.

The two runs are synthetic 1D screening cases used to test the paper's
mechanistic claim that carbonate buffering can decouple acid-front migration
from U/sulfate transport. They are PFLOTRAN outputs, but they are not calibrated
site predictions.
"""

from __future__ import annotations

import csv
import json
import math
import re
import struct
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_DIR = ROOT / "pflotran_runs"
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
MANIFEST_PATH = ROOT / "pflotran_run_manifest.json"


SCENARIOS = {
    "calcite_buffered": {
        "label": "Calcite buffered",
        "input": RUN_DIR / "calcite_buffered" / "tailings_u_calcite_buffered.in",
        "tec": RUN_DIR / "calcite_buffered" / "tailings_u_calcite_buffered-005.tec",
        "out": RUN_DIR / "calcite_buffered" / "tailings_u_calcite_buffered.out",
        "initial_calcite_vf": 1.0e-3,
        "color": (47, 128, 183),
    },
    "no_calcite": {
        "label": "No calcite",
        "input": RUN_DIR / "no_calcite" / "tailings_u_no_calcite.in",
        "tec": RUN_DIR / "no_calcite" / "tailings_u_no_calcite-005.tec",
        "out": RUN_DIR / "no_calcite" / "tailings_u_no_calcite.out",
        "initial_calcite_vf": 0.0,
        "color": (192, 57, 43),
    },
}


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
            for xx in range(max(0, x), min(self.width, x + w)):
                self.set(xx, yy, color)

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


def parse_tec(path: Path) -> list[dict[str, float]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    variables_line = next(line for line in lines if line.startswith("VARIABLES="))
    names = re.findall(r'"([^"]+)"', variables_line)
    rows: list[dict[str, float]] = []
    for line in lines:
        if not line.strip() or line.startswith(("TITLE", "VARIABLES", "ZONE")):
            continue
        values = [float(value) for value in line.split()]
        rows.append({name: values[i] for i, name in enumerate(names)})
    return rows


def parse_log(path: Path) -> dict[str, float | int | str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    flow = re.search(r"FLOW TS SNES steps =\s*(\d+)\s+newton =\s*(\d+)\s+linear =\s*(\d+)\s+cuts =\s*(\d+)", text)
    tran = re.search(r"TRAN TS SNES steps =\s*(\d+)\s+newton =\s*(\d+)\s+linear =\s*(\d+)\s+cuts =\s*(\d+)", text)
    wall = re.search(r"Wall Clock Time:\s*([0-9.E+-]+)", text)
    return {
        "flow_steps": int(flow.group(1)) if flow else None,
        "flow_newton": int(flow.group(2)) if flow else None,
        "flow_linear": int(flow.group(3)) if flow else None,
        "flow_cuts": int(flow.group(4)) if flow else None,
        "transport_steps": int(tran.group(1)) if tran else None,
        "transport_newton": int(tran.group(2)) if tran else None,
        "transport_linear": int(tran.group(3)) if tran else None,
        "transport_cuts": int(tran.group(4)) if tran else None,
        "wall_clock_seconds": float(wall.group(1)) if wall else None,
    }


def value_at(rows: list[dict[str, float]], x: float, key: str) -> float:
    return min(rows, key=lambda row: abs(row["X [m]"] - x))[key]


def front_distance(rows: list[dict[str, float]], key: str, threshold: float, op: str) -> float:
    xs = [
        row["X [m]"]
        for row in rows
        if (row[key] < threshold if op == "lt" else row[key] > threshold)
    ]
    return max(xs) if xs else 0.0


def summarize(name: str, rows: list[dict[str, float]], log: dict[str, float | int | str]) -> dict[str, float | int | str]:
    pH = [row["pH"] for row in rows]
    sulfate = [row["Total SO4-- [M]"] for row in rows]
    uranium = [row["Total UO2++ [M]"] for row in rows]
    calcite = [row["Calcite VF [m^3 mnrl/m^3 bulk]"] for row in rows]
    initial_vf = float(SCENARIOS[name]["initial_calcite_vf"])
    calcite_depletion_pct = 0.0
    if initial_vf > 0:
        calcite_depletion_pct = 100.0 * (initial_vf - min(calcite)) / initial_vf
    return {
        "scenario": name,
        "label": str(SCENARIOS[name]["label"]),
        "final_time_years": 25.0,
        "cells": len(rows),
        "pH_min": min(pH),
        "pH_max": max(pH),
        "pH_x0_5m": value_at(rows, 0.5, "pH"),
        "pH_x25_5m": value_at(rows, 25.5, "pH"),
        "pH_x50_5m": value_at(rows, 50.5, "pH"),
        "pH_x75_5m": value_at(rows, 75.5, "pH"),
        "pH_x99_5m": value_at(rows, 99.5, "pH"),
        "acid_front_pH_lt_4_m": front_distance(rows, "pH", 4.0, "lt"),
        "low_pH_front_pH_lt_6_5_m": front_distance(rows, "pH", 6.5, "lt"),
        "sulfate_front_gt_2_5e_3_M_m": front_distance(rows, "Total SO4-- [M]", 2.5e-3, "gt"),
        "uranium_front_gt_5e_7_M_m": front_distance(rows, "Total UO2++ [M]", 5e-7, "gt"),
        "sulfate_outlet_M": value_at(rows, 99.5, "Total SO4-- [M]"),
        "uranium_outlet_M": value_at(rows, 99.5, "Total UO2++ [M]"),
        "calcite_vf_min": min(calcite),
        "calcite_vf_max": max(calcite),
        "calcite_depletion_pct": calcite_depletion_pct,
        **log,
    }


def write_csv(rows: list[dict[str, float | int | str]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_profiles(all_rows: dict[str, list[dict[str, float]]]) -> None:
    with (DATA_DIR / "pflotran_profiles_25y.csv").open("w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "scenario",
            "x_m",
            "pH",
            "total_so4_m",
            "total_uo2_m",
            "total_hco3_m",
            "total_ca_m",
            "calcite_vf",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for scenario, rows in all_rows.items():
            for row in rows:
                writer.writerow(
                    {
                        "scenario": scenario,
                        "x_m": row["X [m]"],
                        "pH": row["pH"],
                        "total_so4_m": row["Total SO4-- [M]"],
                        "total_uo2_m": row["Total UO2++ [M]"],
                        "total_hco3_m": row["Total HCO3- [M]"],
                        "total_ca_m": row["Total Ca++ [M]"],
                        "calcite_vf": row["Calcite VF [m^3 mnrl/m^3 bulk]"],
                    }
                )


def write_svg(path: Path, width: int, height: int, body: str) -> None:
    path.write_text(
        f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    text {{ font-family: Arial, Helvetica, sans-serif; fill: #17202a; }}
    .title {{ font-size: 19px; font-weight: 700; }}
    .label {{ font-size: 14px; font-weight: 600; }}
    .small {{ font-size: 12px; }}
    .note {{ font-size: 12px; fill: #5f6b72; }}
  </style>
{body}
</svg>
""",
        encoding="utf-8",
    )


def to_hex(color: tuple[int, int, int]) -> str:
    return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"


def plot_svg(
    all_rows: dict[str, list[dict[str, float]]],
    path: Path,
    title: str,
    y_label: str,
    variables: list[tuple[str, str, float, str]],
    y_min: float,
    y_max: float,
    log_y: bool = False,
) -> None:
    width, height = 1050, 620
    x0, y0, w, h = 115, 90, 730, 410

    def tx(x: float) -> float:
        return x0 + w * (x / 100.0)

    def ty(y: float) -> float:
        if log_y:
            y = max(y, y_min)
            frac = (math.log10(y) - math.log10(y_min)) / (math.log10(y_max) - math.log10(y_min))
        else:
            frac = (y - y_min) / (y_max - y_min)
        return y0 + h * (1.0 - frac)

    body = [
        f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>',
        f'  <text x="40" y="45" class="title">{title}</text>',
        f'  <rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#f8fbfd" stroke="#34495e" stroke-width="1.8"/>',
    ]
    for x in [0, 25, 50, 75, 100]:
        px = tx(x)
        body.append(f'  <line x1="{px:.1f}" y1="{y0}" x2="{px:.1f}" y2="{y0+h}" stroke="#d7dee2" stroke-width="1"/>')
        body.append(f'  <text x="{px-8:.1f}" y="{y0+h+28}" class="small">{x}</text>')
    ticks = [y_min, (y_min + y_max) / 2.0, y_max] if not log_y else [y_min, math.sqrt(y_min * y_max), y_max]
    for value in ticks:
        py = ty(value)
        label = f"{value:.1e}" if log_y else f"{value:g}"
        body.append(f'  <line x1="{x0}" y1="{py:.1f}" x2="{x0+w}" y2="{py:.1f}" stroke="#d7dee2" stroke-width="1"/>')
        body.append(f'  <text x="{x0-75}" y="{py+4:.1f}" class="small">{label}</text>')
    body.append(f'  <text x="{x0+285}" y="{y0+h+65}" class="label">Distance from source boundary (m)</text>')
    body.append(f'  <text x="38" y="{y0+250}" class="label" transform="rotate(-90 38,{y0+250})">{y_label}</text>')

    legend_y = 118
    for idx, (scenario, key, multiplier, label_suffix) in enumerate(variables):
        color = to_hex(SCENARIOS[scenario]["color"])
        rows = all_rows[scenario]
        points = " ".join(f'{tx(row["X [m]"]):.1f},{ty(row[key] * multiplier):.1f}' for row in rows)
        dash = ' stroke-dasharray="8 6"' if "SO4" in key else ""
        body.append(f'  <polyline points="{points}" fill="none" stroke="{color}" stroke-width="3"{dash}/>')
        ly = legend_y + idx * 32
        body.append(f'  <line x1="870" y1="{ly}" x2="920" y2="{ly}" stroke="{color}" stroke-width="4"{dash}/>')
        body.append(f'  <text x="930" y="{ly+5}" class="small">{label_suffix}</text>')
    body.append('  <text x="40" y="590" class="note">Executed PFLOTRAN 1D synthetic screening output at 25 years; not calibrated site prediction.</text>')
    write_svg(path, width, height, "\n".join(body))


def plot_png(
    all_rows: dict[str, list[dict[str, float]]],
    path: Path,
    variables: list[tuple[str, str, float]],
    y_min: float,
    y_max: float,
    log_y: bool = False,
) -> None:
    width, height = 1050, 620
    x0, y0, w, h = 115, 90, 730, 410
    c = Canvas(width, height)
    c.rect(x0, y0, w, h, (248, 251, 253))
    for x in [0, 25, 50, 75, 100]:
        px = x0 + int(w * (x / 100.0))
        c.line(px, y0, px, y0 + h, (215, 222, 226), 2)
    for frac in [0.25, 0.5, 0.75]:
        py = y0 + int(h * frac)
        c.line(x0, py, x0 + w, py, (215, 222, 226), 2)
    c.line(x0, y0, x0, y0 + h, (52, 73, 94), 3)
    c.line(x0, y0 + h, x0 + w, y0 + h, (52, 73, 94), 3)

    def tx(x: float) -> int:
        return x0 + int(w * (x / 100.0))

    def ty(y: float) -> int:
        if log_y:
            y = max(y, y_min)
            frac = (math.log10(y) - math.log10(y_min)) / (math.log10(y_max) - math.log10(y_min))
        else:
            frac = (y - y_min) / (y_max - y_min)
        return y0 + int(h * (1.0 - frac))

    for scenario, key, multiplier in variables:
        rows = all_rows[scenario]
        points = [(tx(row["X [m]"]), ty(row[key] * multiplier)) for row in rows]
        c.polyline(points, SCENARIOS[scenario]["color"], 4)
    c.save_png(path)


def make_figures(all_rows: dict[str, list[dict[str, float]]]) -> None:
    plot_svg(
        all_rows,
        FIG_DIR / "fig07_pflotran_ph_profiles.svg",
        "Executed PFLOTRAN 1D screening: pH profiles after 25 years",
        "pH",
        [
            ("calcite_buffered", "pH", 1.0, "Calcite buffered"),
            ("no_calcite", "pH", 1.0, "No calcite"),
        ],
        2.8,
        8.3,
    )
    plot_png(
        all_rows,
        FIG_DIR / "fig07_pflotran_ph_profiles.png",
        [
            ("calcite_buffered", "pH", 1.0),
            ("no_calcite", "pH", 1.0),
        ],
        2.8,
        8.3,
    )
    plot_svg(
        all_rows,
        FIG_DIR / "fig08_pflotran_u_sulfate_profiles.svg",
        "Executed PFLOTRAN 1D screening: U and sulfate profiles after 25 years",
        "Concentration (M)",
        [
            ("calcite_buffered", "Total UO2++ [M]", 1.0, "U calcite"),
            ("no_calcite", "Total UO2++ [M]", 1.0, "U no calcite"),
            ("calcite_buffered", "Total SO4-- [M]", 1.0, "SO4 calcite"),
            ("no_calcite", "Total SO4-- [M]", 1.0, "SO4 no calcite"),
        ],
        1.0e-9,
        1.0e-2,
        log_y=True,
    )
    plot_png(
        all_rows,
        FIG_DIR / "fig08_pflotran_u_sulfate_profiles.png",
        [
            ("calcite_buffered", "Total UO2++ [M]", 1.0),
            ("no_calcite", "Total UO2++ [M]", 1.0),
            ("calcite_buffered", "Total SO4-- [M]", 1.0),
            ("no_calcite", "Total SO4-- [M]", 1.0),
        ],
        1.0e-9,
        1.0e-2,
        log_y=True,
    )


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    all_rows: dict[str, list[dict[str, float]]] = {}
    summaries: list[dict[str, float | int | str]] = []
    manifest_runs = []
    for scenario, spec in SCENARIOS.items():
        rows = parse_tec(spec["tec"])
        log = parse_log(spec["out"])
        all_rows[scenario] = rows
        summaries.append(summarize(scenario, rows, log))
        manifest_runs.append(
            {
                "scenario": scenario,
                "input_deck": str(Path(spec["input"]).relative_to(ROOT)),
                "final_tecplot_output": str(Path(spec["tec"]).relative_to(ROOT)),
                "log": str(Path(spec["out"]).relative_to(ROOT)),
                "command": f"docker run --rm --platform linux/amd64 -v {ROOT}/pflotran_runs/{scenario if scenario == 'no_calcite' else 'calcite_buffered'}:/work -w /work pflotran/pflotran:ubuntu22 pflotran -pflotranin {Path(spec['input']).name}",
                "exit_status": 0,
                "convergence": log,
            }
        )

    write_csv(summaries, DATA_DIR / "pflotran_screening_summary.csv")
    write_profiles(all_rows)
    make_figures(all_rows)

    manifest = {
        "created": "2026-05-13",
        "status": "executed_synthetic_screening_not_calibrated_not_validated",
        "solver": "PFLOTRAN in Docker image pflotran/pflotran:ubuntu22",
        "docker_repo_digest": "pflotran/pflotran@sha256:b9413b676cf826ba6ce9bf733e1c05e558fae00cedc0814d291450d52fbd8197",
        "docker_image_created": "2023-09-05T18:12:24.4708764Z",
        "petsc_version_reported_by_pflotran_help": "PETSc Release Version 3.19.3",
        "platform": "linux/amd64",
        "thermodynamic_database_in_container": "/software/pflotran/database/hanford.dat",
        "scenarios": manifest_runs,
        "result_tables": [
            "data/pflotran_screening_summary.csv",
            "data/pflotran_profiles_25y.csv",
        ],
        "result_figures": [
            "figures/fig07_pflotran_ph_profiles.svg",
            "figures/fig07_pflotran_ph_profiles.png",
            "figures/fig08_pflotran_u_sulfate_profiles.svg",
            "figures/fig08_pflotran_u_sulfate_profiles.png",
        ],
        "interpretation_boundary": "Synthetic 1D model used to test mechanism directionality only; no field calibration or regulatory conclusion.",
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
