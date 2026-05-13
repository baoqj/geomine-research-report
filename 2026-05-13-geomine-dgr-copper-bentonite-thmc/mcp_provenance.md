# MCP Provenance Notes

Date: 2026-05-13  
Workflow: GeoMine Research + THMC Modeling skills  
Topic: crystalline-rock DGR near-field THMC coupling: copper canister, bentonite buffer, fractured crystalline rock, groundwater  

## MCP Calls

| Tool | Query purpose | Retrieval status | Scientific use | Warnings |
|---|---|---|---|---|
| `tool_search` | Check whether live `geomine_thmc` / `geomine_thmc_data` tools are callable in the current Codex session | no live GeoMine THMC MCP tools exposed; unrelated tools surfaced | Establishes that the paper must run in Core Mode plus local/mock provenance | Do not claim live MCP field-data retrieval |
| `normalize_aoi` | Normalize a generic Canadian crystalline-rock DGR near-field system | parsed; network not used | Confirms this is a conceptual Canadian DGR scenario, not a coordinate-specific AOI | No province, coordinates, polygon, NTS sheet, geocoding, area calculation, or CRS transformation |
| `search_cdogs_surveys` | Discover possible Canadian geochemical data lane for groundwater salinity, sulfate/sulfide, radionuclides, crystalline rock | planned; network disabled | Used only as a future source-discovery lane for baseline groundwater geochemistry | No live metadata; no sample medium, analytical method, detection limit, unit, or QA/QC verification |
| `fetch_dataset_metadata: nrcan-cdogs` | Check local static registry for CDoGS source metadata | parsed from local registry | Confirms endpoint pattern for future data retrieval | CRS, scale/resolution, last update, and license remain unresolved |

## Local GeoMine THMC MCP Reference Checks

These commands exercise the repository-local mock-backed MCP reference implementation. They validate schema and workflow shape only.

| Command | Result | Interpretation |
|---|---:|---|
| `python3 scripts/test_thmc_mcp_tools.py` in `plugins/Code/geo-mining-research` | `ok: true`, 20 tools, 22 responses | THMC project/AOI/chemistry/mesh/PHREEQC/OGS/PFLOTRAN/model-version/run-record mock contract is intact |
| `python3 scripts/test_thmc_data_mcp_tools.py` in `plugins/Code/geo-mining-research` | `ok: true`, 13 tools, 13 responses | DGR campaign/borehole/sensor/water/core/packer/stress/data-package mock contract is intact |

## Generated Calculation Artifacts

| Artifact | Purpose | Status |
|---|---|---|
| `scripts/generate_thmc_screening_figures.py` | Rebuild all screening calculations and SVG figures | executed successfully |
| `data/thmc_parameter_sources.csv` | Source-to-parameter provenance table | generated |
| `data/thmc_screening_results.csv` | Machine-readable calculation outputs | generated |
| `data/thmc_screening_summary.json` | Key result summary and limitations | generated |
| `figures/fig1_nearfield_concept.svg` to `figures/fig8_scenario_matrix.svg` | Paper illustrations | generated |

## Boundary Statement

The current session does not expose a live DGR-specific `geomine_thmc` execution layer, PHREEQC job runner, OGS/PFLOTRAN submission, or NWMO/CNSC dataset adapter. The main report therefore uses MCP output as provenance-preserving source discovery and mock workflow validation only. It does not claim site-specific groundwater chemistry, crystalline-rock fracture statistics, copper corrosion rates, bentonite dry density, radionuclide inventory, or calibrated model performance.
