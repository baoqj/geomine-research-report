# U-Ra-Rn-Po-Pb groundwater radionuclide report package

Generated: 2026-05-23

This folder contains the reproducible research package for the Chinese paper:

`铀矿区地下水中 U-Ra-Rn-Po-Pb 系列核素的分布、迁移与剂量贡献`

## Rebuild

```bash
python3 scripts/build_uranium_series_groundwater_package.py
```

## Data handling

- CNSC Cigar Lake IEMP raw CSV rows: 820
- Censored values: For '<' values, mean uses 0.5*detection-limit; maximum screening ratio uses the full detection-limit as an upper bound.
- Swedish 2025 well-water values are literature-summary values from the open article page, not reconstructed raw samples.

## Main outputs

- `Paper.zh.md`: full academic paper in Chinese
- `Paper.zh.pdf`: PDF export, if the local export step has been run
- `data/`: cleaned and derived tables
- `figures/`: SVG visualizations
- `models/`: PHREEQC/state-vector/dose templates
- `sources/`: downloaded source-page snapshots and raw monitoring CSV
