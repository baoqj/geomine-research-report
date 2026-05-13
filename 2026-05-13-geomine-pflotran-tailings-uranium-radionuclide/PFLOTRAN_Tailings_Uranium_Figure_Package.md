# Figure Package: PFLOTRAN Reactive Transport Model for Uranium Tailings Acidic Seepage

## 1. Figure Strategy

The figure package separates three figure classes:

- Conceptual figures that frame the source-pathway-receptor system.
- Model-design figures that document PFLOTRAN regions, boundaries, and chemistry transfer from PHREEQC.
- Screening figures that show sensitivity logic without pretending to be calibrated PFLOTRAN results.
- Executed PFLOTRAN 1D synthetic screening figures that summarize actual solver output without presenting it as site calibration.

The visual grammar uses blue for groundwater flow, red/orange for acidic seepage and sulfate fronts, green for buffering/attenuation, purple for uranium-related behavior, and gray for low-permeability units or uncertain database-supported processes.

## 2. Figure Inventory

| Figure | File | Type | Main message |
|---|---|---|---|
| 1 | `figures/fig01_conceptual_cross_section.svg` / `.png` | Conceptual cross-section | Tailings source connects to a shallow aquifer through seepage; observation wells track plume evolution. |
| 2 | `figures/fig02_reaction_network.svg` / `.png` | Reaction network | PHREEQC should prototype reactions before PFLOTRAN spatialization. |
| 3 | `figures/fig03_domain_boundary_conditions.svg` / `.png` | Model domain schematic | First executable model should be a 2D cross-section with explicit boundaries. |
| 4 | `figures/fig04_acid_buffer_index_heatmap.svg` / `.png` | Screening heatmap | Acid-source strength and buffering capacity define first-order scenario classes. |
| 5 | `figures/fig05_retardation_screening_curves.svg` / `.png` | Breakthrough screening | Retardation delays fronts; final U/Ra behavior must use chemistry-aware transport. |
| 6 | `figures/fig06_sensitivity_tornado.svg` / `.png` | Sensitivity design | The first uncertainty-reduction targets are source rate, buffer capacity, flux, and sorption. |
| 7 | `figures/fig07_pflotran_ph_profiles.svg` / `.png` | Executed PFLOTRAN screening | A calcite-bearing synthetic column buffers pH after the source cell; no-calcite remains acidic through most of the column. |
| 8 | `figures/fig08_pflotran_u_sulfate_profiles.svg` / `.png` | Executed PFLOTRAN screening | UO2++ and sulfate move nearly conservatively in the current minimal reaction network. |

## 3. Figure Specifications

### Figure 1. Conceptual source-pathway-receptor cross-section

#### Intent

Problem-framing figure for the Introduction and Conceptual Model sections.

#### Scientific Content

Tailings source, variably saturated seepage path, shallow aquifer, low-permeability base, downgradient wells, acidic plume, neutralization/precipitation zone.

#### Visual Grammar

Brown/gray for tailings, tan for vadose material, blue for aquifer, red dashed arrows for acidic seepage, blue arrows for groundwater flow, orange dashed arrows for geochemical front.

#### Caption Draft

Conceptual cross-section for sulfide-bearing uranium tailings seepage into a shallow aquifer. The figure shows the modeled source zone, seepage pathway, shallow aquifer, downgradient monitoring points, and expected acid-neutralization and precipitation zone. The diagram is schematic and does not encode measured geometry or concentrations.

### Figure 2. Geochemical reaction-network design

#### Intent

Mechanistic workflow figure for the Methods section.

#### Scientific Content

Sulfide oxidation, acidity/sulfate release, carbonate buffering, Fe/Al hydroxide precipitation, U(VI) carbonate mobility, Ra sulfate/barite or sorption attenuation, Fe-Mn oxide interaction.

#### Caption Draft

Reaction-network design used to transfer PHREEQC prototype insight into PFLOTRAN chemistry blocks. Solid arrows indicate mechanistic dependencies; the network must be reduced to database-supported species, minerals, kinetic reactions, and sorption terms before PFLOTRAN execution.

### Figure 3. PFLOTRAN domain and boundary-condition plan

#### Intent

Model architecture figure for the Model Formulation section.

#### Scientific Content

2D structured cross-section, material regions, source flux, upgradient and downgradient hydraulic boundaries, base boundary, observation points.

#### Caption Draft

Draft PFLOTRAN 2D cross-section configuration. The figure shows region definitions, source-flux placement, possible hydraulic boundaries, and observation points. Boundary values are placeholders until measured hydraulic heads, seepage fluxes, and aquifer geometry are supplied.

### Figure 4. Dimensionless acid-buffer index heatmap

#### Intent

Screening visualization for problem decomposition and sensitivity planning.

#### Scientific Content

The index is defined as a dimensionless ratio between normalized sulfide/seepage forcing and normalized carbonate-buffer capacity. Values greater than one indicate acid forcing dominates the screening balance; values below one indicate buffer-dominated screening cases.

#### Caption Draft

Dimensionless acid-buffer screening index. The heatmap is derived from normalized scenario factors only and is intended to prioritize field measurements and sensitivity runs. It is not a measured acid-base accounting result and is not a PFLOTRAN simulation output.

### Figure 5. Retardation-screening breakthrough curves

#### Intent

Transport interpretation figure showing why constant-retardation screening is useful but insufficient.

#### Scientific Content

Analytic curves show front delay under assumed retardation factors. They explain how sorption can slow breakthrough while also showing why U(VI) under variable alkalinity and carbonate chemistry should not be reduced to a single constant Kd in the final model.

#### Caption Draft

Analytic breakthrough-screening curves under assumed retardation factors. Increasing retardation delays concentration breakthrough relative to a conservative tracer. These curves are not observation data; they are used to motivate chemistry-aware PFLOTRAN output interpretation.

### Figure 6. Sensitivity-analysis priority ranking

#### Intent

Uncertainty planning figure for the Calibration and Validation section.

#### Scientific Content

Prioritizes pyrite oxidation rate, carbonate buffering, seepage flux, sorption capacity, dispersivity, redox boundary location, barite/Ra database support, and permeability anisotropy.

#### Caption Draft

Expert-priority ranking for the first PFLOTRAN sensitivity campaign. The scores are design aids based on mechanism criticality and data-gap severity; they are not variance-based sensitivity indices from executed simulations.

### Figure 7. Executed PFLOTRAN pH profiles

#### Intent

Show the direct numerical test of the carbonate-buffering hypothesis.

#### Scientific Content

The figure plots 25-year pH profiles from two actual PFLOTRAN 1D synthetic screening runs: `calcite_buffered` and `no_calcite`.

#### Caption Draft

Executed PFLOTRAN 1D synthetic screening pH profiles after 25 years. In the calcite-buffered case, pH is acidic only in the first source-adjacent cell and remains near neutral to alkaline downstream. In the no-calcite case, the acidic front propagates through nearly the entire 100 m column. The result supports carbonate buffering as a pH-front control, but it is not a calibrated site prediction.

### Figure 8. Executed PFLOTRAN U and sulfate profiles

#### Intent

Show whether the minimum reaction network supports strong U or sulfate attenuation.

#### Scientific Content

The figure plots total UO2++ and sulfate profiles from the same 25-year PFLOTRAN outputs. Both variables reach the downgradient end in both scenarios under the current chemistry.

#### Caption Draft

Executed PFLOTRAN 1D synthetic screening UO2++ and sulfate profiles after 25 years. Under the simplified chemistry used for the minimum runnable test, sulfate and UO2++ advance to the outlet in both scenarios. Therefore, the executed run supports the pH-buffering mechanism but does not prove U, Ra, Pb, or Po attenuation.

## 4. Cross-Figure Visual Consistency

- Blue arrows: groundwater flow.
- Red/orange arrows or fields: acid/sulfate plume and source forcing.
- Green fields: neutralization, attenuation, and buffering.
- Purple fields: uranium-related mobility.
- Gray fields: low-permeability or uncertain/placeholder processes.
- Caveat line appears on every screening figure.

## 5. Data and Provenance Requirements

The conceptual and analytic screening figure data are saved under `data/` and were produced by `scripts/generate_figures.py`. Executed PFLOTRAN output figures were produced by `scripts/analyze_pflotran_outputs.py` from `pflotran_runs/*/*-005.tec`. SVG files preserve editable labels; PNG files are lightweight PDF-rendering fallbacks. Required provenance for final paper figures after actual model execution:

- PFLOTRAN version, database path/hash, input-deck hash.
- Observation point coordinates, CRS and model grid definition.
- Field sample medium, units, detection limits, analytical method and QA/QC status.
- Calibration/validation split and residual metrics.
- Exact plot script and exported dataset.

## 6. Caveats

The current figures are suitable for a methodology paper and model-design report. Figures 7-8 are executed synthetic PFLOTRAN outputs, but they should not be used as evidence of site plume extent, compliance, receptor risk, remediation performance, or model calibration.

## 7. Machine-Readable JSON Summary

The figure manifest is saved as:

`figure_manifest.json`
