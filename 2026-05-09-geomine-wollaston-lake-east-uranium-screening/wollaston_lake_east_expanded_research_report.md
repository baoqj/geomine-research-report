# Wollaston Lake East Uranium Potential: Expanded GeoMine Research Screening

Date: 2026-05-09  
Research mode: GeoMine Research AOI screening, deposit-model assessment, geodata discovery, evidence-matrix synthesis  
Requested focus: Wollaston Lake East / eastern Wollaston area, Saskatchewan, Canada, with special attention to subsurface conductivity features  
Output status: Expanded screening report, not a Qualified Person opinion, not an NI 43-101 technical report, and not a mineral resource, reserve, or economic assessment

## 1. Executive Summary

The expanded review supports a **moderate to locally high exploration-priority rating at the regional-to-target-generation scale** for uranium in the Wollaston Lake East focus area. The strongest positive evidence is not a single decisive dataset; it is the convergence of: dense electromagnetic conductor coverage, Wollaston-domain metasedimentary rocks, mapped major fault/shear corridors, a large radioactive-boulder population, multiple uranium/radiometric SMDI records, uranium-interest historical drillholes, and newly checked geochemistry layers that include 235 GSC lake-sediment records inside the working proxy envelope.

The highest-value exploration hypothesis remains a **shallow basement-hosted or basement-proximal uranium model along conductive Wollaston metasedimentary packages**, with local pegmatite/radiometric-boulder evidence acting as a parallel but not identical uranium vector. The conductivity evidence is important because Athabasca-style basement-hosted targets commonly use graphitic or sulphidic conductors as structural and lithological guides. However, the present evidence does **not** prove mineralization. Saskatchewan EM conductor metadata warns that conductor locations may be offset by about 200-300 m because many features were compiled from assessment files with variable location quality.

Compared with the previous short report, the main expansion and correction is the geochemical lane. The earlier note treated the local analytical layer as empty because only the Lake Water and Saskatchewan Lake Sediment layers were checked. This expanded review checked the full Saskatchewan **Analytical and Rock Property Data** service and found inside the proxy envelope:

- Lake Water Geochemistry: 0 records.
- Lake Sediment Geochemistry: 0 records.
- GSC Lake Sediment Analyses: 235 records.
- Lithogeochemistry Analyses: 0 records.
- Surficial Geochemistry Analyses: 13 records.
- Geochronology: 14 records.
- Radioisotopic Tracers: 13 records.
- Kimberlite Indicator Mineral Analyses: 0 records.

This materially improves the evidence base but does not by itself establish a uranium anomaly, because the lake-sediment values need background-normalization, lake-basin grouping, method normalization, and glacial transport interpretation. Within the 235 GSC lake-sediment records, uranium values in the `U` field range from 0.7 to 48.0, with a median of 4.5. The report does not rank individual samples because coordinates, analytical methods, detection-limit flags, and lake-catchment context require a separate geochemical QA/QC pass.

## 2. Normalized AOI And Scope

Original user expression:

- "WallaStone Lake East" / "Wollaston Lake East"
- "Athabasca Basin margin, Saskatchewan, Canada"
- Focus area with many underground conductivity features

Normalized AOI:

- Name: Wollaston Lake East focused screening AOI.
- Country: Canada.
- Province: Saskatchewan.
- Regional setting: eastern Wollaston Lake / eastern Wollaston area, near the eastern margin of the Athabasca Basin and adjacent basement domains.
- Working geometry: WGS84 proxy envelope `[-103.9167, 57.3667, -102.9167, 57.8333]`.
- Geometry status: proxy screening box only. It is not a claim boundary, legal property boundary, survey polygon, or permitting boundary.
- Recommended analysis CRS for later GIS work: Saskatchewan projected CRS from source layers, or a suitable UTM Zone 13N workflow after confirming all source layer transformations.

GeoMine MCP normalization result:

- `normalize_aoi` was run twice. The MCP preserved the name, province, country, and CRS assumption, but it did not parse the bbox as authoritative geometry. This is treated as a tool limitation and a reminder that all distance, area, and tenure conclusions remain unsafe until an authoritative AOI polygon is supplied.

Research boundary:

- This report is a screening and target-generation document.
- It does not state that the AOI contains a deposit.
- It does not estimate mineral resources or reserves.
- It does not validate historical work as current disclosure.
- It does not provide legal, investment, engineering, permitting, environmental, or Indigenous consultation advice.

## 3. Methods And Evidence Lanes

GeoMine Research lanes used:

1. AOI / CRS / provenance.
2. Saskatchewan geodata discovery and ArcGIS layer interrogation.
3. Canada geodata and NRCan CDoGS survey discovery.
4. Geology and structural context.
5. Geophysics / conductivity.
6. Radioactive boulders and glacial transport.
7. Mineral occurrences / Saskatchewan Mineral Deposit Index.
8. Drillholes and historical exploration.
9. Geochemistry and analytical data.
10. Infrastructure, tenure, and compliance caveats.
11. Deposit-model fit and target-generation logic.

GeoMine MCP tools used:

- `normalize_aoi`: preserved AOI name and CRS assumptions; flagged missing authoritative geometry.
- `search_saskatchewan_mineral_data`: returned a Saskatchewan GeoAtlas candidate-source plan; live ArcGIS querying is not implemented in the MCP version, so official ArcGIS REST calls were used separately.
- `search_cdogs_surveys`: returned an NRCan CDoGS source plan; live spatial filtering is not implemented in the MCP version, so CDoGS pages were reviewed separately.
- `search_canada_geodata`: returned Canada / Geo.ca and CDoGS source-planning records; planned request only.
- `calculate_infrastructure_distance`: returned required inputs and caveats; no real infrastructure distance was calculated.
- `summarize_dataset_provenance`: summarized supplied Saskatchewan dataset provenance; did not independently verify metadata.

Primary data sources actually queried or reviewed:

- Saskatchewan GeoAtlas / ArcGIS Regional Datasets and Compilations.
- Saskatchewan GeoAtlas / ArcGIS Geology, Geological Domains, Quaternary, Mineral Exploration, and Analytical and Rock Property Data services.
- Saskatchewan Mineral Deposit Index government records and SMDI web links.
- NRCan CDoGS survey metadata pages.
- Government of Canada Publications / Geological Survey of Canada open files for eastern Wollaston EM maps and Athabasca uranium geochemistry.
- Selected company disclosures for regional analogue and neighboring exploration context, treated as lower-grade evidence than government data.

## 4. Expanded Evidence Matrix

| Lane | Evidence | Observation inside or near proxy AOI | Interpretation for uranium potential | Provenance | Confidence | Key caveat |
|---|---:|---|---|---|---|---|
| AOI normalization | Proxy bbox | WGS84 envelope `-103.9167,57.3667,-102.9167,57.8333` used for screening | Adequate for regional source discovery and broad counts | User focus + prior eastern Wollaston map-sheet framing + GeoMine MCP | Medium for screening | Not a claim/property boundary |
| Conductivity | 867 EM conductor features | 830 airborne EM, 37 ground EM | Strong regional targeting signal; conductors are a key exploration guide for basement-hosted uranium | Saskatchewan Regional Datasets FeatureServer layer 7 | Medium-high | Compiled conductor locations may be 200-300 m off |
| Conductor type | VLF-EM dominant | VLF-EM 767; ZTEM 44; HLEM 33; MK VI 9; VTEM 9; VTEM+ 4; Input 1 | Multiple survey types suggest repeated historical interest, but conductor quality differs materially by method | Saskatchewan EM Conductors layer | Medium | VLF linework alone is not enough to rank drill targets |
| Conductor age/source | Assessment-file compilation | Major EM file numbers include 64E-0005, 64E-0015, 64E05-0035, 64E13-0038; years mainly 1979, 1992, 2009-2012 | Older and newer data coexist; modern reprocessing could add value | Saskatchewan EM Conductors attributes | Medium | Need raw survey grids and interpretation maps |
| GSC EM maps | OF 8966 and OF 8967 | Eastern Wollaston area covered by 2023 GSC/SGS EM map sheets; OF 8967 covers longitudes roughly W 103°25' to W 102°55' and latitudes N 57°50' to N 57°30' | High-quality regional conductivity and magnetic context for the focus area | Government of Canada Publications OF 8966/8967 | High for source existence | Map products need georeferenced extraction before line ranking |
| Geological domains | 3 domain polygons | Peter Lake, Wollaston, Wathaman domains intersect the proxy AOI | Wollaston-domain rocks are most relevant for Athabasca-style basement-hosted uranium; Peter Lake adds competing Ni-Cu-PGE/base-metal context | Saskatchewan Geological Domains MapServer | Medium-high | Domain intersection is regional, not target-scale |
| Bedrock geology | 98 bedrock 250k features | Peter Lake domain 54 features; Wollaston 43; Wathaman 1 | Mixed basement setting with metasedimentary and intrusive packages | Saskatchewan Geology MapServer layer 10 | Medium | 1:250k scale is coarse for prospect ranking |
| Wollaston lithology | Metasediments present | Wollaston Group pelitic/psammopelitic gneiss, mixed metasediment, felsic gneiss, metaquartzite, meta-arkose, amphibolite | Pelitic/psammopelitic rocks can host graphitic/sulphidic conductors and structural traps | Saskatchewan Bedrock 250k attributes | Medium | Need graphite, sulphide, alteration, and structure confirmation |
| Peter Lake lithology | Intrusive/mafic packages present | Swan River Complex gabbro/gabbronorite/pyroxenite, granitoids, syenogranite, pegmatite | Competing models include base metals, Ni-Cu-PGE, REE/pegmatite; not all conductors are uranium-positive | Saskatchewan Bedrock 250k attributes | Medium | Could dilute uranium targeting unless conductors coincide with U evidence |
| Faults/shears | 25 faults 250k; 10 major faults/shears 1M | Major mapped features include Tabbernor fault, Needle Falls shear zone NW/SE, Parker Lake shear zone | Regional structural corridors can focus fluid flow and reactivate conductive packages | Saskatchewan Geology MapServer layers 1 and 2 | Medium | Need detailed structural interpretation and kinematics |
| Structure form lines | 111 features | Feature attributes are sparse; count only used | Adds structural complexity, but weakly attributed | Saskatchewan Regional Datasets layer 6 | Low-medium | Cannot rank structures without orientation/type |
| Radioactive boulders | 270 records | CPS range 0-22,000; median 350; mean 964.8 | Strong surface radiometric signal and source-vector opportunity | Saskatchewan Radioactive Boulders layer 4 | Medium-high | U3O8 assay field empty for all 270 records queried |
| Boulder lithology | Granite/gneiss/arkose/pegmatite common | Common lithologies include granite, biotite gneiss, granitic gneiss, meta-arkose, pegmatite, leucogranite | Suggests many radiometric boulders may be basement/pegmatitic or granitoid-derived rather than direct unconformity mineralization | Saskatchewan Radioactive Boulders attributes | Medium | Needs boulder chemistry, transport direction, and source tracing |
| Boulder source files | Assessment concentration | 64E11-0029:129; 64E11-0027:84; 64E12-0043:25; 64E11-0031:15; MAW00135:14; MAW00315:3 | Assessment-file retrieval should be a priority because a few files drive most boulder evidence | Saskatchewan Radioactive Boulders attributes | High for counts | File content not yet reviewed |
| Ice-flow indicators | 157 records | 147 striae; azimuth min 137, median 216, max 240; most in 180-224 bin | Glacial transport is likely generally south to southwest in the queried records, relevant for back-tracing radioactive boulders | Saskatchewan Ice-Flow Indicators layer 1 | Medium | Direction confidence field mostly blank |
| Uranium deposit footprints | 0 footprints | No uranium deposit footprint intersects the proxy envelope | Negative evidence against known deposit overlap | Saskatchewan Uranium Deposit Footprints layer 5 | High for queried layer | Absence of footprint is not absence of prospectivity |
| MDI occurrences | 130 records | 19 primary uranium records; 24 uranium/radiometric/thorium-related records using strict commodity/name filters | Meaningful historical uranium/radiometric occurrence density | Saskatchewan Mineral Exploration MapServer layer 5 + SMDI | Medium-high | Occurrence points do not prove extensions into the AOI |
| MDI discovery type | Float and grab dominant | 62 float-rock discoveries, 52 outcrop grabs, 12 drillhole discoveries overall | Many records are early-stage surface finds rather than drilled systems | SMDI attributes | Medium | Location accuracy and field evidence vary |
| MDI status | Mostly early stage | 65 mineral locations, 31 bedrock/felsenmeer geochemical anomalies, 26 primary exploration occurrences, 3 prospects, 2 advanced exploration deposits overall | Regional exploration maturity is mixed; uranium-specific records are mostly showings/anomalies | SMDI attributes | Medium | Need record-by-record geological summaries |
| Drillholes | 98 drillhole records | 97 with length; total known length about 23.5 km; median length 234 m | Existing historical drill density is useful for basement depth and prior targeting | Saskatchewan Drillholes layer 3 | Medium | Assays and alteration logs not parsed |
| Uranium drill interest | 8 uranium-interest holes | Beeching Lake, Spence Lake, Morwick Lake records from 1969-1970 era | Historical uranium exploration occurred in the broad focus area | Saskatchewan Drillholes attributes | Medium | Need assessment files and assay intervals |
| Cover / basement depth | 67 values | Base of Athabasca sandstone / top crystalline basement depth min 0.3 m, median 6.0 m, max 135.1 m | Supports shallow-basement / thin-cover exploration framing in many records | Saskatchewan Drillholes attributes | Medium | Drillhole locations/projects may not evenly represent whole AOI |
| GSC lake sediment | 235 records | U field range 0.7-48.0, median 4.5; GSC_OF 1643; NTS 064E | Material geochemical evidence now confirmed in AOI | Saskatchewan Analytical FeatureServer layer 2 | Medium-high for data existence | Needs normalization by method, lake basin, LOI, and detection flags |
| Surficial geochemistry | 13 records | Peter Lake Domain till samples; U_PPM max 1.3, median 0.0 in queried attributes | Adds till context but weak uranium signal in these records | Saskatchewan Analytical FeatureServer layer 4 | Medium | Small clustered sample set |
| Geochronology / isotopes | 14 geochronology, 13 radioisotopic records | Ages span about 1581-3100 Ma; Hearne/Reindeer/Wollaston-related basement context | Useful for crustal-domain context, not direct uranium targeting | Saskatchewan Analytical FeatureServer layers 5 and 6 | Medium | Not direct mineralization evidence |
| CDoGS geochemistry | Multiple regional surveys | Relevant surveys include svy070004, svy070011, svy070007, svy210284, svy210422 | Provides regional lake sediment/water, vegetation, till, peat, groundwater context | NRCan CDoGS | Medium | MCP did not live-filter; survey pages need data extraction |
| Regional analogues | Rabbit Lake / East Rim / Wollaston projects | Nearby eastern Athabasca margin has basement-hosted uranium exploration analogues | Supports deposit-model plausibility | Government SMDI + company pages | Low-medium | Company claims are not independent evidence for this AOI |
| Tenure | Not resolved | Mineral Tenure Crown Dispositions FeatureServer required token in this run | Cannot state claim status or ownership | Saskatchewan tenure endpoint | Low | Must use MARS/official tenure export |
| Infrastructure | Not calculated | MCP planner said authoritative AOI + CRS + infrastructure layers are required | No reliable distance to road, power, airstrip, mills calculated | GeoMine MCP infrastructure planner | Low | Later analysis needed in projected CRS |

## 5. Conductivity And Geophysics Lane

The AOI contains a dense compilation of EM conductors. The query returned **867 conductor features** inside the working proxy envelope:

- Survey type: 830 airborne EM and 37 ground EM.
- Conductor type: 767 VLF-EM, 44 ZTEM, 33 HLEM, 9 MK VI, 9 VTEM, 4 VTEM+, and 1 Input.
- Main file-number concentrations: `64E-0005` with 762 records, `64E-0015` with 32 records, `64E05-0035` with 22 records, and a variant ` 64E05-0035` with 21 records.
- Work years in the feature attributes are dominated by 1979 and 1992, with additional records in 2009, 2010, 2011, 2012, and isolated older/newer entries.

Interpretation:

- The conductor density is a genuine positive exploration-lane signal, especially because the user specifically noted underground conductivity features.
- Conductors are most useful when they can be tied to graphitic or sulphidic Wollaston metasedimentary rocks, major structures, alteration, and uranium/radiometric/geochemical support.
- The current conductor evidence is still a hypothesis generator. The next step is not simply "drill conductors"; it is to rank conductor segments by persistence, depth, conductance, late-time response, magnetic disruption, structural bends, and coincidence with radiometric boulders or uranium geochemistry.

Key caution:

- The Saskatchewan EM Conductors metadata states the data are compiled from assessment files and that locations may be offset by about 200-300 m because of datum/projection uncertainty and poor location maps. This is material for field planning and drill targeting.

Government of Canada EM maps:

- GSC/SGS Open File 8966: eastern Wollaston area, parts of NTS 64-E/5, 6, 11, and 12, 2023.
- GSC/SGS Open File 8967: eastern Wollaston area, parts of NTS 64-E/10, 11, 14, and 15, 2023.
- OF 8967 is especially relevant to the eastern side of the proxy area because its catalogue cartographic coverage is W 103°25' to W 102°55' and N 57°50' to N 57°30'. It includes time-decay constant, apparent conductivity, residual magnetic field, first vertical derivative, and interpretation sheets.

Practical target-ranking implication:

1. Treat VLF-EM-only linework as lower-confidence unless supported by ground EM, modern airborne EM, or bedrock/structure evidence.
2. Promote segments where ZTEM, HLEM, VTEM, or modern GSC conductivity maps corroborate older conductors.
3. Promote north-south bends, offsets, breaks, and conductor intersections near major fault/shear corridors.
4. Demote conductors fully explained by lakes, overburden, cultural noise, graphitic barren schist without alteration, or mafic/ultramafic/base-metal-only context.

## 6. Geological And Structural Lane

The proxy envelope intersects three geological domains:

- Wollaston.
- Peter Lake.
- Wathaman.

The 1:250k bedrock query returned 98 features:

- Domain count: Peter Lake 54, Wollaston 43, Wathaman Batholith 1.
- Group/formation count: Wollaston Group 21; most other records do not have a populated group field.
- Notable bedrock units and lithologies include:
  - `Wpsn`: pelitic and psammopelitic gneiss.
  - `Ws`: mixed metasediment in the Wollaston Group / Courtney-Cairns Lake Belt.
  - `Wm`: amphibolite.
  - `Wfn`: felsic gneiss.
  - `Wq`: metaquartzite.
  - `Wr`: meta-arkose.
  - `Wpeg`: granitic pegmatite.
  - `Psm` and `Psmx`: Swan River Complex gabbroic and derived gneissic rocks.
  - `Pga`, `Pg`, and related granitoids.

Uranium model relevance:

- The Wollaston Group metasedimentary package is the most relevant host-framework evidence for an Athabasca-style basement-hosted uranium hypothesis.
- Pelitic/psammopelitic rocks are important because graphitic and sulphidic horizons can form conductors and can be favorable chemical/structural traps.
- Pegmatite and granitic sources are also relevant because many radioactive boulder and SMDI records are described as radioactive pegmatite, radiometric anomaly, or U-Th-Mo-bearing float. This may represent a separate pegmatite/radiometric-boulder target family, not necessarily the same as classic unconformity-associated uranium.

Structural evidence:

- Faults 250k: 25 features intersect the proxy envelope.
- Major faults and shear zones 1M: 10 features, including Tabbernor fault, Needle Falls shear zone NW/SE, and Parker Lake shear zone.
- Structure form lines: 111 features, but attributes are sparse, so they are counted but not heavily interpreted.

Interpretation:

- Major fault/shear corridors increase the plausibility of fluid focusing and structural reactivation.
- Uranium target confidence increases where EM conductors are disrupted by cross-structures or bends and where the same corridor carries uranium, radiometric boulder, or pathfinder geochemical evidence.
- Regional-scale faults are not sufficient by themselves. A target-scale structural interpretation using magnetics, EM, bedrock, and outcrop/field mapping is needed.

## 7. Radioactive Boulder And Ice-Flow Lane

The radioactive-boulder layer returned **270 records** inside the proxy AOI:

- CPS count: 270.
- CPS minimum: 0.
- CPS median: 350.
- CPS mean: 964.8.
- CPS maximum: 22,000.
- U3O8 assay field: empty for all 270 queried records.

Dominant assessment-number sources:

- `64E11-0029`: 129 records.
- `64E11-0027`: 84 records.
- `64E12-0043`: 25 records.
- `64E11-0031`: 15 records.
- `MAW00135`: 14 records.
- `MAW00315`: 3 records.

Common boulder lithologies:

- Granite: 37.
- Biotite gneiss: 24.
- Granitic gneiss: 22.
- Meta-arkose: 17.
- Pegmatite: 15.
- Leucogranite: 15.
- Granite gneiss: 12.
- Quartzite, amphibolite, flaser granite, biotite granite, biotite schist, and other metasedimentary/granitic categories are also present.

Interpretation:

- The radioactive-boulder lane is materially supportive but requires caution. High CPS values and numerous records are significant, but the empty U3O8 assay field means the boulder layer does not provide verified uranium grade for these queried records.
- Boulder lithologies suggest many anomalies may be derived from granitoid, gneissic, meta-arkosic, or pegmatitic sources. Some may vector to uranium-bearing pegmatite/radiometric rocks rather than to unconformity-style ore.
- The highest-priority follow-up is to retrieve the dominant assessment files and extract boulder coordinates, lithology, scintillometer method, U/Th ratio if available, assay values, and interpretation of transport direction.

Ice-flow indicators:

- 157 ice-flow indicator records were queried.
- Flow type: 147 striae, plus minor crescentic fractures/gouges, crag-and-tail, striation, and drumlin records.
- Azimuth statistics: minimum 137°, median 216°, maximum 240°, mean about 215°.
- 45° bins: 4 records in 135-179°, 129 records in 180-224°, 24 records in 225-269°.

Glacial interpretation:

- The queried ice-flow indicators are consistent with dominant south to southwest transport in the proxy area.
- For boulder back-tracing, source search should generally look up-ice, while recognizing multi-phase ice flow and local lake/shoreline reworking could complicate simple back-projection.
- Direction-confidence attributes were mostly blank, so this should be used as a first-pass vector rather than a final boulder-source model.

## 8. Mineral Occurrences / SMDI Lane

The Mineral Deposits Index query returned **130 records** inside the proxy AOI.

Overall commodity distribution:

- Zinc: 33.
- Iron: 27.
- Copper: 23.
- Uranium: 19.
- Lead: 10.
- Rare earth element: 3.
- Graphite: 3.
- Beryl: 2.
- Molybdenum: 2.
- Fluorine: 2.
- Arsenic, silver, tin, gold, amazonite, thorium: one each.

Overall status distribution:

- Mineral Location: 65.
- Anomaly: Bedrock/Felsenmeer Geochemical: 31.
- Occurrence: Primary Exploration: 26.
- Prospect: Primary Exploration: 3.
- Anomaly: 3.
- Deposit: Advanced Exploration: 2.

Overall discovery-type distribution:

- Float Rock: 62.
- Outcrop grab: 52.
- Drillhole: 12.
- Trench: 2.
- Glacial Till: 1.
- Null: 1.

Strict uranium/radiometric/thorium-related subset:

Using a conservative filter based on primary commodities, associated commodities, grouping, and names containing radioactive/radiometric/uranium, 24 records were flagged:

| SMDI | Name | Primary / associated commodities | Status | Discovery type |
|---|---|---|---|---|
| 0543 | Pyett Lake Beryliferous / Amazonstone / Allanite Pegmatites | Beryl; F, LREE, REE, Th | Occurrence | Outcrop grab |
| 0552 | Charles Lake Radiometric Anomaly Number 7 | U | Mineral Location | Float rock |
| 0553 | Charles Lake Radiometric Anomaly Number 8 | U | Mineral Location | Outcrop grab |
| 0561 | Morwick Lake west radioactive pegmatite | U; REE | Mineral Location | Outcrop grab |
| 0588 | Cook Lake east radioactive pegmatite float | U | Mineral Location | Float rock |
| 0589 | Radiometric Anomaly No. 9 / Radiometric Zone 3 | U; Th | Occurrence | Outcrop grab |
| 0590 | Morwick Lake northeast radioactive pegmatite | U | Mineral Location | Outcrop grab |
| 0607 | Woodward Lake radioactive anomalies | U | Mineral Location | Outcrop grab |
| 1702 | Lake L-2 radioactive boulder train | U | Bedrock/Felsenmeer geochemical anomaly | Float rock |
| 1703 | Geikie River west radioactive pegmatite | U; Th | Occurrence | Outcrop grab |
| 1707 | Horton Island northeast peninsula U-Th pegmatite | U; Th | Occurrence | Outcrop grab |
| 1708 | Nekweaga Bay radioactive pegmatite | U | Mineral Location | Outcrop grab |
| 1823 | Anomaly 41 Uranium Showing | U; Cu | Mineral Location | Outcrop grab |
| 1850 | Chip Sample 11677 | U | Mineral Location | Outcrop grab |
| 1851 | Chip Sample 11543 | U | Mineral Location | Outcrop grab |
| 1891 | Radioactive Pegmatite Boulder PM-102 | U; Pb, Th | Bedrock/Felsenmeer geochemical anomaly | Float rock |
| 1892 | Cook Lake east radioactive pegmatite / sample 80CA-203RO | U; Mo | Occurrence | Outcrop grab |
| 1893 | Radioactive Pegmatite Boulder 80CA-90RB | U; Mo, Th | Bedrock/Felsenmeer geochemical anomaly | Float rock |
| 1894 | Cook Lake east radioactive anomaly 5 / sample 80CA-200RB | U; Mo, Th | Bedrock/Felsenmeer geochemical anomaly | Float rock |
| 1895 | Radioactive Pegmatite Boulder 80CA-14RB | U; Mo, Th | Bedrock/Felsenmeer geochemical anomaly | Float rock |
| 2380 | Fordham Lake Sn-Pb Showing | Sn; Pb, W, U | Occurrence | Outcrop grab |
| 2639 | Lyle Lake nepheline-bearing pegmatite/plug | REE; apatite, Be, F, LREE, Nb, Ti, U | Occurrence | Outcrop grab |
| 5531 | Sample JBWLR015 | REE; Th | Anomaly | Float rock |
| 5786 | Samples CSWLR006 and MKWLR022 | Th; REE, U | Anomaly | Float rock |

Interpretation:

- The occurrence lane is supportive because uranium/radiometric/thorium-related records are numerous and thematically consistent with the boulder lane.
- The occurrence lane also shows a competing exploration story: many records are float, outcrop grab, radioactive pegmatite, or U-Th-Mo-bearing boulder/anomaly records. These should not be automatically interpreted as basement-hosted unconformity-style uranium.
- High-priority occurrence clusters for follow-up include Charles Lake radiometric anomalies, Morwick Lake radioactive pegmatites, Cook Lake east radioactive pegmatite/boulder records, the Lake L-2 radioactive boulder train, and Beeching/Spence/Morwick uranium drill contexts.

SMDI caution:

- The Government of Saskatchewan notes that SMDI is a database of known mineral showings and includes a disclaimer. Any reserve or resource figures in the database should not be treated as NI 43-101 compliant unless specifically designated as such. This report uses SMDI only as occurrence evidence.

## 9. Drillhole Lane

The Saskatchewan drillhole layer returned **98 drillhole records** inside the proxy AOI.

Drillhole source-file distribution:

- `64E05-0035`: 36.
- `MAW00080`: 20.
- `64E05-0033`: 8.
- `MAW02607`: 8.
- `64E11-0016`: 5.
- `64E12-0024`: 4.
- `MAW00505`: 4.
- Other smaller sources include `64E05-0018`, `64E12-0021`, `64E11-0008`, `64E12-0051`, `64E06-0008`, and several singletons.

Company / project distribution:

- Canadian Platinum Corp.: 56 holes, largely Peter Lake Project.
- Golden Arch Resources: 8 holes, Wakefield Lakes.
- Fission 3.0: 8 holes, Simon Lake.
- Great Plains Development Company: 5 holes, Beeching Lake.
- Falconbridge-related entries: 9 holes combined.
- Strike Graphite: 4 holes.
- Esso Minerals Canada, Massval Mines, Far West Mining, Voyageur Petroleum, and SGS/SRC entries also appear.

Commodity-of-interest distribution:

- Null: 77.
- Zinc: 9.
- Uranium: 8.
- Lead/Zinc: 2.
- Copper/Lead/Zinc: 2.

Drilling metrics:

- 97 holes have length values.
- Minimum length: 3.8 m.
- Median length: 234.12 m.
- Maximum length: 682.8 m.
- Total known drilled length: about 23,515 m.

Base of Athabasca sandstone / top crystalline basement:

- 67 records have values.
- Minimum: 0.3 m.
- Median: 6.0 m.
- Maximum: 135.1 m.
- Mean: about 22.1 m.

Uranium-interest drillholes:

| Hole | Source | Project | Company | Date | Length |
|---|---|---|---|---|---:|
| 002 | 64E11-0016 | Beeching Lake | Great Plains Development Company | 1969-01-27 to 1969-02-07 | 239.9 m |
| 001A | 64E11-0016 | Beeching Lake | Great Plains Development Company | 1969-01-14 to 1969-01-18 | 137.1 m |
| 001 | 64E05-0018 | Spence Lake | Massval Mines Limited | date not populated | 156.0 m |
| 001 | 64E11-0016 | Beeching Lake | Great Plains Development Company | 1969-01-13 to 1969-01-21 | 185.9 m |
| 2-70 | 64E05-0018 | Spence Lake | Massval Mines Limited | 1970-01-01 | 215.0 m |
| 1-70 | 64E06-0008 | Morwick Lake | Voyageur Petroleum Ltd. | 1970-08-10 to 1970-08-14 | 30.2 m |
| 003 | 64E11-0016 | Beeching Lake | Great Plains Development Company | 1969-02-12 to 1969-02-23 | 106.6 m |
| 004 | 64E11-0016 | Beeching Lake | Great Plains Development Company | date not populated | 93.8 m |

Interpretation:

- The drilling lane confirms that uranium exploration occurred historically in the focus area.
- Shallow basement values are supportive for a basement-hosted or thin-cover exploration approach and can reduce drilling cost relative to deep Athabasca sandstone targets.
- However, the drillhole layer does not provide assay intervals, alteration logs, structures, conductor tests, or reasons why holes were drilled. Those must be extracted from the source assessment files before any conclusion can be made about missed potential or negative historical results.

## 10. Geochemistry And CDoGS Lane

### 10.1 Saskatchewan Analytical And Rock Property Data

The expanded review checked all eight layers in the Saskatchewan Analytical and Rock Property Data FeatureServer.

Layer counts inside the proxy envelope:

| Layer | Name | Count | Screening implication |
|---:|---|---:|---|
| 0 | Lake Water Geochemistry | 0 | No local evidence from this layer |
| 1 | Lake Sediment Geochemistry | 0 | No local evidence from this specific layer |
| 2 | GSC Lake Sediment Analyses | 235 | Important geochemical evidence lane |
| 3 | Lithogeochemistry Analyses | 0 | Data gap for direct rock chemistry |
| 4 | Surficial Geochemistry Analyses | 13 | Limited till evidence |
| 5 | Geochronology | 14 | Basement context, not direct anomaly evidence |
| 6 | Radioisotopic Tracers | 13 | Crustal/source context, not direct anomaly evidence |
| 7 | Kimberlite Indicator Mineral Analyses | 0 | Not material to uranium screening |

GSC Lake Sediment Analyses:

- Count: 235.
- NTS sheet: 064E for all queried records.
- GSC open file field: 1643.
- Lake depth range: 1-21 m; median 3 m.
- LOI range: 3.0-73.8; median 37.0.
- U field: minimum 0.7, median 4.5, maximum 48.0.
- U_INA field is populated as strings and needs numeric parsing with detection-limit handling.
- Other potentially relevant fields include As, Mo, Th_INA, Pb, Cu, Ni, Zn, Fe, Mn, LOI, sediment colour, suspended material, lake area, and terrain relief.

Interpretation:

- The existence of 235 GSC lake-sediment records is a significant improvement over the previous geochemical lane.
- The maximum U value of 48.0 is potentially interesting, but should not be ranked without checking units, method, duplicate/control status, LOI correction, lake-basin hydrology, and background thresholds.
- Lake sediment can reflect adjacent or up-ice bedrock, drainage, glacial material, and lake chemistry. It is not a direct drill target without spatial and geological normalization.

Surficial geochemistry:

- Count: 13.
- Project: Peter Lake Domain.
- Sample type: till.
- Analytical lab: Saskatchewan Research Council Geoanalytical Laboratories.
- U_PPM range in queried records: -2.0 to 1.3, median 0.0.
- Cu_PPM maximum: 260.
- Sample descriptions include routine B-horizon and Bm-horizon diamicton.

Interpretation:

- This small cluster does not show a strong uranium signal in the queried U_PPM field.
- It still matters because it provides surficial/geochemical context in Peter Lake domain rocks and can help separate uranium targeting from base-metal/mafic-system signals.

Geochronology and radioisotopic tracers:

- Geochronology: 14 records; age range about 1581-3100 Ma; isotopic systems include U-Pb, Rb-Sr, and K-Ar.
- Radioisotopic tracers: 13 records; sample materials include arkose, amphibolite, argillite, pelite, syenite, feldspathic arenite, rhyolite, calcic pelite, granite, and psammopelite.

Interpretation:

- These layers support geological context and crustal-domain interpretation but are not direct uranium-anomaly evidence.

### 10.2 NRCan CDoGS

CDoGS surveys relevant to the Wollaston / eastern Athabasca margin context include:

- `svy070004`: Biogeochemical survey, NTS 64L and 74I, northern Saskatchewan, 1980-1982. It describes black spruce twig sampling across the NEA/IAEA Test Area and around Wollaston Lake, with U analysis by delayed-neutron counting. Geographic extent includes parts of 64L, 74I, small portions of 64E and 74H, and mentions Wollaston Lake / Rabbit Lake context.
- `svy070011`: Lake sediment and water survey, parts of NTS 64L, 74I, and 74P, Wollaston Lake area, 1976. The standard page states 426 sediment samples across about 3000 km2 at about one sample per 7 km2, with surface waters collected at all sites. The extended/data page reports 83 sites in the CDoGS loaded coverage and analytical bundles for water U/F and lake sediment U and multi-element analysis.
- `svy070007`: Till sampling, NTS 64E, 64L, and 74H, northeast Saskatchewan, 1992. It covers the Peter Lake Domain, Morwick, Weatherup, Lyle lakes, and Highway 905, with 55-element till analysis and U by fluorometry. This is directly relevant to the eastern Wollaston / Peter Lake focus.
- `svy210284`: Peat, soil, till, and vegetation sampling around the NEA-IAEA Athabasca Basin / Wollaston Lake test area, 1980, including McClean/Midwest-related coverage; more west/northwest than the proxy AOI but relevant for regional methods and uranium pathfinder context.
- `svy210422`: Groundwater, lake sediment, and water survey around Midwest and McClean Lake uranium deposits, 1979-1980. It is not within the proxy envelope but is important as an analogue for geochemical expression near known uranium deposits west/northwest of Wollaston Lake.

Geochemistry next step:

1. Download CDoGS spreadsheets for the exact surveys and restrict to the proxy AOI plus a glacial up-ice buffer.
2. Normalize sample media separately: lake sediment, lake water, vegetation, till, peat, groundwater.
3. Normalize analytical methods, units, detection limits, and negative-coded values.
4. Build U, Th, U/Th, Mo, As, Ni, Co, Cu, Pb, Zn, V, REE, LOI, pH, F, conductivity, and redox/pathfinder maps.
5. Compare anomalies against ice-flow direction, lake catchments, conductor corridors, Wollaston metasediments, and SMDI/boulder clusters.

## 11. Canada Geodata Lane

Canada-first data sources reviewed or identified:

- Government of Canada Publications:
  - Open File 8966 and 8967 eastern Wollaston electromagnetic maps.
  - Open File 7495 Athabasca Basin Uranium Geochemistry Database.
- NRCan CDoGS:
  - Survey metadata and spreadsheet/data links for lake sediment/water, till, vegetation, peat, and groundwater surveys.
- Open Canada / Geo.ca:
  - GeoMine MCP built a planned CKAN request for Wollaston Lake East uranium/geophysics/geochemistry terms, but the MCP version does not execute live HTTP retrieval.

Interpretation:

- Canadian federal data strengthens the report because it provides independent government geophysical and geochemical coverage beyond Saskatchewan GeoAtlas layers.
- The most immediate federal-source task is to georeference or download OF 8966/8967 interpretation products and cross-check them against the Saskatchewan EM conductor layer. Conductors present in both old assessment-derived linework and 2023 GSC/SGS products should be promoted.

## 12. Deposit-Model Fit

Primary model assessed:

- Athabasca Basin margin, unconformity-associated and basement-hosted uranium, especially shallow basement-hosted targets on conductive Wollaston metasedimentary packages.

Secondary or competing models:

- U-Th-Mo or U-REE-bearing radioactive pegmatite / radiometric boulder sources.
- Base-metal / VMS-like or graphitic-sulphidic conductors.
- Peter Lake domain Ni-Cu-PGE / mafic-ultramafic systems.
- REE/alkaline/pegmatite systems.

Expected evidence for a stronger basement-hosted uranium target:

- Graphitic or sulphidic pelitic metasedimentary conductor.
- Structural disruption, bend, offset, cross-fault, or shear intersection.
- Uranium pathfinder geochemistry: U, Ni, Co, As, Cu, Pb, Mo, V, B, P, REE, clay/alteration indicators, radiogenic Pb, or appropriate hydrogeochemical signals.
- Alteration: clay, chlorite, hematite/bleaching, desilicification, brecciation, silicification, carbonate, dravite, or redox features depending on local model.
- Radiometric boulder trains or surface anomalies that can be back-traced up-ice to conductor/structure intersections.
- Historical drilling that either did not test the highest-priority conductor segment or was shallow/poorly oriented relative to structure.

Observed fit:

- Conductors: supportive.
- Wollaston metasedimentary rocks: supportive.
- Major structures: supportive at regional scale.
- Radioactive boulders: supportive, but source type uncertain.
- SMDI uranium/radiometric occurrences: supportive, but mostly early-stage surface/float/grab records.
- Historical uranium-interest drilling: supportive for exploration history, inconclusive for remaining potential.
- Geochemistry: now materially improved due to 235 GSC lake-sediment points, but needs a dedicated anomaly analysis.
- Deposit footprints: absent in the proxy AOI, which is negative for known-deposit overlap but not negative for exploration potential.

Fit assessment:

- Regional geological model fit: **moderate to strong**.
- Current target-scale confidence: **moderate**, constrained by missing conductor ranking, assays, alteration, raw geophysical grids, and assessment-file review.
- Drill-ready status: **not drill-ready from this report alone**.

## 13. Target Themes

### Theme A: Conductive Wollaston metasedimentary corridors

Rationale:

- Dense EM conductor population.
- Wollaston Group pelitic/psammopelitic/mixed metasedimentary rocks.
- Regional major faults and shear zones.
- Shallow basement suggested by many drillhole records.

Best next test:

- Rank conductor segments using OF 8966/8967 map products, raw/processed EM where available, magnetic breaks, structure intersections, and boulder/geochemical support.

Priority:

- Highest conceptual priority for basement-hosted uranium.

### Theme B: Charles Lake - Morwick Lake - Cook Lake radiometric / radioactive pegmatite trend

Rationale:

- Multiple SMDI uranium/radiometric records: Charles Lake radiometric anomalies, Morwick radioactive pegmatites, Cook Lake radioactive pegmatite float/grab records.
- U-Th-Mo/REE associations suggest radiometric source rocks may be present.
- Boulder evidence is abundant and often granitoid/gneiss/pegmatite related.

Best next test:

- Pull SMDI records and assessment files; compile U/Th ratios, boulder source vectors, outcrop geology, and relationship to conductor trends.

Priority:

- High for radiometric/pegmatite-source vectoring; moderate for classic basement-hosted uranium until conductor/structure linkage is proven.

### Theme C: Beeching Lake / Spence Lake / Morwick Lake uranium-interest drilling

Rationale:

- Eight uranium-interest drillholes occur in the queried drillhole layer.
- Historical drilling dates mostly 1969-1970, suggesting old targeting and older geophysical/geochemical constraints.

Best next test:

- Retrieve assessment files `64E11-0016`, `64E05-0018`, and `64E06-0008`; extract collar coordinates, azimuth/dip, logs, assays, radiometrics, alteration, structure, and target rationale.

Priority:

- High for historical due diligence; target priority depends on results of file review.

### Theme D: Peter Lake domain conductor/base-metal distraction filter

Rationale:

- Peter Lake domain has many bedrock and drillhole records.
- MDI distribution includes abundant Zn, Cu, Fe, Pb and base-metal groupings.
- Canadian Platinum / Peter Lake Project drillhole concentration suggests non-uranium exploration may dominate parts of the proxy AOI.

Best next test:

- Classify conductors by host domain and associated commodity evidence. Demote conductors explained by mafic/base-metal-only systems unless uranium/radiometric/geochemical evidence is coincident.

Priority:

- Important negative-filter / risk-reduction workflow.

## 14. Assumptions

This report uses the following assumptions explicitly:

- The user’s "WallaStone Lake East" refers to Wollaston Lake East / eastern Wollaston Lake area in Saskatchewan.
- The working WGS84 proxy envelope is acceptable for regional screening but not for land, distance, area, tenure, permitting, or drill planning.
- Saskatchewan ArcGIS features returned by envelope intersection are treated as intersecting the proxy envelope, not necessarily lying within an eventual claim or property polygon.
- EM conductors are interpreted as exploration guides, not as mineralization.
- Radioactive boulders and radiometric anomalies indicate uranium/thorium/radiometric potential, but not necessarily economic uranium mineralization.
- CDoGS surveys and Saskatchewan analytical layers require method and unit normalization before anomaly thresholds can be applied.
- Company project pages are used only for regional analogy and neighboring-exploration context; government datasets carry higher evidentiary weight.

## 15. Data Gaps

Critical gaps:

- Authoritative AOI polygon or claim boundary.
- Official tenure status and ownership from MARS / Saskatchewan mineral tenure data.
- Raw or gridded EM data, conductor picks, conductivity-depth sections, and interpretation sheets from OF 8966/8967 and assessment files.
- Conductor ranking by quality, conductance, depth, geometry, and structural setting.
- Assessment-file review for the boulder-heavy files `64E11-0029`, `64E11-0027`, `64E12-0043`, `64E11-0031`, `MAW00135`, and `MAW00315`.
- Assessment-file review for uranium drill files `64E11-0016`, `64E05-0018`, and `64E06-0008`.
- Assay values for boulders, outcrops, and drillholes; the queried radioactive-boulder U3O8 field is empty.
- Alteration/mineralogy data: clay, hematite, chlorite, graphite, sulphide, radiogenic Pb, dravite/tourmaline, carbonate, breccia, silicification.
- Geochemical anomaly normalization for the 235 GSC lake-sediment records and 13 till records.
- Glacial transport model with confidence-ranked ice-flow phases.
- Infrastructure distances to roads, winter roads, airstrips, power, camps, water access, and mills.
- Environmental, Indigenous rights/consultation, protected-area, land-use, fish/wildlife, and water-quality constraints.
- Modern QA/QC and field verification.

Moderate gaps:

- Bedrock geology is 1:250k in the current query; target-scale mapping is needed.
- Structure form-line attributes are sparse.
- Drillhole layer lacks assay intervals and target rationale.
- The uranium deposit footprint layer shows no deposit footprint in the proxy AOI, but this does not test undiscovered potential.
- Geochronology and isotope layers are useful context but not yet integrated into a uranium fertility model.

## 16. Recommended Next Steps

### Step 1: Lock AOI geometry

- Obtain the actual claim polygon, target polygon, or working exploration block boundary.
- Store it as GeoJSON and projected GIS layers.
- Re-run all layer intersections using a confirmed CRS and buffer rules.

### Step 2: Build a conductor ranking table

For every conductor segment or conductor corridor, compile:

- Conductor ID / source file.
- Survey type and method.
- Year and data quality.
- Length, orientation, continuity, bends, breaks, offsets.
- Host domain and host bedrock unit.
- Proximity to major structures and cross-structures.
- Coincident magnetic breaks or gradients.
- Coincident radioactive boulders, SMDI uranium records, drillholes, and geochemical anomalies.
- Field-access constraints.
- Priority score and reason.

### Step 3: Retrieve assessment files

Priority assessment sources:

- Boulder files: `64E11-0029`, `64E11-0027`, `64E12-0043`, `64E11-0031`, `MAW00135`, `MAW00315`.
- EM files: `64E-0005`, `64E-0015`, `64E05-0035`, `64E13-0038`, `64E12-0035`, `64E06-0016`, `MAW00343`, `MAW00344`, `64E11-0032`, `64E13-0062`, `MAW01847`.
- Uranium drill files: `64E11-0016`, `64E05-0018`, `64E06-0008`.
- Geochemistry / Peter Lake domain files tied to SGS Data File 27 and GSC OF 1643 where applicable.

### Step 4: Run geochemistry normalization

- Parse GSC lake sediment fields as numeric with detection-limit flags.
- Separate partial extraction and INAA fields.
- Build U, U_INA, Th_INA, U/Th, Mo, As, Pb, Cu, Ni, Co, Zn, V, Fe, Mn, LOI, lake depth, sediment colour, and terrain relief maps.
- Compare each anomaly against local background and lake-basin class.
- Integrate with ice-flow direction and boulder source interpretation.

### Step 5: Field verification

Possible field program sequence:

1. Prospecting and scintillometer verification over boulder/SMDI clusters.
2. Boulder sampling for U3O8, U/Th, Pb isotopes where appropriate, REE, Mo, As, Ni, Co, Cu, V, and QA/QC blanks/duplicates/standards.
3. Ground truthing of conductor corridors with ground EM or fixed-loop EM where warranted.
4. Radon-in-water, lake sediment infill, soil/till orientation surveys only after media suitability is confirmed.
5. Geological mapping of graphite/sulphide, alteration, structure, pegmatite, and radiometric outcrop.

### Step 6: Drill-target readiness gate

A conductor segment should not be advanced to drill-ready status until it has:

- Confirmed geometry in modern geophysics.
- Geological host validation.
- Structural trap evidence.
- Supporting radiometric, geochemical, alteration, or boulder-vector evidence.
- A review of historical drilling showing either no test, poor test, shallow test, or unresolved anomaly.
- Access, environmental, and tenure feasibility screened.

## 17. Provisional Ranking

Area-level ranking:

- Regional uranium potential: **moderate-high**.
- Current target-scale certainty: **moderate**.
- Drill-ready confidence: **low to moderate**, pending conductor ranking and assessment-file review.

Why not higher:

- No uranium deposit footprint intersects the proxy AOI.
- Radioactive boulder assays are not populated in the queried layer.
- Uranium drillholes are historical, sparse, and not yet tied to assays/logs.
- EM conductors are abundant but not yet quality-ranked.
- Tenure and infrastructure distances are unresolved.

Why not lower:

- Conductivity evidence is dense and multi-source.
- Wollaston metasedimentary host rocks are present.
- Major fault/shear corridors are mapped.
- Radioactive boulders are abundant.
- SMDI has a strict subset of 24 uranium/radiometric/thorium-related records.
- Historical uranium-interest drilling exists.
- 235 GSC lake-sediment geochemical records are now confirmed inside the proxy envelope.

## 18. Compliance And Disclosure Caveats

- This report is research assistance only.
- No Qualified Person has reviewed or approved the interpretations.
- No mineral resource, mineral reserve, exploration target tonnage/grade range, or economic conclusion is stated.
- Historical drillholes, occurrences, and assessment-file records are not validated as current disclosure.
- SMDI records are government inventory records, not proof of mineral continuity.
- Company disclosures are used only as context and should be independently verified before use in any investment, filing, or transaction setting.
- Environmental, permitting, Indigenous consultation, and land-access issues were not assessed.

## 19. Source And Provenance Register

Saskatchewan official sources:

- Saskatchewan GeoAtlas / Regional Datasets and Compilations FeatureServer: `https://gis.saskatchewan.ca/egis/rest/services/Economy/Regional_Datasets_and_Compilations/FeatureServer`
- EM Conductors metadata: `https://gisappl.saskatchewan.ca/WebDocs/Geo_Atlas/MetaData/EM_Conductors.html`
- Radioactive Boulders metadata: `https://gisappl.saskatchewan.ca/WebDocs/Geo_Atlas/MetaData/Radioactive_Boulders.html`
- Uranium Deposit Footprints metadata: `https://gisappl.saskatchewan.ca/WebDocs/Geo_Atlas/MetaData/Uranium_Deposit_Footprints.html`
- Saskatchewan Geology MapServer: `https://gis.saskatchewan.ca/arcgis/rest/services/Economy/Geology/MapServer`
- Saskatchewan Geological Domains MapServer: `https://gis.saskatchewan.ca/arcgis/rest/services/Economy/Geological_Domains/MapServer`
- Saskatchewan Quaternary MapServer: `https://gis.saskatchewan.ca/arcgis/rest/services/Economy/Quaternary/MapServer`
- Saskatchewan Mineral Exploration MapServer: `https://gis.saskatchewan.ca/arcgis/rest/services/Economy/Mineral_Exploration/MapServer`
- Saskatchewan Analytical and Rock Property Data FeatureServer: `https://gis.saskatchewan.ca/egis/rest/services/economy/Analytical_and_Rock_Property_Data/FeatureServer`
- GSC Lake Sediment Analyses layer: `https://gis.saskatchewan.ca/egis/rest/services/economy/Analytical_and_Rock_Property_Data/FeatureServer/2`
- Saskatchewan Mineral Deposit Index: `https://www.saskatchewan.ca/business/agriculture-natural-resources-and-industry/mineral-exploration-and-mining/saskatchewan-geological-survey/saskatchewan-mineral-deposit-index-smdi`

NRCan / Government of Canada sources:

- GSC/SGS Open File 8966, eastern Wollaston EM survey: `https://publications.gc.ca/site/eng/9.930046/publication.html`
- GSC/SGS Open File 8967, eastern Wollaston EM survey: `https://publications.gc.ca/site/eng/9.930047/publication.html`
- GSC Open File 7495, Athabasca Basin uranium geochemistry database: `https://publications.gc.ca/site/eng/9.958442/publication.html`
- CDoGS home: `https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm`
- CDoGS `svy070004`: `https://geochem.nrcan.gc.ca/cdogs/content/svy/svy070004_e.htm`
- CDoGS `svy070011`: `https://geochem.nrcan.gc.ca/cdogs/content/svy/svy070011_e.htm`
- CDoGS `svy070007`: `https://geochem.nrcan.gc.ca/cdogs/content/svy/svy070007_e.htm`
- CDoGS `svy210284`: `https://geochem.nrcan.gc.ca/cdogs/content/svy/svy210284_e.htm`
- CDoGS `svy210422`: `https://geochem.nrcan.gc.ca/cdogs/content/svy/svy210422_e.htm`

Context / analogue sources, lower evidence weight:

- Forum Energy Metals Wollaston project page: `https://forumenergymetals.com/projects/wollaston/`
- Forum Energy Metals 2021 Wollaston gravity survey news: `https://forumenergymetals.com/news/2021/forum-commences-gravity-survey-on-its-wollaston-uranium-project-saskatchewan/`
- IsoEnergy East Rim project page: `https://www.isoenergy.ca/portfolio/canada/saskatchewan/east-rim/`
- Baselode / Geiger Energy Wollaston project page: `https://baselode.com/projects/wollaston/about-wollaston/`

## 20. Machine-Readable Summary

```json
{
  "aoi": {
    "normalized_name": "Wollaston Lake East focused screening AOI",
    "province": "Saskatchewan",
    "country": "Canada",
    "proxy_bbox_wgs84": [-103.9167, 57.3667, -102.9167, 57.8333],
    "geometry_status": "proxy screening envelope only"
  },
  "commodity": "uranium",
  "deposit_model": "Athabasca margin basement-hosted / unconformity-associated uranium, with pegmatite-radiometric competing target family",
  "headline_rating": {
    "regional_potential": "moderate-high",
    "target_scale_confidence": "moderate",
    "drill_ready_confidence": "low-to-moderate"
  },
  "key_counts": {
    "em_conductors": 867,
    "airborne_em": 830,
    "ground_em": 37,
    "radioactive_boulders": 270,
    "ice_flow_indicators": 157,
    "mdi_records": 130,
    "strict_uranium_radiometric_thorium_mdi_records": 24,
    "drillholes": 98,
    "uranium_interest_drillholes": 8,
    "gsc_lake_sediment_records": 235,
    "surficial_geochemistry_records": 13,
    "geochronology_records": 14,
    "radioisotopic_tracer_records": 13,
    "uranium_deposit_footprints": 0
  },
  "highest_priority_next_steps": [
    "confirm authoritative AOI polygon",
    "rank conductor corridors against OF 8966 and OF 8967 EM products",
    "retrieve key boulder, EM, and uranium drill assessment files",
    "normalize GSC lake sediment geochemistry and CDoGS surveys",
    "build glacial boulder-source vector model",
    "resolve tenure and access constraints"
  ],
  "major_caveats": [
    "not a QP opinion or NI 43-101 technical report",
    "proxy AOI only",
    "conductor positions may have 200-300 m uncertainty",
    "radioactive boulder U3O8 assay field empty in queried layer",
    "drillhole assays and logs not parsed",
    "tenure and infrastructure distances unresolved"
  ]
}
```

