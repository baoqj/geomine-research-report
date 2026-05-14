# PHREEQC Phase-2 Run Manifest

## Scope

This run is an illustrative post-fire water-chemistry sensitivity calculation anchored to EARMP 2023 surface-water screen values. It is not a calibrated field model and is not a regulatory or dose assessment.

## Files

- Input: `phreeqc_postfire_water_sensitivity_llnl.phr`
- Output: `phreeqc_postfire_water_sensitivity_llnl.out`
- Selected output: `phreeqc_postfire_water_sensitivity_llnl.sel`
- Parsed summary: `../data/processed/phreeqc_postfire_water_sensitivity_summary.csv`
- Database: `/Users/aibao/.local/phreeqc/phreeqc-3.5.0-14000/database/llnl.dat`
- Executable: `/Users/aibao/.local/bin/phreeqc`

## Command

```bash
~/.local/bin/phreeqc phreeqc_postfire_water_sensitivity_llnl.phr phreeqc_postfire_water_sensitivity_llnl.out ~/.local/phreeqc/phreeqc-3.5.0-14000/database/llnl.dat
```

## Run Status

- Completed locally on 2026-05-14.
- PHREEQC MCP tools were not exposed in this session; local PHREEQC was used instead.
- Warning preserved: `Did not find species, RaSO4` for selected molality output. The `RaSO4` saturation index was still reported by the database output.
- Warning preserved: PHREEQC normalized alkalinity equivalent weight.

## Scientific Boundaries

The input uses placeholder major-ion chemistry because EARMP surface-water data in this run contain pH, U, Ra-226 and selected trace elements, but not alkalinity, Ca, Mg, Na, K, Cl, sulfate, Eh, DOC, TSS, Fe/Mn, Pb-210 or Po-210. The results are therefore valid only as a mechanism demonstration: alkaline ash-pulse conditions shift U and Pb toward carbonate complexes, while Ra remains controlled by sulfate/Ba/Sr chemistry that requires additional measured inputs.
