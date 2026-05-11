# GeoMine AOI Screening: Wollaston Lake East Uranium Potential

Research date: 2026-05-09  
Original request: screen `Athabasca Basin margin, Saskatchewan, Canada`, focusing on `WallaStone Lake East` and reported underground conductivity features.  
Normalized AOI: Wollaston Lake East / eastern Wollaston area, northern Saskatchewan, Canada.  
Commodity: uranium.  
Deposit model: Athabasca unconformity-related and shallow basement-hosted uranium.  
Research types: `aoi_screening`, `dataset_discovery`, `geophysical_interpretation`, `geochemical_anomaly_interpretation`, `deposit_model_assessment`, `work_program_design`.

## Research Boundary

This is a screening memo, not legal advice, investment advice, a Qualified Person opinion, a feasibility study, a reserve estimate, or a permitting decision. Conductivity, radioactive boulders, and geochemical anomalies are exploration evidence only; they do not establish mineralization, resources, reserves, or economic viability.

## Executive Summary

The Wollaston Lake East focus area is a credible uranium exploration target at the area scale, mainly because the official Saskatchewan EM Conductors layer and NRCan/Saskatchewan Geological Survey eastern Wollaston EM map products confirm a dense conductor evidence lane in the selected envelope. A live GeoAtlas query over the combined eastern Wollaston map-sheet envelope returned 867 EM conductor line features and 270 radioactive-boulder points. That is a meaningful geophysical/radioactivity signal for Athabasca-style target generation.

The evidence does not yet support a confirmed uranium deposit or drill-ready target conclusion. The queried Uranium Deposit Footprints layer returned zero overlapping deposit-footprint records in the focus envelope, the live Saskatchewan Analytical and Rock Property Data layer returned zero overlapping records, and the local lake-water geochemistry files also contain zero samples in the same envelope. CDoGS has relevant Wollaston/Athabasca regional geochemical surveys, but the reviewed surveys mostly cover west/northwest Wollaston and NEA/IAEA test-area context rather than directly filling the selected eastern Wollaston EM envelope.

The best working interpretation is moderate to high regional exploration potential, with a strong geophysical lane and a supportive radioactive-boulder lane, but low confidence for ranking specific drill collars until conductor quality, structure, radioactive-boulder source vectors, bedrock geology, alteration, geochemistry, assessment reports, and any drilling are integrated.

## Normalized Entities

| Entity | Normalized value | Confidence | Notes |
|---|---|---:|---|
| User AOI | Athabasca Basin margin, Saskatchewan, Canada; WallaStone Lake East | Medium | `WallaStone` treated as spelling variant of `Wollaston`. |
| Normalized focus area | Wollaston Lake East / eastern Wollaston area | Medium | No exact polygon supplied. |
| Jurisdiction | Saskatchewan, Canada | High | Normalized from user text and public sources. |
| Proxy focus envelope | `-103.9167,57.3667,-102.9167,57.8333` WGS84 | Medium | Derived from official eastern Wollaston EM map extents, not a claim boundary. |
| Primary NTS context | 64E/5, 64E/6, 64E/10, 64E/11, 64E/12, 64E/14, 64E/15 | Medium | Based on official EM map sheet titles. |
| Commodity | Uranium | High | User-specified and regionally relevant. |
| Model | Athabasca unconformity-related / shallow basement-hosted uranium | Medium | Appropriate for the Athabasca margin and Wollaston Domain context. |
| Key user hypothesis | Subsurface conductivity features are abundant underground | Medium | Treated as a targeting hypothesis; supported at surface/map-layer level by official EM conductor datasets, but not yet converted into conductor-quality rankings. |

MCP note: GeoMine `normalize_aoi` preserved the AOI string but warned that no authoritative geometry, claim lookup, NTS lookup, area calculation, or CRS transformation was performed. That limitation remains in force.

## Evidence Lanes

- AOI / CRS / GIS normalization.
- Canada geodata and Saskatchewan GeoAtlas discovery.
- NRCan CDoGS geochemistry discovery.
- Geophysics and conductivity.
- Radioactive boulders and near-surface radioactivity.
- Geochemistry and QA/QC.
- Uranium potential, deposit footprints, and mineral occurrence context.
- Deposit model fit.
- Infrastructure and work-program planning.

## Evidence Matrix

| Lane | Evidence | Source and provenance | Grade | Screening implication | Limitation |
|---|---|---|---:|---|---|
| AOI normalization | User AOI normalized to Wollaston Lake East / eastern Wollaston area. No polygon, claim id, or exact coordinate supplied. | GeoMine MCP `normalize_aoi`, retrieved 2026-05-09; analyst normalization. | C for geometry | Good enough for regional screening. | Not valid for tenure, distance, area, or drill-collar planning. |
| Geophysics / conductors | 867 EM conductor features in the combined eastern Wollaston envelope: 830 airborne EM and 37 ground EM. | Saskatchewan GeoAtlas EM Conductors FeatureServer layer 7; live ArcGIS query on 2026-05-09. | A for conductor presence | Strong conductor-focused target-generation lane. | Conductors are not uranium; official layer says locations may be 200-300 m off. |
| Detailed EM maps | 2023 NRCan/SGS eastern Wollaston EM map products include time-decay constant, apparent conductivity, magnetic derivatives, and interpretation sheets at 1:50,000 scale. | Government of Canada Publications Open Files 8966 and 8967. | A | Official confirmation that conductivity mapping is central in this area. | Map sheets need georeferenced extraction and interpretation. |
| Radioactive boulders | 270 radioactive-boulder points in the envelope; CPS median 350, max 22,000. | Saskatchewan GeoAtlas Radioactive Boulders layer 4; live ArcGIS query on 2026-05-09. | A for records; B/C for source vectoring | Supports prioritizing conductor corridors where boulders and conductor trends spatially align. | No populated U3O8 assay values in queried attributes; boulder transport not modeled. |
| Uranium potential | Resource Map Uranium Potential layer intersects the focus envelope. | Saskatchewan GeoAtlas Resource Map layer 11; live query. | B | Supports regional uranium favourability. | Queried attributes were null; regional prospectivity only. |
| Known deposit footprint | Uranium Deposit Footprints returned 0 overlapping features. | Saskatchewan GeoAtlas Uranium Deposit Footprints layer 5; live query. | A | No known mapped uranium deposit footprint confirmed inside the proxy envelope. | Does not replace SMDI/SMAD occurrence and assessment-report review. |
| Analytical / rock-property geochemistry | Live Analytical and Rock Property Data layer returned 0 records in the focus envelope; repo lake-water files also have 0 samples in the envelope. | Saskatchewan FeatureServer layer 0 plus local repo lake-water files. | B for coverage check | Geochemistry is a data gap for this exact focus area. | Absence from checked layers is not evidence of absence. |
| CDoGS regional geochemistry | CDoGS lists relevant Wollaston/Athabasca regional surveys: lake sediment/water, vegetation, peat/soil/till/vegetation, groundwater/lake sediment/lake water, and till. | NRCan CDoGS metadata pages; MCP CDoGS source planner. | A for metadata | Useful for background thresholds and regional context. | Most reviewed CDoGS footprints are west/northwest of Wollaston or NEA/IAEA area, not direct eastern-envelope coverage. |
| Nearby exploration context | Public company pages around the eastern Athabasca/Wollaston corridor report basement-hosted uranium targeting, VTEM/gravity/ANT/conductor targets, alteration, and anomalous drilling. | IsoEnergy East Rim and Geiger Energy Wollaston pages. | B/C | Confirms industry is using the same conductor-plus-basement uranium model nearby. | Company context requires assessment-report and QP verification. |
| Infrastructure | MCP infrastructure planner identified needed inputs; no distance calculated. | GeoMine MCP `calculate_infrastructure_distance`. | D | Infrastructure should be a later GIS lane after AOI geometry is fixed. | No road, power, airstrip, winter road, or mill distance is reported here. |

## Key Findings By Lane

### 1. AOI / CRS / GIS

The requested AOI is not yet a true GIS object. It is a name-based regional target: Wollaston Lake East / eastern Wollaston. For this screen, I used the combined official eastern Wollaston electromagnetic map envelope:

- Open File 8966 / GP 2023-1: W 103°55' to W 103°30', N 57°42' to N 57°22'.
- Open File 8967 / GP 2023-2: W 103°25' to W 102°55', N 57°50' to N 57°30'.

This is a pragmatic screening boundary only. The next technical step is to replace it with a claim block, grid, conductor corridor, or project polygon in the appropriate Saskatchewan projected CRS.

### 2. Geophysics / Conductivity

Evidence:

- The official EM Conductors layer returned 867 conductor line features inside the focus envelope.
- Most are airborne EM features, with a smaller ground EM component.
- Conductor types include VLF-EM, ZTEM, HLEM, MK VI, VTEM, VTEM+, and Input.
- NRCan/SGS 2023 eastern Wollaston EM map products provide apparent conductivity, time-decay constant, magnetic field products, and interpretation sheets.

Interpretation:

- This is the strongest evidence lane in the current screen.
- In an Athabasca margin uranium model, conductive trends can represent graphitic metasedimentary units and/or reactivated structures that are legitimate first-order targeting features.
- Conductivity by itself is not a discovery signal. Conductors must be ranked by geometry, depth, strike continuity, structural intersections, magnetic/gravity/resistivity context, alteration, radioactivity, geochemistry, and drilling.

### 3. Radioactive Boulders

Evidence:

- The official Radioactive Boulders layer returned 270 records in the same focus envelope.
- Reported CPS values range from 0 to 22,000, with a median of 350.
- Dominant assessment-file references include `64E11-0029`, `64E11-0027`, `64E12-0043`, `64E11-0031`, and `MAW00135`.

Interpretation:

- This is a supportive, independent radioactivity lane.
- The strongest near-term target ranking should look for conductor segments that are up-ice or plausibly source-linked to boulder clusters.
- A boulder field is not bedrock mineralization unless transport direction, lithology, assays, and source relation are resolved.

### 4. Canada Geodata / Saskatchewan GeoAtlas Lane

Relevant official data sources identified or queried:

- Saskatchewan GeoAtlas EM Conductors.
- Saskatchewan GeoAtlas Radioactive Boulders.
- Saskatchewan GeoAtlas Uranium Deposit Footprints.
- Saskatchewan Resource Map Uranium Potential.
- Saskatchewan Analytical and Rock Property Data.
- Saskatchewan GeoAtlas / SMAD / SMDI should be used next for assessment reports and mineral occurrences.
- Open Canada / Geo.ca was planned by MCP as a federal catalogue lane; catalogue discovery is not evidence until linked resources are fetched and parsed.

Interpretation:

- GeoAtlas can support a real evidence stack for this AOI, but the current MCP layer is still planner-level for Saskatchewan data. I therefore used live ArcGIS REST queries separately and documented them.

### 5. CDoGS Geochemistry Lane

Relevant CDoGS sources:

- `svy070011`: 1976 lake sediment and water survey, parts of NTS 64L, 74I, 74P, Wollaston Lake area; 426 sediment samples over about 3,000 km2.
- `svy070004`: 1980-1982 biogeochemical survey, NTS 64L and 74I, with small portions of 64E and 74H; black spruce twigs analyzed for uranium.
- `svy210284`: 1980 peat and associated-material sampling, NTS 74I/8 and 64L/5.
- `svy210422`: 1979-1980 groundwater, lake sediment, and lake water survey around Midwest and McClean Lake.
- `svy070007`: 1992 till sampling, NTS 64E, L, 74H, northeast Saskatchewan.

Interpretation:

- CDoGS is relevant for regional background and media-specific uranium/pathfinder thresholds.
- It is not yet direct proof for the eastern Wollaston conductor envelope because the key reviewed survey footprints mostly sit west/northwest of Wollaston Lake or at broader regional scale.
- The `svy070007` till survey is the CDoGS lane most likely to matter for the 64E eastern Wollaston area, but its raw data and method details need to be downloaded and normalized before interpretation.

### 6. Deposit Model Fit

Model assessed: Athabasca unconformity-related and shallow basement-hosted uranium.

Supportive evidence:

- Athabasca Basin margin / Wollaston Domain context.
- Dense EM conductor network.
- Radioactive-boulder clusters.
- Regional uranium potential layer intersection.
- Nearby industry targeting uses basement-hosted uranium, VTEM, gravity, ANT, EM conductors, alteration, and drilling.

Missing evidence:

- No confirmed uranium deposit footprint inside the focus envelope.
- No direct geochemical samples in the checked analytical/lake-water layers.
- No drillhole, alteration, lithology, resistivity, gravity, or assay integration.

Fit assessment: moderate to high at regional exploration scale; insufficient for drill-target ranking.

## Assumptions

- `WallaStone Lake East` means `Wollaston Lake East`.
- The focus area is the official eastern Wollaston EM-map-sheet area, not a specific claim block.
- User-reported underground conductivity is treated as a target hypothesis and is partially supported by official EM conductor and EM-map products.
- Conductive features are favorable only when they plausibly represent graphitic/reactivated basement structures and coincide with uranium/pathfinder evidence.
- CDoGS metadata are used for source planning and regional geochemistry context; no CDoGS analytical tables were downloaded in this run.

## Data Gaps

- Authoritative AOI polygon, claim ids, target-center coordinates, and ownership are missing.
- No SMAD assessment reports were retrieved for conductor files such as `64E-0005`, `64E-0015`, `64E05-0035`, `64E11-0029`, `64E11-0027`, or `64E12-0043`.
- No detailed EM sheet digitization or conductor-quality ranking was completed.
- No bedrock geology, faults, structural intersections, glacial drift thickness, ice-flow vectors, resistivity, gravity, or radiometric grids were overlaid.
- No CDoGS analytical data were downloaded and normalized by medium, method, units, and detection limits.
- No drilling, alteration, lithogeochemistry, downhole radiometrics, or QA/QC data were compiled.
- No infrastructure distances were calculated.

## Conflicting Evidence And Cautions

- Strong conductor density is supportive but not diagnostic. Conductors may reflect graphite, sulphides, clays, water-bearing structures, or unrelated lithologic contrasts.
- Radioactive boulders are supportive but can be transported. Without glacial-direction and source-bedrock analysis, they should not be assumed to sit directly over source mineralization.
- The absence of uranium deposit footprints and analytical-rock-property records in the queried envelope prevents a confirmed-deposit conclusion.
- CDoGS regional survey coverage around Wollaston is relevant but does not yet replace direct sampling over the eastern focus envelope.

## Confidence And Evidence Strength

| Question | Screening answer | Confidence |
|---|---|---:|
| Is Wollaston Lake East a credible uranium target area? | Yes, at regional exploration scale. | Moderate |
| Is the conductivity feature lane real enough to prioritize? | Yes, official EM conductor and EM map products support it. | High for conductor presence; low for mineralization inference |
| Is uranium mineralization confirmed inside the focus envelope? | Not by the queried uranium deposit footprint or analytical layers. | Moderate |
| Is geochemistry sufficient for target ranking? | No. It is a major data gap for the exact eastern envelope. | High |
| Is the area drill-ready based on this screen? | No. Needs integrated geophysics, geology, boulder vectors, geochemistry, assessment reports, and any historical drilling. | High |

## Recommended Next Work Program

1. Lock the AOI geometry:
   - Use exact claim ids, a project polygon, or selected conductor corridors.
   - Re-run all spatial queries in the Saskatchewan service CRS after geometry is confirmed.

2. Build the conductor-target layer:
   - Download/georeference Open File 8966 and 8967 sheets.
   - Extract late-channel apparent conductivity, interpretation, and magnetic-derivative information.
   - Rank conductor segments by continuity, depth proxy, cross-structure intersections, and coincidence with boulders.

3. Pull assessment reports:
   - Prioritize `64E-0005`, `64E-0015`, `64E05-0035`, `64E11-0029`, `64E11-0027`, `64E12-0043`, `64E11-0031`, `64E13-0038`, `MAW00135`, `MAW00315`, and related records.
   - Extract survey specs, conductor picks, boulder assays, geochemistry, geology, and drilling.

4. Build a glacial/vectoring model:
   - Overlay radioactive boulders with ice-flow indicators, surficial geology, drift thickness, and conductor trends.
   - Separate boulder clusters that are plausible source-proximal from transported anomalies.

5. CDoGS geochemistry:
   - Download the relevant CDoGS datasets.
   - Normalize sample media, analytical methods, units, detection limits, and QA/QC.
   - Use CDoGS to define background and anomaly thresholds, not as standalone drill targeting.

6. Target-ranking rule:
   - Advance only target cells where multiple lanes stack: conductor trend + structural intersection + radioactive boulder or compatible geochemical anomaly + favorable bedrock/cover setting + alteration or historical drilling.

## Sources And Provenance

- GeoMine MCP tools: `normalize_aoi`, `search_saskatchewan_mineral_data`, `search_cdogs_surveys`, `search_canada_geodata`, `calculate_infrastructure_distance`.
- Saskatchewan EM Conductors layer: `https://gis.saskatchewan.ca/egis/rest/services/Economy/Regional_Datasets_and_Compilations/FeatureServer/7`
- Saskatchewan Radioactive Boulders layer: `https://gis.saskatchewan.ca/egis/rest/services/Economy/Regional_Datasets_and_Compilations/FeatureServer/4`
- Saskatchewan Uranium Deposit Footprints layer: `https://gis.saskatchewan.ca/egis/rest/services/Economy/Regional_Datasets_and_Compilations/FeatureServer/5`
- Saskatchewan Resource Map Uranium Potential layer: `https://gis.saskatchewan.ca/arcgis/rest/services/Economy/Resource_Map/MapServer/11`
- Saskatchewan Analytical and Rock Property Data layer: `https://gis.saskatchewan.ca/egis/rest/services/Economy/Analytical_and_Rock_Property_Data/FeatureServer/0`
- Government of Canada Publications, eastern Wollaston EM Open File 8966: `https://publications.gc.ca/site/eng/9.930046/publication.html`
- Government of Canada Publications, eastern Wollaston EM Open File 8967: `https://publications.gc.ca/site/eng/9.930047/publication.html`
- Government of Canada Publications, Athabasca Basin Uranium Geochemistry Database Open File 7495: `https://publications.gc.ca/site/eng/9.958442/publication.html`
- CDoGS `svy070004`: `https://geochem.nrcan.gc.ca/cdogs/content/svy/svy070004_e.htm`
- CDoGS `svy070011`: `https://geochem.nrcan.gc.ca/cdogs/content/svy/svy070011_e.htm`
- CDoGS `svy210284`: `https://geochem.nrcan.gc.ca/cdogs/content/svy/svy210284_e.htm`
- CDoGS `svy210422`: `https://geochem.nrcan.gc.ca/cdogs/content/svy/svy210422_e.htm`
- CDoGS `svy070007`: `https://geochem.nrcan.gc.ca/cdogs/content/svy/svy070007_e.htm`
- IsoEnergy East Rim context: `https://www.isoenergy.ca/portfolio/canada/saskatchewan/east-rim/`
- Geiger Energy Wollaston context: `https://baselode.com/projects/wollaston/`

