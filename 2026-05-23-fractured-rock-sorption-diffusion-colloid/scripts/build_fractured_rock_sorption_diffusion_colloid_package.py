#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a reproducible GeoMine report package for fractured-rock radionuclide transport.

The package uses source-derived parameter tables from SKB, NAGRA/Grimsel and
EGU/EURAD public sources, then derives screening-scale retardation, diffusion
penetration and colloid desorption metrics. It does not execute PHREEQC,
PFLOTRAN, COMSOL or OGS.
"""

from __future__ import annotations

import csv
import html
import json
import math
from pathlib import Path
from statistics import median


REPORT = Path(__file__).resolve().parents[1]
DATA = REPORT / "data"
FIG = REPORT / "figures"
MODELS = REPORT / "models"
SOURCES = REPORT / "sources"

SECONDS_PER_YEAR = 365.25 * 24 * 3600
RHO_B = 2700.0  # kg m-3 crystalline-rock matrix density
THETA_M = 0.0018  # 0.18% diffusion-available porosity, SKB TR-10-50
DE_CATION_M2_S = 10 ** -13.7
DE_ANION_M2_S = 10 ** -14.2


def ensure_dirs() -> None:
    for path in (DATA, FIG, MODELS, SOURCES):
        path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def fmt_sci(x: float) -> str:
    if x == 0:
        return "0"
    return f"{x:.3e}"


def table_md(rows: list[dict], cols: list[str], limit: int | None = None) -> str:
    rows = rows if limit is None else rows[:limit]
    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join(["---"] * len(cols)) + " |"
    body = []
    for row in rows:
        body.append("| " + " | ".join(str(row.get(c, "")) for c in cols) + " |")
    return "\n".join([header, sep] + body)


def build_data_tables() -> None:
    bibliography = [
        {
            "id": "EGU26_5127",
            "source_type": "conference_abstract",
            "title": "Identification of knowledge gaps regarding iodine, neptunium and technetium sorption in the context of deep geological nuclear waste disposal",
            "year": "2026",
            "url": "https://meetingorganizer.copernicus.org/EGU26/EGU26-5127.html",
            "doi": "10.5194/egusphere-egu26-5127",
            "used_for": "problem framing: sorption depends on mineral, pH, redox, ionic strength, complexants, microorganisms, space and time",
        },
        {
            "id": "EURAD_2024_RETENTION_TRANSPORT",
            "source_type": "peer_reviewed_review",
            "title": "EURAD state-of-the-art report on the understanding of radionuclide retention and transport in clay and crystalline rocks",
            "year": "2024",
            "url": "https://www.frontiersin.org/journals/nuclear-engineering/articles/10.3389/fnuen.2024.1417827/full",
            "doi": "10.3389/fnuen.2024.1417827",
            "used_for": "state-of-the-art review for diffusion, retention, sorption, redox chemistry and crystalline host rock",
        },
        {
            "id": "SKB_R_10_48",
            "source_type": "parameter_report",
            "title": "Bedrock Kd data and uncertainty assessment for application in SR-Site geosphere transport calculations",
            "year": "2010",
            "url": "https://skb.com/publication/2192981/R-10-48.pdf",
            "doi": "",
            "used_for": "Forsmark recommended Kd distributions for target radionuclides",
        },
        {
            "id": "SKB_TR_10_50",
            "source_type": "safety_assessment_transport_report",
            "title": "Radionuclide transport report for the safety assessment SR-Site",
            "year": "2010",
            "url": "https://www.skb.com/publication/2166831/TR-10-50.pdf",
            "doi": "",
            "used_for": "diffusion-available porosity, effective diffusivity, matrix diffusion formulation and F-factor framing",
        },
        {
            "id": "NAGRA_NTB_16_06",
            "source_type": "field_experiment_modelling_report",
            "title": "Modelling of the Colloid Formation and Migration Experiment at the Grimsel Test Site",
            "year": "2016",
            "url": "https://nagra.ch/wp-content/uploads/2022/08/e_ntb16-006.pdf",
            "doi": "",
            "used_for": "Grimsel CFM field-test colloid recovery, filtration, attachment/detachment and radionuclide/homologue desorption rates",
        },
        {
            "id": "Grimsel_CFM_Aims",
            "source_type": "project_page",
            "title": "Grimsel Test Site CFM project aims",
            "year": "accessed 2026",
            "url": "https://www.grimsel.com/gts-projects/cfm-section/cfm-aims",
            "doi": "",
            "used_for": "project context for bentonite colloid formation and migration",
        },
    ]
    write_csv(DATA / "source_bibliography.csv", bibliography, list(bibliography[0].keys()))

    egu_gaps = [
        {"axis": "radionuclides", "reported_state": "I, Np, Tc selected as safety-relevant representatives", "interpretation": "Use I-129, Np redox states and Tc-99/Tc redox states as gap-sensitive model tests.", "source": "EGU26_5127"},
        {"axis": "studied domain", "reported_state": "neutral to slightly alkaline pH and low to moderate ionic strength extensively studied", "interpretation": "Base-case crystalline groundwater can be parameterized, but extrapolation needs uncertainty.", "source": "EGU26_5127"},
        {"axis": "knowledge gaps", "reported_state": "high ionic strength >1 M, temperature >25 C, organic ligands, microorganisms", "interpretation": "Scenario matrix must include salinity, thermal pulse, organics and microbial colloids.", "source": "EGU26_5127"},
        {"axis": "process statement", "reported_state": "sorption on mineral surfaces constrains radionuclide migration to biosphere", "interpretation": "Kd/surface complexation should be a first-order safety-relevant process, not a secondary correction.", "source": "EGU26_5127"},
    ]
    write_csv(DATA / "egu_2026_knowledge_gap_terms.csv", egu_gaps, list(egu_gaps[0].keys()))

    # Source-derived values from SKB R-10-48 Table 6-1, Forsmark.
    kd_rows = [
        {"species": "U(IV)", "nuclide_group": "U", "charge_class": "tetravalent actinide", "best_kd_m3_kg": 5.29e-2, "lower_kd_m3_kg": 2.84e-3, "upper_kd_m3_kg": 9.84e-1, "log10_m": -1.28, "log10_s": 0.65, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "U(VI)", "nuclide_group": "U", "charge_class": "uranyl oxycation/carbonate complexes", "best_kd_m3_kg": 1.06e-4, "lower_kd_m3_kg": 5.53e-6, "upper_kd_m3_kg": 2.05e-3, "log10_m": -3.97, "log10_s": 0.66, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "Ra(II)", "nuclide_group": "Ra", "charge_class": "alkaline-earth cation", "best_kd_m3_kg": 2.42e-4, "lower_kd_m3_kg": 3.87e-5, "upper_kd_m3_kg": 1.51e-3, "log10_m": -3.62, "log10_s": 0.41, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "Th(IV)", "nuclide_group": "Th", "charge_class": "tetravalent actinide", "best_kd_m3_kg": 5.29e-2, "lower_kd_m3_kg": 2.84e-3, "upper_kd_m3_kg": 9.84e-1, "log10_m": -1.28, "log10_s": 0.65, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "Np(IV)", "nuclide_group": "Np", "charge_class": "tetravalent actinide", "best_kd_m3_kg": 5.29e-2, "lower_kd_m3_kg": 2.84e-3, "upper_kd_m3_kg": 9.84e-1, "log10_m": -1.28, "log10_s": 0.65, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "Np(V)", "nuclide_group": "Np", "charge_class": "pentavalent actinyl", "best_kd_m3_kg": 4.13e-4, "lower_kd_m3_kg": 1.48e-5, "upper_kd_m3_kg": 1.15e-2, "log10_m": -3.38, "log10_s": 0.74, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "Pu(III)", "nuclide_group": "Pu", "charge_class": "trivalent actinide", "best_kd_m3_kg": 1.48e-2, "lower_kd_m3_kg": 5.74e-4, "upper_kd_m3_kg": 3.83e-1, "log10_m": -1.83, "log10_s": 0.72, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "Pu(IV)", "nuclide_group": "Pu", "charge_class": "tetravalent actinide", "best_kd_m3_kg": 5.29e-2, "lower_kd_m3_kg": 2.84e-3, "upper_kd_m3_kg": 9.84e-1, "log10_m": -1.28, "log10_s": 0.65, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "Am(III)", "nuclide_group": "Am", "charge_class": "trivalent actinide", "best_kd_m3_kg": 1.48e-2, "lower_kd_m3_kg": 5.74e-4, "upper_kd_m3_kg": 3.83e-1, "log10_m": -1.83, "log10_s": 0.72, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "I(-I)", "nuclide_group": "I-129", "charge_class": "weakly sorbing anion", "best_kd_m3_kg": 0.0, "lower_kd_m3_kg": 0.0, "upper_kd_m3_kg": 0.0, "log10_m": "", "log10_s": "", "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "Tc(IV)", "nuclide_group": "Tc-99", "charge_class": "reduced tetravalent Tc", "best_kd_m3_kg": 5.29e-2, "lower_kd_m3_kg": 2.84e-3, "upper_kd_m3_kg": 9.84e-1, "log10_m": -1.28, "log10_s": 0.65, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "Tc(VII)", "nuclide_group": "Tc-99", "charge_class": "pertechnetate oxyanion", "best_kd_m3_kg": 0.0, "lower_kd_m3_kg": 0.0, "upper_kd_m3_kg": 0.0, "log10_m": "", "log10_s": "", "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "Se(-II/IV/VI)", "nuclide_group": "Se-79", "charge_class": "redox-sensitive chalcogen/oxyanions", "best_kd_m3_kg": 2.95e-4, "lower_kd_m3_kg": 2.50e-5, "upper_kd_m3_kg": 3.48e-3, "log10_m": -3.53, "log10_s": 0.55, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "Cs(I)", "nuclide_group": "Cs-137", "charge_class": "alkali cation", "best_kd_m3_kg": 3.49e-4, "lower_kd_m3_kg": 3.46e-5, "upper_kd_m3_kg": 3.52e-3, "log10_m": -3.46, "log10_s": 0.51, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
        {"species": "Sr(II)", "nuclide_group": "Sr-90", "charge_class": "alkaline-earth cation", "best_kd_m3_kg": 3.42e-6, "lower_kd_m3_kg": 3.84e-8, "upper_kd_m3_kg": 3.05e-4, "log10_m": -5.47, "log10_s": 0.99, "source": "SKB_R_10_48 Table 6-1 Forsmark"},
    ]
    for row in kd_rows:
        for key in ("best_kd_m3_kg", "lower_kd_m3_kg", "upper_kd_m3_kg"):
            row[key] = float(row[key])
    write_csv(DATA / "skb_forsmark_kd_selected.csv", kd_rows, list(kd_rows[0].keys()))

    transport = [
        {"parameter": "diffusion_available_porosity", "symbol": "theta_m", "value": THETA_M, "unit": "fraction", "source_value": "0.18%", "source": "SKB_TR_10_50 Section 2.5.1", "note": "Flowpath average porosity reduced for possible drilling/core-damage bias."},
        {"parameter": "bulk_density", "symbol": "rho_b", "value": RHO_B, "unit": "kg/m3", "source_value": "assumed crystalline-rock density", "source": "screening assumption", "note": "Used only for derived retardation screening."},
        {"parameter": "effective_diffusivity_cation_neutral", "symbol": "D_e+", "value": DE_CATION_M2_S, "unit": "m2/s", "source_value": "log10 De = -13.7 +/- 0.25", "source": "SKB_TR_10_50 Section 2.5.2", "note": "Converted also to m2/y in derived outputs."},
        {"parameter": "effective_diffusivity_anion", "symbol": "D_e-", "value": DE_ANION_M2_S, "unit": "m2/s", "source_value": "log10 De = -14.2 +/- 0.25", "source": "SKB_TR_10_50 Section 2.5.2", "note": "Anions have lower recommended effective diffusivity."},
    ]
    write_csv(DATA / "skb_transport_reference_parameters.csv", transport, list(transport[0].keys()))

    derived = []
    years = [1e3, 1e4, 1e5]
    for row in kd_rows:
        kd = float(row["best_kd_m3_kg"])
        R = 1.0 + RHO_B * kd / THETA_M
        lower_R = 1.0 + RHO_B * float(row["lower_kd_m3_kg"]) / THETA_M
        upper_R = 1.0 + RHO_B * float(row["upper_kd_m3_kg"]) / THETA_M
        is_anion = row["species"] in {"I(-I)", "Tc(VII)", "Se(-II/IV/VI)"} or "anion" in row["charge_class"] or "oxyanion" in row["charge_class"]
        De = DE_ANION_M2_S if is_anion else DE_CATION_M2_S
        De_y = De * SECONDS_PER_YEAR
        d = {
            "species": row["species"],
            "nuclide_group": row["nuclide_group"],
            "best_kd_m3_kg": kd,
            "retardation_factor_R": R,
            "lower_R": lower_R,
            "upper_R": upper_R,
            "effective_diffusivity_m2_s": De,
            "effective_diffusivity_m2_y": De_y,
            "source": "derived from SKB_R_10_48 Kd and SKB_TR_10_50 porosity/diffusivity",
        }
        for t in years:
            # Retarded diffusion equation R*dC/dt = De*d2C/dz2 gives characteristic depth sqrt(De*t/R).
            d[f"diffusion_depth_m_{int(t)}y"] = math.sqrt(De_y * t / R)
        derived.append(d)
    write_csv(
        DATA / "derived_retardation_and_diffusion.csv",
        derived,
        [
            "species",
            "nuclide_group",
            "best_kd_m3_kg",
            "retardation_factor_R",
            "lower_R",
            "upper_R",
            "effective_diffusivity_m2_s",
            "effective_diffusivity_m2_y",
            "diffusion_depth_m_1000y",
            "diffusion_depth_m_10000y",
            "diffusion_depth_m_100000y",
            "source",
        ],
    )

    cfm_summary = [
        {"test": "08-01/08-02", "outflow_ml_min": "160/165", "inflow_ml_min": "10", "travel_or_observation_time_h": "8-200 range", "conservative_recovery_pct": 99, "colloid_recovery_pct": "near 99 in table context; report notes multiple analyses", "interpretation": "shorter/high-flow dipole; conservative tracer nearly fully recovered", "source": "NAGRA_NTB_16_06 Tab. 3 and Tab. 11"},
        {"test": "10-01", "outflow_ml_min": "48", "inflow_ml_min": "--", "travel_or_observation_time_h": "8-200 range", "conservative_recovery_pct": 84, "colloid_recovery_pct": "53/47 (LIBD-dependent)", "interpretation": "colloid recovery below conservative recovery; reversible plus irreversible filtration needed", "source": "NAGRA_NTB_16_06 Tab. 3, Fig. 17-18, Tab. 11"},
        {"test": "10-03", "outflow_ml_min": "10", "inflow_ml_min": "--", "travel_or_observation_time_h": "8-200 range", "conservative_recovery_pct": 60, "colloid_recovery_pct": 41, "interpretation": "lower flow/longer interaction; colloid recovery decreases, consistent with filtration", "source": "NAGRA_NTB_16_06 Tab. 3, Fig. 16, Tab. 11"},
        {"test": "12-02", "outflow_ml_min": "25", "inflow_ml_min": "0.33", "travel_or_observation_time_h": "8-200 range", "conservative_recovery_pct": 80, "colloid_recovery_pct": 54, "interpretation": "colloid-associated radionuclide breakthrough observed; Am/Pu fitted after field data release", "source": "NAGRA_NTB_16_06 Tab. 3 and Tab. 11"},
    ]
    write_csv(DATA / "nagra_cfm_field_summary.csv", cfm_summary, list(cfm_summary[0].keys()))

    desorption = [
        {"test": "10-01", "species": "Th", "valence_proxy": "tetravalent", "model": "1-site", "kmca_h-1": 0.0253, "source": "NAGRA_NTB_16_06 Tab. 9"},
        {"test": "10-01", "species": "Hf", "valence_proxy": "tetravalent", "model": "1-site", "kmca_h-1": 0.0368, "source": "NAGRA_NTB_16_06 Tab. 9"},
        {"test": "10-01", "species": "Tb", "valence_proxy": "trivalent", "model": "1-site", "kmca_h-1": 0.0740, "source": "NAGRA_NTB_16_06 Tab. 9"},
        {"test": "10-01", "species": "Eu", "valence_proxy": "trivalent", "model": "1-site", "kmca_h-1": 0.0860, "source": "NAGRA_NTB_16_06 Tab. 9"},
        {"test": "10-03", "species": "Th", "valence_proxy": "tetravalent", "model": "1-site", "kmca_h-1": 0.0030, "source": "NAGRA_NTB_16_06 Tab. 9"},
        {"test": "10-03", "species": "Hf", "valence_proxy": "tetravalent", "model": "1-site", "kmca_h-1": 0.0021, "source": "NAGRA_NTB_16_06 Tab. 9"},
        {"test": "10-03", "species": "Tb", "valence_proxy": "trivalent", "model": "1-site", "kmca_h-1": 0.0415, "source": "NAGRA_NTB_16_06 Tab. 9"},
        {"test": "10-03", "species": "Eu", "valence_proxy": "trivalent", "model": "1-site", "kmca_h-1": 0.0260, "source": "NAGRA_NTB_16_06 Tab. 9"},
        {"test": "12-02", "species": "Am", "valence_proxy": "trivalent actinide", "model": "1-site", "kmca_h-1": 0.0163, "source": "NAGRA_NTB_16_06 Tab. 9"},
        {"test": "12-02", "species": "Pu", "valence_proxy": "tetravalent/actinide", "model": "1-site", "kmca_h-1": 0.0077, "source": "NAGRA_NTB_16_06 Tab. 9"},
    ]
    for row in desorption:
        k = float(row["kmca_h-1"])
        row["desorption_half_life_h"] = math.log(2) / k
    write_csv(DATA / "nagra_cfm_desorption_rates.csv", desorption, list(desorption[0].keys()))

    filtration = [
        {"parameter": "colloid_attachment_to_fracture_filling", "symbol": "k_cs", "value_h-1": 0.054, "half_time_h": math.log(2) / 0.054, "source": "NAGRA_NTB_16_06 Fig. 17-18 text", "interpretation": "reversible colloid attachment calibrated for Run 10-01"},
        {"parameter": "colloid_detachment_from_fracture_filling", "symbol": "k_sc", "value_h-1": 0.108, "half_time_h": math.log(2) / 0.108, "source": "NAGRA_NTB_16_06 Fig. 17-18 text", "interpretation": "reversible detachment calibrated for Run 10-01"},
        {"parameter": "irreversible_colloid_filtration", "symbol": "k_cs_irr", "value_h-1": 0.01, "half_time_h": math.log(2) / 0.01, "source": "NAGRA_NTB_16_06 Fig. 17-18 text", "interpretation": "additional irreversible filtration; important for long pathways"},
    ]
    write_csv(DATA / "nagra_cfm_filtration_parameters.csv", filtration, list(filtration[0].keys()))

    class_rows = []
    for row in kd_rows:
        species = row["species"]
        kd = float(row["best_kd_m3_kg"])
        if kd == 0:
            sorption_class = "weak/non-sorbing"
        elif kd < 1e-4:
            sorption_class = "very weak"
        elif kd < 1e-3:
            sorption_class = "weak-to-moderate"
        elif kd < 1e-2:
            sorption_class = "moderate"
        else:
            sorption_class = "strong"
        colloid = "low" if species in {"I(-I)", "Tc(VII)", "Se(-II/IV/VI)", "Sr(II)", "Ra(II)"} else "medium/high for actinides or Cs under favorable colloid stability"
        redox = "yes" if any(x in species for x in ["U(", "Np(", "Pu(", "Tc(", "Se("]) else "limited"
        class_rows.append(
            {
                "species": species,
                "nuclide_group": row["nuclide_group"],
                "sorption_class": sorption_class,
                "redox_sensitivity": redox,
                "colloid_relevance": colloid,
                "expected_migration_scenario": scenario_label(species, kd),
            }
        )
    write_csv(DATA / "radionuclide_classification_matrix.csv", class_rows, list(class_rows[0].keys()))

    alignment = [
        {"claim": "强吸附核素以矿物吸附和基质扩散迟滞为主", "data_evidence": "Forsmark Kd: U(IV), Th(IV), Np(IV), Pu(IV), Tc(IV) = 5.29e-2 m3/kg; Am(III)=1.48e-2 m3/kg. Derived R values are 2.2e4 to 7.9e4.", "model_alignment": "Retardation equation R=1+rho_b Kd/theta predicts very large matrix storage capacity.", "status": "supported for redox/colloid-stable-free case"},
        {"claim": "I-129 and Tc(VII) are weak吸附高迁移性阴离子", "data_evidence": "SKB_R_10_48 assigns Kd=0 for I(-I) and Tc(VII).", "model_alignment": "R=1; transport controlled by fracture connectivity, diffusion-accessible porosity and source term rather than mineral sorption.", "status": "supported"},
        {"claim": "Se-79 is less mobile than I/Tc(VII) but still often weakly sorbing", "data_evidence": "Se(-II/IV/VI) best Kd=2.95e-4 m3/kg, comparable to Ra/Cs order in this dataset but with redox uncertainty.", "model_alignment": "Scenario must distinguish selenide/selenite/selenate and Fe/Mn oxide retention.", "status": "supported with redox caveat"},
        {"claim": "U、Np、Tc redox transition changes mobility by orders of magnitude", "data_evidence": "U(IV)/U(VI) Kd ratio about 499; Np(IV)/Np(V) ratio about 128; Tc(IV)/Tc(VII) ratio is effectively infinite in Kd table because Tc(VII)=0.", "model_alignment": "Eh boundary must be an explicit state variable, not a fixed parameter.", "status": "strongly supported"},
        {"claim": "胶体可增强强吸附核素的表观迁移", "data_evidence": "Grimsel CFM: colloid recovery tens of percent; Th/Hf/Eu/Tb/Am/Pu breakthrough controlled by desorption from bentonite colloids.", "model_alignment": "A mobile colloid-attached state plus filtration/desorption kinetics is required.", "status": "supported for colloid-stable fracture scenarios"},
        {"claim": "胶体增强不是无限制迁移", "data_evidence": "NAGRA Run 10-01 fitted k_cs=0.054 h-1, k_sc=0.108 h-1, k_cs,irr=0.01 h-1; colloid recoveries decline with travel time.", "model_alignment": "Filtration Damkohler number must screen whether colloids survive a given pathway.", "status": "supported"},
    ]
    write_csv(DATA / "model_alignment_matrix.csv", alignment, list(alignment[0].keys()))


def scenario_label(species: str, kd: float) -> str:
    if species in {"I(-I)", "Tc(VII)"}:
        return "weak sorption - high fracture-flow mobility"
    if species in {"U(IV)", "Th(IV)", "Np(IV)", "Pu(IV)", "Tc(IV)", "Am(III)", "Pu(III)"}:
        return "strong sorption - matrix/mineral retention unless colloid-bound"
    if species in {"U(VI)", "Np(V)", "Se(-II/IV/VI)"}:
        return "redox/speciation-sensitive intermediate mobility"
    if species in {"Cs(I)", "Ra(II)", "Sr(II)"}:
        return "cation exchange / mineral-specific sorption"
    return "site-specific"


def svg_text(x: float, y: float, text: str, size: int = 12, fill: str = "#203040", anchor: str = "start", weight: str = "400") -> str:
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-family="Arial, sans-serif" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{html.escape(str(text))}</text>'


def save_svg(path: Path, width: int, height: int, body: str) -> None:
    write_text(path, f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n<rect width="100%" height="100%" fill="#fff"/>\n{body}\n</svg>\n')


def fig_conceptual_model() -> None:
    body = [svg_text(45, 40, "裂隙流动—矿物吸附—基质扩散—胶体携带四过程耦合模型", 20, "#102030", weight="700")]
    body.append('''<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#465a69"/></marker></defs>''')
    body.append('<rect x="70" y="110" width="790" height="65" fill="#e9f2f7" stroke="#7592a3"/>')
    body.append(svg_text(465, 150, "流动裂隙：对流 + 弥散 + 胶体迁移", 18, "#102030", "middle", "700"))
    for x, mineral, color in [(95, "黑云母/绿泥石", "#5f7d4f"), (265, "赤铁矿/磁铁矿", "#9b4d3a"), (435, "方解石", "#6e8fb5"), (580, "黏土/Fe-Mn氧化物", "#7b5fa8"), (765, "有机/微生物胶体", "#bd8b36")]:
        body.append(f'<rect x="{x}" y="205" width="130" height="72" rx="7" fill="#f7f8fa" stroke="{color}" stroke-width="1.6"/>')
        body.append(svg_text(x + 65, 238, mineral, 12, color, "middle", "700"))
        body.append(svg_text(x + 65, 258, "吸附/过滤位点", 11, "#344", "middle"))
        body.append(f'<line x1="{x+65}" y1="205" x2="{x+65}" y2="176" stroke="{color}" marker-end="url(#arr)"/>')
    body.append('<rect x="115" y="325" width="680" height="95" fill="#f5f8fb" stroke="#8da4b2" stroke-dasharray="6 4"/>')
    body.append(svg_text(455, 360, "低渗透岩石基质：Fick 扩散 + Kd/表面络合储存", 16, "#102030", "middle", "700"))
    body.append(svg_text(455, 388, "峰值削减、尾迹拉长；强吸附核素的扩散前缘浅但容量大", 12, "#405060", "middle"))
    body.append(svg_text(130, 475, "状态变量：C_dissolved, C_colloid, S_surface, C_matrix(z), pH, Eh, I, carbonate/sulfate/chloride, DOC, colloid size/stability", 12, "#223"))
    save_svg(FIG / "fig01_multiscale_conceptual_model.svg", 960, 520, "\n".join(body))


def fig_kd_bars() -> None:
    rows = read_csv(DATA / "skb_forsmark_kd_selected.csv")
    selected = ["I(-I)", "Tc(VII)", "Sr(II)", "U(VI)", "Ra(II)", "Se(-II/IV/VI)", "Cs(I)", "Np(V)", "Am(III)", "Pu(IV)", "Th(IV)", "U(IV)", "Tc(IV)"]
    rows = [r for s in selected for r in rows if r["species"] == s]
    width, height = 1040, 620
    x0, y0, plot_w, row_h = 235, 80, 660, 35
    min_log, max_log = -7.5, 0.2
    body = [svg_text(40, 38, "SKB Forsmark Kd：核素吸附强度跨越 5 个以上数量级", 20, "#102030", weight="700")]
    for p in range(-7, 1):
        x = x0 + (p - min_log) / (max_log - min_log) * plot_w
        body.append(f'<line x1="{x:.1f}" y1="{y0-18}" x2="{x:.1f}" y2="{y0+len(rows)*row_h+8}" stroke="#e1e6ea"/>')
        body.append(svg_text(x, y0 + len(rows) * row_h + 30, f"10^{p}", 11, "#59636b", "middle"))
    body.append(f'<line x1="{x0}" y1="{y0+len(rows)*row_h+8}" x2="{x0+plot_w}" y2="{y0+len(rows)*row_h+8}" stroke="#333"/>')
    colors = {"weak": "#8ba6b3", "mid": "#b7834f", "strong": "#6e5aa8"}
    for i, r in enumerate(rows):
        y = y0 + i * row_h
        kd = float(r["best_kd_m3_kg"])
        lower = max(float(r["lower_kd_m3_kg"]), 1e-8)
        upper = max(float(r["upper_kd_m3_kg"]), 1e-8)
        val = max(kd, 1e-8)
        x_l = x0 + (math.log10(lower) - min_log) / (max_log - min_log) * plot_w
        x_u = x0 + (math.log10(upper) - min_log) / (max_log - min_log) * plot_w
        x_v = x0 + (math.log10(val) - min_log) / (max_log - min_log) * plot_w
        c = colors["weak"] if kd < 1e-4 else colors["mid"] if kd < 1e-2 else colors["strong"]
        body.append(svg_text(x0 - 14, y + 18, r["species"], 12, "#223", "end"))
        body.append(f'<line x1="{x_l:.1f}" y1="{y+13}" x2="{x_u:.1f}" y2="{y+13}" stroke="#888" stroke-width="2"/>')
        body.append(f'<circle cx="{x_v:.1f}" cy="{y+13}" r="6" fill="{c}"/>')
        body.append(svg_text(x_v + 10, y + 17, fmt_sci(kd), 10, "#334"))
    body.append(svg_text(55, 585, "点为 best estimate，中线为 2.5%-97.5% Kd 区间；I(-I) 与 Tc(VII) 的 Kd=0 用 1e-8 作绘图下限。", 12, "#445"))
    save_svg(FIG / "fig02_skb_kd_log_range.svg", width, height, "\n".join(body))


def fig_retardation_diffusion() -> None:
    rows = read_csv(DATA / "derived_retardation_and_diffusion.csv")
    selected = ["I(-I)", "Tc(VII)", "Sr(II)", "U(VI)", "Ra(II)", "Cs(I)", "Am(III)", "Pu(IV)", "Tc(IV)"]
    rows = [r for s in selected for r in rows if r["species"] == s]
    width, height = 1030, 560
    body = [svg_text(40, 38, "由 Kd 推导的基质迟滞因子与 10 万年扩散穿透深度", 20, "#102030", weight="700")]
    x0, y0, plot_w = 210, 88, 360
    log_min, log_max = 0, 5.5
    for p in range(0, 6):
        x = x0 + (p - log_min) / (log_max - log_min) * plot_w
        body.append(f'<line x1="{x:.1f}" y1="{y0-20}" x2="{x:.1f}" y2="{y0+len(rows)*42}" stroke="#e6e9ec"/>')
        body.append(svg_text(x, y0 + len(rows) * 42 + 20, f"10^{p}", 10, "#666", "middle"))
    for i, r in enumerate(rows):
        y = y0 + i * 42
        R = max(float(r["retardation_factor_R"]), 1)
        x2 = x0 + (math.log10(R) - log_min) / (log_max - log_min) * plot_w
        body.append(svg_text(x0 - 12, y + 18, r["species"], 12, "#223", "end"))
        body.append(f'<rect x="{x0}" y="{y}" width="{max(2, x2-x0):.1f}" height="22" fill="#4f7f9f"/>')
        body.append(svg_text(x2 + 7, y + 17, f"R={R:.1f}", 10, "#223"))
    x1 = 660
    max_d = max(float(r["diffusion_depth_m_100000y"]) for r in rows)
    body.append(svg_text(x1, 70, "10^5 y 特征扩散深度 sqrt(D_e t / R)", 13, "#102030", weight="700"))
    for i, r in enumerate(rows):
        y = y0 + i * 42
        d = float(r["diffusion_depth_m_100000y"])
        w = d / max_d * 260
        body.append(svg_text(x1 - 12, y + 18, r["species"], 12, "#223", "end"))
        body.append(f'<rect x="{x1}" y="{y}" width="{w:.1f}" height="22" fill="#b7834f"/>')
        body.append(svg_text(x1 + w + 7, y + 17, f"{d:.3f} m", 10, "#223"))
    body.append(svg_text(60, 525, "解释：强吸附提高基质容量和迟滞，但扩散前缘按 sqrt(D_e t/R) 变浅；非吸附阴离子 R=1，扩散更深但储存能力低。", 12, "#445"))
    save_svg(FIG / "fig03_retardation_and_diffusion_depth.svg", width, height, "\n".join(body))


def fig_redox_ratios() -> None:
    rows = {r["species"]: r for r in read_csv(DATA / "skb_forsmark_kd_selected.csv")}
    pairs = [("U(IV)/U(VI)", "U(IV)", "U(VI)"), ("Np(IV)/Np(V)", "Np(IV)", "Np(V)"), ("Tc(IV)/Tc(VII)", "Tc(IV)", "Tc(VII)")]
    width, height = 820, 360
    body = [svg_text(45, 38, "氧化还原转换导致 Kd 数量级突变", 20, "#102030", weight="700")]
    x0, y0, plot_w = 230, 95, 450
    max_log = 6.0
    for p in range(0, 7):
        x = x0 + p / max_log * plot_w
        body.append(f'<line x1="{x:.1f}" y1="{y0-25}" x2="{x:.1f}" y2="{y0+135}" stroke="#e6e9ec"/>')
        body.append(svg_text(x, y0 + 165, f"10^{p}", 10, "#666", "middle"))
    for i, (label, reduced, oxidized) in enumerate(pairs):
        kd_red = float(rows[reduced]["best_kd_m3_kg"])
        kd_ox = float(rows[oxidized]["best_kd_m3_kg"])
        ratio = kd_red / kd_ox if kd_ox > 0 else 1e6
        y = y0 + i * 55
        x2 = x0 + min(math.log10(ratio), max_log) / max_log * plot_w
        body.append(svg_text(x0 - 15, y + 20, label, 13, "#223", "end"))
        body.append(f'<rect x="{x0}" y="{y}" width="{x2-x0:.1f}" height="26" fill="#8c4f6f"/>')
        label_ratio = ">=1e6" if kd_ox == 0 else f"{ratio:.0f}"
        body.append(svg_text(x2 + 9, y + 19, label_ratio, 12, "#223"))
    body.append(svg_text(65, 310, "Tc(VII) 的 Kd=0，图中用 1e6 下限表示“由非吸附到强吸附”的有效突变；模型必须显式求解 Eh/pe。", 12, "#445"))
    save_svg(FIG / "fig04_redox_kd_shift.svg", width, height, "\n".join(body))


def fig_colloid_rates() -> None:
    rows = read_csv(DATA / "nagra_cfm_desorption_rates.csv")
    width, height = 1000, 560
    body = [svg_text(40, 38, "Grimsel CFM：胶体携带核素的解吸半衰期", 20, "#102030", weight="700")]
    x0, y0, plot_w = 190, 80, 610
    max_h = max(float(r["desorption_half_life_h"]) for r in rows)
    for i, r in enumerate(rows):
        y = y0 + i * 42
        h = float(r["desorption_half_life_h"])
        w = h / max_h * plot_w
        color = "#7b5fa8" if r["valence_proxy"].startswith("tri") else "#9b4d3a"
        body.append(svg_text(x0 - 14, y + 18, f'{r["test"]}/{r["species"]}', 11, "#223", "end"))
        body.append(f'<rect x="{x0}" y="{y}" width="{w:.1f}" height="22" fill="{color}"/>')
        body.append(svg_text(x0 + w + 7, y + 17, f'{h:.1f} h', 10, "#223"))
    body.append(svg_text(70, 525, "解吸越慢，核素越可能保持胶体结合并绕过裂隙壁面强吸附位点；但胶体本身还受过滤控制。", 12, "#445"))
    save_svg(FIG / "fig05_grimsel_desorption_half_lives.svg", width, height, "\n".join(body))


def fig_scenario_matrix() -> None:
    rows = read_csv(DATA / "radionuclide_classification_matrix.csv")
    categories = {
        "weak/non-sorbing": (120, "#8ba6b3"),
        "very weak": (220, "#9fb386"),
        "weak-to-moderate": (335, "#b7834f"),
        "moderate": (475, "#a46f7e"),
        "strong": (620, "#6e5aa8"),
    }
    y_map = {"low": 395, "medium/high for actinides or Cs under favorable colloid stability": 190}
    width, height = 900, 520
    body = [svg_text(45, 38, "核素迁移情景矩阵：吸附强度 vs 胶体相关性", 20, "#102030", weight="700")]
    body.append('<rect x="85" y="105" width="680" height="330" fill="#f7f9fb" stroke="#ccd5dc"/>')
    body.append(svg_text(425, 475, "矿物吸附强度 / Kd class", 13, "#223", "middle", "700"))
    body.append(svg_text(35, 280, "胶体相关性", 13, "#223", "middle", "700"))
    for label, (x, color) in categories.items():
        body.append(svg_text(x, 455, label, 10, "#334", "middle"))
        body.append(f'<line x1="{x}" y1="105" x2="{x}" y2="435" stroke="#e1e6ea"/>')
    body.append(svg_text(795, 195, "Pu/Am/Th/U(IV)/Tc(IV)", 12, "#6e5aa8"))
    body.append(svg_text(795, 400, "I/Tc(VII)/Sr/Ra/Se", 12, "#697782"))
    species_offsets = {}
    for r in rows:
        x = categories.get(r["sorption_class"], (430, "#444"))[0]
        y = y_map.get(r["colloid_relevance"], 300)
        key = (x, y)
        species_offsets[key] = species_offsets.get(key, 0) + 1
        dx = ((species_offsets[key] - 1) % 4) * 24 - 36
        dy = ((species_offsets[key] - 1) // 4) * 22
        color = categories.get(r["sorption_class"], (430, "#444"))[1]
        body.append(f'<circle cx="{x+dx}" cy="{y+dy}" r="15" fill="{color}" opacity="0.9"/>')
        body.append(svg_text(x + dx, y + dy + 4, r["nuclide_group"].replace("-137", "").replace("-129", "").replace("-99", "").replace("-90", ""), 9, "#fff", "middle", "700"))
    body.append(svg_text(110, 132, "胶体增强迁移域：强吸附 + 胶体稳定 + 过滤弱 + 解吸慢", 12, "#445"))
    body.append(svg_text(110, 420, "水相高迁移域：非吸附/弱吸附阴离子；主要受裂隙连通性和源项控制", 12, "#445"))
    save_svg(FIG / "fig06_radionuclide_scenario_matrix.svg", width, height, "\n".join(body))


def build_figures() -> None:
    fig_conceptual_model()
    fig_kd_bars()
    fig_retardation_diffusion()
    fig_redox_ratios()
    fig_colloid_rates()
    fig_scenario_matrix()


def write_model_templates() -> None:
    model_spec = {
        "title": "fracture-sorption-matrix-diffusion-colloid conceptual model",
        "coupling_level": "HC with optional THC/THMC extensions",
        "state_variables": {
            "mobile_fracture": ["C_dissolved_i", "C_colloid_particle", "C_colloid_bound_i", "pH", "Eh_or_pe", "ionic_strength", "carbonate", "sulfate", "chloride", "DOC"],
            "fracture_surface": ["S_mineral_i", "site_density_biotite", "site_density_chlorite", "site_density_hematite", "site_density_magnetite", "site_density_calcite", "site_density_clay", "site_density_FeMn_oxide"],
            "rock_matrix": ["C_matrix_i(z)", "theta_m", "D_e_i", "Kd_i", "porosity_accessible_depth"],
            "colloid": ["particle_size_distribution", "zeta_potential", "attachment_rate", "detachment_rate", "irreversible_filtration_rate", "radionuclide_desorption_rate"],
        },
        "governing_processes": ["advection_dispersion", "surface_complexation_or_Kd", "matrix_diffusion", "radioactive_decay", "redox_speciation", "colloid_attachment_detachment_filtration", "colloid_radionuclide_desorption"],
        "source_status": "parameterized from public reports; no site-specific calibration or safety-case execution",
    }
    write_text(MODELS / "reactive_transport_state_vector.json", json.dumps(model_spec, indent=2, ensure_ascii=False))

    pflotran = """# PFLOTRAN conceptual input skeleton: fractured-rock radionuclide migration
# This file is a non-executed template. It requires a mesh, flow field, chemistry database,
# sorption parameters, redox reactions, colloid module implementation or external coupling.

SIMULATION
  SIMULATION_TYPE SUBSURFACE
  PROCESS_MODELS
    SUBSURFACE_FLOW flow
      MODE RICHARDS
    /
    SUBSURFACE_TRANSPORT transport
      MODE GIRT
    /
  /
END

SUBSURFACE
  # FLOW_CONDITION, TRANSPORT_CONDITION, MATERIAL_PROPERTY and REGION blocks go here.
  # Mobile aqueous species: I-, TcO4-, Se oxyanions, U/Np/Pu/Am hydrolysis-carbonate species.
  # Immobile/sorbed terms: Kd or surface-complexation proxies by mineral assemblage.
  # Matrix diffusion can be represented through multi-rate mass transfer or dual-continuum regions.
  # Colloids require either a mobile pseudo-component with attachment/detachment/filtration
  # or coupling to a custom reactive-transport kernel.
END_SUBSURFACE
"""
    write_text(MODELS / "pflotran_fracture_colloid_template.in", pflotran)

    phreeqc = """TITLE PHREEQC speciation and sorption prototype for crystalline-rock fracture water
# Non-executed draft. Use ThermoChimie/SIT/NEA-style database where radionuclide species are available.

SOLUTION 1 Generic reduced crystalline groundwater
    temp 15
    pH 8 charge
    pe -3
    units mol/kgw
    Na 0.1
    Ca 0.01
    Cl 0.12
    C(4) 1e-3
    S(6) 1e-4

SURFACE 1 FeMn_oxide_sites
    Hfo_wOH 1e-5 600 0.09

EXCHANGE 1 Clay_biotite_chlorite_exchange
    X 1e-4

# Add radionuclide total concentrations only when validated source terms are supplied.
# Add SURFACE_MASTER_SPECIES/SURFACE_SPECIES for U, Np, Pu, Am, Cs, Sr if database supports them.
# For I- and TcO4-, test non-sorbing conservative behavior under oxic conditions.
SELECTED_OUTPUT
    -file selected_speciation_sorption.out
    -pH true
    -pe true
    -totals U Np Pu Am I Tc Se Cs Sr Ra Th
END
"""
    write_text(MODELS / "phreeqc_sorption_speciation_template.phr", phreeqc)

    comsol_ogs = {
        "mesh": "2D fracture plus perpendicular 1D matrix columns, or 3D discrete-fracture network with dual-continuum matrix zones",
        "primary_unknowns": ["hydraulic_head", "aqueous_concentration_i", "matrix_concentration_i", "colloid_concentration", "colloid_bound_radionuclide_i"],
        "boundary_conditions": ["source pulse at engineered-barrier interface", "advective outlet", "no-flux symmetry in matrix far boundary or finite matrix depth", "specified groundwater chemistry zones"],
        "calibration_targets": ["conservative tracer breakthrough", "sorbing tracer breakthrough", "colloid recovery", "desorption tailing", "matrix diffusion profiles"],
        "verification_tests": ["mass conservation", "analytical 1D advection-dispersion comparison", "matrix diffusion semi-infinite solution", "Kd retardation benchmark", "colloid filtration first-order benchmark"],
    }
    write_text(MODELS / "comsol_ogs_implementation_manifest.json", json.dumps(comsol_ogs, indent=2, ensure_ascii=False))


def write_mcp_provenance() -> None:
    content = """# MCP provenance

GeoMine MCP was used for provenance-preserving AOI normalization and public Canadian geodata discovery planning.

- `normalize_aoi`: parsed a generic crystalline-rock DGR far-field AOI; no authoritative geometry, distance, claim, NTS or CRS transformation was performed.
- `search_cdogs_surveys`: planned NRCan CDoGS discovery with network disabled; no live geochemical spreadsheet was parsed.

Scientific numeric data in this package therefore come from public literature/report sources downloaded into `sources/`, not from a live GeoMine THMC execution. No PHREEQC, PFLOTRAN, COMSOL or OGS run result is claimed.
"""
    write_text(REPORT / "mcp_provenance.md", content)


def write_paper() -> None:
    kd_rows = read_csv(DATA / "skb_forsmark_kd_selected.csv")
    derived_rows = read_csv(DATA / "derived_retardation_and_diffusion.csv")
    egu_rows = read_csv(DATA / "egu_2026_knowledge_gap_terms.csv")
    cfm_rows = read_csv(DATA / "nagra_cfm_field_summary.csv")
    desorption_rows = read_csv(DATA / "nagra_cfm_desorption_rates.csv")
    filtration_rows = read_csv(DATA / "nagra_cfm_filtration_parameters.csv")
    class_rows = read_csv(DATA / "radionuclide_classification_matrix.csv")
    alignment_rows = read_csv(DATA / "model_alignment_matrix.csv")

    # Compact selected table for the paper.
    kd_paper = []
    for r in kd_rows:
        kd_paper.append(
            {
                "species": r["species"],
                "Kd_m3_kg": fmt_sci(float(r["best_kd_m3_kg"])),
                "lower_upper_m3_kg": f'{fmt_sci(float(r["lower_kd_m3_kg"]))}-{fmt_sci(float(r["upper_kd_m3_kg"]))}',
                "class": next(c["sorption_class"] for c in class_rows if c["species"] == r["species"]),
            }
        )
    derived_paper = []
    for r in derived_rows:
        if r["species"] in {"I(-I)", "Tc(VII)", "Sr(II)", "U(VI)", "Ra(II)", "Cs(I)", "Am(III)", "Pu(IV)", "Tc(IV)", "Se(-II/IV/VI)"}:
            derived_paper.append(
                {
                    "species": r["species"],
                    "R": f'{float(r["retardation_factor_R"]):.2g}',
                    "D_e_m2_s": fmt_sci(float(r["effective_diffusivity_m2_s"])),
                    "depth_1e5y_m": f'{float(r["diffusion_depth_m_100000y"]):.3f}',
                }
            )

    md = r"""---
title: "结晶岩裂隙中核素吸附—基质扩散—胶体促进迁移的多尺度模型"
subtitle: "面向深地质处置库远场安全评价的反应运移框架、公开参数分析与情景排序"
author: "GeoMine Research / OpenMiner"
date: "2026-05-23"
lang: zh-CN
---

# 摘要

深地质处置库远场中的核素迁移不是简单的地下水随流输送过程，而是裂隙流动、矿物表面吸附、裂隙—基质扩散、氧化还原形态转换和胶体携带共同控制的多尺度反应运移问题。EGU 2026 摘要 EGU26-5127 明确指出，工程屏障和围岩矿物表面吸附是约束核素从深地质处置库向生物圈迁移的关键过程，但吸附受矿物类型、pH、Eh、离子强度、络合离子、温度、有机配体和微生物影响，并随空间和时间变化。本文据此构建“裂隙流动—矿物吸附—基质扩散—胶体携带”四过程耦合模型，重点讨论 U、Ra、Th、Np、Pu、Am，I-129、Tc-99、Se-79，以及 Cs-137、Sr-90 在结晶岩裂隙系统中的迁移风险排序。

本文使用三组公开证据进行数据化分析：SKB R-10-48 的 Forsmark 岩体 Kd 推荐值，SKB TR-10-50 的扩散可达孔隙度和有效扩散系数，以及 NAGRA/Grimsel CFM 胶体形成与迁移现场试验参数。以 $\rho_b=2700\ \mathrm{kg\,m^{-3}}$、$\theta_m=0.0018$、$D_e=10^{-13.7}\ \mathrm{m^2\,s^{-1}}$（阳离子/中性）和 $D_e=10^{-14.2}\ \mathrm{m^2\,s^{-1}}$（阴离子）为筛选参数，Kd 表明 I(-I) 与 Tc(VII) 可近似非吸附，Sr(II)、U(VI)、Ra(II)、Se 与 Cs(I) 处于弱到中等吸附区间，U(IV)、Th(IV)、Np(IV)、Pu(IV)、Tc(IV) 与 Am(III) 具有强吸附迟滞。红氧转换可使 Kd 发生 2-6 个数量级突变，例如 U(IV)/U(VI) 约 499，Np(IV)/Np(V) 约 128，Tc(IV)/Tc(VII) 由强吸附转为非吸附。Grimsel CFM 数据则显示，胶体回收率可达几十个百分点，强吸附 Th/Hf/Eu/Tb/Am/Pu 的突破主要受胶体解吸速率控制；Pu 的一位点解吸半衰期约 90 h，Am 约 43 h，说明强吸附核素在胶体稳定和过滤较弱的裂隙中可出现表观迁移增强。

本文最终观点是：结晶岩远场安全评价应避免用单一 Kd 或单一保守示踪剂代表全部核素。强吸附核素通常受矿物吸附和基质扩散迟滞，但在膨润土胶体、有机胶体、Fe-Mn 氧化物胶体或微生物胶体稳定存在时必须引入胶体携带状态；I-129、Tc(VII) 和部分 Se 形态的风险主要来自弱吸附和裂隙连通性；U、Np、Tc 的迁移排序必须以 Eh/pe 为状态变量动态判断。面向 PHREEQC、PFLOTRAN、COMSOL 或 OGS 的模型，应以显式物种形态、矿物表面反应、基质扩散和胶体过滤/解吸为共同骨架。

**关键词**：深地质处置库；结晶岩裂隙；核素迁移；矿物吸附；基质扩散；胶体促进迁移；Kd；PFLOTRAN；PHREEQC

# 1. 引言

在结晶岩处置库远场中，裂隙承担主要水力通道功能，而完整岩石基质的渗透性低、孔隙连通性差。若工程屏障发生极低概率核素释放，溶解态核素首先进入裂隙水；随后一部分被裂隙壁面矿物吸附，一部分扩散进入基质微孔并在基质矿物表面迟滞，另一部分可能吸附在移动胶体上并随裂隙流迁移。这个过程的难点在于尺度分裂：米尺度裂隙控制对流时间，毫米至微米尺度蚀变带控制表面反应与基质扩散，纳米至微米尺度胶体控制强吸附核素的旁路迁移。

EGU 2026 议题把 I、Np、Tc 的矿物吸附知识缺口作为深地质处置库安全评价问题，特别强调高盐度、高温、有机配体和微生物影响仍是知识缺口。该议题的重要性在于：它没有把“吸附”视作一个常数，而是视作随矿物、核素价态、水化学和时间变化的过程。本文在此基础上提出一个多尺度模型，并用公开参数做筛选级演算和可视化。

![概念模型](figures/fig01_multiscale_conceptual_model.svg)

# 2. 数据源与方法

## 2.1 公开证据链

本文使用的证据分为四类。

第一，EGU26-5127 提供问题来源。该摘要指出吸附约束深地质处置库核素向生物圈迁移，且吸附受 redox、ionic strength、pH、complexing ions、microorganisms 等控制；其初步结果指出中性至弱碱性、低至中等离子强度条件研究较多，而高离子强度、大于 25 C 温度、有机配体和微生物影响仍是缺口。

第二，EURAD 2024 综述提供理论背景，说明核素向生物圈迁移取决于处置库距离、主导迁移机制（扩散或对流）以及核素与宿主岩/工程屏障矿物相互作用。

第三，SKB R-10-48 给出 Forsmark 岩体 Kd 推荐值和不确定性区间；SKB TR-10-50 给出 SR-Site 使用的扩散可达孔隙度 0.18% 和有效扩散系数：阳离子/中性物种 $\log_{10}D_e=-13.7\pm0.25$，阴离子 $\log_{10}D_e=-14.2\pm0.25$。

第四，NAGRA NTB 16-06 / Grimsel CFM 提供胶体迁移现场证据。该实验在 Grimsel Test Site 研究 FEBEX 膨润土胶体、保守示踪剂、三价/四价同系物和 Am/Pu 等核素的突破、过滤与解吸。

__EGU_TABLE__

## 2.2 数据整理与筛选演算

本文没有声称完成场址校准或安全案例计算，而是做筛选级、可复核演算。主要数据文件包括：

- `data/skb_forsmark_kd_selected.csv`：从 SKB R-10-48 Table 6-1 整理的目标核素 Kd。
- `data/skb_transport_reference_parameters.csv`：从 SKB TR-10-50 整理的 $\theta_m$ 与 $D_e$。
- `data/derived_retardation_and_diffusion.csv`：由 Kd、孔隙度和扩散系数推导的迟滞因子和扩散深度。
- `data/nagra_cfm_desorption_rates.csv` 与 `data/nagra_cfm_filtration_parameters.csv`：Grimsel CFM 胶体解吸、过滤和可逆附着参数。

# 3. 理论框架与公式推导

## 3.1 裂隙对流—弥散方程

将裂隙近似为平行板通道，水力开度为 $2b$。若忽略密度差异和瞬态储水，裂隙内溶解态核素浓度 $C_f(x,t)$ 满足：

\[
2b R_f \frac{\partial C_f}{\partial t}
=
2bD_L\frac{\partial^2 C_f}{\partial x^2}
-2b v\frac{\partial C_f}{\partial x}
-2J_m
-2J_s
-\lambda 2bR_fC_f
+Q_s .
\]

其中 $v$ 为平均裂隙流速，$D_L=\alpha_Lv+D_m$ 为纵向弥散系数，$J_m$ 为进入岩石基质的扩散通量，$J_s$ 为裂隙壁面吸附/反应通量，$\lambda$ 为放射性衰变常数。若裂隙水体本身不考虑颗粒表面迟滞，则 $R_f\approx1$；若有悬浮颗粒或裂隙填充物参与，可把 $R_f$ 扩展为表观迟滞。

## 3.2 基质扩散与迟滞因子

低渗透岩石基质中的一维垂向扩散为：

\[
R_m\frac{\partial C_m}{\partial t}
=
D_e\frac{\partial^2 C_m}{\partial z^2}
-\lambda R_m C_m ,
\]

边界条件为：

\[
C_m(z=0,t)=C_f(x,t),\qquad C_m(z\rightarrow\infty,t)=0 .
\]

矩阵迟滞因子采用线性 Kd：

\[
R_m=1+\frac{\rho_b K_d}{\theta_m}.
\]

半无限基质中，裂隙进入基质的瞬时扩散通量可写为：

\[
J_m=-\theta_mD_e\left.\frac{\partial C_m}{\partial z}\right|_{z=0}.
\]

若用特征时间 $t$ 估算扩散前缘，强吸附核素满足：

\[
\ell_d(t)\sim\sqrt{\frac{D_e t}{R_m}} .
\]

这个式子解释了一个看似矛盾的现象：强吸附核素的扩散前缘较浅，但一旦进入基质，其单位体积储存容量因 $R_m$ 很大而显著提高，突破峰值被压低并产生长尾。

## 3.3 矿物吸附：Kd、表面络合与离子交换

Kd 模型为：

\[
S_i=K_{d,i}C_i,\qquad K_{d,i}=\frac{S_i}{C_i},
\]

其中 $S_i$ 为固相吸附量，单位可表示为 $\mathrm{Bq\,kg^{-1}}$ 或 $\mathrm{mol\,kg^{-1}}$，$C_i$ 为水相浓度。Kd 模型可直接进入迟滞因子，但它把 pH、Eh、矿物表面位点和络合作用折叠进一个常数，因此只适合筛选或在固定水化学条件下使用。

更机制化的表面络合写为：

\[
\equiv SOH + M^{z+} \rightleftharpoons \equiv SOM^{(z-1)+}+H^+ ,
\]

\[
K_{int}=\frac{a_{\equiv SOM}a_{H^+}}{a_{\equiv SOH}a_{M^{z+}}}\exp\left(\frac{F\psi}{RT}\Delta z\right).
\]

Cs 和 Sr 还可用离子交换表示：

\[
\equiv XNa+Cs^+ \rightleftharpoons \equiv XCs+Na^+ ,
\]

\[
2\equiv XNa+Sr^{2+}\rightleftharpoons (\equiv X)_2Sr+2Na^+ .
\]

这些反应说明，黑云母、绿泥石、黏土矿物、方解石、赤铁矿、磁铁矿和 Fe-Mn 氧化物不会给出统一吸附行为。强吸附锕系元素常由水解、碳酸盐络合、表面络合和胶体结合共同决定；I(-I) 与 TcO4- 在许多条件下则接近非吸附。

## 3.4 红氧形态转换

U、Np、Pu、Tc、Se 的迁移性强烈依赖价态。以 Tc 为例：

\[
\mathrm{TcO_4^- + 4H^+ + 3e^- \rightleftharpoons TcO(OH)_2(s/aq)+H_2O}.
\]

氧化态 Tc(VII) 以 pertechnetate $\mathrm{TcO_4^-}$ 存在，常近似非吸附；还原态 Tc(IV) 则水解和沉淀/吸附显著。Nernst 形式为：

\[
E_h=E^0-\frac{RT}{nF}\ln Q .
\]

这意味着 Eh 不能作为常数背景，而应是迁移模型的状态变量或情景边界。

## 3.5 胶体促进迁移

令 $C_d$ 为溶解态核素，$C_c$ 为移动胶体浓度，$C_{ic}$ 为胶体结合态核素，$S_s$ 为裂隙表面吸附态核素。简化动力学为：

\[
\frac{\partial C_c}{\partial t}
 +v_c\frac{\partial C_c}{\partial x}
=D_c\frac{\partial^2C_c}{\partial x^2}
-k_{att}C_c+k_{det}C_{c,s}-k_{irr}C_c ,
\]

\[
\frac{\partial C_{ic}}{\partial t}
 +v_c\frac{\partial C_{ic}}{\partial x}
=D_c\frac{\partial^2C_{ic}}{\partial x^2}
k_{on}C_dC_c-k_{off}C_{ic}-k_{irr}C_{ic}.
\]

若核素强烈吸附在胶体上且 $k_{off}$ 小，则它可随胶体移动；若 $k_{irr}$ 或过滤系数大，则胶体被裂隙填充物截留。胶体促进迁移的必要条件可写成三个不等式：

\[
K_{pc}C_c\gg 1,\qquad
Da_{off}=\frac{k_{off}L}{v}\ll1,\qquad
Da_{f}=\frac{k_{irr}L}{v}\lesssim1 .
\]

因此，胶体不是“总是增强迁移”，而是在强核素—胶体分配、低解吸、低过滤和足够连通裂隙同时满足时才增强迁移。

# 4. 公开数据分析

## 4.1 Kd 数据与核素吸附分类

SKB R-10-48 Forsmark Kd 表显示，目标核素的吸附强度跨越多个数量级。

__KD_TABLE__

![Kd 数量级](figures/fig02_skb_kd_log_range.svg)

这个结果直接支撑四类迁移情景。I(-I) 与 Tc(VII) 的 $K_d=0$，属于弱吸附高迁移端元；Sr(II)、U(VI)、Ra(II)、Se 和 Cs(I) 为弱到中等吸附，容易受离子强度、碳酸盐、硫酸盐和交换位点影响；Am(III)、Pu(III/IV)、Th(IV)、U(IV)、Np(IV)、Tc(IV) 为强吸附核素，但这些核素也最容易受到胶体携带的影响。

## 4.2 迟滞因子与基质扩散演算

采用 $\rho_b=2700\ \mathrm{kg\,m^{-3}}$ 和 $\theta_m=0.0018$，由 $R_m=1+\rho_bK_d/\theta_m$ 可得：

__DERIVED_TABLE__

![迟滞与扩散](figures/fig03_retardation_and_diffusion_depth.svg)

演算给出三个关键结论。第一，I(-I) 与 Tc(VII) 的 $R_m=1$，其迁移速度主要由裂隙流场、弥散和基质扩散决定。第二，U(VI)、Ra(II)、Se、Cs(I) 虽然 Kd 不高，但由于结晶岩 $\theta_m$ 很小，仍可形成数百量级迟滞。第三，强吸附锕系元素的 $R_m$ 可达 $10^4-10^5$ 量级，导致基质扩散前缘很浅，但基质容量极大，突破曲线表现为低峰值和长尾。

## 4.3 红氧转换的数量级影响

![红氧 Kd 突变](figures/fig04_redox_kd_shift.svg)

同一元素在不同价态下 Kd 可发生数量级突变。U(IV) 与 U(VI) 的 Kd 比约 499，Np(IV) 与 Np(V) 的 Kd 比约 128；Tc(IV) 和 Tc(VII) 的差别更极端，因为 Tc(VII) 在 SKB 表中被视为非吸附。由此可得：

\[
\mathrm{migration\ ranking} = f(Eh,pH,ligands,minerals)
\]

而不是固定核素名单。例如 Tc-99 在氧化裂隙中可能接近保守迁移，在还原 Fe(II)/硫化物环境中则可被强烈迟滞。

## 4.4 Grimsel CFM 胶体迁移约束

Grimsel CFM 提供了现场尺度胶体迁移证据。

__CFM_TABLE__

胶体过滤/附着参数：

__FILTRATION_TABLE__

胶体结合态核素/同系物的解吸速率如下。

__DESORPTION_TABLE__

![胶体解吸半衰期](figures/fig05_grimsel_desorption_half_lives.svg)

NAGRA 报告对 Run 10-01 的胶体突破曲线给出 $k_{cs}=0.054\ \mathrm{h^{-1}}$、$k_{sc}=0.108\ \mathrm{h^{-1}}$ 和不可逆过滤 $k_{cs,irr}=0.01\ \mathrm{h^{-1}}$。这说明胶体在裂隙填充物上存在可逆交换，同时有不可逆损失。核素/同系物方面，Th、Hf、Tb、Eu、Am、Pu 的突破受从胶体解吸的速率控制；Pu 一位点解吸 $k=0.0077\ \mathrm{h^{-1}}$，半衰期约 90 h，Am 为 0.0163 $\mathrm{h^{-1}}$，半衰期约 43 h。若裂隙旅行时间与这些半衰期同阶或更短，胶体结合态就可能显著贡献迁移。

# 5. 情景矩阵与论证对齐

__CLASS_TABLE__

![情景矩阵](figures/fig06_radionuclide_scenario_matrix.svg)

__ALIGNMENT_TABLE__

模型—数据对齐可以概括为：

1. 强吸附锕系元素在无胶体或胶体被过滤条件下迁移距离有限；这一点由高 Kd 和大 $R_m$ 支持。
2. I-129 与 Tc(VII) 的远场重要性来自弱吸附，而不是高放射毒性或高源项本身；它们更接近水文连通性指标。
3. U、Np、Tc、Se 必须进行价态情景拆分；一个固定 Kd 不能同时代表氧化、还原和过渡带。
4. 胶体促进迁移主要改变强吸附核素的表观迁移性，对 I(-I) 或 Tc(VII) 这类本来就弱吸附的阴离子不是主要增强机制。
5. 胶体迁移需要同时考虑胶体稳定、过滤、解吸和裂隙尺度，不应简单假定胶体全程保守。

# 6. 面向 PHREEQC、PFLOTRAN、COMSOL 与 OGS 的模型实现

## 6.1 PHREEQC 原型

PHREEQC 适合处理水化学形态、饱和指数、离子交换和表面络合原型。本文提供 `models/phreeqc_sorption_speciation_template.phr`。建议使用流程为：

1. 输入地下水 pH、pe/Eh、离子强度、碳酸盐、硫酸盐、氯离子、Ca、Na、Fe、Mn、DOC。
2. 对 U、Np、Pu、Am、Tc、Se 进行价态和络合形态计算。
3. 对黑云母/绿泥石/黏土矿物使用交换位点，对 Fe-Mn 氧化物使用表面络合位点。
4. 输出主要水相物种和表面吸附分数，再传递给场尺度反应运移模型。

## 6.2 PFLOTRAN/OGS/COMSOL 场尺度实现

场尺度推荐三种路线：

- **PFLOTRAN**：适合 2D/3D 反应运移和长时间尺度参数扫描；胶体模块可用移动伪组分或外部耦合实现。
- **OpenGeoSys**：适合裂隙—基质扩散、THM/THMC 耦合和有限元网格控制。
- **COMSOL**：适合验证性模型、裂隙-基质多物理场耦合和胶体过滤/解吸方程原型。

模型至少需要以下输入：裂隙开度、连通性、流速、孔隙率、基质扩散系数、裂隙壁面矿物组成、蚀变带厚度、pH、Eh、盐度、碳酸盐/硫酸盐/氯离子、有机质、胶体粒径、胶体稳定性、初始核素形态、Kd、表面络合参数、沉淀/溶解速率和温度。

# 7. 局限性

本文为综述与概念模型构建，不是处置库安全案例。局限性包括：

- SKB Kd 是 Forsmark 条件下的推荐参数，不可直接移植到加拿大 Shield、Revell Batholith 或任何具体场址。
- Kd 模型无法替代表面络合和离子交换模型；它把水化学条件折叠为常数。
- Grimsel CFM 是强约束现场 analogue，但其流场、胶体配方、注入方式和尺度与真实处置库远场并不相同。
- 胶体长期稳定性、微生物胶体、有机胶体和 Fe-Mn 氧化物胶体仍需要更多现场数据。
- 本文未执行 PHREEQC/PFLOTRAN/OGS/COMSOL，因此所有模型输出为筛选演算和概念图，不是数值模拟结果。

# 8. 结论

本文建立了结晶岩裂隙中核素吸附—基质扩散—胶体促进迁移的多尺度模型，并用公开数据进行筛选演算。结论如下。

第一，矿物吸附是远场核素迟滞的核心机制，但它不能被简化为普适常数。Kd 随核素价态、矿物类型、pH、Eh、离子强度和络合离子变化；EGU 2026 指出的高盐度、高温、有机配体和微生物影响仍是关键知识缺口。

第二，基质扩散是结晶岩远场的峰值削减机制。裂隙提供快速水力通道，低渗透基质提供扩散储存空间。强吸附核素的扩散前缘较浅，但迟滞因子极大；非吸附阴离子扩散更深，但储存容量较低。

第三，迁移风险排序应按核素形态而不是元素名称判断。I(-I) 与 Tc(VII) 属于弱吸附高迁移端元；U(IV)、Th(IV)、Np(IV)、Pu(IV)、Am(III) 在无胶体条件下强烈迟滞；U(VI)、Np(V)、Tc(IV/VII)、Se(-II/IV/VI) 必须按 Eh-pH 情景拆分。

第四，胶体促进迁移是强吸附核素远场评价的必要机制，但不是无条件增强项。Grimsel CFM 证据表明胶体可携带 Th、Hf、Eu、Tb、Am、Pu 等迁移，并且突破曲线受解吸速率控制；同时胶体也会被裂隙填充物过滤，回收率随旅行时间降低。因此，胶体模块必须同时包含核素—胶体分配、解吸、可逆附着和不可逆过滤。

第五，面向长期安全评价的模型应采用“四过程耦合”结构：裂隙对流弥散定义水力连通性，矿物吸附定义迟滞和反应位点，基质扩散定义远场储存和尾迹，胶体携带定义强吸附核素的旁路迁移。这个框架能把 U/Ra/Th/Np/Pu/Am、I/Tc/Se、Cs/Sr 三类核素纳入统一但可区分的迁移排序。

# 数据与文件清单

- `data/source_bibliography.csv`：公开证据源列表。
- `data/skb_forsmark_kd_selected.csv`：目标核素 Kd 表。
- `data/skb_transport_reference_parameters.csv`：孔隙度与有效扩散系数。
- `data/derived_retardation_and_diffusion.csv`：迟滞因子和扩散深度演算。
- `data/nagra_cfm_field_summary.csv`：Grimsel CFM 现场试验汇总。
- `data/nagra_cfm_desorption_rates.csv`：胶体结合核素解吸速率。
- `data/model_alignment_matrix.csv`：命题—数据—模型对齐矩阵。
- `figures/*.svg`：论文图件。
- `models/*.json`、`models/*.phr`、`models/*.in`：后续模型模板。
- `sources/*.pdf|*.html|*.txt`：公开源文件和 PDF 文本抽取结果。

# 参考文献

1. Philipp, T., Weyand, T., and Bracke, G. (2026). *Identification of knowledge gaps regarding iodine, neptunium and technetium sorption in the context of deep geological nuclear waste disposal*. EGU General Assembly 2026, EGU26-5127. https://doi.org/10.5194/egusphere-egu26-5127
2. Maes, N., Churakov, S., Glaus, M., Baeyens, B., et al. (2024). *EURAD state-of-the-art report on the understanding of radionuclide retention and transport in clay and crystalline rocks*. Frontiers in Nuclear Engineering. https://doi.org/10.3389/fnuen.2024.1417827
3. Crawford, J. (2010). *Bedrock Kd data and uncertainty assessment for application in SR-Site geosphere transport calculations*. SKB R-10-48. https://skb.com/publication/2192981/R-10-48.pdf
4. SKB. (2010). *Radionuclide transport report for the safety assessment SR-Site*. SKB TR-10-50. https://www.skb.com/publication/2166831/TR-10-50.pdf
5. NAGRA. (2016). *Modelling of the Colloid Formation and Migration Experiment at the Grimsel Test Site*. NAGRA NTB 16-06. https://nagra.ch/wp-content/uploads/2022/08/e_ntb16-006.pdf
6. Grimsel Test Site. *Colloid Formation and Migration project aims*. https://www.grimsel.com/gts-projects/cfm-section/cfm-aims
"""

    replacements = {
        "__EGU_TABLE__": table_md(egu_rows, ["axis", "reported_state", "interpretation"], None),
        "__KD_TABLE__": table_md(kd_paper, ["species", "Kd_m3_kg", "lower_upper_m3_kg", "class"], None),
        "__DERIVED_TABLE__": table_md(derived_paper, ["species", "R", "D_e_m2_s", "depth_1e5y_m"], None),
        "__CFM_TABLE__": table_md(cfm_rows, ["test", "outflow_ml_min", "conservative_recovery_pct", "colloid_recovery_pct", "interpretation"], None),
        "__FILTRATION_TABLE__": table_md([{**r, "half_time_h": f'{float(r["half_time_h"]):.1f}'} for r in filtration_rows], ["parameter", "symbol", "value_h-1", "half_time_h", "interpretation"], None),
        "__DESORPTION_TABLE__": table_md([{**r, "desorption_half_life_h": f'{float(r["desorption_half_life_h"]):.1f}'} for r in desorption_rows], ["test", "species", "valence_proxy", "kmca_h-1", "desorption_half_life_h"], None),
        "__CLASS_TABLE__": table_md(class_rows, ["species", "nuclide_group", "sorption_class", "redox_sensitivity", "colloid_relevance", "expected_migration_scenario"], None),
        "__ALIGNMENT_TABLE__": table_md(alignment_rows, ["claim", "data_evidence", "model_alignment", "status"], None),
    }
    for key, value in replacements.items():
        md = md.replace(key, value)
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
table { border-collapse: collapse; width: 100%; font-size: 9.3px; margin: 16px 0 24px; table-layout: fixed; }
th, td { border: 1px solid #d8dee6; padding: 5px 6px; vertical-align: top; overflow-wrap: anywhere; word-break: break-word; }
th { background: #f4f7fa; }
img { max-width: 100%; margin: 14px 0 22px; }
code { background: #f3f5f7; padding: 1px 4px; }
@page { size: A4; margin: 16mm 14mm; }
"""
    write_text(REPORT / "Paper.print.css", css.strip() + "\n")


def write_readme() -> None:
    content = """# Fractured-rock radionuclide sorption, matrix diffusion and colloid migration package

Generated: 2026-05-23

Main paper:

- `Paper.zh.md`
- `Paper.zh.pdf` after PDF export

Rebuild data, figures, models and Markdown:

```bash
python3 scripts/build_fractured_rock_sorption_diffusion_colloid_package.py
```

Important boundary:

This package performs source-backed screening calculations and conceptual model synthesis. It does not execute PHREEQC, PFLOTRAN, COMSOL or OpenGeoSys and does not claim site-specific safety validation.
"""
    write_text(REPORT / "README.md", content)


def main() -> None:
    ensure_dirs()
    build_data_tables()
    build_figures()
    write_model_templates()
    write_mcp_provenance()
    write_paper()
    write_readme()
    print(json.dumps({"report": str(REPORT), "outputs": sorted(str(p.relative_to(REPORT)) for p in REPORT.rglob("*") if p.is_file())}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
