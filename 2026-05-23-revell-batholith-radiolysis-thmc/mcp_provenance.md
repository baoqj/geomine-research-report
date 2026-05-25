# MCP Provenance

GeoMine Research skills were used in local/core mode.

## Tool Calls

| Tool | Mode / status | Scientific use | Boundary |
|---|---|---|---|
| `mcp__geomine__.normalize_aoi` | parsed locally; no network | Preserved Revell AOI label and CRS assumption | No authoritative geocoding, polygon, NTS or distance calculation |
| `mcp__geomine__.search_canada_geodata` | planned request; live HTTP unsupported in this MCP version | Identified Open Canada/Geo.ca, NRCan CDoGS and Ontario OGSEarth as discovery lanes | Planned catalogue request is not evidence |
| `mcp__geomine__.search_cdogs_surveys` | planned request; no live survey parsing | Confirmed CDoGS as a possible geochemical survey lane | No sample medium, method, units or QA/QC parsed |

## Web / Public Source Use

Public reports and papers were retrieved or referenced directly. Downloaded PDFs are stored in `sources/` when accessible. Extracted numerical values are curated in CSV files with source identifiers. Sample-level groundwater chemistry was not parsed, so PHREEQC artifacts remain templates rather than executed site results.
