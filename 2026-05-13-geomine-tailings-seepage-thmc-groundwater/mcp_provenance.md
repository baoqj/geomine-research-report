# MCP Provenance Notes

Date: 2026-05-13  
Workflow: GeoMine Research + THMC Modeling skills  
Scenario: sulfide-bearing tailings seepage into shallow groundwater  

## MCP Calls

| Tool | Query purpose | Retrieval status | Scientific use in paper | Warnings |
|---|---|---|---|---|
| `normalize_aoi` | Normalize a generic sulfide-bearing tailings impoundment AOI | parsed, network not used | Confirms this is not a site-specific AOI; no geometry-driven claim is made | No province, coordinates, polygon, NTS sheet, or CRS transformation |
| `search_cdogs_surveys` | Discover Canadian public geochemical survey source lane | planned, network disabled | Used as candidate source for later baseline/geochemical context only | No live geochemical metadata; no analytical spreadsheet parsing; medium/method/detection limits unverified |
| `search_saskatchewan_mineral_data` | Discover Saskatchewan GeoAtlas/public geoscience source lane | planned, network disabled | Used as candidate regional geoscience/source-discovery lane only | No live ArcGIS/GeoAtlas query; layer date/CRS/scale/license unverified |
| `search_bc_minfile` | Discover BC MINFILE/mineral occurrence source lane | planned, network disabled | Used as candidate source-discovery lane only, not as occurrence evidence | No live record retrieval, AOI proximity, or target ranking |
| `fetch_dataset_metadata: nrcan-cdogs` | Check local registry metadata | parsed, local registry | Confirms endpoint exists in local registry; metadata incomplete | CRS, scale/resolution, and update date unavailable |
| `fetch_dataset_metadata: bc-minfile` | Check local registry metadata | parsed, local registry | No authoritative metadata was found in local registry | Metadata incomplete |
| `fetch_dataset_metadata: saskatchewan-geoatlas` | Check local registry metadata | parsed, local registry | No authoritative metadata was found in local registry | Metadata incomplete |

## Boundary Statement

The MCP layer supplied provenance-preserving source discovery, not live site measurements. The main paper therefore uses these MCP outputs as a data-acquisition and validation plan. It does not claim measured tailings mineralogy, porewater chemistry, hydraulic conductivity, sample counts, map CRS, detection limits, or calibrated model performance.
