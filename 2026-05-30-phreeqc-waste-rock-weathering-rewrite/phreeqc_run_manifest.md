# PHREEQC Run Manifest

PHREEQC executable: `/Users/aibao/.local/bin/phreeqc`

Databases:

- Major-ion/acid-neutralization screening: `/Users/aibao/.local/phreeqc/phreeqc-3.5.0-14000/database/phreeqc.dat`
- Uranium speciation envelope: `/Users/aibao/.local/phreeqc/phreeqc-3.5.0-14000/database/llnl.dat`

Commands executed by `scripts/build_phreeqc_waste_rock_rewrite_package.py`:

```bash
phreeqc models/01_equilibrium_endmembers.phr models/01_equilibrium_endmembers.out /Users/aibao/.local/phreeqc/phreeqc-3.5.0-14000/database/phreeqc.dat
phreeqc models/02_kinetic_reaction_path.phr models/02_kinetic_reaction_path.out /Users/aibao/.local/phreeqc/phreeqc-3.5.0-14000/database/phreeqc.dat
phreeqc models/03_uranium_speciation_envelope.phr models/03_uranium_speciation_envelope.out /Users/aibao/.local/phreeqc/phreeqc-3.5.0-14000/database/llnl.dat
```

HTML/PDF export can be run with GeoMine `geomine-paper-pdf-export-skill`.
