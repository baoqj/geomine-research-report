# PFLOTRAN Modeling Package

## 1. Research Objective

Design a PFLOTRAN reactive-transport workflow for acidic seepage from sulfide-bearing uranium tailings entering a shallow aquifer. The model focuses on acid generation, sulfate transport, carbonate neutralization, Fe/Al/Mn precipitation, heavy-metal migration, U mobility, Ra/Pb/Po migration, and attenuation by sulfate minerals, Fe-Mn oxides, sorption, and optional porosity/permeability feedback.

This is a modeling package and paper-ready method plan with two executed 1D synthetic PFLOTRAN screening runs. It is not a regulatory model, certified engineering design, calibrated PFLOTRAN run, or site safety conclusion.

## 2. Scenario Classification

- Scenario type: sulfide-bearing uranium tailings acidic seepage.
- Environmental setting: tailings source zone hydraulically connected to a shallow aquifer.
- Primary process: acid rock drainage and reactive transport.
- Secondary process: uranium-series radionuclide and trace-metal migration.
- Recommended first spatial scale: 2D cross-section.
- Screening scale: 1D column for reaction-network and breakthrough logic.
- Future scale: 3D site model after measured topography, hydrostratigraphy, wells, and boundary conditions are available.
- Time scale: years to decades for first simulations, with scenario extension to 100 years only after calibration.

## 3. Why PFLOTRAN Is Appropriate

PFLOTRAN is appropriate because the problem is not limited to one water sample or a batch reaction. The central questions require spatially explicit flow and reactive transport: plume evolution, breakthrough curves, pH and sulfate fronts, mineral precipitation/dissolution fronts, and possible material-property feedback.

PHREEQC is still required first for aqueous speciation, saturation indices, carbonate complexation, sulfate/barite checks, and adsorption scenario screening. PFLOTRAN becomes necessary when those reaction networks must be placed into a distributed aquifer flow field.

## 4. Relationship to THMC / PHREEQC / GeoMine Workflow

The PFLOTRAN skill family is used as an independent solver-specific workflow, not as a sub-skill of conceptual THMC modeling. The proper sequence is:

1. GeoMine research framing and source discovery.
2. PHREEQC reaction-network prototype for chemistry support and missing constants.
3. PFLOTRAN 1D screening column for minimum executable mechanism checks.
4. PFLOTRAN 2D cross-section with observation points.
5. Calibration, validation, sensitivity, and uncertainty analysis.
6. Optional THC or porosity/permeability feedback once the first reactive-transport model is stable.

## 5. Conceptual Model

The conceptual model contains four physical regions:

- Tailings source: sulfide-bearing material, pyrite or other sulfides, possible U-bearing residual phases, carbonate amendment if present.
- Vadose/transition zone: variably saturated seepage, oxygen access, source-term modulation.
- Shallow aquifer: advective-dispersive transport and reactive attenuation.
- Low-permeability base: no-flow or leakage boundary depending on measured geology.

The process network is:

```text
sulfide oxidation
  -> H+ and SO4 generation
  -> carbonate neutralization and Ca/Mg release
  -> Fe/Al hydroxide precipitation
  -> adsorption/co-precipitation of trace metals and radionuclides
  -> U(VI) carbonate-complex mobility under oxic carbonate-rich water
  -> Ra attenuation through sulfate/barite or sorption, if database-supported
  -> downgradient pH, sulfate, U, Ra, Pb, Po and heavy-metal breakthrough
```

Excluded from the first model: detailed microbial sulfur cycling, gas transport, full geomechanics, colloid-facilitated transport, climate-change hydrology, engineered cover performance, and regulatory dose assessment beyond screening ratios.

## 6. Process Mode Selection

| Process | First choice | Alternative | Reason |
|---|---|---|---|
| Flow | RICHARDS | Saturated flow | Use RICHARDS if tailings/vadose seepage controls source flux; use saturated flow if modeling only the aquifer below a known seepage boundary. |
| Transport | Reactive transport | Conservative tracer pre-run | Acid, sulfate, metals, U/Ra/Pb/Po and mineral reactions are central. |
| Thermal | Excluded first | THC later | No temperature gradient or thermal source was supplied. Temperature sensitivity can be added through rate laws and database support. |
| Mechanics | Excluded first | Chemical porosity/permeability feedback | No stress, deformation, or settlement data were supplied. |

## 7. Model Domain and Grid

Recommended first executable domain:

- 2D vertical cross-section from tailings source to downgradient receptor.
- Structured grid for transparency and rapid iteration.
- Local refinement around tailings base, neutralization front, aquifer interface, and monitoring wells.
- Observation points at three downgradient distances, with exact locations replaced by measured well coordinates.

The 1D column version should only test reaction-network behavior and breakthrough logic. It cannot represent plume spreading, boundary effects, or aquifer heterogeneity.

## 8. Regions and Material Properties

| Region | Required properties | Placeholder fields |
|---|---|---|
| Tailings | porosity, permeability tensor, sulfide sulfur, carbonate abundance, mineral volume fractions, moisture/saturation relation | `<POROSITY_TAILINGS>`, `<PERMEABILITY_TAILINGS_X_M2>`, `<PYRITE_VOLUME_FRACTION>` |
| Vadose/transition zone | saturation curve, permeability, recharge/seepage flux, tortuosity | `<VADOSE_CC_IF_RICHARDS>`, `<PERMEABILITY_VADOSE_M2>` |
| Aquifer | porosity, permeability tensor, dispersivity, background chemistry | `<POROSITY_AQUIFER>`, `<PERMEABILITY_AQUIFER_X_M2>`, `<LONGITUDINAL_DISPERSIVITY_M>` |
| Base layer | leakage/no-flow behavior, vertical permeability | `<PERMEABILITY_BASE_M2>` |

No porosity, permeability, dispersivity, mineral abundance, or source flux is invented in this package.

## 9. Initial Conditions

Initial conditions must be separated into background aquifer water and tailings seepage/source water.

| Initial condition | Required data |
|---|---|
| Hydraulic state | pressure or hydraulic head, saturation if variably saturated |
| Background water | pH, Eh/pe, temperature, alkalinity, major ions, sulfate, Fe/Mn/Al, U/Ra/Pb/Po, relevant heavy metals |
| Tailings source water | pH/acidity, sulfate, Fe, Al, Mn, U, Ra, Pb, Po, As/Ni/Co/Cu/Zn if relevant |
| Mineral state | pyrite/sulfide fraction, calcite/dolomite, Fe/Al hydroxides, barite/Ba/Sr support, clay/oxide surface capacity |

## 10. Boundary Conditions

| Boundary | Candidate type | Required support |
|---|---|---|
| Tailings source | flux with source chemistry or Dirichlet seepage chemistry | seepage rate, water balance, porewater monitoring |
| Upgradient aquifer | fixed head or specified flux | head survey, hydraulic gradient |
| Downgradient aquifer | fixed head, hydrostatic pressure, or open outflow | receptor boundary and monitoring wells |
| Top boundary | infiltration/recharge if RICHARDS | climate/recharge estimate, cover condition |
| Base | no-flow or leakage | stratigraphy and vertical hydraulic conductivity |

## 11. Flow and Transport Configuration

The first flow setup should use conservative tracer checks before full chemistry:

1. Verify pressure/head field and water balance.
2. Verify advective travel-time order of magnitude.
3. Add sulfate and acidity as reactive components.
4. Add U and Ra only after carbonate/sulfate and mineral saturation behavior is stable.
5. Add Pb/Po and heavy metals as supported by database and monitoring data.

## 12. Chemistry Configuration

Primary aqueous species should include at minimum H, O, C, Ca, Mg, Na, K, Cl, S, Fe, Al, Mn, U, Ra, Pb, Po, and optional As, Ni, Co, Cu, Zn. Chemistry must remain database-driven where possible.

| Process | Treatment | Missing data |
|---|---|---|
| Pyrite oxidation | conceptual kinetic reaction | rate law, surface area, oxygen access, microbial effect |
| Carbonate neutralization | calcite/dolomite equilibrium or kinetic phases | carbonate mineral abundance, rate law |
| Fe/Al precipitation | Fe(OH)3(am), gibbsite or supported phases | database support, redox partitioning |
| Uranium mobility | U(VI) carbonate/hydroxide complexes; redox-sensitive U(IV)/U(VI) boundary | thermodynamic support, Eh/pe, Ca-carbonate complexes |
| Ra attenuation | barite/solid-solution or sorption placeholder | Ba/Sr/SO4 data, Ra-barite database support |
| Fe-Mn oxide interaction | surface-complexation or Kd placeholder | site density, constants, oxide abundance |
| Pb/Po | supported aqueous species or conservative/sorbing surrogates | database support and radionuclide-specific measurements |

## 13. Thermal-Hydrologic-Chemical Coupling, if applicable

Thermal coupling is not required for the first model because no thermal gradient or heat source was supplied. It becomes relevant if:

- tailings temperature varies seasonally enough to change reaction rates;
- rate constants are calibrated with activation energies;
- thermal gradients affect density, viscosity, or solubility.

## 14. Geomechanics Scope, if applicable

Full geomechanics is excluded. Chemical porosity/permeability feedback can be added as a scenario if mineral precipitation or dissolution significantly changes pore space. Treat feedback as optional until mineral volume changes are supported by PFLOTRAN output and field/lab evidence.

## 15. Generated PFLOTRAN Input Deck Skeleton

The draft input deck is saved as:

`pflotran_tailings_uranium_template.in`

It contains `SIMULATION`, `SUBSURFACE`, `GRID`, `REGION`, `MATERIAL_PROPERTY`, `FLOW_CONDITION`, `TRANSPORT_CONDITION`, `INITIAL_CONDITION`, `BOUNDARY_CONDITION`, `CHEMISTRY`, `OBSERVATION`, and `OUTPUT` blocks with explicit placeholders.

## 16. Database and Reaction Network Requirements

The thermodynamic database must be checked for:

- carbonate, sulfate, Fe, Al and Mn aqueous reactions;
- U(VI) carbonate and Ca-U-carbonate complexes;
- U(IV)/U(VI) redox treatment if used;
- Ba/Sr/Ra sulfate and barite behavior if Ra attenuation is modeled mechanistically;
- Pb and Po speciation, or a justified surrogate strategy;
- mineral phases for calcite, dolomite, gypsum, barite, Fe hydroxide, Al hydroxide, and U-bearing phases.

If the database does not support Ra or Po adequately, PFLOTRAN should not be used to claim mechanistic Ra/Po attenuation. Use a placeholder or post-processing risk screen.

## 17. Run Command and Execution Plan

Local command:

```bash
pflotran -pflotranin pflotran_tailings_uranium_template.in
```

MPI/HPC example:

```bash
mpirun -np 16 pflotran -pflotranin pflotran_tailings_uranium_template.in
```

Recommended organization:

```text
model/
  input/
  database/
  runs/<model_version>/
  outputs/
  logs/
  postprocess/
  figures/
```

Run manifest fields are saved in `run_manifest.json`.

The skeleton structure check is saved in `input_deck_validation.json`. It reports no missing required/recommended blocks and 88 intentional placeholders, so the deck is structurally organized but not execution-ready.

Executed synthetic screening addendum:

| Scenario | Input deck | Runtime status | Interpretation |
|---|---|---|---|
| `calcite_buffered` | `pflotran_runs/calcite_buffered/tailings_u_calcite_buffered.in` | converged; FLOW 111 steps / TRAN 119 steps / 0 cuts | Tests whether calcite buffers the acid source. |
| `no_calcite` | `pflotran_runs/no_calcite/tailings_u_no_calcite.in` | converged; FLOW 111 steps / TRAN 161 steps / 0 cuts | Counterfactual without carbonate buffering. |

Execution manifest, logs and output inventory are saved in `pflotran_run_manifest.json`.

## 18. Output / Observation Design

Observation points should be located at measured downgradient monitoring wells or planned virtual wells:

- OBS-1: near-source aquifer interface;
- OBS-2: mid-plume neutralization zone;
- OBS-3: receptor/downgradient boundary.

Required outputs:

- pH, alkalinity, sulfate;
- Fe, Al, Mn;
- U, Ra, Pb, Po;
- selected As, Ni, Co, Cu, Zn;
- hydraulic head/pressure, saturation;
- mineral volume fractions;
- porosity/permeability if feedback enabled;
- mass balance, convergence, and charge-balance diagnostics.

Executed 1D screening outputs currently available:

- `data/pflotran_screening_summary.csv`
- `data/pflotran_profiles_25y.csv`
- `figures/fig07_pflotran_ph_profiles.svg` / `.png`
- `figures/fig08_pflotran_u_sulfate_profiles.svg` / `.png`
- `pflotran_runs/*/tailings_u_*-005.tec`

## 19. Calibration and Validation Plan

Calibration targets:

- hydraulic heads and seepage fluxes;
- pH, EC/TDS, sulfate, alkalinity;
- Fe/Mn/Al and major ions;
- U/Ra/Pb/Po and relevant heavy metals;
- spatial location of neutralization/precipitation fronts.

Validation should use independent downgradient wells and different time windows. Do not use the same wells and dates for both calibration and validation.

## 20. Sensitivity and Uncertainty Plan

Priority parameters:

1. pyrite oxidation rate and effective reactive surface area;
2. carbonate neutralization capacity;
3. seepage flux and hydraulic gradient;
4. Fe-Mn oxide sorption capacity;
5. dispersivity and diffusion;
6. redox boundary location;
7. Ra/barite thermodynamic support;
8. permeability anisotropy.

Recommended analysis:

- one-at-a-time screening for stability;
- Morris or Sobol design after the model runs reliably;
- scenario ensemble for acidic, buffered, and redox-transition cases.

## 21. Expected Figures and Tables

Saved figures:

- `figures/fig01_conceptual_cross_section.svg`
- `figures/fig02_reaction_network.svg`
- `figures/fig03_domain_boundary_conditions.svg`
- `figures/fig04_acid_buffer_index_heatmap.svg`
- `figures/fig05_retardation_screening_curves.svg`
- `figures/fig06_sensitivity_tornado.svg`
- `figures/fig07_pflotran_ph_profiles.svg`
- `figures/fig08_pflotran_u_sulfate_profiles.svg`

PNG render fallbacks with the same stems are also generated for formula-safe PDF export.

Saved screening datasets:

- `data/screening_parameter_sweep.csv`
- `data/retardation_scenarios.csv`
- `data/sensitivity_screening_rank.csv`
- `data/pflotran_screening_summary.csv`
- `data/pflotran_profiles_25y.csv`

Figures 1-6 are method/screening visuals, not calibrated PFLOTRAN output. Figures 7-8 are executed synthetic PFLOTRAN screening outputs, not calibrated site predictions.

## 22. Paper-ready Methods Draft

The modeling workflow begins with a PHREEQC geochemical prototype to test speciation, saturation indices, carbonate complexation, sulfate/barite controls, and adsorption placeholders. Database-supported reactions are then translated into a PFLOTRAN reactive-transport input deck. The first PFLOTRAN model is a structured 2D cross-section from the tailings source zone to downgradient observation points. Flow is represented by RICHARDS mode when the unsaturated tailings/vadose source must be modeled explicitly, or by saturated groundwater flow when the aquifer receives a measured seepage flux. Reactive transport tracks pH, sulfate, alkalinity, Fe, Al, Mn, U, Ra, Pb, Po and selected heavy metals. Mineral reactions and sorption are enabled only when thermodynamic, kinetic and surface-complexation data are available; otherwise they remain explicitly labeled placeholders.

## 23. Paper-ready Results Interpretation Plan

Results should be interpreted in this order:

1. water-balance and convergence checks;
2. conservative travel time and dispersion;
3. pH and sulfate plume evolution;
4. carbonate neutralization and secondary mineral precipitation;
5. U mobility under carbonate and redox conditions;
6. Ra attenuation through sulfate/barite or sorption if supported;
7. Pb/Po transport and uncertainty;
8. sensitivity of receptor breakthrough to source flux, reaction rates, buffering and sorption.

For the executed 1D synthetic screening runs, the valid result is limited to mechanism directionality: calcite buffering confines pH < 4 to the first 0.5 m grid cell, while the no-calcite case keeps pH < 4 to 98.5 m. UO2++ and sulfate both advance to 99.5 m in the minimum network, so the run does not demonstrate U or radionuclide attenuation. No site breakthrough curve or plume map should be described as a field result until produced by a parameterized, calibrated and independently validated site model.

## 24. Limitations and Assumptions

- No site coordinates, hydrostratigraphy, or monitoring-well locations were supplied.
- No measured concentrations, mineral fractions, kinetic constants, surface constants, or hydraulic properties were supplied.
- The 2D site-scale PFLOTRAN input deck is a skeleton and may not execute before syntax and database checks.
- The two executed 1D PFLOTRAN runs are synthetic screening cases, not calibrated field models.
- The executed network does not include Ra/Pb/Po mechanistic attenuation, sorption, ion exchange, or porosity/permeability feedback.
- Pb and Po treatment may require surrogate or post-processing if database support is insufficient.
- Constant Kd formulas are useful for screening but inadequate for final U(VI) transport under variable alkalinity and carbonate chemistry.
- This package does not determine compliance, safety, environmental liability, or remediation design.

## 25. Future MCP / Remote Compute Extension

Future tools should remain optional and default-off unless explicitly installed:

- `validate_input_deck`
- `run_pflotran_local`
- `submit_pflotran_remote`
- `get_run_status`
- `fetch_run_logs`
- `fetch_pflotran_outputs`
- `query_mesh_from_postgis`
- `fetch_parameter_field_from_r2`
- `save_model_version`
- `save_run_record`
- `parse_observation_output`
- `generate_result_summary`

## 26. Machine-readable Model Manifest

The machine-readable model manifest is saved as:

`model_manifest.json`
