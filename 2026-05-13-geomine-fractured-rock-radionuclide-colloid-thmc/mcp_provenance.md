# MCP Provenance Notes

Date: 2026-05-13  
Workflow: GeoMine Research + THMC Modeling skills  
Topic: fractured crystalline rock radionuclide sorption, matrix diffusion, and colloid-facilitated transport  

## Live Tool Availability

| Tool / layer | Query purpose | Retrieval status | Scientific use | Warnings |
|---|---|---|---|---|
| `tool_search` | Check whether live `geomine_thmc` / `geomine_thmc_data` tools are callable in the current Codex session | no live GeoMine THMC MCP tools exposed; unrelated tools surfaced | Establishes Core Mode plus local/mock workflow validation | Do not claim live MCP field-data retrieval |
| Web search/open | Verify EGU26-5127, SKB, Grimsel, NEA, RES3T, ThermoChimie and colloid references | live web retrieval | Source discovery and citation verification | Web pages do not provide full site-specific parameter tables |

## Local GeoMine THMC MCP Reference Checks

These commands exercise the repository-local mock-backed MCP reference implementation. They validate schema and workflow shape only.

| Command | Result | Interpretation |
|---|---:|---|
| `python3 scripts/test_thmc_mcp_tools.py` in `plugins/Code/geo-mining-research` | `ok: true`, 20 tools, 22 responses | THMC project/AOI/chemistry/mesh/PHREEQC/OGS/PFLOTRAN/model-version/run-record mock contract is intact |
| `python3 scripts/test_thmc_data_mcp_tools.py` in `plugins/Code/geo-mining-research` | `ok: true`, 13 tools, 13 responses | DGR campaign/borehole/sensor/water/core/packer/stress/data-package mock contract is intact |

## Generated Calculation Artifacts

| Artifact | Purpose | Status |
|---|---|---|
| `scripts/generate_fracture_colloid_figures.py` | Rebuild all screening calculations and SVG figures | executed successfully |
| `data/fracture_colloid_parameter_sources.csv` | Source-to-parameter provenance table | generated |
| `data/fracture_colloid_nuclide_parameters.csv` | Radionuclide Kd and colloid-screening table | generated |
| `data/fracture_colloid_screening_results.csv` | Machine-readable calculation outputs | generated |
| `data/fracture_colloid_screening_summary.json` | Key result summary and limitations | generated |
| `figures/fig1_fractured_rock_concept.svg` to `figures/fig8_scenario_risk_matrix.svg` | Paper illustrations | generated |

## Boundary Statement

The current session does not expose a live DGR-specific `geomine_thmc` execution layer, PHREEQC job runner, OGS/PFLOTRAN submission, SKB table extractor, Grimsel raw breakthrough-curve adapter, RES3T adapter, or ThermoChimie PHREEQC execution adapter. The main report therefore uses MCP output as provenance-preserving source discovery and mock workflow validation only. It does not claim site-specific groundwater chemistry, fracture statistics, Kd tables, colloid concentrations, radionuclide source terms, or calibrated model performance.
