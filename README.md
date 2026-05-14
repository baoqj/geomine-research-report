# GeoMine Research Report Index

Default language: English. For Chinese, see [README.zh-CN.md](./README.zh-CN.md).

This repository collects GeoMine Research outputs for geoscience, mining exploration, hydrogeochemistry, radiochemistry, THMC modeling, PHREEQC/PFLOTRAN workflow design, and research-method documentation. Most dated folders are self-contained research packages with Markdown papers, PDF exports, provenance notes, machine-readable summaries, data tables, figures, and local scripts.

Research boundary: these materials are for scientific exploration, screening, workflow design, and methodological reasoning. They are not investment advice, legal advice, Qualified Person opinions, NI 43-101 technical reports, resource or reserve estimates, mining feasibility studies, environmental permits, nuclear-safety conclusions, or field-validated site assessments. Claim status, regulatory conclusions, water quality, radiation dose, engineering safety, and disclosure decisions must be checked against official systems and qualified professionals.

## Current Inventory

- 18 dated research packages, ordered newest to oldest below.
- 4 top-level skill capability or methodology guides.
- Main deliverable types: Markdown papers, PDF exports, figure packages, provenance notes, JSON/CSV data products, PHREEQC/PFLOTRAN model artifacts, and local analysis scripts.
- Newly indexed since the older README: all 2026-05-12, 2026-05-13, and 2026-05-14 research packages, plus the THMC, PHREEQC, PFLOTRAN, and geochemistry paper-architecture guides.

## Directory Convention

- Date-prefixed folders are research packages: `YYYY-MM-DD-topic-slug/`.
- A mature package should include a package `README.md`, one or more main papers, PDF exports when available, `mcp_provenance.md` when tools or public sources were used, and a clear `data/`, `figures/`, `models/`, or `scripts/` layout when needed.
- Files ending in `.normalized.md` or `.normalized.pdf` are usually export-normalized versions for math, chemistry notation, Mermaid, or figure rendering.
- Top-level `GeoMine_*.md` files are capability guides and methodology documents rather than individual research papers.

## Research Packages and Papers

### 2026-05-14

#### [Wildfire and Extreme Rainfall Radionuclide Remobilization](./2026-05-14-wildfire-rainfall-radionuclide-remobilization/)

- Main papers:
  - [Wildfire_Extreme_Rainfall_Radionuclide_Remobilization_Athabasca.zh.md](./2026-05-14-wildfire-rainfall-radionuclide-remobilization/Wildfire_Extreme_Rainfall_Radionuclide_Remobilization_Athabasca.zh.md)
  - [Wildfire_Postfire_Water_Chemistry_Long_Term_Risk_Phase2.zh.md](./2026-05-14-wildfire-rainfall-radionuclide-remobilization/Wildfire_Postfire_Water_Chemistry_Long_Term_Risk_Phase2.zh.md)
- PDFs: phase-1 and phase-2 normalized PDF exports are included in the package.
- Supporting files: [figure_package.md](./2026-05-14-wildfire-rainfall-radionuclide-remobilization/figure_package.md), [mcp_provenance.md](./2026-05-14-wildfire-rainfall-radionuclide-remobilization/mcp_provenance.md), `data/`, `figures/`, `models/`, and `scripts/`.
- Focus: a public-data research framework for wildfire, extreme rainfall, first-flush chemistry, sediment secondary sources, PHREEQC sensitivity, and radionuclide remobilization around Athabasca uranium districts.
- Boundary: screening and research-design output only; not a dose assessment, site compliance judgment, or regulatory conclusion.

### 2026-05-13

#### [PFLOTRAN Tailings Uranium Radionuclide Paper](./2026-05-13-geomine-pflotran-tailings-uranium-radionuclide/)

- Main paper: [PFLOTRAN_Tailings_Uranium_Radionuclide_Paper.zh.md](./2026-05-13-geomine-pflotran-tailings-uranium-radionuclide/PFLOTRAN_Tailings_Uranium_Radionuclide_Paper.zh.md)
- Modeling package: [PFLOTRAN_Modeling_Package.md](./2026-05-13-geomine-pflotran-tailings-uranium-radionuclide/PFLOTRAN_Modeling_Package.md)
- Figure package: [PFLOTRAN_Tailings_Uranium_Figure_Package.md](./2026-05-13-geomine-pflotran-tailings-uranium-radionuclide/PFLOTRAN_Tailings_Uranium_Figure_Package.md)
- Supporting files: PFLOTRAN input template, run manifests, validation JSON, CSV screening tables, and publication figures in PNG/SVG.
- Focus: PFLOTRAN-style reactive transport package for uranium tailings seepage, sulfate, pH buffering, retardation, sensitivity ranking, and paper-ready figure generation.

#### [PHREEQC U-Ra-SO4-CO3 Groundwater Workflow](./2026-05-13-geomine-phreeqc-u-ra-so4-co3-groundwater/)

- Main paper: [u_ra_so4_co3_phreeqc_groundwater_academic_paper_zh.md](./2026-05-13-geomine-phreeqc-u-ra-so4-co3-groundwater/u_ra_so4_co3_phreeqc_groundwater_academic_paper_zh.md)
- PDFs: original and normalized PDF exports are included.
- Supporting files: `models/phreeqc/`, [workflow_manifest.json](./2026-05-13-geomine-phreeqc-u-ra-so4-co3-groundwater/workflow_manifest.json), [datasets_evidence.json](./2026-05-13-geomine-phreeqc-u-ra-so4-co3-groundwater/datasets_evidence.json), figures, scripts, and provenance.
- Focus: PHREEQC-based uranium/radium/sulfate/carbonate speciation, saturation index, geochemical control, and groundwater migration-risk screening workflow.
- Boundary: demonstrates a research chain with placeholder or synthetic endmembers where real monitored chemistry is unavailable.

#### [Fractured Rock Radionuclide Sorption, Matrix Diffusion, and Colloid THMC](./2026-05-13-geomine-fractured-rock-radionuclide-colloid-thmc/)

- Main paper: [Fractured_Rock_Radionuclide_Sorption_Diffusion_Colloid_THMC_Model.zh.md](./2026-05-13-geomine-fractured-rock-radionuclide-colloid-thmc/Fractured_Rock_Radionuclide_Sorption_Diffusion_Colloid_THMC_Model.zh.md)
- PDFs: original and normalized PDF exports are included.
- Supporting files: parameter/source CSVs, screening results, summary JSON, SVG figures, scripts, and provenance.
- Focus: conceptual THMC screening of radionuclide mobility in fractured crystalline rock, including sorption, matrix diffusion, colloid association, and scenario ranking.

#### [DGR Copper-Bentonite-Crystalline Rock THMC Model](./2026-05-13-geomine-dgr-copper-bentonite-thmc/)

- Main paper: [DGR_Copper_Bentonite_Crystalline_Rock_THMC_Model.zh.md](./2026-05-13-geomine-dgr-copper-bentonite-thmc/DGR_Copper_Bentonite_Crystalline_Rock_THMC_Model.zh.md)
- PDFs: original and normalized PDF exports are included.
- Supporting files: THMC parameter/source tables, screening outputs, SVG figure set, scripts, and provenance.
- Focus: copper canister, bentonite buffer, crystalline host rock, groundwater ingress, thermal decay, salinity, swelling/permeability, sulfide corrosion, hydrogen generation, and radionuclide diffusion.

#### [Tailings Seepage THMC Groundwater Paper](./2026-05-13-geomine-tailings-seepage-thmc-groundwater/)

- Main paper: [Tailings_Seepage_THMC_Groundwater_Paper.zh.md](./2026-05-13-geomine-tailings-seepage-thmc-groundwater/Tailings_Seepage_THMC_Groundwater_Paper.zh.md)
- PDF: [Tailings_Seepage_THMC_Groundwater_Paper.pdf](./2026-05-13-geomine-tailings-seepage-thmc-groundwater/Tailings_Seepage_THMC_Groundwater_Paper.pdf)
- Supporting files: package README and MCP provenance notes.
- Focus: sulfide tailings oxidation, acid generation, carbonate neutralization, secondary mineral precipitation, metal retardation, seasonal groundwater movement, and THMC model selection.

### 2026-05-12

#### [Saskatchewan Uranium Decay-Series Groundwater Academic Paper](./2026-05-12-geomine-saskatchewan-uranium-decay-series-groundwater/)

- Main paper: [saskatchewan_uranium_decay_series_groundwater_academic_paper_zh.md](./2026-05-12-geomine-saskatchewan-uranium-decay-series-groundwater/saskatchewan_uranium_decay_series_groundwater_academic_paper_zh.md)
- PDFs: original and normalized PDF exports are included.
- Supporting files: package README and datasets evidence JSON.
- Focus: uranium decay-series groundwater geochemistry, radionuclide mobility, data-source evidence, and academic-paper style synthesis.

#### [Revell Batholith Radiolysis Geochemical Framework](./2026-05-12-geomine-revell-batholith-radiolysis-geochemical-framework/)

- Main papers:
  - [revell_batholith_radiolysis_geochemical_framework_zh.md](./2026-05-12-geomine-revell-batholith-radiolysis-geochemical-framework/revell_batholith_radiolysis_geochemical_framework_zh.md)
  - [revell_batholith_radiolysis_academic_paper_zh.md](./2026-05-12-geomine-revell-batholith-radiolysis-geochemical-framework/revell_batholith_radiolysis_academic_paper_zh.md)
- PDFs: original and normalized PDF exports are included for both papers.
- Supporting files: [datasets_evidence.json](./2026-05-12-geomine-revell-batholith-radiolysis-geochemical-framework/datasets_evidence.json)
- Focus: Revell Batholith deep groundwater chemistry, natural radiolytic hydrogen, sulfate/microbial redox coupling, and THMC interface for crystalline-rock DGR safety research.

#### [Porous Media Radiolysis-Electrolysis Frontier](./2026-05-12-geomine-porous-radiolysis-electrolysis-frontier/)

- Main paper: [porous_media_radiolysis_electrolysis_research_report_zh.md](./2026-05-12-geomine-porous-radiolysis-electrolysis-frontier/porous_media_radiolysis_electrolysis_research_report_zh.md)
- PDFs: original, normalized, and export-test PDFs are included.
- Supporting files: [mcp_provenance.md](./2026-05-12-geomine-porous-radiolysis-electrolysis-frontier/mcp_provenance.md), normalized Markdown, and math conversion support.
- Focus: porous media water radiolysis, radiation-assisted electrolysis, carrier separation, G-value boundaries, engineering feasibility, geochemistry, and nuclear-waste relevance.

### 2026-05-11

#### [Radiolytic Natural Hydrogen in Revell Batholith and Athabasca Basement](./2026-05-11-geomine-radiolytic-natural-hydrogen-revell-athabasca/)

- Main paper: [radiolytic_natural_hydrogen_revell_athabasca_research_report_zh.md](./2026-05-11-geomine-radiolytic-natural-hydrogen-revell-athabasca/radiolytic_natural_hydrogen_revell_athabasca_research_report_zh.md)
- PDF: [radiolytic_natural_hydrogen_revell_athabasca_research_report_zh.pdf](./2026-05-11-geomine-radiolytic-natural-hydrogen-revell-athabasca/radiolytic_natural_hydrogen_revell_athabasca_research_report_zh.pdf)
- Supporting files: evidence matrix and machine-readable summary.
- Focus: U-Th-K decay, deep-water radiolysis, H2 production, redox halo formation, sulfate balance, and radionuclide-migration feedbacks.

#### [Patterson Lake Corridor Claim-Gap Screening](./2026-05-11-geomine-patterson-lake-corridor-claim-gap/)

- Main paper: [patterson_lake_corridor_claim_gap_research_report_zh.md](./2026-05-11-geomine-patterson-lake-corridor-claim-gap/patterson_lake_corridor_claim_gap_research_report_zh.md)
- PDF: [patterson_lake_corridor_claim_gap_research_report_zh.pdf](./2026-05-11-geomine-patterson-lake-corridor-claim-gap/patterson_lake_corridor_claim_gap_research_report_zh.pdf)
- Supporting files: evidence matrix, machine-readable summary, data tables, and screening script.
- Focus: Saskatchewan Patterson Lake Corridor uranium/gold/critical-mineral claim-gap screening using official tenure, geology, mineral occurrence, and exploration evidence.

### 2026-05-10

#### [NWT and Nunavut Mining Market Entry SWOT](./2026-05-10-geomine-northern-canada-mining-market-entry/)

- Main paper: [nwt_nunavut_mining_market_entry_swot_report.md](./2026-05-10-geomine-northern-canada-mining-market-entry/nwt_nunavut_mining_market_entry_swot_report.md)
- Focus: why NWT and Nunavut host fewer mining companies, what makes northern projects difficult, and where gold, uranium, and critical-mineral opportunities may still justify disciplined entry.

#### [NWT Gold Phase-2 Tenure Subtraction](./2026-05-10-geomine-nwt-gold-phase2-tenure-subtraction/)

- Main paper: [nwt_gold_phase2_tenure_subtraction_report.md](./2026-05-10-geomine-nwt-gold-phase2-tenure-subtraction/nwt_gold_phase2_tenure_subtraction_report.md)
- Companion note: [south_rae_claim_gap_explanation.md](./2026-05-10-geomine-nwt-gold-phase2-tenure-subtraction/south_rae_claim_gap_explanation.md)
- PDF: [nwt_gold_phase2_tenure_subtraction_report.pdf](./2026-05-10-geomine-nwt-gold-phase2-tenure-subtraction/nwt_gold_phase2_tenure_subtraction_report.pdf)
- Focus: exact active-tenure subtraction, open-ground grid ranking, anomaly-source tracing, and South Rae/Hearne margin prioritization.

#### [NWT Gold Prospectivity and Claim-Gap Screening](./2026-05-10-geomine-nwt-gold-prospectivity/)

- Main paper: [nwt_gold_prospectivity_report.md](./2026-05-10-geomine-nwt-gold-prospectivity/nwt_gold_prospectivity_report.md)
- PDF: [nwt_gold_prospectivity_report.pdf](./2026-05-10-geomine-nwt-gold-prospectivity/nwt_gold_prospectivity_report.pdf)
- Focus: mineral showings, till-gold geochemistry, tenure pressure, deposit models, and follow-up windows in Northwest Territories gold belts.

#### [Radiolysis-Assisted Hydrogen Production Feasibility](./2026-05-10-radiolysis-assisted-hydrogen-production/)

- Main paper: [radiolysis_assisted_hydrogen_industrial_feasibility_report.md](./2026-05-10-radiolysis-assisted-hydrogen-production/radiolysis_assisted_hydrogen_industrial_feasibility_report.md)
- PDF: [radiolysis_assisted_hydrogen_industrial_feasibility_report.pdf](./2026-05-10-radiolysis-assisted-hydrogen-production/radiolysis_assisted_hydrogen_industrial_feasibility_report.pdf)
- Focus: whether radiation, porous semiconductors, or clay composites could improve water electrolysis for hydrogen production under realistic energy and G-value constraints.

#### [Porous Media Radiolysis Literature Review](./2026-05-10-radiolysis-porous-media-review/)

- Main paper: [radiolysis_porous_media_chinese_review.md](./2026-05-10-radiolysis-porous-media-review/radiolysis_porous_media_chinese_review.md)
- PDF: [radiolysis_porous_media_chinese_review.pdf](./2026-05-10-radiolysis-porous-media-review/radiolysis_porous_media_chinese_review.pdf)
- Focus: water radiolysis in porous media, electron migration, electric-field effects, reaction networks, and control-equation derivation.

### 2026-05-09

#### [Wollaston Lake East Uranium Screening](./2026-05-09-geomine-wollaston-lake-east-uranium-screening/)

- First-pass paper: [wollaston_lake_east_uranium_screening_report.md](./2026-05-09-geomine-wollaston-lake-east-uranium-screening/wollaston_lake_east_uranium_screening_report.md)
- Expanded paper: [wollaston_lake_east_expanded_research_report.md](./2026-05-09-geomine-wollaston-lake-east-uranium-screening/wollaston_lake_east_expanded_research_report.md)
- PDFs: Chinese PDF exports are included for both papers.
- Supporting files: evidence matrix and machine-readable summary.
- Focus: Athabasca margin uranium screening using conductors, Wollaston metasedimentary rocks, radioactive boulders, SMDI records, drillholes, and geochemical lanes.

### 2026-05-08

#### [Cigar Lake Uranium Screening](./2026-05-08-geomine-cigar-lake-uranium-screening/)

- Main paper: [cigar_lake_uranium_screening_report.md](./2026-05-08-geomine-cigar-lake-uranium-screening/cigar_lake_uranium_screening_report.md)
- PDFs: English and Chinese PDF exports are included.
- Supporting files: package README, machine-readable summary, and MCP provenance notes.
- Focus: Cigar Lake as a high-grade Athabasca unconformity-related uranium deposit, including deposit-model fit, production status, geochemistry, geophysics, infrastructure, and regulatory context.

## Skill Capability and Methodology Guides

### 2026-05-14

#### [GeoMine Research Geochemistry Paper Architecture Skill Methodology](./GeoMine_Research_Geochemistry_Paper_Architecture_Skill_Methodology.md)

- Focus: a method document for upgrading GeoMine paper writing from report-style summaries to problem-driven, data-constrained, method-transparent, mechanism-oriented geochemistry papers.

### 2026-05-13

#### [GeoMine PFLOTRAN Modeling Skill Guide](./GeoMine_PFLOTRAN_Modeling_Skill_Guide_zh.md)

- Focus: design purpose, architecture, boundaries, triggers, THMC connections, MCP design, local scripts, use cases, and paper-writing value for the PFLOTRAN modeling skill family.

#### [GeoMine PHREEQC Skill Capability Guide](./GeoMine_PHREEQC_Skill_Capability_Guide.md)

- Focus: PHREEQC skill purpose, model types, input audit, database selection, keyword planning, selected output, reproducibility, examples, and limitations.

### 2026-05-12

#### [GeoMine THMC Skill Family Guide](./GeoMine_THMC_Skill_Family_Guide.md)

- Focus: THMC skill-family positioning, coupling levels, child skill responsibilities, modeling-package output structure, router behavior, reaction-network references, templates, and validation expectations.

## Recommended Reading Paths

- Mining exploration and claim screening: Cigar Lake, Wollaston Lake East, NWT gold prospectivity, NWT phase-2 tenure subtraction, Patterson Lake Corridor.
- Radiolysis and natural hydrogen: porous media radiolysis review, radiolysis-assisted hydrogen production, Revell/Athabasca radiolytic hydrogen, porous radiolysis-electrolysis frontier, Revell Batholith geochemical framework.
- Groundwater and radionuclide geochemistry: Saskatchewan uranium decay-series groundwater, PHREEQC U-Ra-SO4-CO3 workflow, wildfire/rainfall radionuclide remobilization.
- THMC and reactive transport modeling: tailings seepage THMC, DGR copper-bentonite THMC, fractured-rock radionuclide/colloid THMC, PFLOTRAN tailings uranium workflow.
- GeoMine plugin methodology: THMC guide, PHREEQC guide, PFLOTRAN guide, geochemistry paper architecture guide.

## Data and Review Boundaries

- Tenure and claim status are time-sensitive. Always re-check official provincial or territorial registries before staking, acquisition, or disclosure.
- Company disclosures and historical reports are background evidence. They do not replace official tenure checks, technical reports, QP review, or field validation.
- Geochemical anomalies are not proof of mineralization. Interpret them with sample medium, analytical method, detection limits, QA/QC, transport direction, lithology, structure, and alteration context.
- PHREEQC/PFLOTRAN/THMC artifacts are research workflows and screening models unless calibrated against field data.
- Radiation, radionuclide, nuclear-waste, groundwater, and hydrogen conclusions require qualified technical review before engineering, regulatory, or safety use.
