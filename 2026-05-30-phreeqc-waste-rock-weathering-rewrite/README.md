# PHREEQC-supported rewrite of Li Zhenze waste-rock paper

This report package rewrites the supplied acid-generating uranium waste-rock manuscript using the supplied geochemical review logic, with PHREEQC calculations used to support the central claims.

Main paper:

- `LiZhenze_PHREEQC_Waste_Rock_Rewritten_Paper.zh.md`

PHREEQC outputs:

- `models/01_equilibrium_endmembers.phr/out/sel`
- `models/02_kinetic_reaction_path.phr/out/sel`
- `models/03_uranium_speciation_envelope.phr/out/sel`
- `models/04_U_HFO_surface_complexation_extension_template.phr`

Important boundary:

- Raw weekly HCT CSV data were not provided. The PHREEQC calculations are mechanism-supporting scenarios and reproducible model templates, not a new independent calibration against all measured time-series data.
