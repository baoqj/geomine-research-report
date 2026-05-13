# GeoMine Provenance and Source Notes

Date: 2026-05-13  
Workflow: GeoMine Research + PFLOTRAN Modeling Skill Family + Academic Paper Research Writer + Academic Figure Package + PDF Export  
Scenario: sulfide-bearing uranium tailings acidic seepage into a shallow aquifer

## Local Prompt

- Source prompt: `plugins/PRD/THMC/GeoMine_PFLOTRAN_Tailings_Acid_Seepage_Uranium_Radionuclide_Prompt.md`
- Retrieval status: parsed locally.
- Use: defined the required PFLOTRAN package structure, PHREEQC comparison, strict placeholder rules, figure package requirements, and model manifest fields.

## GeoMine MCP Calls

| Tool | Query purpose | Retrieval status | Scientific use | Warnings |
|---|---|---|---|---|
| `normalize_aoi` | Normalize a generic uranium tailings / shallow aquifer scenario | parsed, network not used | Confirms this is not a site-specific AOI and no coordinate-driven claim is valid | No province, coordinates, polygon, NTS sheet, or CRS transformation |
| `search_canada_geodata` | Plan Canadian public dataset discovery for uranium tailings, ARD, groundwater, radionuclide monitoring | planned, network disabled | Used as data-acquisition plan and source-lane inventory | No live catalogue records fetched; resource license/date/CRS not verified |
| `search_saskatchewan_mineral_data` | Plan Saskatchewan uranium-context public geoscience discovery | planned, network disabled | Used as candidate regional source lane only | No live GeoAtlas/ArcGIS query |
| `search_cdogs_surveys` | Plan CDoGS geochemical survey discovery | planned, network disabled | Used as future baseline geochemistry source lane | No analytical spreadsheet parsing; medium/method/detection limits unverified |

## Web / Literature Sources Used

| Source | Link | Use in paper |
|---|---|---|
| PFLOTRAN documentation | https://documentation.pflotran.org/ | Solver scope: massively parallel subsurface flow and reactive transport |
| PFLOTRAN RICHARDS theory guide | https://documentation.pflotran.org/theory_guide/mode_richards.html | Variably saturated flow equation and Darcy flux form |
| PFLOTRAN SUBSURFACE_FLOW card | https://pflotran.org/documentation-release/user_guide/cards/simulation/subsurface_flow_card.html | Flow-mode choices: RICHARDS, TH, GENERAL, etc. |
| PFLOTRAN method of solution | https://documentation.pflotran.org/theory_guide/appendixB.html | Finite-volume reactive-transport discretization and retardation screening equation context |
| PFLOTRAN reactive transport theory | https://documentation.pflotran.org/theory_guide/mode_reactive_transport.html | Primary species, minerals, sorption, and porosity/permeability feedback scope |
| USGS PHREEQC Version 3 | https://www.usgs.gov/software/phreeqc-version-3 | PHREEQC role for speciation, batch reaction, 1D transport, surface complexation, isotope capabilities and PhreeqcRM |
| INAP GARD Guide | https://www.inap.com.au/gard-guide/ | ARD/AMD process, prediction, prevention, management and sulfide oxidation framing |
| MEND uranium tailings wet-barrier report page | https://mend-nedem.org/mend-report/wet-barriers-on-pyrite-uranium-tailings-part-i-and-ii-laboratory-lysimeter-studies-of-oxidation-leaching-and-limestone-neutralization-characteristics-of-uranium-tailings-and-waste-rock/ | Uranium-tailings acid generation and limestone neutralization as an empirical study class |
| Health Canada radiological parameters guideline | https://www.canada.ca/en/health-canada/services/publications/healthy-living/guidelines-drinking-water-quality-radiological-parameters.html | Canadian screening context for Ra-226, Ra-228, Pb-210, Po-210 and gross alpha/beta screening |
| Health Canada uranium guideline | https://www.canada.ca/en/health-canada/services/publications/healthy-living/guidelines-canadian-drinking-water-quality-guideline-technical-document-uranium.html | Uranium chemical-toxicity MAC and mobility controls |
| USGS U(VI) reactive transport paper page | https://www.usgs.gov/publications/simulation-reactive-transport-uraniumvi-groundwater-variable-chemical-conditions | U(VI), alkalinity, nonlinear sorption and reactive transport context |
| PNNL calcite-U(VI) reactive transport paper page | https://www.pnnl.gov/publications/influence-calcite-uraniumvi-reactive-transport-groundwater-river-mixing-zone | Calcite/carbonate influence on U(VI) reactive transport |
| USGS Ra-226 sorption paper page | https://www.usgs.gov/publications/sorption-radium-226-oil-production-brine-sediments-and-soils | Ra sorption/precipitation with sulfate-bearing minerals and clay fractions |
| USGS radium attenuation/mobilization paper page | https://www.usgs.gov/publications/radium-attenuation-and-mobilization-stream-sediments-following-oil-and-gas-wastewater | Barite/barite-celestite co-precipitation and Fe-Mn oxide adsorption evidence |

## PFLOTRAN Execution Evidence

| Item | Value |
|---|---|
| Local native PFLOTRAN | Not found on PATH |
| Execution method | Docker |
| Docker image | `pflotran/pflotran:ubuntu22` |
| Image digest | `pflotran/pflotran@sha256:b9413b676cf826ba6ce9bf733e1c05e558fae00cedc0814d291450d52fbd8197` |
| Image created | 2023-09-05T18:12:24.4708764Z |
| PETSc reported by PFLOTRAN help | PETSc Release Version 3.19.3 |
| Database | `/software/pflotran/database/hanford.dat` |
| Executed decks | `pflotran_runs/calcite_buffered/tailings_u_calcite_buffered.in`; `pflotran_runs/no_calcite/tailings_u_no_calcite.in` |
| Logs | `pflotran_runs/calcite_buffered/tailings_u_calcite_buffered.out`; `pflotran_runs/no_calcite/tailings_u_no_calcite.out` |
| Parsed output tables | `data/pflotran_screening_summary.csv`; `data/pflotran_profiles_25y.csv` |
| Parser | `scripts/analyze_pflotran_outputs.py` |

## Boundary Statement

This paper uses source discovery, literature synthesis, and two executed synthetic PFLOTRAN screening runs to design a modeling workflow. It does not claim measured tailings mineralogy, porewater chemistry, hydraulic conductivity, seepage rate, plume extent, calibrated site-scale PFLOTRAN output, regulatory compliance, or site-specific environmental safety. Every missing value remains a placeholder or a required field/lab measurement.
