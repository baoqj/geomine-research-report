#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build data tables, figures, model templates, and the paper package.

The script intentionally uses only the Python standard library so the report can
be regenerated in a clean research workspace.
"""

from __future__ import annotations

import csv
import html
import json
import math
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean


REPORT = Path(__file__).resolve().parents[1]
DATA = REPORT / "data"
FIG = REPORT / "figures"
MODELS = REPORT / "models"
SOURCES = REPORT / "sources"


def ensure_dirs() -> None:
    for path in (DATA, FIG, MODELS, SOURCES):
        path.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def parse_measurement(text: str) -> dict:
    raw = (text or "").strip().replace("\ufeff", "")
    raw = raw.replace("μ", "u").replace("µ", "u").replace("�g", "ug")
    censored = raw.startswith("<")
    clean = raw[1:] if censored else raw
    m = re.search(r"[-+]?\d[\d,]*(?:\.\d+)?", clean)
    if not m:
        return {"raw": text, "censored": censored, "value": None, "unit": ""}
    value = float(m.group(0).replace(",", ""))
    unit = clean[m.end() :].strip()
    return {"raw": text, "censored": censored, "value": value, "unit": unit}


def unit_for_parameter(parameter: str, unit: str) -> str:
    unit = unit.replace("μ", "u").replace("µ", "u").replace("�g", "ug")
    if parameter in {"Total hardness", "Total Suspended Solids"}:
        return "mg/L"
    if parameter in {"Lead-210", "Polonium-210", "Radium-226", "Radium-228", "Thorium-230"}:
        if "Bq/L" in unit:
            return "Bq/L"
        if "Bq/kg" in unit:
            return "Bq/kg fresh weight"
    if parameter == "Uranium":
        if "mg/L" in unit:
            return "ug/L"
        if "ug/L" in unit:
            return "ug/L"
        if "ug/g" in unit or "mg/kg" in unit:
            return "ug/g fresh weight"
    if parameter == "pH":
        return "pH"
    if "mg/L" in unit:
        return "mg/L"
    if "ug/L" in unit:
        return "ug/L"
    return unit.strip()


def convert_value(parameter: str, value: float | None, unit: str, target: str) -> float | None:
    if value is None:
        return None
    norm = unit.replace("μ", "u").replace("µ", "u").replace("�g", "ug")
    if target == "ug/L":
        if "mg/L" in norm:
            return value * 1000.0
        return value
    if target == "Bq/L":
        return value
    if target == "Bq/kg fresh weight":
        return value
    if target == "ug/g fresh weight":
        if "mg/kg" in norm:
            return value
        return value
    if target == "mg/L":
        if "ug/L" in norm:
            return value / 1000.0
        return value
    return value


def summarize_iemp_csv() -> tuple[list[dict], list[dict], dict]:
    source = DATA / "cnsc_iemp_cigar_lake_2020_2024.csv"
    if not source.exists():
        raise FileNotFoundError(source)

    with source.open("r", encoding="utf-8", errors="replace", newline="") as f:
        rows = list(csv.DictReader(f))

    water_params = {"Uranium", "Lead-210", "Polonium-210", "Radium-226", "Thorium-230", "pH", "Total hardness", "Total Hardness", "Total Suspended Solids"}
    water_groups: dict[str, list[dict]] = defaultdict(list)
    food_groups: dict[tuple[str, str], list[dict]] = defaultdict(list)

    for row in rows:
        parameter = row.get("Parameter", "").strip()
        parameter_key = "Total hardness" if parameter == "Total Hardness" else parameter
        sample_type = row.get("Sample Type", "").strip()
        if sample_type == "Water" and parameter in water_params:
            water_groups[parameter_key].append(row)
        if sample_type == "Food" and parameter in {"Uranium", "Lead-210", "Polonium-210", "Radium-226", "Thorium-230"}:
            food_groups[(row.get("Sample Description", "").strip(), parameter)].append(row)

    water_summary: list[dict] = []
    for parameter_key, group in sorted(water_groups.items()):
        values_half_dl: list[float] = []
        values_upper: list[float] = []
        guideline_values: list[float] = []
        censored_count = 0
        target_unit = None
        years = set()
        stations = set()
        for row in group:
            result = parse_measurement(row.get("Result", ""))
            guide = parse_measurement(row.get("Guideline/Screening Levels", ""))
            target_unit = target_unit or unit_for_parameter(parameter_key, result["unit"] or guide["unit"])
            val = convert_value(parameter_key, result["value"], result["unit"], target_unit)
            guide_val = convert_value(parameter_key, guide["value"], guide["unit"], target_unit)
            if val is None:
                continue
            years.add(str(row.get("Year", "")).replace(".0", ""))
            stations.add(row.get("Station ID", ""))
            if result["censored"]:
                censored_count += 1
                values_half_dl.append(val / 2.0)
                values_upper.append(val)
            else:
                values_half_dl.append(val)
                values_upper.append(val)
            if guide_val is not None:
                guideline_values.append(guide_val)
        if not values_upper:
            continue
        guide_min = min(guideline_values) if guideline_values else None
        if parameter_key in {"pH", "Total hardness", "Total Suspended Solids"}:
            guide_min = None
            ratio = None
        else:
            ratio = max(values_upper) / guide_min if guide_min and guide_min > 0 else None
        water_summary.append(
            {
                "parameter": parameter_key,
                "sample_type": "Water",
                "n": len(values_upper),
                "years": ";".join(sorted(y for y in years if y)),
                "stations": ";".join(sorted(s for s in stations if s)),
                "unit": target_unit or "",
                "left_censored_n": censored_count,
                "mean_half_dl": round(mean(values_half_dl), 6),
                "max_upper_bound": round(max(values_upper), 6),
                "min_upper_bound": round(min(values_upper), 6),
                "iemp_guideline_or_screening": round(guide_min, 6) if guide_min else "",
                "max_upper_to_iemp_screening_ratio": round(ratio, 6) if ratio is not None else "",
                "interpretation": "below IEMP screening under conservative upper-bound treatment" if ratio is not None and ratio < 1 else "no numeric screening ratio",
            }
        )

    water_summary = sorted(water_summary, key=lambda r: r["parameter"])

    food_summary: list[dict] = []
    for (sample_desc, parameter), group in sorted(food_groups.items()):
        target_unit = None
        vals_half: list[float] = []
        vals_upper: list[float] = []
        guide_vals: list[float] = []
        censored_count = 0
        years = set()
        for row in group:
            result = parse_measurement(row.get("Result", ""))
            guide = parse_measurement(row.get("Guideline/Screening Levels", ""))
            target_unit = target_unit or unit_for_parameter(parameter, result["unit"] or guide["unit"])
            val = convert_value(parameter, result["value"], result["unit"], target_unit)
            guide_val = convert_value(parameter, guide["value"], guide["unit"], target_unit)
            if val is None:
                continue
            years.add(str(row.get("Year", "")).replace(".0", ""))
            if result["censored"]:
                censored_count += 1
                vals_half.append(val / 2.0)
                vals_upper.append(val)
            else:
                vals_half.append(val)
                vals_upper.append(val)
            if guide_val is not None:
                guide_vals.append(guide_val)
        if not vals_upper:
            continue
        guide_min = min(guide_vals) if guide_vals else None
        ratio = max(vals_upper) / guide_min if guide_min and guide_min > 0 else None
        food_summary.append(
            {
                "sample_description": sample_desc,
                "parameter": parameter,
                "n": len(vals_upper),
                "years": ";".join(sorted(y for y in years if y)),
                "unit": target_unit or "",
                "left_censored_n": censored_count,
                "mean_half_dl": round(mean(vals_half), 6),
                "max_upper_bound": round(max(vals_upper), 6),
                "iemp_screening": round(guide_min, 6) if guide_min else "",
                "max_upper_to_iemp_screening_ratio": round(ratio, 6) if ratio is not None else "",
            }
        )

    metadata = {
        "raw_rows": len(rows),
        "water_rows_used": sum(int(r["n"]) for r in water_summary),
        "food_rows_used": sum(int(r["n"]) for r in food_summary),
        "censored_rule": "For '<' values, mean uses 0.5*detection-limit; maximum screening ratio uses the full detection-limit as an upper bound.",
    }

    return water_summary, food_summary, metadata


def build_source_tables(water_summary: list[dict], food_summary: list[dict]) -> None:
    bibliography = [
        {
            "id": "Vengosh2022_STOTEN_review",
            "type": "peer_reviewed_review",
            "title": "A critical review on the occurrence and distribution of the uranium- and thorium-decay nuclides and their effect on the quality of groundwater",
            "year": "2022",
            "url": "https://www.sciencedirect.com/science/article/pii/S0048969721069904",
            "doi": "10.1016/j.scitotenv.2021.151914",
            "used_for": "mechanistic framework: differential U/Ra/Rn/Pb/Po occurrence, recoil, sorption, precipitation, residence time",
        },
        {
            "id": "PineroGarcia2025_Sweden_wells",
            "type": "peer_reviewed_open_access_article",
            "title": "Comprehensive analysis of naturally occurring radionuclides in well water: Isotopic ratios, mitigation, and dose assessment",
            "year": "2025",
            "url": "https://www.sciencedirect.com/science/article/pii/S0147651324015562",
            "doi": "10.1016/j.ecoenv.2024.117480",
            "used_for": "comparative well-water data and dose ranking for 210Po, 210Pb, 226Ra, 228Ra, 238U, 234U",
        },
        {
            "id": "HealthCanada2025_Radiological_DWQ",
            "type": "regulatory_guideline",
            "title": "Guidelines for Canadian drinking water quality: Radiological parameters",
            "year": "2025",
            "url": "https://www.canada.ca/en/health-canada/services/publications/healthy-living/guidelines-drinking-water-quality-radiological-parameters.html",
            "doi": "",
            "used_for": "Canadian MACs/reference concentrations, screening formula, 1 mSv/y and 1.53 L/day intake assumption",
        },
        {
            "id": "HealthCanada2019_Uranium_DWQ",
            "type": "regulatory_guideline",
            "title": "Guidelines for Canadian Drinking Water Quality Guideline Technical Document - Uranium",
            "year": "2019",
            "url": "https://www.canada.ca/en/health-canada/services/publications/healthy-living/guidelines-canadian-drinking-water-quality-guideline-technical-document-uranium.html",
            "doi": "",
            "used_for": "total natural uranium MAC of 0.02 mg/L based primarily on chemical toxicity",
        },
        {
            "id": "CNSC_IEMP_CigarLake_2024",
            "type": "public_monitoring_dataset",
            "title": "Independent Environmental Monitoring Program: Cigar Lake Operation",
            "year": "2024",
            "url": "https://www.cnsc-ccsn.gc.ca/eng/resources/maps-of-nuclear-facilities/iemp/cigar-lake/",
            "doi": "",
            "used_for": "public mine-environment CSV data for water and food around a high-grade uranium mine",
        },
        {
            "id": "Frontiers2020_U_speciation",
            "type": "peer_reviewed_review",
            "title": "Speciation of Uranium and Plutonium From Nuclear Legacy Sites to the Environment: A Mini Review",
            "year": "2020",
            "url": "https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2020.00630/full",
            "doi": "10.3389/fchem.2020.00630",
            "used_for": "U(VI)/U(IV), carbonate/hydroxyl complexes, redox and sorption controls",
        },
    ]
    write_csv(DATA / "source_bibliography.csv", bibliography, list(bibliography[0].keys()))

    health = [
        {"analyte": "Gross alpha", "value": 0.5, "unit": "Bq/L", "basis": "initial screening criterion", "source": "HealthCanada2025_Radiological_DWQ"},
        {"analyte": "Gross beta", "value": 1.0, "unit": "Bq/L", "basis": "initial screening criterion", "source": "HealthCanada2025_Radiological_DWQ"},
        {"analyte": "Lead-210", "value": 2.0, "unit": "Bq/L", "basis": "MAC from 1 mSv/y reference dose", "source": "HealthCanada2025_Radiological_DWQ"},
        {"analyte": "Radium-226", "value": 5.0, "unit": "Bq/L", "basis": "MAC from 1 mSv/y reference dose", "source": "HealthCanada2025_Radiological_DWQ"},
        {"analyte": "Radium-228", "value": 2.0, "unit": "Bq/L", "basis": "MAC from 1 mSv/y reference dose", "source": "HealthCanada2025_Radiological_DWQ"},
        {"analyte": "Polonium-210", "value": 1.0, "unit": "Bq/L", "basis": "Appendix C reference concentration from 1 mSv/y", "source": "HealthCanada2025_Radiological_DWQ"},
        {"analyte": "Radon-222", "value": 2000.0, "unit": "Bq/L", "basis": "Appendix C reference concentration; inhalation from indoor air remains primary management pathway", "source": "HealthCanada2025_Radiological_DWQ"},
        {"analyte": "Total natural uranium", "value": 20.0, "unit": "ug/L", "basis": "MAC based primarily on chemical toxicity", "source": "HealthCanada2019_Uranium_DWQ"},
    ]
    write_csv(DATA / "health_canada_reference_levels.csv", health, list(health[0].keys()))

    annual_intake_l = 1.53 * 365.0
    dose_parameters = []
    for row in health:
        if row["unit"] == "Bq/L" and row["analyte"] not in {"Gross alpha", "Gross beta"}:
            coeff = 1.0e-3 / (float(row["value"]) * annual_intake_l)
            dose_parameters.append(
                {
                    "analyte": row["analyte"],
                    "reference_concentration_Bq_L": row["value"],
                    "annual_intake_L_y": round(annual_intake_l, 2),
                    "reference_dose_Sv_y": 0.001,
                    "mac_equivalent_dose_coefficient_Sv_Bq": f"{coeff:.6e}",
                    "note": "Back-calculated from Health Canada reference concentration; use for screening-index comparison, not as a substitute for ICRP age-specific coefficients.",
                }
            )
    write_csv(DATA / "dose_model_parameters.csv", dose_parameters, list(dose_parameters[0].keys()))

    properties = [
        {
            "nuclide": "238U",
            "half_life": "4.468e9 y",
            "decay_mode": "alpha",
            "dominant_aqueous_behavior": "U(VI) uranyl carbonate complexes in oxic carbonate water; U(IV) low-solubility phases under reducing conditions",
            "migration_controls": "Eh, pH, alkalinity, Ca/Mg carbonate complexes, Fe/Mn oxides, phosphate, organic matter, colloids",
            "risk_role": "chemical toxicity often more limiting than radiological dose for natural uranium in drinking water",
        },
        {
            "nuclide": "234U",
            "half_life": "2.455e5 y",
            "decay_mode": "alpha",
            "dominant_aqueous_behavior": "chemically uranium; activity ratio affected by alpha recoil and preferential leaching",
            "migration_controls": "same as uranium plus recoil-induced disequilibrium",
            "risk_role": "useful disequilibrium tracer; dose usually lower than Pb/Ra/Po in Swedish well evidence",
        },
        {
            "nuclide": "226Ra",
            "half_life": "1600 y",
            "decay_mode": "alpha",
            "dominant_aqueous_behavior": "divalent alkaline-earth cation; not redox sensitive",
            "migration_controls": "Ba/Sr/Ca competition, sulfate and barite/celestite solid solution, carbonate, ionic strength, cation exchange, recoil",
            "risk_role": "dose-relevant and chemically decoupled from dissolved uranium",
        },
        {
            "nuclide": "228Ra",
            "half_life": "5.75 y",
            "decay_mode": "beta",
            "dominant_aqueous_behavior": "divalent radium from 232Th series",
            "migration_controls": "same geochemistry as Ra-226; source tied to Th-bearing minerals rather than U abundance",
            "risk_role": "high dose coefficient; Swedish dose rank second in mean contribution",
        },
        {
            "nuclide": "222Rn",
            "half_life": "3.82 d",
            "decay_mode": "alpha",
            "dominant_aqueous_behavior": "noble gas dissolved in groundwater; volatile at air-water interfaces",
            "migration_controls": "226Ra distribution, emanation coefficient, fracture aperture, residence time, degassing, advection length",
            "risk_role": "mainly inhalation after outgassing; water concentration is a fracture/lithology tracer",
        },
        {
            "nuclide": "210Pb",
            "half_life": "22.2 y",
            "decay_mode": "beta,gamma",
            "dominant_aqueous_behavior": "particle-reactive Pb(II), carbonate/chloride complexes possible",
            "migration_controls": "Fe/Mn oxides, organic matter, colloids, redox cycling, corrosion/scale deposition",
            "risk_role": "top mean contributor to Swedish well-water indicative dose",
        },
        {
            "nuclide": "210Po",
            "half_life": "138.3 d",
            "decay_mode": "alpha",
            "dominant_aqueous_behavior": "strongly particle-reactive chalcophile/metalloid behavior; surface and organic association",
            "migration_controls": "Fe/Mn oxides, sulfides, organic matter, colloids, unsupported production from Pb-210, filtration/aeration response",
            "risk_role": "hotspot dose driver when unsupported Po is high; also important in biota/sediment pathways",
        },
    ]
    write_csv(DATA / "radionuclide_properties.csv", properties, list(properties[0].keys()))

    swedish = [
        {"radionuclide": "210Po", "n_or_detection": ">90% detected", "range_min_mBq_L": 0.2, "range_max_mBq_L": 1410, "mean_mBq_L": 100, "sd_mBq_L": 300, "median_mBq_L": 6, "iqr_mBq_L": 30, "dose_rank": 3, "note": "For wells with >150 mBq/L, Po may contribute 50-90% of indicative dose.", "source": "PineroGarcia2025_Sweden_wells"},
        {"radionuclide": "210Pb", "n_or_detection": "all samples detected", "range_min_mBq_L": "", "range_max_mBq_L": "", "mean_mBq_L": "", "sd_mBq_L": "", "median_mBq_L": "", "iqr_mBq_L": "", "dose_rank": 1, "note": "Mean dose contribution ranked first; source page did not expose a machine-readable numeric activity table.", "source": "PineroGarcia2025_Sweden_wells"},
        {"radionuclide": "226Ra", "n_or_detection": "all 56 detected", "range_min_mBq_L": 0.8, "range_max_mBq_L": 598, "mean_mBq_L": 40, "sd_mBq_L": 100, "median_mBq_L": 10, "iqr_mBq_L": 40, "dose_rank": 4, "note": "Radium is chemically decoupled from uranium and controlled by alkaline-earth/sulfate chemistry.", "source": "PineroGarcia2025_Sweden_wells"},
        {"radionuclide": "228Ra", "n_or_detection": "about 85% detected", "range_min_mBq_L": 1, "range_max_mBq_L": 258, "mean_mBq_L": 30, "sd_mBq_L": 50, "median_mBq_L": 10, "iqr_mBq_L": 30, "dose_rank": 2, "note": "Despite lower mean activity than U isotopes, dose rank is high because of dose coefficient.", "source": "PineroGarcia2025_Sweden_wells"},
        {"radionuclide": "238U", "n_or_detection": "55 samples", "range_min_mBq_L": 0.2, "range_max_mBq_L": 2300, "mean_mBq_L": 120, "sd_mBq_L": 240, "median_mBq_L": 10, "iqr_mBq_L": 110, "dose_rank": 6, "note": "Seven wells exceeded Swedish chemical uranium threshold of 30 ug/L.", "source": "PineroGarcia2025_Sweden_wells"},
        {"radionuclide": "234U", "n_or_detection": "56 samples", "range_min_mBq_L": "", "range_max_mBq_L": "", "mean_mBq_L": 200, "sd_mBq_L": 410, "median_mBq_L": 20, "iqr_mBq_L": 220, "dose_rank": 5, "note": "Higher mean activity than Ra, but lower mean dose rank.", "source": "PineroGarcia2025_Sweden_wells"},
        {"radionuclide": "Indicative dose", "n_or_detection": "56 wells", "range_min_mBq_L": "", "range_max_mBq_L": "", "mean_mBq_L": "", "sd_mBq_L": "", "median_mBq_L": "", "iqr_mBq_L": "", "dose_rank": "", "note": "ID ranged 3-1474 uSv/y, mean 130 uSv/y, and about 40% exceeded the 100 uSv/y Swedish/Euratom reference.", "source": "PineroGarcia2025_Sweden_wells"},
    ]
    write_csv(DATA / "swedish_well_2025_summary.csv", swedish, list(swedish[0].keys()))

    alignment = [
        {"hypothesis": "U high does not necessarily mean Ra/Pb/Po dose dominance", "mechanistic_basis": "U redox/carbonate speciation differs from Ra alkaline-earth chemistry and Pb/Po surface reactivity.", "data_alignment": "Swedish mean U activity can exceed Ra activity, yet mean dose ranking is Pb-210 > Ra-228 > Po-210 > Ra-226 > U-234 > U-238.", "status": "supported"},
        {"hypothesis": "Ra can be high when U is not high", "mechanistic_basis": "Ra is controlled by ion exchange, recoil, residence time, ionic strength and sulfate/barite sinks rather than U(VI) carbonate mobility.", "data_alignment": "Vengosh et al. review identifies reducing/permeable settings where Ra is mobile; Health Canada treats Ra-226/Ra-228 as primary Canadian drinking-water radionuclides.", "status": "supported mechanistically"},
        {"hypothesis": "Rn is a fracture/residence-time indicator rather than a dissolved-U proxy", "mechanistic_basis": "Rn is a noble gas produced from Ra-bearing solids, transported over a short decay length and lost by degassing.", "data_alignment": "Health Canada manages radon mainly through indoor-air testing; groundwater may contribute through outgassing but cannot be inferred from U alone.", "status": "supported"},
        {"hypothesis": "Po/Pb are better long-term radiological risk indicators than total U alone", "mechanistic_basis": "Pb/Po have high dose coefficients and strong association with particles, Fe/Mn oxides, organic matter and biota/sediments.", "data_alignment": "Swedish well data place Pb-210 first and Po-210 third in mean dose contribution; CNSC Cigar Lake food data show Po-210 as the main series radionuclide with values governed by regional background rather than mine exposure alone.", "status": "supported"},
        {"hypothesis": "Mine surface-water monitoring can look safe while private well groundwater remains variable", "mechanistic_basis": "Surface water is aerated, diluted and short-residence; bedrock wells integrate water-rock contact and fracture sources.", "data_alignment": "Cigar Lake IEMP surface-water radionuclides are below screening levels, whereas Swedish private wells show strong variability and 40% ID exceedance.", "status": "supported but requires site-specific groundwater data"},
    ]
    write_csv(DATA / "hypothesis_alignment_matrix.csv", alignment, list(alignment[0].keys()))

    write_csv(
        DATA / "cnsc_iemp_water_summary.csv",
        water_summary,
        [
            "parameter",
            "sample_type",
            "n",
            "years",
            "stations",
            "unit",
            "left_censored_n",
            "mean_half_dl",
            "max_upper_bound",
            "min_upper_bound",
            "iemp_guideline_or_screening",
            "max_upper_to_iemp_screening_ratio",
            "interpretation",
        ],
    )
    write_csv(
        DATA / "cnsc_iemp_food_series_summary.csv",
        food_summary,
        [
            "sample_description",
            "parameter",
            "n",
            "years",
            "unit",
            "left_censored_n",
            "mean_half_dl",
            "max_upper_bound",
            "iemp_screening",
            "max_upper_to_iemp_screening_ratio",
        ],
    )


def svg_text(x: float, y: float, text: str, size: int = 13, fill: str = "#223", anchor: str = "start", weight: str = "400") -> str:
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-family="Arial, sans-serif" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{html.escape(str(text))}</text>'


def save_svg(path: Path, width: int, height: int, body: str) -> None:
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="100%" height="100%" fill="#ffffff"/>
{body}
</svg>
'''
    write_text(path, content)


def fig_decay_map() -> None:
    nodes = [
        ("238U", "4.468e9 y", "U(VI)/U(IV)\ncarbonate/redox", 60),
        ("234U", "2.455e5 y", "recoil disequilibrium", 190),
        ("230Th", "7.54e4 y", "particle reactive", 320),
        ("226Ra", "1600 y", "Ba/Sr/SO4\nion exchange", 450),
        ("222Rn", "3.82 d", "fracture gas\nresidence time", 580),
        ("210Pb", "22.2 y", "Fe/Mn oxides\nscale/colloid", 710),
        ("210Po", "138.3 d", "organic/sulfide\nbiota hotspot", 840),
    ]
    body = [svg_text(40, 40, "U-238 衰变链地下水迁移控制图", 20, "#102030", weight="700")]
    y = 120
    for i, (nuclide, half, note, x) in enumerate(nodes):
        body.append(f'<rect x="{x}" y="{y}" width="96" height="74" rx="7" fill="#f5f8fb" stroke="#46627f" stroke-width="1.2"/>')
        body.append(svg_text(x + 48, y + 24, nuclide, 18, "#102030", "middle", "700"))
        body.append(svg_text(x + 48, y + 43, half, 11, "#4d5b66", "middle"))
        for j, line in enumerate(note.split("\n")):
            body.append(svg_text(x + 48, y + 59 + j * 13, line, 10, "#394b59", "middle"))
        if i < len(nodes) - 1:
            body.append(f'<line x1="{x+96}" y1="{y+37}" x2="{nodes[i+1][3]}" y2="{y+37}" stroke="#8c3f2b" stroke-width="2" marker-end="url(#arrow)"/>')
    legend = '''<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#8c3f2b"/></marker></defs>'''
    body.append(legend)
    body.append(svg_text(80, 245, "关键推论：同一衰变链中的核素具有不同化学形态；因此活度平衡、迁移性与剂量贡献不会自动随总 U 同步变化。", 14, "#223"))
    body.append(svg_text(80, 278, "模型入口：Bateman 生成项 + 水化学反应项 + 裂隙迁移/滞留项 + 摄入/吸入剂量项。", 14, "#223"))
    save_svg(FIG / "fig01_decay_series_process_map.svg", 1000, 330, "\n".join(body))


def fig_health_reference() -> None:
    rows = list(csv.DictReader((DATA / "health_canada_reference_levels.csv").open(encoding="utf-8")))
    items = [r for r in rows if r["unit"] == "Bq/L" and "Gross" not in r["analyte"]]
    width, height = 900, 430
    margin_l, margin_b, margin_t = 170, 70, 70
    plot_w, plot_h = 640, 270
    vals = [float(r["value"]) for r in items]
    log_min, log_max = -1.0, math.ceil(math.log10(max(vals)))
    body = [svg_text(40, 38, "Health Canada 放射性饮用水参考浓度/MAC（对数轴）", 19, "#102030", weight="700")]
    body.append(f'<line x1="{margin_l}" y1="{margin_t+plot_h}" x2="{margin_l+plot_w}" y2="{margin_t+plot_h}" stroke="#333"/>')
    body.append(f'<line x1="{margin_l}" y1="{margin_t}" x2="{margin_l}" y2="{margin_t+plot_h}" stroke="#333"/>')
    for p in range(int(log_min), int(log_max) + 1):
        x = margin_l + (p - log_min) / (log_max - log_min) * plot_w
        body.append(f'<line x1="{x:.1f}" y1="{margin_t}" x2="{x:.1f}" y2="{margin_t+plot_h}" stroke="#e5e8ec"/>')
        body.append(svg_text(x, margin_t + plot_h + 25, f"10^{p}", 11, "#555", "middle"))
    bar_h = 30
    colors = ["#2f6f73", "#7b4f9f", "#b96f36", "#4b79a8", "#9b3f4e"]
    for i, r in enumerate(items):
        y = margin_t + 26 + i * 48
        v = float(r["value"])
        x2 = margin_l + (math.log10(v) - log_min) / (log_max - log_min) * plot_w
        body.append(svg_text(margin_l - 12, y + 20, r["analyte"], 13, "#223", "end"))
        body.append(f'<rect x="{margin_l}" y="{y}" width="{x2-margin_l:.1f}" height="{bar_h}" fill="{colors[i % len(colors)]}"/>')
        body.append(svg_text(x2 + 8, y + 21, f'{v:g} Bq/L', 12, "#223"))
    body.append(svg_text(40, 395, "注：U 的 20 ug/L 为化学毒性基准，不与 Bq/L 图同轴绘制；Rn-222 参考浓度主要用于解释水向室内空气释氡场景。", 12, "#445"))
    save_svg(FIG / "fig02_health_canada_reference_levels.svg", width, height, "\n".join(body))


def fig_swedish_alignment() -> None:
    rows = list(csv.DictReader((DATA / "swedish_well_2025_summary.csv").open(encoding="utf-8")))
    activity_items = [r for r in rows if r["mean_mBq_L"]]
    dose_items = [r for r in rows if r["dose_rank"]]
    width, height = 950, 520
    body = [svg_text(35, 36, "2025 瑞典井水证据：平均活度与剂量排序并不等价", 19, "#102030", weight="700")]
    x0, y0, plot_w, plot_h = 90, 80, 360, 310
    max_v = max(float(r["mean_mBq_L"]) for r in activity_items)
    body.append(svg_text(x0, y0 - 20, "平均活度（mBq/L）", 14, "#223", weight="700"))
    for i, r in enumerate(activity_items):
        y = y0 + i * 52
        v = float(r["mean_mBq_L"])
        w = v / max_v * plot_w
        body.append(svg_text(x0 - 8, y + 21, r["radionuclide"], 12, "#223", "end"))
        body.append(f'<rect x="{x0}" y="{y}" width="{w:.1f}" height="28" fill="#4b79a8"/>')
        body.append(svg_text(x0 + w + 8, y + 20, f"{v:g}", 12, "#223"))
    x1 = 560
    body.append(svg_text(x1, y0 - 20, "平均剂量贡献排序（1=最高）", 14, "#223", weight="700"))
    for i, r in enumerate(sorted(dose_items, key=lambda z: int(z["dose_rank"]))):
        y = y0 + i * 45
        rank = int(r["dose_rank"])
        body.append(f'<circle cx="{x1+22}" cy="{y+12}" r="15" fill="#b96f36"/>')
        body.append(svg_text(x1 + 22, y + 17, str(rank), 12, "#fff", "middle", "700"))
        body.append(svg_text(x1 + 50, y + 17, r["radionuclide"], 13, "#223"))
    body.append(svg_text(85, 440, "关键对齐：U-234 与 U-238 的平均活度不低，但剂量排序低于 Pb-210、Ra-228、Po-210 与 Ra-226。", 13, "#223"))
    body.append(svg_text(85, 465, "解释：剂量由活度、摄入量与核素剂量系数共同决定；迁移由各元素化学行为控制，而非由总 U 单变量决定。", 13, "#223"))
    save_svg(FIG / "fig03_swedish_activity_vs_dose_rank.svg", width, height, "\n".join(body))


def fig_iemp_water() -> None:
    rows = list(csv.DictReader((DATA / "cnsc_iemp_water_summary.csv").open(encoding="utf-8")))
    items = [r for r in rows if r["max_upper_to_iemp_screening_ratio"] and r["parameter"] in {"Uranium", "Lead-210", "Polonium-210", "Radium-226", "Thorium-230"}]
    width, height = 980, 460
    body = [svg_text(35, 36, "CNSC Cigar Lake IEMP 水样：保守上限 / IEMP 筛选值", 19, "#102030", weight="700")]
    x0, y0, plot_w = 220, 85, 620
    body.append(f'<line x1="{x0}" y1="{y0+290}" x2="{x0+plot_w}" y2="{y0+290}" stroke="#333"/>')
    for tick in [0.001, 0.01, 0.1, 1.0]:
        x = x0 + (math.log10(tick) + 3) / 3 * plot_w
        body.append(f'<line x1="{x:.1f}" y1="{y0}" x2="{x:.1f}" y2="{y0+290}" stroke="#e4e7ea"/>')
        body.append(svg_text(x, y0 + 314, f"{tick:g}", 11, "#555", "middle"))
    body.append(f'<line x1="{x0+plot_w}" y1="{y0}" x2="{x0+plot_w}" y2="{y0+290}" stroke="#9b3f4e" stroke-dasharray="6 5"/>')
    colors = ["#2f6f73", "#7b4f9f", "#b96f36", "#4b79a8", "#9b3f4e"]
    for i, r in enumerate(items):
        y = y0 + 25 + i * 50
        ratio = max(float(r["max_upper_to_iemp_screening_ratio"]), 0.001)
        x2 = x0 + (math.log10(ratio) + 3) / 3 * plot_w
        body.append(svg_text(x0 - 14, y + 20, r["parameter"], 13, "#223", "end"))
        body.append(f'<rect x="{x0}" y="{y}" width="{max(2, x2-x0):.1f}" height="28" fill="{colors[i % len(colors)]}"/>')
        body.append(svg_text(x2 + 8, y + 20, f'{float(r["max_upper_to_iemp_screening_ratio"]):.4g}', 12, "#223"))
    body.append(svg_text(220, 430, "左删失处理：上限比值使用检出限本身；均值另用 0.5*检出限。所有图示水样指标低于 IEMP 筛选值。", 12, "#445"))
    save_svg(FIG / "fig04_cigar_lake_iemp_water_screening.svg", width, height, "\n".join(body))


def fig_conceptual_controls() -> None:
    width, height = 980, 570
    body = [svg_text(35, 36, "U-Ra-Rn-Po-Pb 迁移控制矩阵与评价入口", 19, "#102030", weight="700")]
    columns = [("U", "Eh-pH\n碳酸盐\nCa/Mg络合\nFe/Mn吸附", "#4b79a8"), ("Ra", "Ba/Sr竞争\nSO4/重晶石\n离子强度\n阳离子交换", "#2f6f73"), ("Rn", "Ra源项\n裂隙开度\n停留时间\n逸散", "#b96f36"), ("Pb/Po", "Fe/Mn氧化物\n有机质/硫化物\n胶体/颗粒\n沉积累积", "#7b4f9f")]
    x0, y0, box_w, box_h = 70, 95, 190, 180
    for i, (title, notes, color) in enumerate(columns):
        x = x0 + i * 225
        body.append(f'<rect x="{x}" y="{y0}" width="{box_w}" height="{box_h}" rx="7" fill="#f7f9fb" stroke="{color}" stroke-width="2"/>')
        body.append(svg_text(x + box_w / 2, y0 + 34, title, 22, color, "middle", "700"))
        for j, line in enumerate(notes.split("\n")):
            body.append(svg_text(x + box_w / 2, y0 + 72 + j * 25, line, 13, "#223", "middle"))
        body.append(f'<line x1="{x+box_w/2}" y1="{y0+box_h}" x2="{x+box_w/2}" y2="{y0+box_h+55}" stroke="{color}" stroke-width="2" marker-end="url(#arrow2)"/>')
    body.append('''<defs><marker id="arrow2" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#555"/></marker></defs>''')
    y2 = 350
    bottom = [("反应地球化学", "PHREEQC: 络合、饱和指数、吸附/共沉淀"), ("裂隙迁移", "对流-弥散-滞留 + Bateman 生成/衰变"), ("剂量评价", "饮水摄入、释氡吸入、食物/沉积累积"), ("不确定性", "左删失、季节性、K_d、停留时间、端元混合")]
    for i, (t, n) in enumerate(bottom):
        x = 70 + i * 225
        body.append(f'<rect x="{x}" y="{y2}" width="{box_w}" height="105" rx="7" fill="#fff" stroke="#9aa7b3"/>')
        body.append(svg_text(x + box_w / 2, y2 + 32, t, 15, "#102030", "middle", "700"))
        body.append(svg_text(x + box_w / 2, y2 + 65, n, 11, "#344", "middle"))
    body.append(svg_text(70, 515, "论文观点：安全评价应把衰变链核素作为耦合系统处理；总 U 只能描述一个源项维度，不能替代 Ra/Rn/Pb/Po 的剂量与迁移评价。", 13, "#223"))
    save_svg(FIG / "fig05_coupled_control_matrix.svg", width, height, "\n".join(body))


def build_figures() -> None:
    fig_decay_map()
    fig_health_reference()
    fig_swedish_alignment()
    fig_iemp_water()
    fig_conceptual_controls()


def write_model_templates() -> None:
    state_vector = {
        "aqueous_state": ["pH", "pe_or_Eh", "alkalinity", "DIC", "sulfate", "chloride", "ionic_strength", "Ca", "Mg", "Ba", "Sr", "Fe_total", "Mn_total", "DOC"],
        "hydrogeology": ["porosity", "bulk_density", "fracture_aperture", "hydraulic_gradient", "groundwater_velocity", "residence_time", "dispersivity"],
        "radionuclides": ["U238", "U234", "Ra226", "Ra228", "Rn222", "Pb210", "Po210", "Th230"],
        "solid_sinks": ["ferrihydrite", "birnessite_or_Mn_oxide", "barite", "celestite", "calcite", "organic_matter", "sulfides", "clay_exchange_sites"],
        "dose_pathways": ["drinking_water_ingestion", "radon_outgassing_inhalation", "fish_or_country_food_ingestion", "sediment_resuspension_or_scale_release"],
        "uncertainty_parameters": ["Kd_by_nuclide", "emanation_coefficient", "barite_coprecipitation_rate", "colloid_fraction", "left_censored_substitution_rule", "seasonal_variability"],
    }
    write_text(MODELS / "reactive_transport_state_vector.json", json.dumps(state_vector, ensure_ascii=False, indent=2))

    dose_template = {
        "drinking_water_ingestion": {
            "equation": "D_ing = sum_i C_i * I * e_i",
            "units": {"C_i": "Bq/L", "I": "L/y", "e_i": "Sv/Bq", "D_ing": "Sv/y"},
            "health_canada_reference": {"I_L_per_day": 1.53, "reference_dose_mSv_per_y": 1.0},
            "swedish_well_study": {"I_L_per_y": 730, "ID_unit": "uSv/y"},
        },
        "screening_index": {
            "equation": "SI = sum_i C_i / MAC_i",
            "interpretation": "SI <= 1 satisfies the additive Health Canada MAC criterion for listed radionuclides.",
        },
        "radon_water_to_air": {
            "equation": "C_air_add = T_wa * C_water, followed by indoor-air radon dose model",
            "note": "Health Canada recommends measuring radon in air rather than extrapolating from water alone.",
        },
    }
    write_text(MODELS / "dose_calculation_template.json", json.dumps(dose_template, ensure_ascii=False, indent=2))

    phr = """TITLE U-Ra-Rn-Po-Pb decay-series groundwater conceptual PHREEQC template
# This is a conceptual input deck. It requires site-specific groundwater chemistry,
# thermodynamic database choices, and validated sorption/solid-solution parameters
# before quantitative use.

SOLUTION 1 Oxic carbonate uranium-bearing groundwater
    temp      10
    pH        7.5
    pe        6
    units     mg/L
    Ca        30
    Mg        10
    Na        20
    K         2
    S(6)      20 as SO4
    C(4)      150 as HCO3
    U         0.02
    Ba        0.05
    Sr        0.2

EQUILIBRIUM_PHASES 1
    Barite    0 0
    Celestite 0 0
    Calcite   0 0
    Ferrihydrite 0 0

# Representative reactions to be parameterized:
# UO2+2 + 3CO3-2 = UO2(CO3)3-4
# Ca+2 + UO2(CO3)3-4 = CaUO2(CO3)3-2
# Ra+2 + SO4-2 = RaSO4(aq or solid-solution proxy)
# X-Na + Ra+2 exchange requires EXCHANGE block and selectivity constants.
# Pb/Po sorption requires SURFACE blocks for Fe/Mn oxides and organic matter.

SELECTED_OUTPUT
    -file selected_u_ra_pb_po.out
    -pH true
    -pe true
    -totals U Ba Sr S(6) C(4)
    -si Barite Celestite Calcite
END
"""
    write_text(MODELS / "uranium_series_phreeqc_template.phr", phr)


def table_md(rows: list[dict], columns: list[str], limit: int | None = None) -> str:
    rows = rows[:limit] if limit else rows
    header = "| " + " | ".join(columns) + " |"
    sep = "| " + " | ".join(["---"] * len(columns)) + " |"
    lines = [header, sep]
    for row in rows:
        vals = [str(row.get(c, "")) for c in columns]
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)


def write_paper(metadata: dict) -> None:
    health_rows = list(csv.DictReader((DATA / "health_canada_reference_levels.csv").open(encoding="utf-8")))
    water_rows = list(csv.DictReader((DATA / "cnsc_iemp_water_summary.csv").open(encoding="utf-8")))
    swedish_rows = list(csv.DictReader((DATA / "swedish_well_2025_summary.csv").open(encoding="utf-8")))
    food_rows = list(csv.DictReader((DATA / "cnsc_iemp_food_series_summary.csv").open(encoding="utf-8")))
    align_rows = list(csv.DictReader((DATA / "hypothesis_alignment_matrix.csv").open(encoding="utf-8")))

    water_key = [r for r in water_rows if r["parameter"] in {"Uranium", "Lead-210", "Polonium-210", "Radium-226", "Thorium-230", "pH", "Total hardness"}]
    food_po = [r for r in food_rows if r["parameter"] == "Polonium-210"]

    md = r"""---
title: "铀矿区地下水中 U-Ra-Rn-Po-Pb 系列核素的分布、迁移与剂量贡献"
subtitle: "从衰变链生成、水化学迁移到饮用水和矿区环境风险的耦合分析"
author: "GeoMine Research / OpenMiner"
date: "2026-05-23"
lang: zh-CN
---

# 摘要

铀矿区和富铀地质背景区的地下水风险不能由总铀浓度单独刻画。铀、镭、氡、铅、钋虽属于 U/Th 衰变系列，但它们在地下水中的化学形态、源项生成机制、滞留过程、迁移距离和人体剂量系数显著不同。本文围绕“U 高不必然 Ra/Rn/Po/Pb 高，Ra/Rn/Po/Pb 异常也不必然对应高 U”的核心命题，建立一个可验证的地球化学-放射性剂量框架。研究综合了三类公开证据：第一，2025 年瑞典私井研究的开放论文数据摘要，覆盖 56 口井的 $^{{210}}$Po、$^{{210}}$Pb、$^{{226}}$Ra、$^{{228}}$Ra、$^{{238}}$U 和 $^{{234}}$U；第二，Health Canada 2025 饮用水放射性参数指南和 2019 铀饮用水指南；第三，CNSC Independent Environmental Monitoring Program (IEMP) Cigar Lake Operation 2020/2024 公开 CSV 数据。结果显示，瑞典井水中平均剂量贡献排序为 $^{{210}}$Pb > $^{{228}}$Ra > $^{{210}}$Po > $^{{226}}$Ra > $^{{234}}$U > $^{{238}}$U，尽管 U 同位素平均活度并不最低；约 40% 的井水指示剂量超过 100 $\\mu$Sv/y。相反，Cigar Lake IEMP 地表水样在保守左删失上限处理下，U、Pb-210、Po-210、Ra-226、Th-230 均低于 IEMP 筛选值。这种对比说明：铀矿环境表层水监测“低于筛选值”与私井/裂隙地下水“强变异性”并不矛盾，二者反映不同水文地球化学域。

本文的最终观点是：铀矿区地下水安全评价应从“总 U 单指标”升级为“衰变链核素系统评价”。实际评价中至少应同步纳入 U 同位素、Ra-226/Ra-228、Rn-222、Pb-210、Po-210 以及 pH-Eh、碱度、硫酸盐、Ba/Sr、离子强度、Fe/Mn 氧化物、有机质、裂隙结构和地下水停留时间。Po/Pb 更适合作为长期放射性剂量和沉积/生物累积风险指标，Ra 更适合识别碱土金属-硫酸盐-离子交换控制，Rn 更适合识别裂隙连通性和短停留时间气体迁移。

**关键词**：铀矿区地下水；镭；氡；铅-210；钋-210；U decay series；剂量评价；PHREEQC；反应迁移

# 1. 研究问题与判据

本文研究对象是铀矿区、富铀结晶岩/砂岩含水层、私井和矿区周边环境水体中的 U-Ra-Rn-Po-Pb 衰变系列核素。论文不把任一公开监测结果直接外推为某个矿区的健康结论，而是建立可复核的解释框架，回答三个问题：

1. **分布问题**：$^{{238}}$U、$^{{234}}$U、$^{{226}}$Ra、$^{{228}}$Ra、$^{{222}}$Rn、$^{{210}}$Pb、$^{{210}}$Po 在地下水和矿区环境水中是否同步变化？
2. **迁移问题**：Eh-pH、碳酸盐络合、硫酸盐、Ba/Sr 共沉淀、离子强度、Fe/Mn 氧化物吸附、裂隙发育和停留时间如何分别控制这些核素？
3. **剂量问题**：饮水摄入、释氡吸入、矿区排水/尾矿渗滤液和长期沉积累积中，哪类核素更可能支配剂量或风险解释？

判据上，本文采用“双基准”而非单一阈值：加拿大饮用水侧使用 Health Canada 的放射性参数 MAC/参考浓度和铀化学毒性 MAC；矿区环境侧使用 CNSC IEMP 数据自带筛选值，并保留其 0.1 mSv/y 筛选逻辑。两个基准的剂量水平和适用场景不同，因此只做结构化对比，不将 IEMP 筛选值替代饮用水 MAC。

![衰变链过程图](figures/fig01_decay_series_process_map.svg)

# 2. 数据源、采集与可复现性

## 2.1 公开数据源

本文使用的公开源如下。

- Vengosh et al. (2022) 对 U/Th 衰变链核素地下水赋存进行了综述，明确指出 U、Ra、Rn、Pb、Po 的地下水浓度由“生成/反冲/溶出”与“吸附/沉淀/离子交换/滞留”的净平衡控制，而非由铀含量单变量决定。来源：<https://www.sciencedirect.com/science/article/pii/S0048969721069904>。
- Piñero-García et al. (2025) 瑞典井水开放论文研究了 56 口井的 $^{{210}}$Po、$^{{210}}$Pb、$^{{226}}$Ra、$^{{228}}$Ra、$^{{238}}$U、$^{{234}}$U，并给出指示剂量公式和剂量排序。来源：<https://www.sciencedirect.com/science/article/pii/S0147651324015562> 与 PubMed <https://pubmed.ncbi.nlm.nih.gov/39644567/>。
- Health Canada (2025) 放射性饮用水指南给出 Pb-210、Ra-226、Ra-228 的 MAC、Po-210/Rn-222 参考浓度、gross alpha/beta 筛选值，并说明 MAC 由 1 mSv/y 参考剂量和 1.53 L/day 饮水量推导。来源：<https://www.canada.ca/en/health-canada/services/publications/healthy-living/guidelines-drinking-water-quality-radiological-parameters.html>。
- Health Canada (2019) 铀饮用水指南给出总天然铀 0.02 mg/L (20 ug/L) MAC，且该值主要基于化学毒性。来源：<https://www.canada.ca/en/health-canada/services/publications/healthy-living/guidelines-canadian-drinking-water-quality-guideline-technical-document-uranium.html>。
- CNSC IEMP Cigar Lake Operation 页面和 CSV 给出 2020/2024 年水样、鱼、蓝莓和 Labrador tea 中的 U、Pb-210、Po-210、Ra-226、Th-230 等监测结果。来源：<https://www.cnsc-ccsn.gc.ca/eng/resources/maps-of-nuclear-facilities/iemp/cigar-lake/>。

原始 CSV、网页快照、整理后的中间表、图件和模型模板均保存在本报告目录。CNSC 原始 CSV 共 __RAW_ROWS__ 行；本文水样汇总使用 __WATER_ROWS_USED__ 个参数-样品记录，食物/生物介质汇总使用 __FOOD_ROWS_USED__ 个记录。

## 2.2 左删失数据处理

公开监测数据中大量结果以“<检出限”给出。本文采用两个并行量：

\\[
\\bar C_{{1/2DL}}=\\frac1n\\sum_j
\\begin{{cases}}
C_j, & C_j \\text{{ 为检出值}}\\\\
\\frac12DL_j, & C_j<DL_j
\\end{{cases}}
\\]

用于描述性均值；筛选比值使用保守上限：

\\[
R_{{max}}=\\max_j\\left(\\frac{{
\\begin{{cases}}
C_j, & C_j \\text{{ 为检出值}}\\\\
DL_j, & C_j<DL_j
\\end{{cases}}}}{{C_{{screen}}}}\\right).
\\]

这种处理不会把未检出值解释为零，也不会把保守上限误用为真实均值。

# 3. 理论框架与公式推导

## 3.1 放射性衰变链与非平衡

单核素衰变满足：

\\[
\\frac{{dN_i}}{{dt}}=-\\lambda_i N_i,\\qquad
\\lambda_i=\\frac{{\\ln 2}}{{T_{{1/2,i}}}},\\qquad
A_i=\\lambda_iN_i .
\\]

连续衰变链 $1\\rightarrow2\\rightarrow\\cdots\\rightarrow k$ 在初始仅有母体 $N_1(0)$ 的理想封闭条件下，Bateman 解为：

\\[
N_k(t)=N_1(0)\\left(\\prod_{{j=1}}^{{k-1}}\\lambda_j\\right)
\\sum_{{j=1}}^k
\\frac{{e^{{-\\lambda_jt}}}}{{\\prod_{{m=1,m\\ne j}}^k(\\lambda_m-\\lambda_j)}} .
\\]

若母体半衰期远大于子体，且体系封闭，则经历若干子体半衰期后可趋于长期平衡：

\\[
A_1\\approx A_2\\approx\\cdots\\approx A_k .
\\]

但地下水不是封闭体系。水-岩反应、吸附、沉淀、反冲、对流、弥散、脱气和抽水会打破活度平衡。对第 $i$ 个核素，含迁移和滞留的反应迁移式可写为：

\\[
R_i\\frac{{\\partial C_i}}{{\\partial t}}
=\\nabla\\cdot(D_i\\nabla C_i)-\\nabla\\cdot(\\mathbf v C_i)
+\\lambda_{{i-1}}R_{{i-1}}C_{{i-1}}
-\\lambda_iR_iC_i
+S_i-k_iC_i .
\\]

其中 $C_i$ 为水相活度浓度，$R_i$ 为迟滞因子，$D_i$ 为水动力弥散张量，$\\mathbf v$ 为孔隙水速度，$S_i$ 包含矿物溶出、反冲和外部输入，$k_i$ 代表沉淀、不可逆吸附或脱气等一阶损失。线性吸附近似下：

\\[
R_i=1+\\frac{{\\rho_bK_{{d,i}}}}{{\\theta}},
\\]

其中 $\\rho_b$ 为介质干密度，$\\theta$ 为有效孔隙度，$K_d$ 为分配系数。不同核素 $K_d$ 差异很大，意味着同一衰变链中的子体不会按同一速度迁移。

## 3.2 铀：Eh-pH 与碳酸盐络合控制

铀在天然水中主要以 U(IV) 和 U(VI) 两类价态控制迁移。氧化、中性至弱碱性、富碳酸盐水中，U(VI) 以 uranyl 碳酸盐络合物存在：

\\[
\\mathrm{{UO_2^{{2+}}+2CO_3^{{2-}}\\rightleftharpoons UO_2(CO_3)_2^{{2-}}}},
\\]

\\[
\\mathrm{{UO_2^{{2+}}+3CO_3^{{2-}}\\rightleftharpoons UO_2(CO_3)_3^{{4-}}}},
\\]

并可形成 Ca-U-carbonate 络合物：

\\[
\\mathrm{{Ca^{{2+}}+UO_2(CO_3)_3^{{4-}}\\rightleftharpoons CaUO_2(CO_3)_3^{{2-}}}},
\\]

\\[
\\mathrm{{2Ca^{{2+}}+UO_2(CO_3)_3^{{4-}}\\rightleftharpoons Ca_2UO_2(CO_3)_3(aq)}} .
\\]

这些络合物提高溶解度并降低部分矿物表面吸附。还原条件下：

\\[
\\mathrm{{UO_2^{{2+}}+2e^-+4H^+\\rightleftharpoons UO_2(s)+2H_2O}},
\\]

U(VI) 可转化为低溶解度 U(IV) 固相。Nernst 形式说明 Eh、pH 与溶解铀之间的耦合：

\\[
E_h=E^0-\\frac{{RT}}{{2F}}\\ln
\\left(\\frac{{a_{{\\mathrm{{UO_2(s)}}}}a_{{H_2O}}^2}}{{a_{{\\mathrm{{UO_2^{{2+}}}}}}a_{{H^+}}^4}}\\right).
\\]

因此，U 高常对应氧化-碳酸盐环境或局部酸性淋滤，但这并不必然提高 Ra、Rn、Po、Pb。

## 3.3 镭：Ba/Sr、硫酸盐、离子强度与交换位点

Ra-226 是 U-238 系列子体，Ra-228 来自 Th-232 系列。两者水化学行为近似碱土金属二价阳离子，而非铀的 uranyl 碳酸盐体系。镭的核心反应包括阳离子交换：

\\[
\\mathrm{{2X{-}Na+Ra^{{2+}}\\rightleftharpoons X_2Ra+2Na^+}},
\\]

以及与硫酸盐矿物的共沉淀/固溶：

\\[
\\mathrm{{Ba^{{2+}}+SO_4^{{2-}}\\rightleftharpoons BaSO_4(s)}},
\\]

\\[
\\mathrm{{Ra^{{2+}}+SO_4^{{2-}}\\rightleftharpoons RaSO_4(s)}} .
\\]

若以重晶石-镭固溶体表示：

\\[
D_{{Ra/Ba}}=
\\frac{{x_{{RaSO_4}}/x_{{BaSO_4}}}}{{a_{{Ra^{{2+}}}}/a_{{Ba^{{2+}}}}}},
\\]

则水中 Ba、SO4、Sr、Ca 和离子强度会通过活度系数、竞争交换和固溶分配共同控制溶解 Ra。高硫酸盐并不总是提高 Ra；当 Ba 充足且重晶石过饱和时，Ra 可被有效带入固相。相反，在低硫酸盐、高离子强度或交换位点被 Na/Ca 竞争占据的水中，Ra 可更易释放。

## 3.4 氡：短半衰期气体、裂隙与停留时间

Rn-222 来自 Ra-226 衰变，是惰性气体。含水裂隙中的氡可用一维近似表示：

\\[
\\frac{{\\partial C_{{Rn}}}}{{\\partial t}}
=\\frac{{E\\rho_s A_{{Ra}}\\lambda_{{Ra}}}}{{\\theta}}
-\\lambda_{{Rn}}C_{{Rn}}
-k_{{deg}}C_{{Rn}}
-v\\frac{{\\partial C_{{Rn}}}}{{\\partial x}}
D\\frac{{\\partial^2C_{{Rn}}}}{{\\partial x^2}},
\\]

其中 $E$ 是 emanation coefficient，$A_{{Ra}}$ 是固相 Ra 活度，$k_{{deg}}$ 是脱气损失。一维稳态、忽略弥散时：

\\[
C(x)=C_{{eq}}+(C_0-C_{{eq}})\\exp\\left[-\\frac{{(\\lambda_{{Rn}}+k_{{deg}})x}}{{v}}\\right],
\\qquad
C_{{eq}}=\\frac{{E\\rho_sA_{{Ra}}\\lambda_{{Ra}}}}{{\\theta(\\lambda_{{Rn}}+k_{{deg}})}} .
\\]

因此 Rn 更反映固相 Ra 分布、裂隙面面积、流速、停留时间和逸散条件。它可以高于 U 预期，也可以在高 U 水中因强脱气或短路径而低。

## 3.5 Pb/Po：表面反应、胶体和长期累积

Pb-210 和 Po-210 不应只被视为“铀的后代”。Pb(II) 易与 Fe/Mn 氧化物、碳酸盐、腐蚀垢和有机质结合：

\\[
\\equiv SOH+\\mathrm{{Pb^{{2+}}}}
\\rightleftharpoons
\\equiv SOPb^+ + \\mathrm{{H^+}} .
\\]

Po 的价态和络合更复杂，但在许多环境中表现为强颗粒/有机质/硫化物亲和。用分配系数表示：

\\[
K_d=\\frac{{C_s}}{{C_w}},\\qquad
f_{{diss}}=\\frac1{{1+\\rho_bK_d/\\theta}} .
\\]

这意味着 Pb/Po 在水样、悬浮颗粒、沉积物、管网垢层和生物组织之间的再分配可能支配长期剂量。若只测溶解 U，容易漏掉 Pb/Po 的沉积-再释放风险。

## 3.6 剂量公式与筛选指数

饮水摄入剂量的一般式为：

\\[
D_{{ing}}=\\sum_i C_i I e_i ,
\\]

其中 $C_i$ 为活度浓度 (Bq/L)，$I$ 为年饮水量 (L/y)，$e_i$ 为摄入剂量系数 (Sv/Bq)。瑞典井水论文采用：

\\[
ID(\\mu Sv)=\\sum_i a_i V e_i,\qquad V=730\\;L/y .
\\]

Health Canada 的 MAC 可写成反推形式：

\\[
MAC_i=\\frac{{D_{{ref}}}}{{I e_i}},
\\qquad
D_{{ref}}=1\\;mSv/y,\quad I=1.53\\;L/day .
\\]

当多个核素共同存在时，Health Canada 使用加和判据：

\\[
\\sum_i\\frac{{C_i}}{{MAC_i}}\\le 1 .
\\]

这个式子是风险筛选指数，不是每个场址的最终剂量模型。年龄组、饮水量、食物摄入、处理前后水样、季节性和左删失数据都会改变实际剂量估计。

# 4. 数据分析结果

## 4.1 加拿大饮用水基准

Health Canada 的放射性饮用水基准显示，Pb-210、Ra-226、Ra-228 是加拿大饮用水中最重要的天然放射性核素；Po-210 和 Rn-222 作为特殊场景参考浓度列出；铀则主要按化学毒性给出 20 ug/L MAC。

__HEALTH_TABLE__

![Health Canada 参考浓度](figures/fig02_health_canada_reference_levels.svg)

这一基准本身已经支持一个重要判断：铀不是饮水放射性剂量的唯一核心。Health Canada 明确将 U 作为弱放射性、以化学毒性为主的参数处理，而 Pb-210、Ra-226、Ra-228 构成放射性 MAC 主体。对矿区地下水而言，这意味着“总 U 达标”不能推出“放射性剂量达标”，尤其在 Ra/Pb/Po 未测时。

## 4.2 2025 年瑞典井水研究：活度高低与剂量排序分离

瑞典研究的 56 口井展示了典型的私井/裂隙地下水强变异性。开放页面给出的关键统计如下。

__SWEDISH_TABLE__

![瑞典井水平均活度与剂量排序](figures/fig03_swedish_activity_vs_dose_rank.svg)

这组结果对本文命题非常关键。U-234 的平均活度约 200 mBq/L，U-238 约 120 mBq/L，高于 Ra-226 和 Ra-228 的平均活度量级；然而平均剂量贡献排序中 U-234 和 U-238 位居第五、第六。相反，Pb-210 虽然开放页面没有给出可机读平均活度表，却在平均剂量贡献中居首；Ra-228 平均活度约 30 mBq/L，却居第二；Po-210 在高值井中可贡献 50%-90% 指示剂量。由此可见：

\\[
\\text{{剂量重要性}}\\ne\\text{{活度浓度排序}}\\ne\\text{{总 U 浓度排序}} .
\\]

这种分离来自两个因素。第一，核素摄入剂量系数不同；第二，子体核素在地下水中处于非平衡状态。U 的碳酸盐迁移、Ra 的碱土金属交换/共沉淀、Pb/Po 的颗粒表面反应相互独立，导致同一口井中各核素可能不相关甚至反相关。

## 4.3 Cigar Lake IEMP 公开数据：矿区地表水低于筛选值

CNSC IEMP Cigar Lake CSV 是真实公开监测数据。本文仅将其作为“铀矿环境地表水/食物监测”证据，不把它等同于深部地下水。水样关键汇总如下。

__IEMP_WATER_TABLE__

![Cigar Lake IEMP 水样筛选比值](figures/fig04_cigar_lake_iemp_water_screening.svg)

保守上限分析表明，水样 U、Pb-210、Po-210、Ra-226、Th-230 均低于 IEMP 筛选值。页面正文亦说明 2024 年水样放射性和非放射性污染物处于自然背景水平并低于适用指南。这一结果与瑞典井水的高变异性并不冲突：IEMP 数据是湖泊表层水和生态介质监测，受稀释、曝气、短停留时间和区域背景控制；私井/裂隙地下水则长期接触富 U/Th 岩石，可积累衰变链核素并形成局部非平衡。

## 4.4 Po/Pb 的生态介质信号

CNSC 食物/生物介质数据中，Po-210 是最需要解释的核素之一。CSV 汇总中 Po-210 的样品类型结果如下。

__IEMP_FOOD_PO_TABLE__

IEMP 页面指出，2024 年 Cigar Lake 区域鱼类 Po-210 最高值为 3.5 Bq/kg fresh weight，位于区域自然背景范围 0.02-14 Bq/kg fresh weight 内，且参考站与潜在影响站结果相似，因而不能解释为矿山单独造成。这个结果对地下水课题仍有意义：Po/Pb 是长期沉积、生物摄入和颗粒相迁移中更敏感的子体核素；它们可能在水相低值时仍通过食物网或沉积物成为剂量评价关键项。

# 5. 机制解释：为何 U、Ra、Rn、Po/Pb 不同步

![迁移控制矩阵](figures/fig05_coupled_control_matrix.svg)

## 5.1 U 高不必然 Ra 高

U(VI) 在氧化、碳酸盐水中以阴离子或中性络合物迁移，主要受 Eh-pH、DIC、Ca/Mg 和 Fe/Mn 氧化物吸附控制。Ra 是二价阳离子，不参与 uranyl 碳酸盐体系，主要受 Ba/Sr/Ca 竞争、硫酸盐矿物饱和度、阳离子交换容量和离子强度控制。因此，同一含水层内可能出现：

- 氧化碳酸盐水中 U 高、Ra 低：U 形成可迁移络合物，而 Ra 被重晶石/交换位点截留。
- 还原或高离子强度水中 U 低、Ra 高：U(IV) 沉淀或吸附，而 Ra 从交换位点释放，且缺乏硫酸盐/重晶石沉淀。
- 富 Th 岩性中 Ra-228 高但 U 不高：Ra-228 母体来自 Th-232 系列，与 U-238 源项不同。

这解释了为什么以总 U 作为唯一指标会误判 Ra 剂量。

## 5.2 Ra 高不必然 Rn 高，Rn 高也不必然 U 高

Rn-222 的半衰期只有 3.82 天，迁移距离受流速和裂隙连通性约束。若地下水在富 Ra 裂隙面附近快速进入井筒且脱气少，Rn 可很高；若路径长、曝气强或停留时间相对半衰期过长，Rn 会衰变或逸散。Rn 还可由固相 Ra 的反冲进入水相，而不需要高溶解 U。因此，Rn 更适合作为裂隙系统、岩性和短时标水-岩接触的示踪，而不是 U 浓度代理。

Health Canada 也强调，水中 Rn 对室内空气的贡献需要通过空气检测来管理，不能简单由水浓度外推。这一监管逻辑与上述迁移方程一致。

## 5.3 Po/Pb 适合长期风险和累积风险评价

Pb-210 半衰期 22.2 年，Po-210 半衰期 138.3 天，二者在矿区水-沉积物-生物体系中具有较强表面反应和生物地球化学循环特征。它们可以通过以下路径影响长期评价：

- 管网或井壁 Fe/Mn 氧化物、腐蚀垢和沉积物吸附 Pb/Po，水力扰动后再释放。
- 有机质和硫化物富集 Po，形成与溶解 U 不同步的热点。
- Rn 衰变子体沉积可生成 unsupported Pb-210/Po-210，使 Po/Pb 活度与溶解 U 脱耦。
- 食物网中 Po-210 可能成为剂量敏感项，Cigar Lake IEMP 鱼类结果即显示 Po-210 是需要单独解释的生态介质指标。

因此，长期风险评价中只测 U 不足以覆盖 Pb/Po 的沉积和累积路径。

# 6. 与预设命题的对齐

__ALIGNMENT_TABLE__

综合来看，公开数据和理论模型对齐良好：瑞典井水数据提供“井水强变异性与剂量排序脱钩”的直接证据；Health Canada 基准提供“Pb/Ra 是饮用水放射性评价核心，U 主要是化学毒性”的监管证据；CNSC IEMP 提供“矿区地表环境监测可低于筛选值，但 Po/Pb/Ra 仍需在生态介质和地下水中单独评价”的场景证据；Vengosh 等综述和铀形态综述提供机制支撑。

# 7. 面向 PHREEQC/COMSOL/PINN 的模型框架

## 7.1 反应网络

建议把状态变量分为四组：

\\[
\\mathbf y=
[\\mathrm{{pH}}, Eh, I, Alk, SO_4, Cl, Ba, Sr, Ca, Fe, Mn, DOC,
U_{{238}},U_{{234}},Ra_{{226}},Ra_{{228}},Rn_{{222}},Pb_{{210}},Po_{{210}}].
\\]

反应网络包含：

1. U(VI)-carbonate-Ca/Mg 络合和 U(IV) 还原沉淀。
2. Ra 与 Ba/Sr/Ca 的阳离子交换、barite/celestite 固溶和硫酸盐控制。
3. Rn 由固相 Ra 反冲/emanation 进入水相，并发生衰变和脱气。
4. Pb/Po 在 Fe/Mn 氧化物、有机质、硫化物、胶体和沉积物上的吸附/解吸。
5. 各核素按 Bateman 生成项耦合，但迁移项和滞留项分别参数化。

本报告已提供 `models/uranium_series_phreeqc_template.phr`、`models/reactive_transport_state_vector.json` 和 `models/dose_calculation_template.json`，作为后续建模起点。

## 7.2 计算流程

推荐工作流如下：

1. 以水样 pH、Eh/pe、碱度、SO4、Cl、Ba、Sr、Ca、Fe、Mn、DOC 和 U/Ra/Pb/Po 活度作为输入。
2. PHREEQC 计算 U 络合物比例、barite/celestite/calcite 饱和指数和主要离子活度。
3. 将 PHREEQC 输出的饱和指数、络合比例和吸附容量转入反应迁移模型。
4. 对 Rn 单独计算 emanation、裂隙对流和脱气；不把 Rn 简化为溶解 U 的函数。
5. 剂量模块分别计算饮水摄入、释氡吸入和食物/沉积累积贡献。
6. 对 $K_d$、停留时间、Ba/Sr、SO4、DOC、Fe/Mn 氧化物和左删失处理进行敏感性分析。

# 8. 局限性

本文是综述性和二次数据分析研究，不替代场址调查或饮用水合规判断。主要局限包括：

- 瑞典 2025 论文的原始样品表开放页面未提供机器可下载数据，本文使用开放页面给出的统计摘要和剂量排序，未重构单井原始数据。
- CNSC IEMP Cigar Lake 数据为矿区周边地表水和生态介质监测，不是深部地下水或私井数据；本文将其用于矿区环境对比，而非地下水源项拟合。
- Health Canada MAC 和 IEMP 筛选值剂量基准不同，前者为饮用水 1 mSv/y 参考，后者常按 0.1 mSv/y 环境筛选设置；本文仅比较结构和数量级，不混同监管含义。
- Rn 的主要健康路径是室内空气吸入，水样 Rn 只能作为潜在贡献源和裂隙示踪，不能替代室内空气检测。
- Pb/Po 的吸附和胶体模型需要场址特定 Fe/Mn 氧化物、有机质、颗粒粒径和沉积物数据；现阶段只能建立反应路径图。

# 9. 结论与论文最终观点

本文的核心结论如下。

第一，铀矿区地下水放射性风险不能用总 U 浓度单独判断。U、Ra、Rn、Pb、Po 属于衰变链系统，但地下水不是封闭衰变容器；水-岩反应、裂隙流、离子交换、共沉淀、吸附、脱气和生物地球化学过程会造成长期非平衡。

第二，Ra 是与 U 显著脱耦的剂量关键核素。Ra-226/Ra-228 受 Ba/Sr、SO4、离子强度和交换位点控制，且 Ra-228 还反映 Th 系列源项。高 U 不保证高 Ra，低 U 也不能排除 Ra 风险。

第三，Rn 是裂隙-停留时间-emanation 指标，不是 U 浓度代理。水中 Rn 受固相 Ra、裂隙面、流速和脱气控制，并且健康管理上应与室内空气检测耦合。

第四，Pb-210 和 Po-210 对长期剂量、沉积累积和生态介质评价尤其重要。2025 年瑞典井水研究显示 Pb-210、Ra-228、Po-210、Ra-226 的平均剂量贡献均高于 U 同位素；CNSC IEMP 数据也说明 Po-210 需要在鱼类等生物介质中单独解释，即便水样低于筛选值。

第五，一个严谨的铀矿区地下水评价框架应至少同时包含：U 同位素活度/质量浓度、Ra-226/Ra-228、Rn-222、Pb-210、Po-210；水化学端元和 Eh-pH；SO4、Ba、Sr、Ca、碱度、离子强度；Fe/Mn 氧化物、有机质和胶体；裂隙结构与地下水停留时间；饮水、吸入和食物/沉积三类剂量路径。论文的最终观点是：应把铀矿区地下水视为一个“衰变链生成-反应迁移-地球化学截留-人体剂量”的耦合系统，而不是把总铀作为唯一风险代理变量。

# 数据与文件清单

- `data/cnsc_iemp_cigar_lake_2020_2024.csv`：CNSC IEMP 原始 CSV。
- `data/cnsc_iemp_water_summary.csv`：IEMP 水样标准化统计与筛选比值。
- `data/cnsc_iemp_food_series_summary.csv`：IEMP 食物/生物介质 U-Ra-Pb-Po 系列统计。
- `data/swedish_well_2025_summary.csv`：瑞典井水论文开放页面统计摘要。
- `data/health_canada_reference_levels.csv`：加拿大饮用水放射性与铀基准。
- `data/dose_model_parameters.csv`：由 Health Canada MAC 反推的筛选等效剂量系数。
- `data/hypothesis_alignment_matrix.csv`：理论命题、机制和数据证据对齐表。
- `figures/*.svg`：论文图件。
- `models/*.json`、`models/*.phr`：后续 PHREEQC/反应迁移/剂量模型模板。
- `sources/*.html`：网页源快照。

# 参考文献

1. Vengosh, A., Coyte, R. M., Podgorski, J., & Johnson, T. M. (2022). *A critical review on the occurrence and distribution of the uranium- and thorium-decay nuclides and their effect on the quality of groundwater*. Science of The Total Environment, 808, 151914. <https://www.sciencedirect.com/science/article/pii/S0048969721069904>
2. Piñero-García, F., Thomas, R., Forssell-Aronsson, E., & Isaksson, M. (2025). *Comprehensive analysis of naturally occurring radionuclides in well water: Isotopic ratios, mitigation, and dose assessment*. Ecotoxicology and Environmental Safety, 289, 117480. <https://www.sciencedirect.com/science/article/pii/S0147651324015562>
3. Health Canada. (2025). *Guidelines for Canadian drinking water quality: Radiological parameters*. <https://www.canada.ca/en/health-canada/services/publications/healthy-living/guidelines-drinking-water-quality-radiological-parameters.html>
4. Health Canada. (2019). *Guidelines for Canadian Drinking Water Quality Guideline Technical Document - Uranium*. <https://www.canada.ca/en/health-canada/services/publications/healthy-living/guidelines-canadian-drinking-water-quality-guideline-technical-document-uranium.html>
5. Canadian Nuclear Safety Commission. (2025). *Independent Environmental Monitoring Program: Cigar Lake Operation*. <https://www.cnsc-ccsn.gc.ca/eng/resources/maps-of-nuclear-facilities/iemp/cigar-lake/>
6. Martell, E. A. M., et al. / Frontiers in Chemistry review source used for uranium speciation context: *Speciation of Uranium and Plutonium From Nuclear Legacy Sites to the Environment: A Mini Review*. <https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2020.00630/full>
"""
    md = (
        md.replace("__RAW_ROWS__", str(metadata["raw_rows"]))
        .replace("__WATER_ROWS_USED__", str(metadata["water_rows_used"]))
        .replace("__FOOD_ROWS_USED__", str(metadata["food_rows_used"]))
        .replace("__HEALTH_TABLE__", table_md(health_rows, ["analyte", "value", "unit", "basis"], None))
        .replace("__SWEDISH_TABLE__", table_md(swedish_rows, ["radionuclide", "n_or_detection", "range_min_mBq_L", "range_max_mBq_L", "mean_mBq_L", "median_mBq_L", "dose_rank", "note"], None))
        .replace("__IEMP_WATER_TABLE__", table_md(water_key, ["parameter", "n", "years", "unit", "left_censored_n", "mean_half_dl", "max_upper_bound", "iemp_guideline_or_screening", "max_upper_to_iemp_screening_ratio"], None))
        .replace("__IEMP_FOOD_PO_TABLE__", table_md(food_po, ["sample_description", "n", "years", "unit", "mean_half_dl", "max_upper_bound", "iemp_screening", "max_upper_to_iemp_screening_ratio"], None))
        .replace("__ALIGNMENT_TABLE__", table_md(align_rows, ["hypothesis", "mechanistic_basis", "data_alignment", "status"], None))
    )
    md = md.replace("\\\\", "\\")
    md = md.replace("{{", "{").replace("}}", "}")
    write_text(REPORT / "Paper.zh.md", md)

    css = """
body {
  font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, "Noto Sans CJK SC", sans-serif;
  line-height: 1.62;
  color: #18222d;
  max-width: 980px;
  margin: 0 auto;
  padding: 36px 44px 64px;
}
h1, h2, h3 { color: #102030; line-height: 1.25; }
h1 { border-bottom: 1px solid #d8dee6; padding-bottom: 8px; margin-top: 34px; }
table { border-collapse: collapse; width: 100%; font-size: 9.5px; margin: 16px 0 24px; table-layout: fixed; }
th, td { border: 1px solid #d8dee6; padding: 5px 6px; vertical-align: top; overflow-wrap: anywhere; word-break: break-word; }
th { background: #f4f7fa; }
img { max-width: 100%; margin: 14px 0 22px; }
code { background: #f3f5f7; padding: 1px 4px; }
@page { size: A4; margin: 16mm 14mm; }
"""
    write_text(REPORT / "Paper.print.css", css.strip() + "\n")


def write_readme(metadata: dict) -> None:
    content = f"""# U-Ra-Rn-Po-Pb groundwater radionuclide report package

Generated: 2026-05-23

This folder contains the reproducible research package for the Chinese paper:

`铀矿区地下水中 U-Ra-Rn-Po-Pb 系列核素的分布、迁移与剂量贡献`

## Rebuild

```bash
python3 scripts/build_uranium_series_groundwater_package.py
```

## Data handling

- CNSC Cigar Lake IEMP raw CSV rows: {metadata["raw_rows"]}
- Censored values: {metadata["censored_rule"]}
- Swedish 2025 well-water values are literature-summary values from the open article page, not reconstructed raw samples.

## Main outputs

- `Paper.zh.md`: full academic paper in Chinese
- `Paper.zh.pdf`: PDF export, if the local export step has been run
- `data/`: cleaned and derived tables
- `figures/`: SVG visualizations
- `models/`: PHREEQC/state-vector/dose templates
- `sources/`: downloaded source-page snapshots and raw monitoring CSV
"""
    write_text(REPORT / "README.md", content)


def main() -> None:
    ensure_dirs()
    water_summary, food_summary, metadata = summarize_iemp_csv()
    build_source_tables(water_summary, food_summary)
    build_figures()
    write_model_templates()
    write_paper(metadata)
    write_readme(metadata)
    print(json.dumps({"report": str(REPORT), "metadata": metadata}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
