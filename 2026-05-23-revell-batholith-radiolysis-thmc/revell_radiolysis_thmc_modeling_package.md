# Revell Batholith Radiolysis-THMC Modeling Package

## 1. Research Objective

Build a defensible, literature-grounded THMC framework for Revell Batholith groundwater chemistry, U-Th-K radiolysis, H2/sulfate generation, microbial energy, corrosion, bentonite evolution and radionuclide migration.

## 2. Scenario Classification

- Scenario: nuclear waste repository / crystalline-rock DGR.
- Coupling level: THMC.
- Readiness: L1 methods protocol with screening calculations.

## 3. Conceptual THMC Model

The host rock supplies low but persistent radiogenic energy. Water accessibility is constrained by low connected porosity and fracture geometry. H2 and oxidants alter redox and microbial boundary conditions. Salinity, sulfate and sulfide influence corrosion and sorption. Mechanical effects enter through fracture aperture, permeability and bentonite gas-entry/self-sealing behavior.

## 4. Coupling Matrix

| From / To | Thermal | Hydrological | Mechanical | Chemical |
|---|---|---|---|---|
| Thermal | radiogenic heat, waste heat | viscosity/density and diffusion | thermal stress | reaction rates |
| Hydrological | advective heat | fracture/matrix flow | pore pressure and aperture | solute delivery, gas transport |
| Mechanical | stress-dependent heat paths | permeability/aperture | swelling, damage | reactive surface and transport pathway |
| Chemical | redox heat negligible | precipitation/dissolution affects porosity | bentonite exchange and swelling | radiolysis, corrosion, sorption, decay |

## 5. Governing Equations

See `data/equation_registry.csv` and the main paper. Required equations include U-Th-K heat production, radiolysis source term, H2 mass balance, sulfate/sulfide stoichiometry, ideal-gas/Henry pressure screen, sorption-retarded transport and THMC state variables.

## 6. Parameters and Data Requirements

| Parameter group | Current status | Required next data |
|---|---|---|
| U-Th-K and density | public compiled values available | spatial distribution by borehole/depth |
| Porosity/permeability | public ranges available | fracture-scale transmissivity and matrix diffusion |
| Groundwater chemistry | public framework available | sample-level pH, Eh/pe, Cl, Br, SO4, alkalinity, Fe, U, sulfide |
| H2/sulfate production | public Revell H2 value available | full source-paper tables, uncertainty distribution, sulfate rate |
| Microbial kinetics | not calibrated | sulfate reducers, methanogens, maintenance-energy thresholds |
| Corrosion and bentonite | not site calibrated | material-specific corrosion, gas-entry, swelling and diffusion data |

## 7. Solver Route

1. PHREEQC: end-member speciation, saturation indices, U/carbonate/sulfide sensitivity.
2. PFLOTRAN or OGS: fracture-matrix reactive transport with long-term H2 and radionuclide source terms.
3. COMSOL: near-field coupled THMC with bentonite swelling/gas entry and corrosion source terms.
4. PINN: only as a constrained surrogate after measured training/validation data exist.

## 8. Calibration and Validation Plan

- Calibrate chemistry with sample-level groundwater tables.
- Calibrate transport with packer tests, hydraulic head and tracer/diffusion experiments.
- Calibrate radiolysis geometry with mineralogy, porosity and source-paper Monte Carlo assumptions.
- Validate against independent borehole chemistry, temperature and microbial observations.

## 9. Uncertainty Plan

Primary uncertainty lanes: water-accessible radiolysis fraction, fracture connectivity, deep-water mixing, sulfate reduction kinetics, sulfide diffusion to copper, H2 solubility under salinity/temperature, radionuclide sorption under high ionic strength.

## 10. Figure Plan

Generated figures are listed in `figure_manifest.json`; the most important panels are U-Th-K heat/H2, energy-partition attenuation, groundwater depth framework, closed H2 accumulation and THMC reaction network.

## 11. Machine-Readable Model Spec

```json
{
  "research_type": "academic_paper_generation + thmc_modeling + radiolysis_nuclear_geochemistry",
  "scenario": "nuclear_waste_repository / Revell crystalline-rock groundwater-radiolysis system",
  "coupling_level": "THMC",
  "active_processes": {
    "thermal": true,
    "hydrological": true,
    "mechanical": true,
    "chemical": true
  },
  "readiness_level": "L1_methods_protocol_with_screening_calculations",
  "not_claimed": [
    "site safety conclusion",
    "regulatory compliance",
    "validated PHREEQC/PFLOTRAN/COMSOL run"
  ]
}
```
