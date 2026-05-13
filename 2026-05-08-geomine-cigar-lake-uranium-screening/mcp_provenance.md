# GeoMine MCP Provenance Notes

Research date: 2026-05-08

## Tools Used

### `normalize_aoi`

- Input: `Cigar Lake uranium mine area, eastern Athabasca Basin, Saskatchewan, Canada. Approximate screening point near 58.07 N, 104.53 W; no tenure polygon supplied; treat as named mine/AOI, not a claim boundary.`
- Default CRS: `EPSG:4326`
- Retrieval status: parsed
- Retrieved at: `2026-05-08T15:52:57.545468+00:00`
- Source: GeoMine MCP local AOI normalizer
- Network: not used
- Key limitation: no authoritative geocoding, claim lookup, NTS lookup, area calculation, or CRS transformation was performed.
- Tool warnings:
  - Canadian AOI is missing province or territory.
  - No coordinates, polygon, bounding box, or point supplied.
- Analyst handling: the report normalizes jurisdiction to Saskatchewan, Canada from official Cigar Lake sources and preserves the MCP geometry warning.

### `search_saskatchewan_mineral_data`

- Input AOI: `Cigar Lake mine area, eastern Athabasca Basin, Saskatchewan`
- Commodity: `uranium`
- `allow_network`: `false`
- Retrieved at: `2026-05-08T15:53:15.693585+00:00`
- Source candidate: Saskatchewan GeoAtlas / public geoscience data
- Source URL: `https://gisappl.saskatchewan.ca/Html5Ext/index.html?viewer=GeoAtlas`
- Retrieval status: planned
- Key limitation: the current MCP implementation plans Saskatchewan mineral-data discovery only; it did not perform live GeoAtlas or ArcGIS querying.

### `search_cdogs_surveys`

- Province: `Saskatchewan`
- AOI: `Cigar Lake mine area, eastern Athabasca Basin`
- Commodity: `uranium`
- `allow_network`: `false`
- Retrieved at: `2026-05-08T15:53:17.831605+00:00`
- Source candidate: NRCan CDoGS
- Source URL: `https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm`
- Retrieval status: planned
- Key limitation: no live spatial filtering, metadata fetch, spreadsheet parsing, or QA/QC review was performed.

### `search_canada_geodata`

- Query: `Cigar Lake uranium Athabasca Basin geology geochemistry geophysics mineral occurrence`
- Province: `Saskatchewan`
- Commodity: `uranium`
- Rows: `10`
- `allow_network`: `false`
- Retrieved at: `2026-05-08T15:53:19.504704+00:00`
- Planned request: `https://open.canada.ca/data/api/3/action/package_search?q=Cigar+Lake+uranium+Athabasca+Basin+geology+geochemistry+geophysics+mineral+occurrence&rows=10&start=0`
- Retrieval status: planned
- Key limitation: planned catalogue requests are not evidence until fetched, filtered, and parsed.

### `calculate_infrastructure_distance`

- AOI: `Cigar Lake mine area, eastern Athabasca Basin, Saskatchewan; approximate point 58.07 N, 104.53 W`
- Infrastructure type: `road, airstrip, uranium mill, power`
- `allow_network`: `false`
- Retrieved at: `2026-05-08T15:53:21.687677+00:00`
- Retrieval status: planned
- Result: no distance calculated
- Required inputs identified by MCP:
  - authoritative AOI geometry
  - confirmed CRS
  - infrastructure layer

## Local Data Check

Local Saskatchewan Geological Survey lake-water geochemistry files were checked:

- Samples: `Skills/mining-AI/data/staging/geochemistry/lake_water_samples.csv`
- Measurements: `Skills/mining-AI/data/staging/geochemistry/lake_water_measurements.csv`
- Total local samples: 566
- Approximate screening point used for radius check: `58.066 N, -104.536 W`
- Samples within 25 km: 17
- Samples with uranium values within 25 km: 17
- Uranium range within 25 km: min `0.0 ppm`, median `0.00005 ppm`, max `0.0001 ppm`
- Samples within 50 km: 365
- Samples with uranium values within 50 km: 365
- Uranium range within 50 km: min `0.0 ppm`, median `0.00005 ppm`, max `2.3 ppm`
- Highest 50 km uranium value: sample `773193`, about `49.7 km` from the approximate screening point, NTS `64L`, `2.3 ppm U`

Interpretation caveat: these local lake-water data are useful regional context but are not decisive for a deep, covered, known unconformity uranium deposit. They should not be used to downgrade the known Cigar Lake deposit, and they should not be used as standalone target evidence without survey-method and QA/QC review.

