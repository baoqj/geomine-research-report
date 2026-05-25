#!/usr/bin/env python3
"""Build a reproducible Revell Batholith radiolysis-THMC paper package.

The script intentionally uses only the Python standard library so the package
can be rebuilt in a minimal research environment.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from textwrap import dedent
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIGURES = ROOT / "figures"
MODELS = ROOT / "models"
SOURCES_DIR = ROOT / "sources"

SECONDS_PER_YEAR = 365.25 * 24 * 3600
ROCK_DENSITY_G_CM3 = 2.66
G_H2_MOLECULES_PER_100EV = 0.45
MOLECULE_100EV_TO_UMOL_J = 0.10364
G_H2_MOL_J = G_H2_MOLECULES_PER_100EV * MOLECULE_100EV_TO_UMOL_J * 1e-6
REVELL_H2_NMOL_M3_YR = 1.6
REVELL_HEAT_UW_M3 = 1.08
CONNECTED_POROSITY = 0.0045
TOTAL_POROSITY = 0.0132
TEMPERATURE_K = 283.15
H2_HENRY_MOL_L_ATM = 7.8e-4
R_GAS = 8.314462618


SOURCES = [
    {
        "id": "nwmo_2022_confidence_revell",
        "title": "Confidence in Safety: Revell Site",
        "organization": "Nuclear Waste Management Organization",
        "year": 2022,
        "url": "https://www.nwmo.ca/-/media/Reports-MASTER/Technical-reports/NWMO-TR-2022-14-Confidence-in-Safety-Revell-Site-2022-03.ashx?rev=7e56d8a81d714d70a8d6004b1c2cce49&sc_lang=en",
        "local_file": "sources/NWMO-TR-2022-14-Confidence-in-Safety-Revell-Site.pdf",
        "used_for": "Revell site investigation context, boreholes, hydrogeochemistry depth framework, low-permeability crystalline-rock safety context.",
    },
    {
        "id": "nwmo_2023_confidence_revell_update",
        "title": "Confidence in Safety: Revell Site - 2023 Update",
        "organization": "Nuclear Waste Management Organization",
        "year": 2023,
        "url": "https://www.nwmo.ca/-/media/Reports-MASTER/Technical-reports/NWMO-TR-2023-07-Confidence-in-Safety---Revell-Site---2023-Update.ashx?rev=6180a2f1bd95498f96d4dec51c8e406c&sc_lang=en",
        "local_file": "sources/NWMO-TR-2023-07-Confidence-in-Safety-Revell-Update.pdf",
        "used_for": "Public Revell update values for lithology, porosity, hydrochemistry zones, hydraulic conductivity and sulphide detection boundary.",
    },
    {
        "id": "villamizar_2024_arma",
        "title": "Developing a coupled thermal-hydraulic-mechanical-chemical model for the Revell Batholith, Ontario, Canada",
        "organization": "ARMA / Villamizar et al.",
        "year": 2024,
        "url": "https://armarocks.net/papers/379.pdf",
        "local_file": "sources/ARMA-24-379-Revell-thermal-model.pdf",
        "used_for": "Borehole-scale U-Th-K, density, heat production, temperature gradient and repository-depth THMC model context.",
    },
    {
        "id": "nwmo_mapping_2017",
        "title": "Phase 2 Geological Mapping: Township of Ignace and Area, Ontario",
        "organization": "Nuclear Waste Management Organization",
        "year": 2017,
        "url": "https://www.nwmo.ca/-/media/Reports---Reports/APM-REP-01332-0225-Phase-2-Geological-Mapping-Township-of-Ignace-and-Area-11-17.ashx?hash=2B490F4795C7E3BB59C39AB3EAB296CF&rev=a36ce8c7c16e4020b5896e539fdce61e&sc_lang=en",
        "local_file": "sources/NWMO-Phase2-Geological-Mapping-Ignace-Revell.pdf",
        "used_for": "Surface lithology and U-Th-K summary statistics for Revell-area crystalline rocks.",
    },
    {
        "id": "higgins_2025_radiolysis",
        "title": "Natural H2 and Sulfate Production via Radiolysis in Low Porosity and Permeability Crystalline Rocks",
        "organization": "Higgins et al.",
        "year": 2025,
        "url": "https://doi.org/10.1021/acsearthspacechem.5c00072",
        "used_for": "Revell Batholith H2 production rate, Kidd Creek comparison, and sulfate-production contrast.",
    },
    {
        "id": "usgs_phreeqc_v3",
        "title": "PHREEQC Version 3 documentation",
        "organization": "USGS",
        "year": 2024,
        "url": "https://water.usgs.gov/water-resources/software/PHREEQC/documentation/phreeqc3-html/phreeqc3.htm",
        "used_for": "PHREEQC speciation, reaction, transport and inverse-modeling workflow boundary.",
    },
]


LITHOLOGY = [
    {
        "unit": "Granodiorite",
        "occurrence_count": 142,
        "occurrence_pct": 55,
        "K_wt_pct_mean": 2.10,
        "K_wt_pct_sd": 0.58,
        "U_ppm_mean": 1.56,
        "U_ppm_sd": 1.07,
        "Th_ppm_mean": 7.05,
        "Th_ppm_sd": 3.49,
        "source": "nwmo_mapping_2017",
        "notes": "Dominant surface intrusive lithology; mapped Revell-area statistics.",
    },
    {
        "unit": "Tonalite",
        "occurrence_count": 98,
        "occurrence_pct": 36,
        "K_wt_pct_mean": 1.43,
        "K_wt_pct_sd": 0.31,
        "U_ppm_mean": 1.33,
        "U_ppm_sd": 1.14,
        "Th_ppm_mean": 6.14,
        "Th_ppm_sd": 2.53,
        "source": "nwmo_mapping_2017",
        "notes": "Common granitoid lithology in Revell mapping.",
    },
    {
        "unit": "Granite",
        "occurrence_count": 46,
        "occurrence_pct": 18,
        "K_wt_pct_mean": 3.20,
        "K_wt_pct_sd": 0.47,
        "U_ppm_mean": 2.67,
        "U_ppm_sd": 1.87,
        "Th_ppm_mean": 12.20,
        "Th_ppm_sd": 4.68,
        "source": "nwmo_mapping_2017",
        "notes": "Higher U-Th-K felsic end-member; useful sensitivity case.",
    },
    {
        "unit": "Diorite-quartz diorite",
        "occurrence_count": 9,
        "occurrence_pct": 4,
        "K_wt_pct_mean": 0.91,
        "K_wt_pct_sd": 0.22,
        "U_ppm_mean": 0.83,
        "U_ppm_sd": 0.42,
        "Th_ppm_mean": 4.60,
        "Th_ppm_sd": 2.06,
        "source": "nwmo_mapping_2017",
        "notes": "Mafic-intermediate intrusive sensitivity case.",
    },
    {
        "unit": "Revell borehole mean",
        "occurrence_count": 93,
        "occurrence_pct": 97,
        "K_wt_pct_mean": 2.079,
        "K_wt_pct_sd": None,
        "U_ppm_mean": 2.081,
        "U_ppm_sd": None,
        "Th_ppm_mean": 5.247,
        "Th_ppm_sd": None,
        "source": "villamizar_2024_arma",
        "notes": "Whole-rock borehole mean used as the reference heat-production and radiolysis calibration case.",
    },
]


PUBLIC_PARAMETERS = [
    {
        "parameter": "Revell Batholith mapped area",
        "value": 455,
        "unit": "km2",
        "source": "nwmo_mapping_2017",
        "status": "public compiled value",
        "interpretation": "Regional scale is large enough that site-scale fracture and hydrochemical heterogeneity must not be inferred from one borehole alone.",
    },
    {
        "parameter": "Batholith length",
        "value": 40,
        "unit": "km",
        "source": "nwmo_mapping_2017; villamizar_2024_arma",
        "status": "public compiled value",
        "interpretation": "Regional pluton-scale model domain boundary.",
    },
    {
        "parameter": "Batholith width",
        "value": 15,
        "unit": "km",
        "source": "nwmo_mapping_2017",
        "status": "public compiled value",
        "interpretation": "Regional pluton-scale model domain boundary.",
    },
    {
        "parameter": "Repository-depth host-rock interval",
        "value": "500-800",
        "unit": "m below ground surface",
        "source": "nwmo_2022_confidence_revell; villamizar_2024_arma",
        "status": "public design-depth range",
        "interpretation": "Depth window for hydrochemical and THMC screening.",
    },
    {
        "parameter": "Borehole whole-rock U",
        "value": 2.081,
        "unit": "ppm",
        "source": "villamizar_2024_arma",
        "status": "public compiled borehole mean",
        "interpretation": "Reference U concentration for heat and radiolysis source-term calculation.",
    },
    {
        "parameter": "Borehole whole-rock Th",
        "value": 5.247,
        "unit": "ppm",
        "source": "villamizar_2024_arma",
        "status": "public compiled borehole mean",
        "interpretation": "Reference Th concentration for heat and radiolysis source-term calculation.",
    },
    {
        "parameter": "Borehole whole-rock K",
        "value": 2.079,
        "unit": "wt%",
        "source": "villamizar_2024_arma",
        "status": "public compiled borehole mean",
        "interpretation": "Reference K concentration for heat and radiolysis source-term calculation.",
    },
    {
        "parameter": "Borehole density",
        "value": 2.66,
        "unit": "g cm-3",
        "source": "villamizar_2024_arma",
        "status": "public compiled borehole mean",
        "interpretation": "Density term for radiogenic heat production.",
    },
    {
        "parameter": "Borehole heat production",
        "value": 1.08,
        "unit": "microW m-3",
        "source": "villamizar_2024_arma",
        "status": "public compiled borehole mean",
        "interpretation": "Reference energy source for water radiolysis screening.",
    },
    {
        "parameter": "Connected porosity",
        "value": 0.45,
        "unit": "%",
        "source": "nwmo_2023_confidence_revell_update",
        "status": "public compiled value",
        "interpretation": "Controls water-accessible radiolysis, diffusion capacity and gas storage in intact crystalline rock.",
    },
    {
        "parameter": "Total porosity",
        "value": 1.32,
        "unit": "%",
        "source": "nwmo_2023_confidence_revell_update",
        "status": "public compiled value",
        "interpretation": "Upper bound on pore volume; connected porosity is the more conservative transport-relevant input.",
    },
    {
        "parameter": "Effective porous-medium hydraulic conductivity at 500-800 m",
        "value": "1e-13 to 1e-12",
        "unit": "m s-1",
        "source": "nwmo_2023_confidence_revell_update",
        "status": "public compiled value",
        "interpretation": "Supports a diffusion-dominated safety model but does not remove discrete-fracture uncertainty.",
    },
    {
        "parameter": "Discrete flowing-fracture hydraulic conductivity",
        "value": "1e-12 to 1e-6",
        "unit": "m s-1",
        "source": "nwmo_2023_confidence_revell_update",
        "status": "public compiled value",
        "interpretation": "Fracture pathways define the key uncertainty lane for advection and gas migration.",
    },
    {
        "parameter": "Sulphide concentration boundary",
        "value": "<0.02",
        "unit": "mg L-1",
        "source": "nwmo_2023_confidence_revell_update",
        "status": "public detection-boundary statement",
        "interpretation": "Low measured sulphide reduces immediate sulphide-corrosion concern, but sulfate reduction remains scenario-dependent.",
    },
    {
        "parameter": "Revell radiolytic H2 production",
        "value": 1.6,
        "unit": "nmol m-3 rock yr-1",
        "source": "higgins_2025_radiolysis",
        "status": "public model result / article abstract value",
        "interpretation": "Central calibration point for screening H2 generation in low-porosity Revell crystalline rock.",
    },
]


HYDROCHEMISTRY = [
    {
        "zone": "Shallow recharge water",
        "depth_min_m": 0,
        "depth_max_m": 300,
        "dominant_chemistry": "Ca-HCO3 type, comparatively dilute",
        "redox": "more oxidizing than deep system; exact Eh requires site samples",
        "salinity_status": "low salinity / fresh-to-dilute category in NWMO summaries",
        "source": "nwmo_2022_confidence_revell; nwmo_2023_confidence_revell_update",
        "data_status": "public qualitative-to-semiquantitative framework",
    },
    {
        "zone": "Transition / mixed fracture water",
        "depth_min_m": 300,
        "depth_max_m": 600,
        "dominant_chemistry": "Mixing between shallow recharge and deeper Ca-Na-Cl-HCO3 water",
        "redox": "transition toward reducing conditions",
        "salinity_status": "increasing Cl/TDS with depth; exact concentrations not extracted here",
        "source": "nwmo_2022_confidence_revell; nwmo_2023_confidence_revell_update",
        "data_status": "public conceptual boundary",
    },
    {
        "zone": "Repository-depth crystalline-rock water",
        "depth_min_m": 500,
        "depth_max_m": 800,
        "dominant_chemistry": "Ca-Na-Cl-HCO3 and deeper saline fracture-water influence",
        "redox": "reducing, old-water tendency expected; exact Eh/pH must be sample-specific",
        "salinity_status": "salinity increases with depth; deep-water mixing possible",
        "source": "nwmo_2022_confidence_revell; nwmo_2023_confidence_revell_update",
        "data_status": "public safety-case depth framework",
    },
    {
        "zone": "Deep saline end-member",
        "depth_min_m": 600,
        "depth_max_m": 1000,
        "dominant_chemistry": "Ca-Na-Cl dominated deep fracture water / brine tendency",
        "redox": "reducing; microbial and mineral redox buffers possible",
        "salinity_status": "highest salinity in public Revell summaries",
        "source": "nwmo_2022_confidence_revell; nwmo_2023_confidence_revell_update",
        "data_status": "public qualitative framework; no raw sample table parsed",
    },
]


SCENARIOS = [
    {
        "scenario": "S0 reducing low-salinity baseline",
        "dominant_controls": "low K, low connected porosity, diffusion-dominated transport, reducing groundwater",
        "expected_result": "low radiolytic H2 source term; radionuclide mobility controlled by sorption/diffusion",
        "computed_status": "screening computed",
        "alignment": "consistent with low Revell H2 rate after geometric attenuation",
    },
    {
        "scenario": "S1 deep saline / Cl-rich fracture mixing",
        "dominant_controls": "Cl activity, ionic strength, fracture connectivity, matrix diffusion",
        "expected_result": "potentially lower sorption for some species and different copper corrosion chemistry",
        "computed_status": "conceptual, requires raw water chemistry",
        "alignment": "public depth framework supports scenario, but no sample-level PHREEQC run was claimed",
    },
    {
        "scenario": "S2 radiolytic H2 accumulation in closed pores",
        "dominant_controls": "H2 source rate, connected porosity, residence time, diffusion, microbial/mineral sinks",
        "expected_result": "host-rock radiolysis alone is small annually but can become mM-scale over Myr if closed",
        "computed_status": "screening computed",
        "alignment": "partly aligned; pressure risk is a transport/closure question, not a source-rate question alone",
    },
    {
        "scenario": "S3 sulfate generation and microbial sulfate reduction",
        "dominant_controls": "sulfide mineral availability, oxidant yield, sulfate supply, H2 electron donor flux",
        "expected_result": "low sulfate source in Revell relative to sulfide-rich Kidd Creek; microbial energy limited",
        "computed_status": "energy-flux screening computed; sulfate rate requires source paper/table",
        "alignment": "aligned with published Revell-Kidd Creek contrast",
    },
    {
        "scenario": "S4 engineered near-field corrosion H2",
        "dominant_controls": "copper/container corrosion, steel components, groundwater composition, bentonite gas entry pressure",
        "expected_result": "likely dominates over host-rock radiolytic H2 near the container",
        "computed_status": "not computed; outside public Revell host-rock dataset",
        "alignment": "kept as THMC safety-interface path, not field-derived result",
    },
]


EQUATIONS = [
    ["E1", "Radioactive decay", r"$N_i(t)=N_{i,0}e^{-\lambda_i t}$; $A_i=\lambda_iN_i$", "nuclide inventory and activity"],
    ["E2", "Radiogenic heat production", r"$A_h=10^{-2}\rho(9.52C_U+2.56C_{Th}+3.48C_K)$", "microW m^-3, rho in g cm^-3, U/Th ppm, K wt%"],
    ["E3", "Radiolytic H2 generation", r"$R_{H_2}=G_{H_2}\epsilon_w A_h10^{-6}t_y$", "mol m^-3 yr^-1"],
    ["E4", "H2 mass balance", r"$\partial_t(\phi C_{H_2})=\nabla\cdot(D_e\nabla C_{H_2})-\nabla\cdot(qC_{H_2})+R_{H_2}-R_{bio}-R_{min}-R_{gas}$", "reactive transport source-sink form"],
    ["E5", "Sulfate from sulfide oxidation", r"$\mathrm{FeS_2}+3.75\mathrm{O_2}+3.5\mathrm{H_2O}\rightarrow\mathrm{Fe(OH)_3}+2\mathrm{SO_4^{2-}}+4\mathrm{H^+}$", "oxidant-to-sulfate pathway"],
    ["E6", "Microbial sulfate reduction", r"$4\mathrm{H_2}+\mathrm{SO_4^{2-}}+\mathrm{H^+}\rightarrow\mathrm{HS^-}+4\mathrm{H_2O}$", "H2 electron donor pathway"],
    ["E7", "Gas pressure screening", r"$P=nRT/V_g$", "closed-gas-volume upper-bound screen"],
    ["E8", "Henry equilibrium", r"$C_{H_2}=k_HP_{H_2}$", "dissolved H2 pressure equivalent"],
    ["E9", "Sorption-retarded transport", r"$R_f\partial_t C=D_e\nabla^2 C-v\nabla C-\lambda C+S$; $R_f=1+\rho_bK_d/\phi$", "radionuclide transport"],
    ["E10", "THMC state vector", r"$\mathbf{y}=[T,p_l,S_l,\sigma,\phi,k,pH,Eh,\mathbf{c},C_{H_2},p_g]$", "coupled model state variables"],
]


def ensure_dirs() -> None:
    for path in [DATA, FIGURES, MODELS, SOURCES_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def heat_production_micro_w_m3(u_ppm: float, th_ppm: float, k_wt_pct: float, rho_g_cm3: float = ROCK_DENSITY_G_CM3) -> float:
    return 0.01 * rho_g_cm3 * (9.52 * u_ppm + 2.56 * th_ppm + 3.48 * k_wt_pct)


def h2_all_energy_nmol_m3_yr(heat_micro_w_m3: float) -> float:
    energy_j_m3_yr = heat_micro_w_m3 * 1e-6 * SECONDS_PER_YEAR
    return energy_j_m3_yr * G_H2_MOL_J * 1e9


def h2_calibrated_nmol_m3_yr(heat_micro_w_m3: float) -> float:
    return REVELL_H2_NMOL_M3_YR * heat_micro_w_m3 / REVELL_HEAT_UW_M3


def pressure_screens(h2_nmol_m3_yr: float, years: float, phi: float = CONNECTED_POROSITY) -> dict[str, float]:
    n_mol = h2_nmol_m3_yr * 1e-9 * years
    gas_p_bar = n_mol * R_GAS * TEMPERATURE_K / max(phi, 1e-12) / 1e5
    water_l = phi * 1000.0
    dissolved_p_atm = n_mol / max(H2_HENRY_MOL_L_ATM * water_l, 1e-30)
    return {
        "years": years,
        "n_mol_m3_rock": n_mol,
        "h2_mmol_m3_rock": n_mol * 1000.0,
        "closed_gas_pressure_bar": gas_p_bar,
        "dissolved_equiv_pressure_atm": dissolved_p_atm,
    }


def derived_rows() -> list[dict[str, object]]:
    rows = []
    for row in LITHOLOGY:
        heat = heat_production_micro_w_m3(row["U_ppm_mean"], row["Th_ppm_mean"], row["K_wt_pct_mean"])
        all_h2 = h2_all_energy_nmol_m3_yr(heat)
        cal_h2 = h2_calibrated_nmol_m3_yr(heat)
        screens_1myr = pressure_screens(cal_h2, 1e6)
        rows.append(
            {
                **row,
                "heat_microW_m3": heat,
                "h2_all_energy_nmol_m3_yr": all_h2,
                "h2_calibrated_nmol_m3_yr": cal_h2,
                "effective_attenuation_fraction": cal_h2 / all_h2,
                "h2_1Myr_mmol_m3_rock": screens_1myr["h2_mmol_m3_rock"],
                "closed_gas_pressure_bar_1Myr": screens_1myr["closed_gas_pressure_bar"],
                "dissolved_equiv_pressure_atm_1Myr": screens_1myr["dissolved_equiv_pressure_atm"],
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, obj: object) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fmt(x: float, digits: int = 3) -> str:
    if abs(x) >= 1000 or (abs(x) > 0 and abs(x) < 0.01):
        return f"{x:.{digits}e}"
    return f"{x:.{digits}f}"


def svg_base(title: str, body: str, width: int = 1180, height: int = 620) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="{width}" height="{height}" fill="#ffffff"/>
  <text x="36" y="42" font-size="24" font-weight="700" fill="#172033">{escape(title)}</text>
  {body}
</svg>
"""


def bar_chart(rows: list[dict[str, object]]) -> str:
    max_heat = max(float(r["heat_microW_m3"]) for r in rows)
    max_h2 = max(float(r["h2_calibrated_nmol_m3_yr"]) for r in rows)
    x0, y0, chart_w, chart_h = 95, 96, 980, 360
    group_w = chart_w / len(rows)
    parts = [
        f'<line x1="{x0}" y1="{y0+chart_h}" x2="{x0+chart_w}" y2="{y0+chart_h}" stroke="#334155" stroke-width="1.5"/>',
        f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+chart_h}" stroke="#334155" stroke-width="1.5"/>',
        f'<text x="{x0}" y="{y0+chart_h+72}" font-size="15" fill="#475569">Heat production bars use public U-Th-K data; H2 line uses Higgins Revell calibration.</text>',
    ]
    for tick in range(5):
        val = max_heat * tick / 4
        y = y0 + chart_h - chart_h * tick / 4
        parts.append(f'<line x1="{x0-6}" y1="{y}" x2="{x0+chart_w}" y2="{y}" stroke="#e2e8f0" stroke-width="1"/>')
        parts.append(f'<text x="34" y="{y+5}" font-size="12" fill="#475569">{val:.2f}</text>')
    line_points = []
    for i, row in enumerate(rows):
        heat = float(row["heat_microW_m3"])
        h2 = float(row["h2_calibrated_nmol_m3_yr"])
        x = x0 + i * group_w + group_w * 0.35
        bw = group_w * 0.30
        h = chart_h * heat / max_heat
        y = y0 + chart_h - h
        parts.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{h}" fill="#2563eb" opacity="0.82"/>')
        cx = x0 + i * group_w + group_w * 0.50
        cy = y0 + chart_h - chart_h * h2 / max_h2
        line_points.append((cx, cy))
        label = escape(str(row["unit"]).replace("Revell borehole mean", "Borehole mean"))
        parts.append(f'<text x="{cx}" y="{y0+chart_h+22}" text-anchor="middle" font-size="12" fill="#172033">{label}</text>')
        parts.append(f'<text x="{cx}" y="{y-8}" text-anchor="middle" font-size="12" fill="#1e3a8a">{heat:.2f}</text>')
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in line_points)
    parts.append(f'<polyline points="{poly}" fill="none" stroke="#b45309" stroke-width="3"/>')
    for x, y in line_points:
        parts.append(f'<circle cx="{x}" cy="{y}" r="5" fill="#f59e0b" stroke="#92400e" stroke-width="1"/>')
    parts.append('<rect x="820" y="74" width="320" height="64" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>')
    parts.append('<rect x="840" y="94" width="24" height="12" fill="#2563eb" opacity="0.82"/>')
    parts.append('<text x="874" y="105" font-size="13" fill="#172033">Heat production, microW m-3</text>')
    parts.append('<line x1="840" y1="122" x2="864" y2="122" stroke="#b45309" stroke-width="3"/>')
    parts.append('<text x="874" y="126" font-size="13" fill="#172033">Calibrated H2, nmol m-3 yr-1</text>')
    return svg_base("Revell U-Th-K heat production and calibrated H2 source", "\n  ".join(parts))


def energy_partition_svg(ref_row: dict[str, object]) -> str:
    all_h2 = float(ref_row["h2_all_energy_nmol_m3_yr"])
    cal_h2 = float(ref_row["h2_calibrated_nmol_m3_yr"])
    attenuation = cal_h2 / all_h2
    labels = ["All radiogenic energy to water", "Revell low-porosity calibrated"]
    values = [all_h2, cal_h2]
    y0, h = 132, 78
    parts = []
    log_min, log_max = -1, 4
    x0, w = 160, 790
    for e in range(log_min, log_max + 1):
        x = x0 + (e - log_min) / (log_max - log_min) * w
        parts.append(f'<line x1="{x}" y1="100" x2="{x}" y2="330" stroke="#e2e8f0"/>')
        parts.append(f'<text x="{x}" y="352" text-anchor="middle" font-size="12" fill="#475569">10^{e}</text>')
    for i, (label, val) in enumerate(zip(labels, values)):
        y = y0 + i * 120
        x_end = x0 + (math.log10(val) - log_min) / (log_max - log_min) * w
        color = "#0f766e" if i == 0 else "#b45309"
        parts.append(f'<text x="48" y="{y+26}" font-size="15" fill="#172033">{escape(label)}</text>')
        parts.append(f'<rect x="{x0}" y="{y}" width="{max(1, x_end-x0)}" height="{h}" fill="{color}" opacity="0.82"/>')
        parts.append(f'<text x="{x_end+12}" y="{y+47}" font-size="15" fill="#172033">{fmt(val)} nmol m-3 yr-1</text>')
    parts.append(f'<text x="48" y="424" font-size="16" fill="#172033">Effective water-accessible energy fraction = {attenuation:.3e}.</text>')
    parts.append('<text x="48" y="452" font-size="14" fill="#475569">This is not a universal constant; it back-calculates the attenuation needed for the public Revell H2 rate.</text>')
    return svg_base("Energy partition: why heat production overpredicts H2 without pore-scale attenuation", "\n  ".join(parts), height=520)


def depth_framework_svg() -> str:
    y_top, y_bot = 90, 545
    x_axis = 170
    depth_max = 1000
    def y(depth: float) -> float:
        return y_top + (depth / depth_max) * (y_bot - y_top)
    parts = [
        f'<line x1="{x_axis}" y1="{y_top}" x2="{x_axis}" y2="{y_bot}" stroke="#172033" stroke-width="2"/>',
        '<text x="48" y="82" font-size="14" fill="#475569">Depth, m bgs</text>',
    ]
    for d in range(0, 1001, 100):
        yy = y(d)
        parts.append(f'<line x1="{x_axis-7}" y1="{yy}" x2="{x_axis+7}" y2="{yy}" stroke="#172033"/>')
        parts.append(f'<text x="112" y="{yy+5}" font-size="12" fill="#475569">{d}</text>')
    colors = ["#dbeafe", "#e0f2fe", "#fef3c7", "#fee2e2"]
    for idx, zone in enumerate(HYDROCHEMISTRY):
        y1, y2 = y(zone["depth_min_m"]), y(zone["depth_max_m"])
        x = 235 + idx * 210
        parts.append(f'<rect x="{x}" y="{y1}" width="180" height="{max(y2-y1, 12)}" rx="4" fill="{colors[idx]}" stroke="#64748b"/>')
        parts.append(f'<text x="{x+90}" y="{y1+22}" text-anchor="middle" font-size="13" font-weight="700" fill="#172033">{escape(zone["zone"])}</text>')
        for j, line in enumerate(wrap_text(zone["dominant_chemistry"], 22)[:3]):
            parts.append(f'<text x="{x+10}" y="{y1+46+j*17}" font-size="12" fill="#172033">{escape(line)}</text>')
    parts.append(f'<rect x="220" y="{y(500)}" width="880" height="{y(800)-y(500)}" fill="none" stroke="#dc2626" stroke-width="3" stroke-dasharray="8 7"/>')
    parts.append(f'<text x="672" y="{y(510)}" text-anchor="middle" font-size="15" fill="#dc2626">500-800 m repository-depth screening window</text>')
    parts.append('<text x="48" y="590" font-size="14" fill="#475569">Quantitative pH/Eh/Cl-Br sample values require raw NWMO tables; this figure preserves only public framework-level constraints.</text>')
    return svg_base("Revell groundwater chemistry depth framework", "\n  ".join(parts), height=640)


def gas_pressure_svg() -> str:
    years = [1e3, 1e4, 1e5, 1e6, 1e7, 1e8]
    rows = [pressure_screens(REVELL_H2_NMOL_M3_YR, t) for t in years]
    x0, y0, w, h = 95, 92, 910, 380
    pmax = max(r["dissolved_equiv_pressure_atm"] for r in rows)
    parts = [
        f'<line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0+h}" stroke="#172033"/>',
        f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+h}" stroke="#172033"/>',
    ]
    for i, t in enumerate(years):
        x = x0 + i / (len(years) - 1) * w
        parts.append(f'<line x1="{x}" y1="{y0+h}" x2="{x}" y2="{y0+h+7}" stroke="#172033"/>')
        parts.append(f'<text x="{x}" y="{y0+h+28}" text-anchor="middle" font-size="12" fill="#475569">1e{int(math.log10(t))}</text>')
    for tick in range(5):
        val = pmax * tick / 4
        yy = y0 + h - h * tick / 4
        parts.append(f'<line x1="{x0-6}" y1="{yy}" x2="{x0+w}" y2="{yy}" stroke="#e2e8f0"/>')
        parts.append(f'<text x="30" y="{yy+5}" font-size="12" fill="#475569">{val:.1f}</text>')
    dissolved_points = []
    gas_points = []
    for i, r in enumerate(rows):
        x = x0 + i / (len(rows) - 1) * w
        yd = y0 + h - h * r["dissolved_equiv_pressure_atm"] / pmax
        yg = y0 + h - h * r["closed_gas_pressure_bar"] / pmax
        dissolved_points.append((x, yd))
        gas_points.append((x, yg))
    parts.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in dissolved_points)}" fill="none" stroke="#7c2d12" stroke-width="3"/>')
    parts.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in gas_points)}" fill="none" stroke="#0369a1" stroke-width="3"/>')
    for x, y in dissolved_points:
        parts.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#ea580c"/>')
    for x, y in gas_points:
        parts.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#0284c7"/>')
    parts.append('<rect x="704" y="90" width="390" height="78" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>')
    parts.append('<line x1="728" y1="115" x2="758" y2="115" stroke="#7c2d12" stroke-width="3"/>')
    parts.append('<text x="770" y="120" font-size="13" fill="#172033">Dissolved-equilibrium P_H2, atm</text>')
    parts.append('<line x1="728" y1="145" x2="758" y2="145" stroke="#0369a1" stroke-width="3"/>')
    parts.append('<text x="770" y="150" font-size="13" fill="#172033">Closed gas-volume pressure, bar</text>')
    parts.append('<text x="96" y="530" font-size="14" fill="#475569">Closed-system screen uses phi_conn=0.45%; real systems also include diffusion, fracture flow, microbial and mineral sinks.</text>')
    return svg_base("Closed-system H2 accumulation screen from host-rock radiolysis", "\n  ".join(parts), height=585)


def reaction_network_svg() -> str:
    nodes = [
        ("U-Th-K minerals", 72, 110, "#fef3c7"),
        ("radiogenic energy", 302, 110, "#dbeafe"),
        ("water radiolysis", 532, 110, "#e0f2fe"),
        ("H2 + oxidants", 762, 110, "#dcfce7"),
        ("microbial energy", 972, 70, "#fef3c7"),
        ("sulfate / sulfide", 972, 155, "#fee2e2"),
        ("Cu corrosion", 302, 305, "#fee2e2"),
        ("bentonite evolution", 532, 305, "#f8fafc"),
        ("radionuclide transport", 762, 305, "#ede9fe"),
    ]
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (5, 6), (3, 6), (6, 7), (7, 8), (3, 8), (5, 8)
    ]
    parts = [
        '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#475569"/></marker></defs>'
    ]
    for a, b in edges:
        x1, y1 = nodes[a][1] + 75, nodes[a][2] + 28
        x2, y2 = nodes[b][1], nodes[b][2] + 28
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>')
    for label, x, y, color in nodes:
        parts.append(f'<rect x="{x}" y="{y}" width="150" height="56" rx="7" fill="{color}" stroke="#334155" stroke-width="1.3"/>')
        for i, line in enumerate(wrap_text(label, 17)[:2]):
            parts.append(f'<text x="{x+75}" y="{y+24+i*17}" text-anchor="middle" font-size="13" fill="#172033">{escape(line)}</text>')
    parts.append('<text x="72" y="505" font-size="14" fill="#475569">The network is a screening map: arrows indicate process coupling, not a validated kinetic model.</text>')
    return svg_base("Safety-relevant reaction pathway map", "\n  ".join(parts), height=560)


def wrap_text(text: str, width: int) -> list[str]:
    words = text.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= width:
            current = (current + " " + word).strip()
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    header = "| " + " | ".join(columns) + " |"
    sep = "| " + " | ".join(["---"] * len(columns)) + " |"
    lines = [header, sep]
    for row in rows:
        vals = []
        for col in columns:
            val = row.get(col, "")
            if isinstance(val, float):
                vals.append(fmt(val))
            else:
                vals.append(str(val).replace("|", "/"))
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)


def clean_markdown(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if line.startswith("        "):
            lines.append(line[8:])
        else:
            lines.append(line)
    return "\n".join(lines).strip() + "\n"


def write_figures(rows: list[dict[str, object]]) -> None:
    (FIGURES / "fig01_radioelements_heat_h2.svg").write_text(bar_chart(rows), encoding="utf-8")
    ref = next(r for r in rows if r["unit"] == "Revell borehole mean")
    (FIGURES / "fig02_energy_partition_attenuation.svg").write_text(energy_partition_svg(ref), encoding="utf-8")
    (FIGURES / "fig03_groundwater_depth_framework.svg").write_text(depth_framework_svg(), encoding="utf-8")
    (FIGURES / "fig04_h2_closed_system_pressure.svg").write_text(gas_pressure_svg(), encoding="utf-8")
    (FIGURES / "fig05_thmc_reaction_network.svg").write_text(reaction_network_svg(), encoding="utf-8")


def write_models() -> None:
    (MODELS / "revell_phreeqc_screening_template.phr").write_text(
        dedent(
            r"""
            TITLE Revell Batholith groundwater-radiolysis screening template
            # Purpose:
            #   Placeholder PHREEQC structure for shallow, mixed and deep Revell groundwater end-members.
            #   Replace every FIXME value with measured sample chemistry before execution.
            # Database:
            #   Use phreeqc.dat for simple carbonate/redox screening or llnl.dat/ThermoChimie-style
            #   databases after uranium/copper/sulfide species are audited.

            SOLUTION 1 Shallow_Ca_HCO3_placeholder
              temp      FIXME
              pH        FIXME charge
              pe        FIXME
              units     mg/L
              Ca        FIXME
              Na        FIXME
              K         FIXME
              Mg        FIXME
              Cl        FIXME
              S(6)      FIXME as SO4
              Alkalinity FIXME as HCO3
              O(0)      FIXME

            SOLUTION 2 Deep_Ca_Na_Cl_placeholder
              temp      FIXME
              pH        FIXME charge
              pe        FIXME
              units     mg/L
              Ca        FIXME
              Na        FIXME
              K         FIXME
              Mg        FIXME
              Cl        FIXME
              S(6)      FIXME as SO4
              Alkalinity FIXME as HCO3
              Fe        FIXME
              U         FIXME

            GAS_PHASE 1 H2_screen
              -fixed_pressure
              -pressure FIXME
              H2(g) FIXME

            SELECTED_OUTPUT 1
              -file revell_selected_output.csv
              -pH true
              -pe true
              -ionic_strength true
              -saturation_indices Calcite Gypsum Pyrite FeS
              -molalities H2 UO2+2 UO2CO3 UO2(CO3)2-2 UO2(CO3)3-4 HS- SO4-2
            END
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )
    write_json(
        MODELS / "comsol_thmc_variable_map.json",
        {
            "status": "model-design-only",
            "state_variables": ["T", "p_l", "S_l", "sigma_eff", "phi", "k", "pH", "Eh", "Cl", "SO4", "H2", "U_aq", "p_g"],
            "physics": {
                "heat_transfer": ["radiogenic heat", "waste heat boundary if repository model is added"],
                "darcy_fracture_flow": ["matrix permeability", "fracture transmissivity", "salinity-dependent density optional"],
                "solid_mechanics": ["effective stress", "fracture aperture", "bentonite swelling if near-field is added"],
                "transport_reactions": ["diffusion/advection", "radiolysis source", "sulfate reduction", "sorption/decay"],
            },
            "required_calibration_data": ["sample-level chemistry", "fracture transmissivity", "diffusion coefficients", "microbial rates", "corrosion rates", "Kd/surface complexation constants"],
        },
    )
    write_json(
        MODELS / "pinn_training_spec.json",
        {
            "status": "loss-function-specification-only",
            "inputs": ["x", "y", "z", "t", "lithology", "fracture_indicator"],
            "outputs": ["T", "head", "Cl", "SO4", "H2", "pH", "Eh", "radionuclide_concentration"],
            "physics_losses": ["heat equation residual", "groundwater flow residual", "reactive-transport residual", "decay-sorption residual", "nonnegative concentration constraint"],
            "data_losses": ["borehole temperature", "water chemistry samples", "packer tests", "lab diffusion/sorption tests"],
            "warning": "Do not train or claim prediction without measured sample tables and train/test split.",
        },
    )


def paper_markdown(rows: list[dict[str, object]]) -> str:
    ref = next(r for r in rows if r["unit"] == "Revell borehole mean")
    attenuation = ref["effective_attenuation_fraction"]
    energy_flux = REVELL_H2_NMOL_M3_YR * 1e-9 * 38_000.0
    gas_1myr = pressure_screens(REVELL_H2_NMOL_M3_YR, 1e6)
    gas_10myr = pressure_screens(REVELL_H2_NMOL_M3_YR, 1e7)
    source_table = markdown_table(
        [
            {"source": s["id"], "year": s["year"], "use": s["used_for"], "url": s["url"]}
            for s in SOURCES
        ],
        ["source", "year", "use", "url"],
    )
    lith_table = markdown_table(
        rows,
        ["unit", "K_wt_pct_mean", "U_ppm_mean", "Th_ppm_mean", "heat_microW_m3", "h2_calibrated_nmol_m3_yr", "effective_attenuation_fraction"],
    )
    scenario_table = markdown_table(SCENARIOS, ["scenario", "dominant_controls", "expected_result", "computed_status", "alignment"])
    return clean_markdown(dedent(
        f"""
        # Revell Batholith 地下水化学、放射性辐解产氢与深地质处置库长期安全性的耦合分析

        **论文类型**：综述-方法学论文 / THMC 反应路径框架。  
        **研究边界**：本文不评价 Revell Batholith 处置库是否安全，也不构成监管安全案例、工程认证或选址结论；本文只把公开 Revell 勘探资料、公开 U-Th-K/热产率数据与公开辐解产氢结果组织成可复核的地球化学-THMC 分析框架。  
        **数据状态**：原始 PDF 和源链接保存在 `sources/`；二次整理数据保存在 `data/`；计算与图件由 `scripts/build_revell_radiolysis_thmc_package.py` 生成。

        ## 摘要

        Revell Batholith 是加拿大安大略省西北部一个以花岗质-英云闪长质结晶岩为主的区域性岩体，也是加拿大深地质处置库研究中反复讨论的候选结晶岩体系之一。与把场址直接简化为工程处置空间不同，本文将其视为一个长期演化的深部水-岩-气-微生物反应系统：低孔隙度、低渗透率岩石中的 U-Th-K 矿物持续产生放射性热和电离能量，孔隙/裂隙水在该能量场中发生水辐解，生成 H2、氧化剂和可能的硫酸盐通量；这些组分又会影响微生物代谢、氧化还原缓冲、铜容器腐蚀、膨润土缓冲材料演化以及核素迁移。

        本文基于公开 NWMO Revell 报告、Revell THMC/热学论文、Revell 辐解论文和 PHREEQC 官方文档，建立了三个层级的分析：第一，整理 Revell 的岩性、孔隙度、水化学分带、导水率与 U-Th-K 数据；第二，从放射性衰变、热产率、水辐解 G 值、H2 质量守恒、硫酸盐还原能量学和气体压力筛选公式出发，推导长期 H2 生成与闭合孔隙积累的数量级；第三，把 H2、硫酸盐、微生物、腐蚀、膨润土和核素迁移纳入 THMC 状态变量与反应网络。计算显示，Revell borehole mean 的公开 U-Th-K 数据对应热产率约 ${ref["heat_microW_m3"]:.2f}\\ \\mu\\mathrm{{W}}\\ \\mathrm{{m}}^{{-3}}$；如果把全部放射性热能直接沉积到水中，H2 会被高估到 ${ref["h2_all_energy_nmol_m3_yr"]:.1f}\\ \\mathrm{{nmol}}\\ \\mathrm{{m}}^{{-3}}\\ \\mathrm{{yr}}^{{-1}}$。与公开 Revell 辐解结果 $1.6\\ \\mathrm{{nmol}}\\ \\mathrm{{m}}^{{-3}}\\ \\mathrm{{yr}}^{{-1}}$ 对齐时，等效水可达能量分数约为 ${attenuation:.2e}$，说明低连通孔隙度和矿物-水几何关系是源项解释的关键。封闭孔隙筛选表明，在没有扩散、微生物和矿物消耗的极端条件下，$10^6$ 年可积累约 {gas_1myr["h2_mmol_m3_rock"]:.2f} mmol H2 m-3 rock；但年度通量很小，安全相关风险主要取决于是否存在闭合滞留、气体迁移门槛以及工程近场腐蚀 H2 的叠加。

        **最终观点**：Revell Batholith 的长期安全评价不应把放射性辐解 H2 简化为“有/无风险”的单因子判断。更严谨的表述是：宿主岩 U-Th-K 辐解提供了可持续但低通量的深部还原性电子供体；其安全意义由水可达能量分数、裂隙-基质连通性、硫/铁矿物反应、微生物消耗、膨润土气体阈值、容器腐蚀 H2 与核素迁移参数共同决定。现有公开数据足以支持一个 L1-L2 级的方法学框架和筛选计算，但不足以支持站址级定量安全结论；下一步必须进入样品级 PHREEQC 物种计算、裂隙-基质反应输运和场地校准。

        **关键词**：Revell Batholith；深地质处置库；地下水化学；水辐解；U-Th-K；H2；硫酸盐；微生物；铜腐蚀；膨润土；THMC；PHREEQC。

        ## 1. 引言

        结晶岩深地质处置库的长期安全性通常依赖多重屏障：废物形态、金属容器、膨润土缓冲层、封堵材料和低渗透围岩。对 Revell Batholith 这样的花岗质结晶岩体系而言，围岩不只是力学稳定的被动介质，而是长期地球化学能量和反应边界的来源。U、Th、K 衰变释放的能量一部分以热形式表现为地温梯度和岩石热产率，一部分通过电离辐射在矿物-水界面附近驱动水辐解。即使源项很小，百万年至千万年尺度也可能在低通量环境中塑造 H2、氧化剂、硫酸盐、硫化物和氧化还原边界。

        本文围绕三个问题展开：

        1. Revell Batholith 地下水的主要化学特征、盐度分层、氧化还原状态和水岩作用路径是什么？
        2. 围岩 U-Th-K 衰变在长期尺度上可能产生多少 H2，这些 H2 是更可能被矿物/微生物消耗，还是形成气体压力风险？
        3. 上述过程应如何进入 DGR 的 THMC 安全评价框架，并影响核素释放、迁移与封闭后风险判断？

        ## 2. 数据源、证据等级与可复现性

        本文使用的公开来源如下。所有数值均作为二次整理数据进入 `data/`，不把未解析的 PDF 图件当作样品级数据库。

        {source_table}

        **证据等级**：

        - A 级：公开报告或论文中直接给出的数值，如 U、Th、K、热产率、孔隙度、导水率量级、H2 生成率。
        - B 级：公开报告中的概念性或图示性趋势，如浅部 Ca-HCO3 水、深部 Ca-Na-Cl-HCO3/Cl 型水、盐度随深度升高。
        - C 级：本文为了建立模型路径而进行的推导、筛选计算或情景假设。

        GeoMine MCP 在本轮用于 AOI 标准化与数据源发现，但该 MCP 版本未执行实时目录抓取；因此本文把 MCP 结果列为来源发现与工作流 provenance，而不是站址测量数据。

        ## 3. Revell Batholith 的岩性与地下水化学框架

        ### 3.1 岩性与 U-Th-K 约束

        Revell 区域公开地质资料显示，研究对象以花岗闪长岩、英云闪长岩和局部花岗岩为主。不同岩性的 U-Th-K 差异决定了热产率和辐解源项的一阶空间差异。由公开 U-Th-K 数据计算得到的热产率与校准 H2 源项如下。

        {lith_table}

        ![U-Th-K heat and H2](figures/fig01_radioelements_heat_h2.svg)

        ### 3.2 孔隙度、导水率与水化学分带

        公开 Revell 更新资料给出结晶岩连通孔隙度约 0.45%、总孔隙度约 1.32%。这一数量级对辐解和输运有两重意义：第一，只有非常有限的水体积直接参与水辐解和溶解 H2 储存；第二，若裂隙连通性弱，扩散控制会放大长期滞留效应。水化学框架可概括为浅部补给水、过渡混合水、处置深度水和深部盐水端元。公开资料足以支持“盐度随深度升高、处置深度受深部裂隙水影响”的框架，但本文没有解析样品级 Cl、Br、SO4、Fe、U、Eh 或 pH 表，因此不宣称完成站址级 PHREEQC 物种计算。

        ![Groundwater depth framework](figures/fig03_groundwater_depth_framework.svg)

        ## 4. 理论框架与公式推导

        ### 4.1 放射性衰变、活度与热产率

        对任一放射性核素 $i$，原子数和活度为：

        $$
        N_i(t)=N_{{i,0}}e^{{-\\lambda_i t}},\\qquad A_i(t)=\\lambda_i N_i(t)
        $$

        若以岩石体积为基准，放射性热功率密度可写成：

        $$
        Q_h=\\sum_i A_i E_i \\eta_i
        $$

        其中 $E_i$ 是每次衰变释放能量，$\\eta_i$ 是沉积为局部热/电离能的比例。地球化学中常用的 U-Th-K 岩石热产率经验式为：

        $$
        A_h=10^{{-2}}\\rho\\left(9.52C_U+2.56C_{{Th}}+3.48C_K\\right)
        $$

        其中 $A_h$ 单位为 $\\mu\\mathrm{{W}}\\ \\mathrm{{m}}^{{-3}}$，$\\rho$ 单位为 $\\mathrm{{g}}\\ \\mathrm{{cm}}^{{-3}}$，$C_U$ 与 $C_{{Th}}$ 单位为 ppm，$C_K$ 单位为 wt%。将 Revell borehole mean 的公开值 $C_U=2.081$ ppm、$C_{{Th}}=5.247$ ppm、$C_K=2.079$ wt%、$\\rho=2.66$ 代入，有：

        $$
        A_h=10^{{-2}}\\times2.66\\times(9.52\\times2.081+2.56\\times5.247+3.48\\times2.079)
        \\approx {ref["heat_microW_m3"]:.2f}\\ \\mu\\mathrm{{W}}\\ \\mathrm{{m}}^{{-3}}
        $$

        该结果与公开 Revell 热产率约 $1.08\\ \\mu\\mathrm{{W}}\\ \\mathrm{{m}}^{{-3}}$ 对齐。

        ### 4.2 水辐解 H2 源项

        水辐解的产额可由 G 值表示。若 $G_{{H_2}}=0.45$ molecule/100 eV，则：

        $$
        G_{{H_2}}=0.45\\times0.10364\\times10^{{-6}}
        ={G_H2_MOL_J:.3e}\\ \\mathrm{{mol}}\\ \\mathrm{{J}}^{{-1}}
        $$

        若把岩石热产率全部视作水吸收能量，则单位体积岩石每年的 H2 生成率为：

        $$
        R_{{H_2}}^{{all}}=G_{{H_2}}A_h10^{{-6}}t_y
        $$

        对 Revell borehole mean：

        $$
        R_{{H_2}}^{{all}}={G_H2_MOL_J:.3e}\\times {ref["heat_microW_m3"]:.2f}\\times10^{{-6}}\\times{SECONDS_PER_YEAR:.0f}
        \\approx {ref["h2_all_energy_nmol_m3_yr"]:.1f}\\ \\mathrm{{nmol}}\\ \\mathrm{{m}}^{{-3}}\\ \\mathrm{{yr}}^{{-1}}
        $$

        但公开 Revell 辐解模型给出的代表性结果约为：

        $$
        R_{{H_2}}^{{Revell}}=1.6\\ \\mathrm{{nmol}}\\ \\mathrm{{m}}^{{-3}}\\ \\mathrm{{rock}}\\ \\mathrm{{yr}}^{{-1}}
        $$

        因而定义水可达能量分数：

        $$
        \\epsilon_w=\\frac{{R_{{H_2}}^{{Revell}}}}{{R_{{H_2}}^{{all}}}}\\approx {attenuation:.2e}
        $$

        该值不是常数，而是把公开 Revell H2 源项与 U-Th-K 热产率对齐后得到的有效几何/能量分配因子。它代表低孔隙度、矿物-水接触面积、alpha/beta/gamma 能量沉积路径和孔隙水可达性的综合效果。

        ![Energy partition](figures/fig02_energy_partition_attenuation.svg)

        ### 4.3 H2 质量守恒、扩散与裂隙输运

        H2 在裂隙-基质系统中的质量守恒可写为：

        $$
        \\frac{{\\partial(\\phi C_{{H_2}})}}{{\\partial t}}
        =\\nabla\\cdot(D_e\\nabla C_{{H_2}})
        -\\nabla\\cdot(\\mathbf{{q}}C_{{H_2}})
        +R_{{H_2}}^{{rad}}-R_{{bio}}-R_{{min}}-R_{{gas}}
        $$

        其中 $R_{{H_2}}^{{rad}}$ 是辐解源项，$R_{{bio}}$ 是微生物消耗，$R_{{min}}$ 是矿物/氧化剂反应消耗，$R_{{gas}}$ 是气相逸出或两相流损失。Revell 的关键不是源项是否存在，而是上述源-汇项的相对大小。

        ### 4.4 硫酸盐生成与微生物能量

        辐解氧化剂可把硫化物氧化为硫酸盐。以黄铁矿为例：

        $$
        \\mathrm{{FeS_2}}+3.75\\mathrm{{O_2}}+3.5\\mathrm{{H_2O}}
        \\rightarrow \\mathrm{{Fe(OH)_3}}+2\\mathrm{{SO_4^{{2-}}}}+4\\mathrm{{H^+}}
        $$

        若 H2 与硫酸盐还原菌相耦合，则反应可写为：

        $$
        4\\mathrm{{H_2}}+\\mathrm{{SO_4^{{2-}}}}+\\mathrm{{H^+}}
        \\rightarrow \\mathrm{{HS^-}}+4\\mathrm{{H_2O}}
        $$

        采用保守的能量数量级 $|\\Delta G|\\approx38\\ \\mathrm{{kJ}}\\ \\mathrm{{mol}}^{{-1}}\\ H_2$，Revell 宿主岩辐解 H2 的能量通量约为：

        $$
        \\Phi_G=1.6\\times10^{{-9}}\\times 3.8\\times10^4
        \\approx {energy_flux:.2e}\\ \\mathrm{{J}}\\ \\mathrm{{m}}^{{-3}}\\ \\mathrm{{yr}}^{{-1}}
        $$

        这说明宿主岩辐解可作为持续电子供体，但在年度尺度上能量通量很低；微生物过程是否显著，更可能受局部裂隙水停留时间、硫酸盐供应、表面积和群落阈值控制。

        ### 4.5 气体压力与溶解度筛选

        在极端封闭条件下，若 H2 完全以气体占据连通孔隙体积 $V_g=\\phi V_{{rock}}$，压力可用理想气体式筛选：

        $$
        P=\\frac{{nRT}}{{V_g}}
        $$

        若 H2 以溶解态与水相平衡，则：

        $$
        C_{{H_2}}=k_HP_{{H_2}}
        $$

        以 $\\phi=0.45\\%$、$T=283.15\\ \\mathrm{{K}}$、$k_H=7.8\\times10^{{-4}}\\ \\mathrm{{mol}}\\ \\mathrm{{L}}^{{-1}}\\ \\mathrm{{atm}}^{{-1}}$ 进行筛选，$10^6$ 年闭合系统可得到约 {gas_1myr["closed_gas_pressure_bar"]:.3f} bar 的气相体积压力或 {gas_1myr["dissolved_equiv_pressure_atm"]:.2f} atm 的溶解平衡分压；$10^7$ 年对应 {gas_10myr["closed_gas_pressure_bar"]:.3f} bar 或 {gas_10myr["dissolved_equiv_pressure_atm"]:.2f} atm。该结果不能直接转化为处置库压力结论，因为实际系统存在扩散、裂隙流、矿物/微生物消耗、两相流和工程近场 H2 叠加。

        ![Closed-system pressure](figures/fig04_h2_closed_system_pressure.svg)

        ### 4.6 核素迁移与 THMC 状态变量

        对可溶核素的筛选输运方程可写为：

        $$
        R_f\\frac{{\\partial C}}{{\\partial t}}=
        D_e\\nabla^2C-\\mathbf{{v}}\\cdot\\nabla C-\\lambda C+S
        $$

        $$
        R_f=1+\\frac{{\\rho_bK_d}}{{\\phi}}
        $$

        其中 $K_d$ 或表面络合模型由 pH、Eh、离子强度、碳酸盐、硫酸盐、Fe/Mn 氧化物和黏土交换位点控制。THMC 模型的最小状态向量可写为：

        $$
        \\mathbf{{y}}=[T,p_l,S_l,\\sigma',\\phi,k,pH,Eh,\\mathbf{{c}},C_{{H_2}},p_g]
        $$

        ![THMC reaction network](figures/fig05_thmc_reaction_network.svg)

        ## 5. 数据分析结果与预期对齐

        ### 5.1 U-Th-K 热产率与 H2 源项

        花岗岩端元的 U、Th、K 明显高于英云闪长岩和闪长质端元，因此热产率与校准 H2 源项最高。Revell borehole mean 的热产率与公开热学论文对齐，说明本文的 U-Th-K 热模型没有数量级偏差。更重要的是，直接把热产率换算为水辐解 H2 会高估约三阶数量级；只有引入低孔隙度、低水可达性和矿物-水界面效应，才能与公开 Revell 辐解结果对齐。

        ### 5.2 地下水化学与安全相关过程

        公开资料支持以下判断：浅部水以 Ca-HCO3 型补给水为主；深部水受 Ca-Na-Cl-HCO3/Cl 型端元影响，盐度随深度增加；处置深度位于浅部补给与深部盐水影响之间。该框架符合结晶岩 DGR 的一般预期：低渗透基质提供扩散屏障，裂隙控制少量快速通道，高盐度和还原性影响金属腐蚀、膨润土交换/膨胀和核素络合。由于本文没有解析样品级 Cl-Br、SO4、Fe、U、Eh、pH 数据，所有 PHREEQC 计算仍停留在模板层级。

        ### 5.3 H2、硫酸盐与微生物

        公开 Revell 辐解论文指出 Revell H2 生成率远低于硫化物丰富的 Kidd Creek 体系，硫酸盐生成更低多个数量级。本文计算表明，H2 年度能量通量仅约 ${energy_flux:.2e}\\ \\mathrm{{J}}\\ \\mathrm{{m}}^{{-3}}\\ \\mathrm{{yr}}^{{-1}}$，因此宿主岩辐解 H2 更适合作为“长期低通量电子供体”而非“短期强能源”。如果局部裂隙长期封闭，则百万年尺度的累积可能有地球化学意义；如果裂隙连通或微生物/矿物汇强，则 H2 将表现为红氧缓冲通量而不是气压问题。

        ### 5.4 情景矩阵

        {scenario_table}

        ## 6. PHREEQC、COMSOL 与 PINN 模型化路径

        ### 6.1 PHREEQC

        `models/revell_phreeqc_screening_template.phr` 给出了浅部 Ca-HCO3 端元和深部 Ca-Na-Cl 端元的占位输入结构。执行前必须填入样品级温度、pH、pe/Eh、Ca、Na、K、Mg、Cl、SO4、碱度、Fe、U 和气相 H2。优先输出应包括离子强度、饱和指数、H2、U-碳酸盐物种、HS- 与 SO4 物种。没有这些样品级输入，不应报告“Revell PHREEQC 结果”。

        ### 6.2 COMSOL / OGS / PFLOTRAN

        连续介质 THMC 可使用 COMSOL 或 OpenGeoSys 建立热-流-力-化耦合；场尺度反应输运可由 PFLOTRAN 或 PhreeqcRM-耦合框架承担。最小控制方程组包括热传导/对流、达西流、有效应力、孔隙率-渗透率更新、多组分反应输运、辐解源项和气相压力项。本文将变量映射写入 `models/comsol_thmc_variable_map.json`。

        ### 6.3 PINN

        PINN 适合在已有样品和物理方程约束下构建代理模型，而不适合作为无数据条件下的事实生成器。`models/pinn_training_spec.json` 只定义输入、输出和物理残差项；训练必须等待样品级水化学、温度、导水率、扩散/吸附和腐蚀数据。

        ## 7. 讨论

        ### 7.1 放射性辐解 H2 的双重角色

        Revell 宿主岩 H2 不是一个简单的风险源。低通量 H2 可维持深部还原环境，有利于降低某些氧化态核素的迁移性；但 H2 也可能作为硫酸盐还原菌电子供体，间接形成硫化物并影响铜腐蚀。其影响方向取决于 sulfate/sulfide 供应、微生物活性、裂隙连通性和近场工程材料。

        ### 7.2 硫酸盐与硫化物不是同一个安全指标

        公开资料中低 sulphide 检测边界支持“即时硫化物腐蚀压力较低”的解释，但不能排除长期 sulfate reduction 情景。安全评价中应分别追踪 sulfate 生成、sulfate 输入、microbial sulfate reduction、HS- 扩散和铜表面反应，而不是只用一个总硫指标替代。

        ### 7.3 气体压力风险由源项、储存和输运共同决定

        本文的闭合孔隙筛选说明，年度 H2 源项很低，但百万年至千万年封闭滞留可达到 mM 级溶解浓度或可观的分压筛选值。实际 DGR 风险必须与扩散、裂隙排散、两相流、膨润土气体进入压力以及工程近场腐蚀 H2 一起求解。宿主岩辐解 H2 很可能不是近场最大 H2 源，但它是深部背景红氧和微生物能量边界。

        ### 7.4 核素迁移的关键耦合

        对 U、Tc、Se、I、Cs、Sr、Ra、Np、Pu 等核素而言，pH/Eh、碳酸盐、硫酸盐、Fe/Mn 氧化物、胶体和黏土交换位点共同决定迁移性。Revell 的深部 Cl-rich 端元可能改变离子强度、膨润土交换和金属络合；还原性 H2 背景可能降低某些多价元素迁移性，但对保守阴离子和弱吸附核素帮助有限。

        ## 8. 局限性

        1. 本文未解析 NWMO 原始水样表，因此不报告样品级 pH、Eh、Cl-Br、SO4、Fe、U 物种结果。
        2. H2 源项采用公开 Revell 辐解结果进行对齐；没有重建该论文的完整 Monte Carlo 几何模型。
        3. 硫酸盐生成只给出反应路径和相对解释；绝对 sulfate rate 需要源论文完整表格或补充资料。
        4. 气体压力筛选是假设性闭合系统，不代表裂隙网络或工程近场两相流结果。
        5. 铜腐蚀、膨润土演化和核素 Kd/表面络合参数未校准；本文只给出模型路径。

        ## 9. 结论与论文最终观点

        1. Revell Batholith 可被理解为低孔隙度、低渗透率、U-Th-K 低至中等含量的结晶岩水-岩-气-微生物系统；其地下水化学随深度从浅部 Ca-HCO3 补给水向深部 Ca-Na-Cl-HCO3/Cl 端元演化。
        2. U-Th-K 热产率公式能够复现公开 borehole mean 热产率；但热产率到 H2 生成之间必须引入水可达能量分数。Revell 的公开 H2 结果对应约 ${attenuation:.2e}$ 的有效分配比例，证明“低孔隙度几何衰减”是解释辐解源项的核心。
        3. 宿主岩辐解 H2 的年度通量很低，但长期封闭条件下可积累到地球化学上有意义的浓度；它对安全评价的关键作用不是单独形成风险，而是改变红氧、微生物、硫循环和近场腐蚀边界。
        4. 硫酸盐/硫化物链条必须作为独立反应路径进入 THMC 模型。低 sulphide 检测边界降低 immediate corrosion concern，但不等于长期 sulfate reduction 风险为零。
        5. 最终安全相关模型应采用 PHREEQC 进行端元物种与反应网络筛选，用 PFLOTRAN/OGS/COMSOL 描述裂隙-基质反应输运和 THMC 反馈，再用 PINN 作为经样品数据约束的代理模型。没有样品级数据和模型执行结果时，结论应停留在方法学与筛选层级。

        **论文最终观点**：Revell Batholith 的深地质处置库长期安全评价中，放射性辐解产氢应被纳入安全案例，但不应被孤立夸大。它是一个低通量、长寿命、强耦合的背景过程：在还原缓冲方面可能有正面作用，在硫酸盐还原、气体积累和腐蚀方面具有条件性负面作用。最严谨的评价路径是把 H2 作为 THMC 状态变量和反应源项，与地下水盐度、裂隙连通性、硫循环、微生物、膨润土气体阈值和核素迁移共同求解。

        ## 参考文献

        - NWMO. 2022. *Confidence in Safety: Revell Site*. URL: https://www.nwmo.ca/-/media/Reports-MASTER/Technical-reports/NWMO-TR-2022-14-Confidence-in-Safety-Revell-Site-2022-03.ashx?rev=7e56d8a81d714d70a8d6004b1c2cce49&sc_lang=en
        - NWMO. 2023. *Confidence in Safety: Revell Site - 2023 Update*. URL: https://www.nwmo.ca/-/media/Reports-MASTER/Technical-reports/NWMO-TR-2023-07-Confidence-in-Safety---Revell-Site---2023-Update.ashx?rev=6180a2f1bd95498f96d4dec51c8e406c&sc_lang=en
        - NWMO. 2017. *Phase 2 Geological Mapping: Township of Ignace and Area, Ontario*. URL: https://www.nwmo.ca/-/media/Reports---Reports/APM-REP-01332-0225-Phase-2-Geological-Mapping-Township-of-Ignace-and-Area-11-17.ashx?hash=2B490F4795C7E3BB59C39AB3EAB296CF&rev=a36ce8c7c16e4020b5896e539fdce61e&sc_lang=en
        - Villamizar et al. 2024. *Developing a coupled thermal-hydraulic-mechanical-chemical model for the Revell Batholith, Ontario, Canada*. ARMA. URL: https://armarocks.net/papers/379.pdf
        - Higgins et al. 2025. *Natural H2 and Sulfate Production via Radiolysis in Low Porosity and Permeability Crystalline Rocks*. ACS Earth and Space Chemistry. DOI: https://doi.org/10.1021/acsearthspacechem.5c00072
        - USGS. *PHREEQC Version 3 documentation*. URL: https://water.usgs.gov/water-resources/software/PHREEQC/documentation/phreeqc3-html/phreeqc3.htm

        ## 附录 A：符号与单位

        | 符号 | 含义 | 单位 |
        |---|---|---|
        | $A_h$ | 放射性热产率 | $\\mu\\mathrm{{W}}\\ \\mathrm{{m}}^{{-3}}$ |
        | $C_U,C_{{Th}},C_K$ | U、Th、K 含量 | ppm, ppm, wt% |
        | $G_{{H_2}}$ | H2 辐解 G 值 | mol J-1 |
        | $\\epsilon_w$ | 水可达能量分数 | dimensionless |
        | $R_{{H_2}}$ | H2 生成率 | mol m-3 yr-1 |
        | $\\phi$ | 孔隙度 | dimensionless |
        | $D_e$ | 有效扩散系数 | m2 s-1 |
        | $K_d$ | 分配系数 | m3 kg-1 |
        | $R_f$ | 迟滞因子 | dimensionless |
        | $p_g$ | 气相压力 | Pa or bar |

        ## 附录 B：过程文件

        - `data/lithology_radioelements.csv`
        - `data/revell_public_parameters.csv`
        - `data/derived_radiolysis_screening.csv`
        - `data/groundwater_depth_framework.csv`
        - `data/scenario_matrix.csv`
        - `data/equation_registry.csv`
        - `figures/fig01_radioelements_heat_h2.svg`
        - `figures/fig02_energy_partition_attenuation.svg`
        - `figures/fig03_groundwater_depth_framework.svg`
        - `figures/fig04_h2_closed_system_pressure.svg`
        - `figures/fig05_thmc_reaction_network.svg`
        - `models/revell_phreeqc_screening_template.phr`
        - `models/comsol_thmc_variable_map.json`
        - `models/pinn_training_spec.json`
        """
    ))


def modeling_package_markdown(rows: list[dict[str, object]]) -> str:
    planning_json = {
        "research_type": "academic_paper_generation + thmc_modeling + radiolysis_nuclear_geochemistry",
        "scenario": "nuclear_waste_repository / Revell crystalline-rock groundwater-radiolysis system",
        "coupling_level": "THMC",
        "active_processes": {"thermal": True, "hydrological": True, "mechanical": True, "chemical": True},
        "readiness_level": "L1_methods_protocol_with_screening_calculations",
        "not_claimed": ["site safety conclusion", "regulatory compliance", "validated PHREEQC/PFLOTRAN/COMSOL run"],
    }
    return clean_markdown(dedent(
        f"""
        # Revell Batholith Radiolysis-THMC Modeling Package

        ## 1. Research Objective

        Build a defensible, literature-grounded THMC framework for Revell Batholith groundwater chemistry, U-Th-K radiolysis, H2/sulfate generation, microbial energy, corrosion, bentonite evolution and radionuclide migration.

        ## 2. Scenario Classification

        - Scenario: nuclear waste repository / crystalline-rock DGR.
        - Coupling level: THMC.
        - Readiness: L1 methods protocol with screening calculations.

        ## 3. Conceptual THMC Model

        The host rock supplies low but persistent radiogenic energy. Water accessibility is constrained by low connected porosity and fracture geometry. H2 and oxidants alter redox and microbial boundary conditions. Salinity, sulfate and sulfide influence corrosion and sorption. Mechanical effects enter through fracture aperture, permeability and bentonite gas-entry/self-sealing behavior.

        ## 4. Coupling Matrix

        | From / To | Thermal | Hydrological | Mechanical | Chemical |
        |---|---|---|---|---|
        | Thermal | radiogenic heat, waste heat | viscosity/density and diffusion | thermal stress | reaction rates |
        | Hydrological | advective heat | fracture/matrix flow | pore pressure and aperture | solute delivery, gas transport |
        | Mechanical | stress-dependent heat paths | permeability/aperture | swelling, damage | reactive surface and transport pathway |
        | Chemical | redox heat negligible | precipitation/dissolution affects porosity | bentonite exchange and swelling | radiolysis, corrosion, sorption, decay |

        ## 5. Governing Equations

        See `data/equation_registry.csv` and the main paper. Required equations include U-Th-K heat production, radiolysis source term, H2 mass balance, sulfate/sulfide stoichiometry, ideal-gas/Henry pressure screen, sorption-retarded transport and THMC state variables.

        ## 6. Parameters and Data Requirements

        | Parameter group | Current status | Required next data |
        |---|---|---|
        | U-Th-K and density | public compiled values available | spatial distribution by borehole/depth |
        | Porosity/permeability | public ranges available | fracture-scale transmissivity and matrix diffusion |
        | Groundwater chemistry | public framework available | sample-level pH, Eh/pe, Cl, Br, SO4, alkalinity, Fe, U, sulfide |
        | H2/sulfate production | public Revell H2 value available | full source-paper tables, uncertainty distribution, sulfate rate |
        | Microbial kinetics | not calibrated | sulfate reducers, methanogens, maintenance-energy thresholds |
        | Corrosion and bentonite | not site calibrated | material-specific corrosion, gas-entry, swelling and diffusion data |

        ## 7. Solver Route

        1. PHREEQC: end-member speciation, saturation indices, U/carbonate/sulfide sensitivity.
        2. PFLOTRAN or OGS: fracture-matrix reactive transport with long-term H2 and radionuclide source terms.
        3. COMSOL: near-field coupled THMC with bentonite swelling/gas entry and corrosion source terms.
        4. PINN: only as a constrained surrogate after measured training/validation data exist.

        ## 8. Calibration and Validation Plan

        - Calibrate chemistry with sample-level groundwater tables.
        - Calibrate transport with packer tests, hydraulic head and tracer/diffusion experiments.
        - Calibrate radiolysis geometry with mineralogy, porosity and source-paper Monte Carlo assumptions.
        - Validate against independent borehole chemistry, temperature and microbial observations.

        ## 9. Uncertainty Plan

        Primary uncertainty lanes: water-accessible radiolysis fraction, fracture connectivity, deep-water mixing, sulfate reduction kinetics, sulfide diffusion to copper, H2 solubility under salinity/temperature, radionuclide sorption under high ionic strength.

        ## 10. Figure Plan

        Generated figures are listed in `figure_manifest.json`; the most important panels are U-Th-K heat/H2, energy-partition attenuation, groundwater depth framework, closed H2 accumulation and THMC reaction network.

        ## 11. Machine-Readable Model Spec

        ```json
        {json.dumps(planning_json, ensure_ascii=False, indent=2)}
        ```
        """
    ))


def figure_package_markdown() -> str:
    rows = [
        {"id": "fig01", "file": "figures/fig01_radioelements_heat_h2.svg", "claim": "U-Th-K differences among lithologies create first-order heat/H2 source-term variation."},
        {"id": "fig02", "file": "figures/fig02_energy_partition_attenuation.svg", "claim": "All-energy conversion overpredicts H2 unless low-porosity attenuation is included."},
        {"id": "fig03", "file": "figures/fig03_groundwater_depth_framework.svg", "claim": "Repository-depth interpretation sits between shallow recharge and deeper saline fracture-water influence."},
        {"id": "fig04", "file": "figures/fig04_h2_closed_system_pressure.svg", "claim": "H2 pressure concern depends on closed-system retention time and pore volume, not source rate alone."},
        {"id": "fig05", "file": "figures/fig05_thmc_reaction_network.svg", "claim": "H2, sulfate, microbes, corrosion, bentonite and radionuclide transport form one coupled reaction network."},
    ]
    return clean_markdown("# Figure Package\n\n" + markdown_table(rows, ["id", "file", "claim"]) + "\n")


def readme_markdown() -> str:
    return clean_markdown(dedent(
        """
        # Revell Batholith Radiolysis-THMC Paper Package

        This folder contains the reproducible GeoMine Research package for the paper:
        `Revell Batholith 地下水化学、放射性辐解产氢与深地质处置库长期安全性的耦合分析`.

        ## Main outputs

        - `Revell_Batholith_Radiolysis_THMC_Paper.zh.md` - main Chinese academic paper.
        - `Revell_Batholith_Radiolysis_THMC_Paper.zh.pdf` - PDF export when generated.
        - `revell_radiolysis_thmc_modeling_package.md` - THMC modeling package.
        - `figure_package.md` / `figure_manifest.json` - figure inventory.
        - `data/` - public extracted parameters and derived screening calculations.
        - `figures/` - generated SVG visualization results.
        - `models/` - PHREEQC, COMSOL and PINN starter specifications.
        - `sources/` - downloaded public PDF source files where accessible.
        - `mcp_provenance.md` - GeoMine MCP and source-discovery boundary notes.

        ## Status

        L1 methods protocol with screening calculations. The package does not claim a site-specific safety conclusion, raw water-sample PHREEQC result, regulatory compliance or validated THMC simulation.

        ## Rebuild

        ```bash
        python3 report/2026-05-23-revell-batholith-radiolysis-thmc/scripts/build_revell_radiolysis_thmc_package.py
        ```
        """
    ))


def mcp_provenance_markdown() -> str:
    return clean_markdown(dedent(
        """
        # MCP Provenance

        GeoMine Research skills were used in local/core mode.

        ## Tool Calls

        | Tool | Mode / status | Scientific use | Boundary |
        |---|---|---|---|
        | `mcp__geomine__.normalize_aoi` | parsed locally; no network | Preserved Revell AOI label and CRS assumption | No authoritative geocoding, polygon, NTS or distance calculation |
        | `mcp__geomine__.search_canada_geodata` | planned request; live HTTP unsupported in this MCP version | Identified Open Canada/Geo.ca, NRCan CDoGS and Ontario OGSEarth as discovery lanes | Planned catalogue request is not evidence |
        | `mcp__geomine__.search_cdogs_surveys` | planned request; no live survey parsing | Confirmed CDoGS as a possible geochemical survey lane | No sample medium, method, units or QA/QC parsed |

        ## Web / Public Source Use

        Public reports and papers were retrieved or referenced directly. Downloaded PDFs are stored in `sources/` when accessible. Extracted numerical values are curated in CSV files with source identifiers. Sample-level groundwater chemistry was not parsed, so PHREEQC artifacts remain templates rather than executed site results.
        """
    ))


def main() -> None:
    ensure_dirs()
    rows = derived_rows()
    write_csv(DATA / "lithology_radioelements.csv", LITHOLOGY)
    write_csv(DATA / "revell_public_parameters.csv", PUBLIC_PARAMETERS)
    write_csv(DATA / "derived_radiolysis_screening.csv", rows)
    write_csv(DATA / "groundwater_depth_framework.csv", HYDROCHEMISTRY)
    write_csv(DATA / "scenario_matrix.csv", SCENARIOS)
    write_csv(DATA / "equation_registry.csv", [{"id": e[0], "name": e[1], "equation": e[2], "use": e[3]} for e in EQUATIONS])
    write_json(ROOT / "Revell_Batholith_Radiolysis_THMC_Paper.sources.json", SOURCES)
    write_figures(rows)
    write_models()
    write_json(
        ROOT / "figure_manifest.json",
        [
            {"id": "fig01", "file": "figures/fig01_radioelements_heat_h2.svg"},
            {"id": "fig02", "file": "figures/fig02_energy_partition_attenuation.svg"},
            {"id": "fig03", "file": "figures/fig03_groundwater_depth_framework.svg"},
            {"id": "fig04", "file": "figures/fig04_h2_closed_system_pressure.svg"},
            {"id": "fig05", "file": "figures/fig05_thmc_reaction_network.svg"},
        ],
    )
    (ROOT / "Revell_Batholith_Radiolysis_THMC_Paper.zh.md").write_text(paper_markdown(rows), encoding="utf-8")
    (ROOT / "revell_radiolysis_thmc_modeling_package.md").write_text(modeling_package_markdown(rows), encoding="utf-8")
    (ROOT / "figure_package.md").write_text(figure_package_markdown(), encoding="utf-8")
    (ROOT / "README.md").write_text(readme_markdown(), encoding="utf-8")
    (ROOT / "mcp_provenance.md").write_text(mcp_provenance_markdown(), encoding="utf-8")
    write_json(
        ROOT / "workflow_manifest.json",
        {
            "package": "revell-batholith-radiolysis-thmc",
            "created": "2026-05-23",
            "skills": [
                "geomine-research-router-skill",
                "academic-geochemistry-paper-architect",
                "thmc-groundwater-router-skill",
                "natural-analogue-thmc-dgr-modeling-skill",
                "academic-paper-research-writer",
                "geomine-paper-pdf-export-skill",
            ],
            "status": "L1 methods protocol with screening calculations",
            "main_markdown": "Revell_Batholith_Radiolysis_THMC_Paper.zh.md",
            "data_files": [p.name for p in sorted(DATA.glob("*.csv"))],
            "figures": [p.name for p in sorted(FIGURES.glob("*.svg"))],
            "models": [p.name for p in sorted(MODELS.glob("*"))],
        },
    )


if __name__ == "__main__":
    main()
