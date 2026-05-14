# Figure Package: Wildfire and Extreme Rainfall Radionuclide Remobilization

## 1. Figure Strategy

The figure set supports a research paper rather than a decorative report. It moves from spatial evidence, to temporal fire/rainfall forcing, to radionuclide source terms, to screening synthesis, then to mechanistic and theoretical interpretation.

## 2. Figure Inventory

| Figure | Section | Type | Main message | Data source |
| --- | --- | --- | --- | --- |
| Fig. 1 | Study area and data | GIS screening map | Uranium mine/mill facilities spatially overlap the 2020-2024 wildfire disturbance domain. | CWFIS NBAC, CNSC/Open Canada, WSC stations |
| Fig. 2 | Results | Time-series bar/line chart | Wildfire disturbance is recurrent; 2021, 2023 and 2024 provide recent analysis windows. | CWFIS NBAC |
| Fig. 3 | Results | Event time-series | Fire timing, rainfall pulses and regional discharge must be analyzed at event scale, not only annually. | ECCC climate daily, WSC HYDAT daily mean |
| Fig. 4 | Results | Geochemical source-term heatmap | Facilities differ by U mass discharge and decay-series activity discharge. | CNSC/Open Canada radionuclide releases |
| Fig. 5 | Results/synthesis | Screening index bar chart | Rabbit Lake and McArthur River are highest-priority first-pass sampling targets under the current open-data model. | Processed multi-source index |
| Fig. 6 | Mechanism | Conceptual process diagram | Fire, ash, runoff, geochemical partitioning and exposure must be separated mechanistically. | Paper model |
| Fig. 7 | Theory | Dimensionless sensitivity plot | High Kd can reduce dissolved mobility while high TSS can still increase event-scale particulate load. | Derived equations |

## 3. Visual Grammar

- Purple triangles: uranium mine/mill facilities.
- Blue circles: WSC hydrometric stations.
- Red/orange polygons: NBAC wildfire perimeters.
- Blue bars/line: precipitation and discharge.
- Purple bars: final screening index.
- Green process block: geochemical partitioning.

## 4. Publication Checks

- Figures are SVG and reproducible from `scripts/analyze_wildfire_rainfall_radionuclide.py`.
- Map figure includes AOI bounds and source limitation text in caption context.
- Geochemical heatmap preserves units and does not add U kg to MBq activity values.
- Screening figure labels the index as research-priority only, not a dose or compliance result.
- Theoretical sensitivity plot is explicitly marked as non-calibrated.

## 5. Caveats

- The map is screening-grade because NBAC polygons are not clipped and facility polygons are not available.
- The hydrologic response figure uses WSC 06DA004 as a regional proxy.
- All figures require professional revision before journal submission, especially map scale bar, north arrow and final cartographic layout.

## 6. Phase-2 Figure Addendum

| Figure | Section | Type | Main message | Data source |
| --- | --- | --- | --- | --- |
| Fig. 8 | Integrated framework | Causal workflow diagram | The three directions form a causal sequence: screening, first-flush chemistry, then long-term sediment secondary source. | Paper model |
| Fig. 9 | Data and methods | Data-readiness matrix | Fire burn severity and sediment cores are the critical gaps; EARMP, CNSC, ECCC, WSC and NBAC are already usable. | Open Canada/Geo.ca catalog, downloaded data |
| Fig. 10 | Results | Multi-panel water-chemistry chart | EARMP surface water constrains recent regional pH, U and Ra-226 but does not capture first-flush peaks. | CNSC EARMP |
| Fig. 11 | Mechanism | Phase-partitioning sensitivity plot | High TSS and high Kd can make particle-bound flux dominate first-flush loads. | Derived equations |
| Fig. 12 | Prediction | Sediment secondary-source sensitivity plot | Long-term risk depends on retention, burial and resuspension, not only first-year dissolved concentration. | Derived model |
| Fig. 13 | Receptor map | Screening map | Facilities, EARMP communities and recent fire centroids define the initial source-pathway-receptor network. | NBAC, CNSC releases, EARMP |

### Phase-2 Publication Checks

- EARMP values are plotted as reported screening values; censored records are not treated as confirmed concentrations above detection limits.
- PHREEQC results are labelled as mechanism sensitivity because major ions, alkalinity, Eh, DOC and TSS are incomplete in EARMP.
- The receptor map uses community points, not verified drinking-water intake coordinates.
- Fire burn severity is explicitly marked as missing for northern Saskatchewan in this run.
