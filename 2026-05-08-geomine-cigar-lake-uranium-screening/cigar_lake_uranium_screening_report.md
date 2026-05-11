# GeoMine AOI Screening: Cigar Lake Uranium Potential

Research date: 2026-05-08  
AOI: Cigar Lake Mine area, eastern Athabasca Basin, northern Saskatchewan, Canada  
Commodity: Uranium  
Deposit model: Unconformity-related uranium  
Research types: `aoi_screening`, `deposit_model_assessment`, `mineral_occurrence_context`, `geochemical_anomaly_interpretation`, `infrastructure_and_regulatory_context`

## Research Boundary

This is a research-assistance screening memo, not legal advice, investment advice, a Qualified Person opinion, a feasibility study, a reserve estimate, a permitting decision, or an environmental compliance opinion. Current reserves and resources are only reported from cited public sources and are not independently audited here.

## Executive Summary

Cigar Lake is not merely prospective for uranium; it is a known, operating, high-grade uranium mine and one of the strongest possible positive controls for uranium potential at the AOI scale. The best-supported interpretation is: confirmed very high uranium potential at the known mine/deposit scale, with additional near-mine potential best framed around extension and satellite targeting along documented structural, geophysical, alteration, and drill-tested trends.

The core evidence is strong across multiple independent lanes: Saskatchewan SMDI identifies Cigar Lake Mine as SMDI 1856, a production uranium deposit; Cameco's technical report describes a classic unconformity-related uranium setting at the Athabasca Group/Wollaston Group unconformity; current Cameco reserve reporting lists very high average U3O8 grade and large proven and probable reserves; and CNSC identifies Cigar Lake as an operating licensed uranium mine.

The main caution is that this screening is point/name based. No authoritative mine lease, claim, or AOI polygon was loaded, and GeoMine MCP tools currently planned Saskatchewan/CDoGS/Open Canada data discovery rather than retrieving live GIS layers. Local lake-water geochemistry near the approximate Cigar Lake point is weak within 25 km and should be treated as a data-gap/context signal, not as negative evidence against a deep, covered, already known deposit.

## Normalized Entities

| Entity | Normalized value | Provenance | Confidence |
|---|---:|---|---|
| AOI name | Cigar Lake Mine | User input plus SMDI record 1856 | High |
| Country/province | Canada, Saskatchewan | CNSC, SMDI, Cameco | High |
| Mineral occurrence id | SMDI 1856 | Government of Saskatchewan SMDI | High |
| NTS sheet | 074I02 | SMDI 1856 | High |
| Coordinate reference | NAD83 UTM Zone 13 | SMDI 1856 | High |
| UTM coordinate | 527220 E, 6436470 N | SMDI 1856 | High for point record |
| Approximate screening point | 58.066 N, -104.536 W | Analyst approximate point used only for local lake-water radius checks | Low to moderate |
| Commodity | Uranium | SMDI and Cameco | High |
| Associated commodities/pathfinders | Co, Cu, Pb, Ni, Zn, Mo, As | SMDI and Cameco technical report | High |
| Deposit model | Unconformity-related uranium | Cameco technical report | High |
| Status | Operating / production deposit | CNSC, Cameco, SMDI | High |

MCP note: `normalize_aoi` preserved the AOI string but warned that no authoritative geometry, claim lookup, NTS lookup, area calculation, or CRS transformation was performed. The analyst normalization above uses official public Cigar Lake records and keeps that geometry limitation in force.

## Evidence Lanes Used

- AOI / CRS / GIS normalization.
- Geology and structural context.
- Deposit model fit.
- Geochemistry and pathfinder context.
- Geophysics and exploration method context.
- Mineral occurrence and production context.
- Infrastructure, processing, regulatory, and environmental monitoring context.
- Data-gap and next-work planning.

## Evidence Matrix

| Lane | Evidence | Grade | Screening implication | Key limitation |
|---|---|---:|---|---|
| AOI and occurrence | SMDI record 1856 lists Cigar Lake Mine, project Cigar Lake, primary commodity uranium, associated Co/Cu/Pb/Ni/Zn, NTS 074I02, NAD83 UTM Z13 point, and status `Deposit: Production`. | A for identity/status | Confirms this AOI is a known producing uranium deposit. | SMDI warns that resource/reserve figures in the database are not NI 43-101 compliant unless explicitly designated. |
| Geology | Cigar Lake lies near the eastern Athabasca Basin margin at the Athabasca Group/Wollaston Group unconformity; Manitou Falls sandstone and Wollaston basement rocks host mineralization. | A | Very strong match to Athabasca unconformity uranium setting. | Public report-scale geology does not replace mine model data. |
| Structure | Technical report describes graphitic breccia/fault zones, east-west structural control, a basement high, and intersecting structures controlling clay alteration. | A | Strong structural vectoring and fluid-pathway evidence. | Needs raw structural and geophysical layers for new target ranking. |
| Alteration | SMDI and technical report describe bleaching, hematization, illite-chlorite clay alteration, quartz dissolution, and alteration halo around mineralization. | A | Strong hydrothermal alteration evidence consistent with the model. | Alteration footprint needs 3D and drillhole context for vectoring. |
| Mineralization | Technical report identifies high-grade mineralization at/proximal to the unconformity, mainly uraninite and pitchblende with Ni-Co arsenides and other metals. | A | Direct uranium mineralization evidence. | Existing mine evidence does not automatically extend beyond drilled zones. |
| Reserves and resources | Cameco reports, as of Dec. 31, 2025, Cigar Lake proven and probable reserves of 479.0 thousand tonnes at 16.33% U3O8, containing 172.4 million lb U3O8 on a 100% basis. | A | Confirms current high-grade reserve base from public company reporting. | Not independently audited in this screening. |
| Production | Cameco says Cigar Lake is in northern Saskatchewan, began commercial operation in May 2015, and had produced 174.5 million lb U3O8 on a 100% basis since commissioning as of Dec. 31, 2025. | A | Confirms operational proof of uranium endowment. | Production history is not a future production guarantee. |
| Geophysics | Technical report states the deposit was discovered by drilling EM geophysical anomalies; EM and resistivity surveys remain core exploration tools. | A | Supports continued near-mine targeting by conductors/resistivity/structure. | Raw geophysical grids were not loaded. |
| Local lake-water geochemistry | Local SGS-derived lake-water files have 17 samples within 25 km of the approximate point; U range is 0.0 to 0.0001 ppm, median 0.00005 ppm. Within 50 km, max U is 2.3 ppm at about 49.7 km. | B/C | Useful regional context; weak near-point surface signal. | Not decisive for a deep, covered, unconformity deposit; no QA/QC audit in this screen. |
| Processing/infrastructure | Cameco states Cigar Lake ore is processed about 70 km northeast at Orano's McClean Lake mill. | A | Established processing pathway materially supports project viability context. | GeoMine MCP did not calculate road, airstrip, power, or mill distances. |
| Regulation/environment | CNSC lists Cigar Lake as operating, licensed to Cameco, with licence issued July 1, 2021 and expiring June 30, 2031. CNSC IEMP reports 2020 and 2024 results consistent with Cameco data and no anticipated health impacts near the operation. | A | Active regulated uranium mine with current licence and monitoring context. | Licence conditions handbook was not obtained; regulatory context can change. |

## Key Findings By Lane

### 1. AOI / CRS / GIS

Evidence:

- SMDI 1856 identifies the Cigar Lake Mine and provides a point coordinate in NAD83 UTM Zone 13: 527220 E, 6436470 N, NTS 074I02.
- GeoMine MCP `normalize_aoi` did not geocode the AOI or infer geometry. It warned that authoritative geometry is required before distance, area, buffer, or proximity conclusions.

Interpretation:

- For a first-pass screen, the named AOI is sufficiently normalized as a point-level producing mine/deposit record.
- It is not sufficient for tenure, infrastructure-distance, environmental-buffer, Indigenous consultation, or claim-neighbor analysis.

### 2. Geology and Structure

Evidence:

- Cameco's technical report places the deposit at the unconformity between Athabasca Group sandstone and Wollaston Group basement rocks.
- The report identifies the Lower Pelitic unit of the Wollaston Group as favourable and describes the MF Formation as 420 to 445 m thick in the Cigar Lake area.
- The deposit is positioned on an east-west trending basement high, with graphitic pelite and sulphide-rich basement directly below uranium mineralization.
- Faulting, graphitic breccia zones, and intersecting structures are documented as key controls.

Interpretation:

- This is very strong geology/structure evidence for unconformity-related uranium potential.
- The strongest exploration controls are not generic basin presence alone, but the specific combination of redox boundary, graphitic/reactivated fault zones, clay alteration, and basement-high geometry.

### 3. Deposit Model Fit

Evidence:

- Cameco's technical report explicitly identifies Cigar Lake as an unconformity-related uranium deposit.
- The high-grade mineralization is at or close to the unconformity and is mainly uraninite and pitchblende, with Ni-Co arsenides and other associated metals.
- SMDI describes alteration and pathfinder association including U with As, Ni, Co, Cu, Mo, and Pb.

Fit assessment:

- Model: unconformity-related uranium.
- Fit: strong.
- Confidence: high.

Why:

- The AOI contains the deposit type being screened for.
- Core model elements are present: Athabasca unconformity, graphitic basement/fault zones, redox boundary, intense clay alteration, high-grade uranium oxides, and pathfinder metals.

### 4. Geochemistry

Evidence:

- Deposit-scale geochemistry is strongly supportive: SMDI and the technical report describe U mineralization with Ni, Co, Cu, Pb, Zn, Mo, As and rare earth element associations.
- Local repo lake-water data check:
  - Total checked samples: 566.
  - Samples within 25 km of the approximate point: 17.
  - U range within 25 km: 0.0 to 0.0001 ppm; median 0.00005 ppm.
  - Samples within 50 km: 365.
  - Max U within 50 km: 2.3 ppm at about 49.7 km from the approximate point.

Interpretation:

- Deposit-scale geochemistry strongly supports uranium potential.
- Local lake-water geochemistry does not add strong direct support at the approximate mine point. This is not a meaningful contradiction, because Cigar Lake is a deep, sandstone-covered, high-grade unconformity deposit with glacial cover and a strong structural/geophysical discovery history.
- Surface water/lake-water geochemistry should be treated as a regional screening layer, not a direct test of Cigar Lake ore potential.

### 5. Geophysics and Exploration

Evidence:

- Cameco's technical report says the Cigar Lake deposit was discovered in 1981 through drilling of geophysical anomalies, specifically electromagnetic conductors, located by airborne and ground surveys.
- The same report describes continued use of EM and resistivity methods across near-mine grids and lists Cigar East, Cigar West, Cigar Southwest, Powerline, Tucker, Waterbury, Kelly Bay, and other grids as exploration areas.
- Cigar East is described as an unconformity-style uranium zone east of CL Main, but no mineral resource is reported for it in the cited section.

Interpretation:

- For new work, geophysical conductors and resistivity/alteration signatures are materially more useful than surface geochemistry alone.
- Near-mine potential should be screened by integrating EM conductors, resistivity lows/highs, graphitic structures, clay alteration, drilling, and unconformity topography.

### 6. Mineral Occurrence, Reserves, and Production

Evidence:

- SMDI status: `Deposit: Production`.
- Cameco reports Cigar Lake as the world's highest-grade uranium mine and says it has produced 174.5 million lb U3O8 on a 100% basis since commissioning as of Dec. 31, 2025.
- Cameco's current reserve page lists proven and probable reserves as 479.0 thousand tonnes grading 16.33% U3O8 and containing 172.4 million lb U3O8 on a 100% basis, with 94.1 million lb Cameco share.
- Cameco states reserves and resources are reported under CIM definitions and NI 43-101.

Interpretation:

- The mine/deposit-scale uranium potential is confirmed and high confidence.
- Any forward-looking statement about mine life, expansion, or extensions still depends on current technical reports, reserve/resource updates, permitting, operating constraints, and commodity assumptions.

### 7. Infrastructure, Processing, and Regulatory Context

Evidence:

- Cameco states Cigar Lake ore is processed at Orano's McClean Lake mill about 70 km northeast of the mine.
- CNSC lists Cigar Lake as an operating uranium mine licensed to Cameco, with licence issued July 1, 2021 and expiring June 30, 2031.
- CNSC IEMP states 2020 and 2024 independent monitoring results are consistent with Cameco-submitted results and support CNSC's assessment that people and the environment near the operation are protected.
- GeoMine MCP `calculate_infrastructure_distance` did not calculate distances and identified the need for authoritative geometry, CRS, and infrastructure layers.

Interpretation:

- Existing processing and regulatory infrastructure materially de-risk the known operation compared with a greenfield uranium prospect.
- Regulatory and environmental evidence is supportive of current operating status, but any new expansion or exploration work still requires specific licence, permit, environmental, and consultation review.

## Assumptions

- The AOI means the Cigar Lake mine/deposit area, not the entire Waterbury property, all surrounding claims, a specific MARS disposition, or a custom exploration polygon.
- The SMDI point and approximate latitude/longitude are adequate for a screening memo only.
- Public official and company sources are sufficient for first-pass evidence-lane screening.
- Cameco's reserve/resource data are treated as current to their stated effective date of Dec. 31, 2025.
- Local lake-water geochemistry is treated as regional context, not as a decisive exploration test.
- No independent QP validation, resource audit, mine-plan audit, or environmental compliance audit was performed.

## Data Gaps

- No authoritative mine lease, claim, or project polygon was loaded.
- No live Saskatchewan GeoAtlas, SMDI API, SMAD, NRCan CDoGS, or Open Canada CKAN resources were downloaded through MCP.
- No raw drillhole collars, assays, downhole radiometrics, structural logs, clay mineralogy, density, geotechnical, hydrogeology, or 3D mine model data were accessed.
- No raw EM, resistivity, magnetic, gravity, or radiometric grids were loaded.
- No current MARS mineral tenure and neighboring claim scan was completed.
- The CNSC licence and licence conditions handbook were not obtained.
- IEMP data were noted but not independently reanalyzed.
- Local lake-water data were not QA/QC audited and may not be spatially or analytically adequate for deposit-scale interpretation.

## Conflicting Evidence And Cautions

- SMDI contains historical and descriptive resource/grade statements, but the SMDI page warns that reserves or resources in the database are not NI 43-101 compliant unless designated. For current reserve/resource conclusions, use Cameco's current reserve/resource reporting and technical reports instead.
- Weak near-point lake-water uranium values do not conflict with the known high-grade deposit because the deposit is deep, covered, structurally controlled, and was discovered through geophysics and drilling rather than direct surface geochemical expression.
- Current operating and environmental monitoring evidence does not imply that future expansion, new targets, or new work programs are automatically permitted.

## Confidence And Evidence Strength

| Question | Answer | Confidence |
|---|---|---:|
| Does the AOI contain uranium mineralization? | Yes, directly and materially. | High |
| Is the deposit model fit strong? | Yes, unconformity-related uranium fit is explicit and well supported. | High |
| Is there current production/reserve support? | Yes, based on Cameco and CNSC public sources. | High |
| Is near-mine extension potential plausible? | Yes, but requires drill/geophysics/structure integration. | Moderate |
| Can surface lake-water geochemistry alone rank targets here? | No. | High |
| Can this report support tenure, distance, or permitting decisions? | No, not without authoritative geometry and regulatory review. | High |

## Recommended Next Work Program

1. Resolve authoritative geometry:
   - Load SMDI 1856 geometry, mine lease ML 5521, MARS mineral dispositions, surface lease, and surrounding claim polygons.
   - Use a projected CRS suitable for northern Saskatchewan before computing area, buffers, and distances.

2. Build a public-source GIS package:
   - Saskatchewan GeoAtlas bedrock, surficial geology, mineral occurrences, faults/lineaments, geophysics, roads, power, water, protected areas, and administrative layers.
   - NRCan/Open Canada/CDoGS catalogue records for geochemistry and geophysics.

3. Compile technical report evidence:
   - Extract the Cigar Lake technical report sections on geology, exploration, drilling, sample preparation, QA/QC, resources/reserves, mining, processing, infrastructure, environmental studies, and adjacent-property exploration.
   - Separate CL Main, CLEXT, Cigar East, and other nearby grids as different target domains.

4. Target ranking:
   - Build an evidence grid using graphitic conductors, resistivity signatures, unconformity depth/topography, basement-high geometry, clay alteration, structure intersections, pathfinder geochemistry, and drill intercept density.
   - Do not rank drill targets from lake-water geochemistry alone.

5. Regulatory and environmental review:
   - Obtain the CNSC licence and licence conditions handbook.
   - Review CNSC regulatory actions, IEMP data, environmental monitoring reports, financial assurance decisions, and provincial approvals.
   - Separate current-operation compliance from new exploration or expansion permitting.

6. Reporting upgrade:
   - Create a QP-review-ready evidence binder with source ids, effective dates, CRS, scale, method, QA/QC status, and uncertainty notes.

## Sources And Provenance

Primary public sources:

- Cameco Cigar Lake operation page: `https://www.cameco.com/businesses/uranium-operations/canada/cigar-lake`
- Cameco Cigar Lake reserves and resources: `https://www.cameco.com/businesses/uranium-operations/canada/cigar-lake/reserves-resources`
- Cameco Cigar Lake technical report PDF: `https://www.cameco.com/sites/default/files/documents/cameco-2023-cigar-lake-technical-report.pdf`
- CNSC Cigar Lake Mine facility page: `https://www.cnsc-ccsn.gc.ca/eng/uranium/mines-and-mills/nuclear-facilities/cigar-lake/`
- CNSC Independent Environmental Monitoring Program, Cigar Lake: `https://www.cnsc-ccsn.gc.ca/eng/resources/maps-of-nuclear-facilities/iemp/cigar-lake/`
- Saskatchewan SMDI overview: `https://www.saskatchewan.ca/business/agriculture-natural-resources-and-industry/mineral-exploration-and-mining/saskatchewan-geological-survey/saskatchewan-mineral-deposit-index-smdi`
- Saskatchewan SMDI record 1856, Cigar Lake Mine: `https://mineraldeposits.saskatchewan.ca/Home/Viewdetails/1856`

GeoMine MCP sources used in this run:

- `normalize_aoi`, retrieved `2026-05-08T15:52:57.545468+00:00`
- `search_saskatchewan_mineral_data`, retrieved `2026-05-08T15:53:15.693585+00:00`
- `search_cdogs_surveys`, retrieved `2026-05-08T15:53:17.831605+00:00`
- `search_canada_geodata`, retrieved `2026-05-08T15:53:19.504704+00:00`
- `calculate_infrastructure_distance`, retrieved `2026-05-08T15:53:21.687677+00:00`

Local repo data used:

- `Skills/mining-AI/data/staging/geochemistry/lake_water_samples.csv`
- `Skills/mining-AI/data/staging/geochemistry/lake_water_measurements.csv`
- Source URL embedded in local data: `https://gis.saskatchewan.ca/egis/rest/services/Economy/Analytical_and_Rock_Property_Data/FeatureServer/0`
- Local retrieval timestamp embedded in data: `2026-04-22T00:41:50Z`

## Machine-Readable Summary

See `machine_readable_summary.json` in this directory.

