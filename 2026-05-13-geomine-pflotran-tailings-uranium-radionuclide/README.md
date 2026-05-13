# GeoMine PFLOTRAN Tailings Uranium Radionuclide Paper

This folder contains a GeoMine Research academic-paper package for PFLOTRAN reactive-transport modeling of acidic seepage from sulfide-bearing uranium tailings into a shallow aquifer.

- `PFLOTRAN_Tailings_Uranium_Radionuclide_Paper.zh.md` - main Chinese academic paper with problem framing, decomposition, source discovery, initial/boundary conditions, equations, screening calculations, figures, model alignment, judgment and conclusions.
- `PFLOTRAN_Tailings_Uranium_Radionuclide_Paper.zh.pdf` - PDF export of the main paper with MathML-converted formulas and PNG figure fallbacks.
- `PFLOTRAN_Tailings_Uranium_Radionuclide_Paper.normalized.md` / `.normalized.pdf` - normalized source and PDF generated during formula-safe export.
- `PFLOTRAN_Modeling_Package.md` - 26-section PFLOTRAN Modeling Package with executed 1D screening addendum.
- `PFLOTRAN_Tailings_Uranium_Figure_Package.md` - academic figure package and captions.
- `pflotran_tailings_uranium_template.in` - draft PFLOTRAN input deck skeleton with placeholders.
- `pflotran_runs/` - executed 1D synthetic PFLOTRAN screening decks, logs, Tecplot outputs and velocity outputs.
- `model_manifest.json` - machine-readable model manifest.
- `run_manifest.json` - run-command and reproducibility manifest.
- `pflotran_run_manifest.json` - actual Docker PFLOTRAN execution manifest and convergence records.
- `input_deck_validation.json` - skeleton-structure validation report; placeholders remain by design.
- `figure_manifest.json` - figure inventory manifest.
- `mcp_provenance.md` - GeoMine MCP, local prompt, and web/literature provenance.
- `scripts/generate_figures.py` - reproducible script for method/screening figures.
- `scripts/analyze_pflotran_outputs.py` - parser for executed PFLOTRAN Tecplot outputs and convergence logs.
- `figures/` - SVG conceptual/screening figures plus PNG rendering fallbacks for PDF export.
- `data/` - generated screening CSV data and parsed PFLOTRAN 25-year profile tables.

Status: revised academic modeling paper with two executed 1D synthetic PFLOTRAN screening runs. The screening runs are converged but not calibrated or validated. The 2D site-scale deck remains a placeholder model package until site data are supplied.
