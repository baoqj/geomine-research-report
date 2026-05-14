# MCP and Source Provenance

## GeoMine MCP Use

### `normalize_aoi`

- Input: Athabasca Basin uranium mining district, northern Saskatchewan; approximate bbox lon -107 to -102, lat 56.5 to 59.0; facilities include Key Lake, McArthur River, Cigar Lake, McClean Lake, Rabbit Lake.
- Result: Local AOI normalizer preserved the AOI name and CRS request but did not geocode authoritative geometry.
- Warning kept: no authoritative geocoding, claim lookup, NTS lookup, area calculation, or CRS transformation was performed.
- How used: the paper treats the AOI as an analyst-defined screening bbox, not an official project boundary.

### `search_canada_geodata`

- Query: wildfire burned area severity, hydrometric climate, uranium mine radionuclide releases, northern Saskatchewan Athabasca Basin.
- Result: GeoMine returned Open Canada / Geo.ca and NRCan CDoGS as candidate registry sources.
- Warning kept: live HTTP retrieval is not implemented in this MCP version; planned catalogue requests are not evidence until fetched and parsed.
- How used: the script performed direct public API/file retrieval outside the MCP planner.

Additional phase-2 queries were made for:

- wildfire burn severity and post-fire severity mapping;
- MRDEM/CDEM elevation and hydrologic routing;
- Canadian Hydrospatial Network / National Hydro Network waterlines and waterbodies;
- Indigenous communities, drinking-water systems and water-intake receptor context.

Result: GeoMine MCP again returned catalogue/planned-request objects rather than live data. Direct public catalogue and service retrievals were therefore saved under `data/raw/catalog/`.

### `search_saskatchewan_mineral_data`

- Query: Athabasca Basin uranium mining district, uranium.
- Result: GeoMine identified Saskatchewan GeoAtlas/public geoscience data as a candidate source.
- Warning kept: no live Saskatchewan mineral data query was performed.
- How used: the paper notes Saskatchewan GeoAtlas as a future data source but does not use it as fetched evidence.

## Public Data Actually Downloaded and Parsed

| Dataset | Source URL | Local file | Retrieval role |
| --- | --- | --- | --- |
| CWFIS NBAC fire polygons | `https://cwfis.cfs.nrcan.gc.ca/geoserver/public/wfs` | `data/raw/nbac_athabasca_bbox_1986_2024.geojson` | Fire-year, fire-area, fire-cause, mine-to-fire proximity screening |
| ECCC climate daily observations | `https://api.weather.gc.ca/collections/climate-daily` | `data/raw/eccc_key_lake_daily_2020_2024.geojson` | Key Lake daily precipitation and post-fire rainfall windows |
| WSC HYDAT daily mean hydrometric data | `https://api.weather.gc.ca/collections/hydrometric-daily-mean` | `data/raw/wsc_06DA004_daily_2020_2024.geojson` | Regional discharge proxy for post-fire hydrologic response |
| WSC hydrometric stations | `https://api.weather.gc.ca/collections/hydrometric-stations` | `data/raw/wsc_hydrometric_stations_aoi.geojson` | AOI station inventory |
| CNSC radionuclide releases | `https://open.canada.ca/data/en/dataset/6ed50cd9-0d8c-471b-a5f6-26088298870e` | `data/raw/cnsc_uranium_mines_mills_radionuclide_loadings.xlsx` | Facility coordinates and annual U/Th/Ra/Pb/Po source terms |
| CNSC EARMP chemistry | `https://open.canada.ca/data/en/dataset/c372958b-9610-4153-9370-9583eb8d0a6b` and `https://maps-cartes.services.geo.ca/server_serveur/rest/services/CNSC/Eastern_Athabasca_Regional_Monitoring_Program_en/MapServer/0` | `data/raw/earmp_chemistry_data.xlsx`; `data/raw/earmp_layer0_features_*.geojson` | Regional receptor water/biota chemistry; surface-water pH, U, Ra-226, trace metals |
| MRDEM metadata and STAC | `https://open.canada.ca/data/en/dataset/18752265-bda3-498c-a4ba-9dfe68cb98da`; `https://datacube.services.geo.ca/stac/api/search?collections=mrdem-30` | `data/raw/catalog/open_canada_dem.json`; `data/raw/catalog/mrdem_stac_bbox.json` | DEM source discovery for future flow routing |
| CHN metadata | `https://open.canada.ca/data/en/dataset/ae385105-e48c-4b54-bd0f-dfb7303301cb` and CHN MapServer | `data/raw/catalog/chn_mapserver_layers.json` | Hydrography source discovery; current service coverage did not include AOI |
| NHN metadata | `https://open.canada.ca/data/en/dataset/a4b190fe-e090-4e6d-881e-b87956c07977` | `data/raw/catalog/nhn_package_show.json` | NHN work-unit download planning for northern Saskatchewan hydrography |
| Indigenous community infrastructure metadata | `https://open.canada.ca/data/en/dataset/62155d6f-9167-4972-b77c-b90734b628dc` | `data/raw/catalog/indigenous_community_infrastructure_package_show.json` | Community receptor context and water-system screening |
| StatCan freshwater intake metadata | `https://open.canada.ca/data/en/dataset/0aa3fa53-43ef-451f-bb35-cfb43ebf06fb` | `data/raw/catalog/statcan_freshwater_intake_metadata.json` | Drainage-region surface-water intake context |

## Key Data Limitations Preserved

- NBAC fire polygons are not clipped to the AOI; area is full intersecting fire-polygon area.
- Mine facility points come from CNSC/Open Canada NPRI-format releases, not surveyed facility boundary polygons.
- Key Lake climate stations 4063753 and 4063757 were co-located by station name and merged by maximum daily precipitation.
- WSC 06DA004 is a regional proxy, not a site-specific runoff gauge for every facility.
- No measured ash, soil, stream water, suspended sediment, sediment-core or porewater chemistry was available in this run.
- EARMP provides regional late-season surface-water chemistry and country-food chemistry, but not first-flush runoff, TSS, alkalinity, major ions, Eh, Pb-210, Po-210, grain-size fractions or sediment-core profiles.
- A national fire burn-severity layer for northern Saskatchewan was not downloaded in this run; burn severity remains a priority remote-sensing derivation or source-discovery gap.
- PHREEQC MCP tools were not available in this session. A local PHREEQC run was completed and documented in `models/phreeqc_run_manifest_phase2.md`.
