# Revell Batholith Radiolysis-THMC Paper Package

This folder contains the reproducible GeoMine Research package for the paper:
`Revell Batholith 地下水化学、放射性辐解产氢与深地质处置库长期安全性的耦合分析`.

## Main outputs

- `Revell_Batholith_Radiolysis_THMC_Paper.zh.md` - main Chinese academic paper.
- `Revell_Batholith_Radiolysis_THMC_Paper.zh.pdf` - PDF export when generated.
- `revell_radiolysis_thmc_modeling_package.md` - THMC modeling package.
- `figure_package.md` / `figure_manifest.json` - figure inventory.
- `data/` - public extracted parameters and derived screening calculations.
- `figures/` - generated SVG visualization results.
- `models/` - PHREEQC, COMSOL and PINN starter specifications.
- `sources/` - downloaded public PDF source files where accessible.
- `mcp_provenance.md` - GeoMine MCP and source-discovery boundary notes.

## Status

L1 methods protocol with screening calculations. The package does not claim a site-specific safety conclusion, raw water-sample PHREEQC result, regulatory compliance or validated THMC simulation.

## Rebuild

```bash
python3 report/2026-05-23-revell-batholith-radiolysis-thmc/scripts/build_revell_radiolysis_thmc_package.py
```
