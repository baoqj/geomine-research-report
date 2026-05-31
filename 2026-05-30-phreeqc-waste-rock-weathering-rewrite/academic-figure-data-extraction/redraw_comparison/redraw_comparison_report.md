# Redraw Comparison Report

- Charts compared: 35
- Baseline summary: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31/redraw_comparison/redraw_comparison_summary.xlsx`
- Improved against baseline: 7
- Similar against baseline: 23
- Regressed against baseline: 5

| chart_id | rows | mean_abs_diff | high_diff_percent | baseline_delta_mean_abs_diff | assessment |
|---|---:|---:|---:|---:|---|
| p028_fig2_sampleA_ion_log | 423 | 71.97 | 31.92 | -0.14 | similar_image_difference |
| p059_fig2_sampleA_ion_log_revision | 401 | 71.92 | 32.2 | 0.02 | similar_image_difference |
| p030_fig3_A_major_original | 207 | 70.17 | 30.65 | -0.68 | similar_image_difference |
| p030_fig3_B_major_original | 211 | 72.46 | 32.1 | -0.71 | similar_image_difference |
| p030_fig3_A_trace_original | 283 | 71.34 | 31.37 | -1.61 | similar_image_difference |
| p030_fig3_B_trace_original | 281 | 73.09 | 32.34 | -1.83 | similar_image_difference |
| p030_fig3_A_H_SO4_original | 114 | 66.52 | 28.09 | -0.2 | similar_image_difference |
| p030_fig3_B_H_SO4_original | 105 | 66.36 | 27.91 | -0.61 | similar_image_difference |
| p061_fig3_A_major_revision | 195 | 69.93 | 30.65 | -0.68 | similar_image_difference |
| p061_fig3_B_major_revision | 187 | 72.19 | 32.06 | -0.77 | similar_image_difference |
| p061_fig3_A_trace_revision | 282 | 71.21 | 31.43 | -1.32 | improved_lower_image_difference |
| p061_fig3_B_trace_revision | 243 | 72.82 | 32.32 | -1.84 | improved_lower_image_difference |
| p061_fig3_A_H_SO4_revision | 105 | 66.33 | 28.08 | -0.18 | similar_image_difference |
| p061_fig3_B_H_SO4_revision | 105 | 66.26 | 27.97 | -0.48 | similar_image_difference |
| p033_fig4_acid_base_original | 105 | 15.7 | 8.57 | -0.02 | similar_image_difference |
| p033_fig5_buffer_capacity_original | 225 | 90.91 | 38.4 | 0.62 | similar_image_difference |
| p065_fig5_buffer_capacity_revision | 227 | 91.11 | 38.77 | 0.87 | similar_image_difference |
| p039_fig6A_major_original | 801 | 82.76 | 37.7 | -0.41 | improved_lower_image_difference |
| p039_fig6A_H_SO4_original | 357 | 71.82 | 30.69 | 1.22 | similar_image_difference |
| p040_fig6B_major_original | 717 | 79.76 | 36.43 | -0.63 | similar_image_difference |
| p040_fig6B_H_SO4_original | 288 | 71.62 | 29.99 | -0.87 | similar_image_difference |
| p072_fig6A_major_revision | 768 | 82.67 | 37.87 | -0.34 | improved_lower_image_difference |
| p072_fig6A_H_SO4_revision | 362 | 71.4 | 30.91 | 0.95 | similar_image_difference |
| p072_fig6B_major_revision | 708 | 79.0 | 36.52 | -0.55 | improved_lower_image_difference |
| p072_fig6B_H_SO4_revision | 291 | 71.55 | 30.38 | -0.76 | similar_image_difference |
| p042_fig7_uranium_original | 240 | 13.93 | 7.55 | -1.55 | improved_lower_image_difference |
| p075_fig7_uranium_revision | 240 | 13.93 | 7.55 | -1.55 | improved_lower_image_difference |
| p043_fig8_primary_sampleA | 570 | 23.92 | 14.83 | 4.17 | regressed_higher_image_difference |
| p043_fig8_secondary_sampleA | 336 | 15.74 | 9.01 | 0.44 | similar_image_difference |
| p044_fig9_primary_sampleB | 686 | 22.87 | 14.06 | 3.14 | regressed_higher_image_difference |
| p044_fig9_secondary_sampleB | 345 | 18.7 | 10.31 | 2.34 | regressed_higher_image_difference |
| p076_fig8_primary_sampleA_revision | 570 | 19.79 | 12.71 | 2.62 | regressed_higher_image_difference |
| p076_fig8_secondary_sampleA_revision | 330 | 15.57 | 8.97 | -1.88 | similar_image_difference |
| p077_fig9_primary_sampleB_revision | 679 | 23.2 | 14.33 | 4.82 | regressed_higher_image_difference |
| p077_fig9_secondary_sampleB_revision | 342 | 17.52 | 9.61 | 0.76 | similar_image_difference |

## Per-Chart Notes

### p028_fig2_sampleA_ion_log

- Title: Ion concentrations in seepage water over HCT cycles, Sample A
- Axes: HCT cycles (weeks), linear, 0..175; Elemental concentrations (M), log10, 1e-07..0.001
- Series: Al:59; Ca:49; K:47; Mg:37; Na:34; Ca_trend:85; Na_trend:112
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p028_fig2_sampleA_ion_log_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p028_fig2_sampleA_ion_log_comparison.png`

### p059_fig2_sampleA_ion_log_revision

- Title: Ion concentrations in seepage water over HCT cycles, Sample A
- Axes: HCT cycles (weeks), linear, 0..175; Elemental concentrations (M), log10, 1e-07..0.001
- Series: Al:57; Ca:49; K:45; Mg:37; Na:30; Ca_trend:84; Na_trend:99
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p059_fig2_sampleA_ion_log_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p059_fig2_sampleA_ion_log_revision_comparison.png`

### p030_fig3_A_major_original

- Title: Dissolved species over HCT cycles, SampleA, A_major
- Axes: HCT cycles (weeks), linear, 0..175; Concentration (M), log10, 1e-07..0.001
- Series: Al:49; Ca:45; K:45; Mg:39; Na:29
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p030_fig3_A_major_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p030_fig3_A_major_original_comparison.png`

### p030_fig3_B_major_original

- Title: Dissolved species over HCT cycles, SampleB, B_major
- Axes: HCT cycles (weeks), linear, 0..150; Concentration (M), log10, 1e-07..0.001
- Series: Al:39; Ca:37; K:35; Mg:50; Na:50
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p030_fig3_B_major_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p030_fig3_B_major_original_comparison.png`

### p030_fig3_A_trace_original

- Title: Dissolved species over HCT cycles, SampleA, A_trace
- Axes: HCT cycles (weeks), linear, 0..175; Concentration (M), log10, 1e-10..0.001
- Series: Cd:66; Co:38; Cu:38; Fe:44; Ni:38; U:59
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p030_fig3_A_trace_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p030_fig3_A_trace_original_comparison.png`

### p030_fig3_B_trace_original

- Title: Dissolved species over HCT cycles, SampleB, B_trace
- Axes: HCT cycles (weeks), linear, 0..150; Concentration (M), log10, 1e-10..0.001
- Series: Cd:88; Co:43; Cu:36; Fe:31; Ni:31; U:52
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p030_fig3_B_trace_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p030_fig3_B_trace_original_comparison.png`

### p030_fig3_A_H_SO4_original

- Title: Dissolved species over HCT cycles, SampleA, A_H_SO4
- Axes: HCT cycles (weeks), linear, 0..175; Concentration (M), log10, 1e-07..0.001
- Series: H:41; SO4:73
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p030_fig3_A_H_SO4_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p030_fig3_A_H_SO4_original_comparison.png`

### p030_fig3_B_H_SO4_original

- Title: Dissolved species over HCT cycles, SampleB, B_H_SO4
- Axes: HCT cycles (weeks), linear, 0..150; Concentration (M), log10, 1e-07..0.001
- Series: H:53; SO4:52
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p030_fig3_B_H_SO4_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p030_fig3_B_H_SO4_original_comparison.png`

### p061_fig3_A_major_revision

- Title: Dissolved species over HCT cycles, SampleA, A_major
- Axes: HCT cycles (weeks), linear, 0..175; Concentration (M), log10, 1e-07..0.001
- Series: Al:49; Ca:45; K:42; Mg:34; Na:25
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p061_fig3_A_major_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p061_fig3_A_major_revision_comparison.png`

### p061_fig3_B_major_revision

- Title: Dissolved species over HCT cycles, SampleB, B_major
- Axes: HCT cycles (weeks), linear, 0..150; Concentration (M), log10, 1e-07..0.001
- Series: Al:36; Ca:35; K:30; Mg:46; Na:40
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p061_fig3_B_major_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p061_fig3_B_major_revision_comparison.png`

### p061_fig3_A_trace_revision

- Title: Dissolved species over HCT cycles, SampleA, A_trace
- Axes: HCT cycles (weeks), linear, 0..175; Concentration (M), log10, 1e-10..0.001
- Series: Cd:67; Co:38; Cu:36; Fe:43; Ni:38; U:60
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p061_fig3_A_trace_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p061_fig3_A_trace_revision_comparison.png`

### p061_fig3_B_trace_revision

- Title: Dissolved species over HCT cycles, SampleB, B_trace
- Axes: HCT cycles (weeks), linear, 0..150; Concentration (M), log10, 1e-10..0.001
- Series: Cd:80; Co:39; Cu:25; Fe:29; Ni:22; U:48
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p061_fig3_B_trace_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p061_fig3_B_trace_revision_comparison.png`

### p061_fig3_A_H_SO4_revision

- Title: Dissolved species over HCT cycles, SampleA, A_H_SO4
- Axes: HCT cycles (weeks), linear, 0..175; Concentration (M), log10, 1e-07..0.001
- Series: H:39; SO4:66
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p061_fig3_A_H_SO4_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p061_fig3_A_H_SO4_revision_comparison.png`

### p061_fig3_B_H_SO4_revision

- Title: Dissolved species over HCT cycles, SampleB, B_H_SO4
- Axes: HCT cycles (weeks), linear, 0..150; Concentration (M), log10, 1e-07..0.001
- Series: H:53; SO4:52
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p061_fig3_B_H_SO4_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p061_fig3_B_H_SO4_revision_comparison.png`

### p033_fig4_acid_base_original

- Title: Cation/sulfate ratio over time
- Axes: HCT cycles (weeks), linear, 0..160; Cations/SO4 molar ratio (dimensionless), linear, 0..1.8
- Series: cation_sulfate_ratio:105
- Issue summary: main differences are expected from fonts, ticks, legend placement, and marker style
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p033_fig4_acid_base_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p033_fig4_acid_base_original_comparison.png`

### p033_fig5_buffer_capacity_original

- Title: H+/SO4 ratio over HCT cycles for samples A and B
- Axes: HCT cycles (weeks), linear, 0..150; H+/SO4 ratio (dimensionless), linear, 0..1
- Series: sample_A_red:129; sample_B_blue:96
- Issue summary: excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p033_fig5_buffer_capacity_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p033_fig5_buffer_capacity_original_comparison.png`

### p065_fig5_buffer_capacity_revision

- Title: H+/SO4 ratio over HCT cycles for samples A and B
- Axes: HCT cycles (weeks), linear, 0..150; H+/SO4 ratio (dimensionless), linear, 0..1
- Series: sample_A_red:130; sample_B_blue:97
- Issue summary: excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p065_fig5_buffer_capacity_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p065_fig5_buffer_capacity_revision_comparison.png`

### p039_fig6A_major_original

- Title: Model and measured dissolved species, SampleA, A_major
- Axes: HCT cycles (weeks), linear, 0..175; Concentration (M), log10, 1e-07..0.001
- Series: Al_mod:113; Ca_mod:113; Fe_mod:109; K_mod:88; Mg_mod:107; Na_mod:43; Al:43; Ca:39; Fe:45; K:42; Mg:35; Na:24
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p039_fig6A_major_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p039_fig6A_major_original_comparison.png`

### p039_fig6A_H_SO4_original

- Title: Model and measured dissolved species, SampleA, A_H_SO4
- Axes: HCT cycles (weeks), linear, 0..175; Concentration (M), log10, 1e-07..0.001
- Series: H_mod:112; SO4_mod:111; H:62; SO4:72
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p039_fig6A_H_SO4_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p039_fig6A_H_SO4_original_comparison.png`

### p040_fig6B_major_original

- Title: Model and measured dissolved species, SampleB, B_major
- Axes: HCT cycles (weeks), linear, 0..150; Concentration (M), log10, 1e-07..0.001
- Series: Al_mod:112; Ca_mod:103; Fe_mod:109; K_mod:107; Mg_mod:106; Al:32; Ca:43; Fe:19; K:34; Mg:46; Na:6
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p040_fig6B_major_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p040_fig6B_major_original_comparison.png`

### p040_fig6B_H_SO4_original

- Title: Model and measured dissolved species, SampleB, B_H_SO4
- Axes: HCT cycles (weeks), linear, 0..150; Concentration (M), log10, 1e-08..0.001
- Series: H_mod:113; SO4_mod:114; H:29; SO4:32
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p040_fig6B_H_SO4_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p040_fig6B_H_SO4_original_comparison.png`

### p072_fig6A_major_revision

- Title: Model and measured dissolved species, SampleA, A_major
- Axes: HCT cycles (weeks), linear, 0..175; Concentration (M), log10, 1e-07..0.001
- Series: Al_mod:113; Ca_mod:113; Fe_mod:109; K_mod:87; Mg_mod:90; Na_mod:42; Al:44; Ca:38; Fe:43; K:37; Mg:29; Na:23
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p072_fig6A_major_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p072_fig6A_major_revision_comparison.png`

### p072_fig6A_H_SO4_revision

- Title: Model and measured dissolved species, SampleA, A_H_SO4
- Axes: HCT cycles (weeks), linear, 0..175; Concentration (M), log10, 1e-07..0.001
- Series: H_mod:113; SO4_mod:113; H:62; SO4:74
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p072_fig6A_H_SO4_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p072_fig6A_H_SO4_revision_comparison.png`

### p072_fig6B_major_revision

- Title: Model and measured dissolved species, SampleB, B_major
- Axes: HCT cycles (weeks), linear, 0..150; Concentration (M), log10, 1e-07..0.001
- Series: Al_mod:109; Ca_mod:94; Fe_mod:107; K_mod:109; Mg_mod:107; Al:31; Ca:36; Fe:19; K:37; Mg:45; Na:14
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p072_fig6B_major_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p072_fig6B_major_revision_comparison.png`

### p072_fig6B_H_SO4_revision

- Title: Model and measured dissolved species, SampleB, B_H_SO4
- Axes: HCT cycles (weeks), linear, 0..150; Concentration (M), log10, 1e-08..0.001
- Series: H_mod:113; SO4_mod:112; H:30; SO4:36
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | high layout-level pixel difference; data redraw is not a style clone
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p072_fig6B_H_SO4_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p072_fig6B_H_SO4_revision_comparison.png`

### p042_fig7_uranium_original

- Title: Uranium concentration model and measured samples
- Axes: HCT cycles (weeks), linear, 0..160; Concentration (M), log10, 1e-10..0.001
- Series: model_a:113; model_b:113; sample_a:6; sample_b:8
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | main differences are expected from fonts, ticks, legend placement, and marker style
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p042_fig7_uranium_original_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p042_fig7_uranium_original_comparison.png`

### p075_fig7_uranium_revision

- Title: Uranium concentration model and measured samples
- Axes: HCT cycles (weeks), linear, 0..160; Concentration (M), log10, 1e-10..0.001
- Series: model_a:113; model_b:113; sample_a:6; sample_b:8
- Issue summary: log-scale pixel errors can create large value differences | excluded legend/annotation regions can leave missing points | main differences are expected from fonts, ticks, legend placement, and marker style
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required | recover obscured data from source tables or mark as missing | calibrate log-axis ticks panel by panel
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p075_fig7_uranium_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p075_fig7_uranium_revision_comparison.png`

### p043_fig8_primary_sampleA

- Title: Saturation index (primary) for SampleA
- Axes: HCT cycles (weeks), linear, 0..160; Saturation index (dimensionless), linear, -50..10
- Series: si_Anorthite:114; si_Albite:114; si_K-mica:114; si_Chlorite(14A):114; si_Biotite_FeMg:114
- Issue summary: main differences are expected from fonts, ticks, legend placement, and marker style
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p043_fig8_primary_sampleA_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p043_fig8_primary_sampleA_comparison.png`

### p043_fig8_secondary_sampleA

- Title: Saturation index (secondary) for SampleA
- Axes: HCT cycles (weeks), linear, 0..160; Saturation index (dimensionless), linear, -1..1.5
- Series: si_Hydrobasaluminite:109; si_Jarosite-K:113; si_Fe(OH)3(a):114
- Issue summary: main differences are expected from fonts, ticks, legend placement, and marker style
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p043_fig8_secondary_sampleA_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p043_fig8_secondary_sampleA_comparison.png`

### p044_fig9_primary_sampleB

- Title: Saturation index (primary) for SampleB
- Axes: HCT cycles (weeks), linear, 0..160; Saturation index (dimensionless), linear, -60..20
- Series: si_Anorthite:115; si_Albite:111; si_K-mica:115; si_Chlorite(14A):115; si_Biotite_FeMg:115; si_Dolomite:115
- Issue summary: main differences are expected from fonts, ticks, legend placement, and marker style
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p044_fig9_primary_sampleB_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p044_fig9_primary_sampleB_comparison.png`

### p044_fig9_secondary_sampleB

- Title: Saturation index (secondary) for SampleB
- Axes: HCT cycles (weeks), linear, 0..160; Saturation index (dimensionless), linear, -16..2
- Series: si_Hydrobasaluminite:115; si_Jarosite-K:115; si_Fe(OH)3(a):115
- Issue summary: main differences are expected from fonts, ticks, legend placement, and marker style
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p044_fig9_secondary_sampleB_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p044_fig9_secondary_sampleB_comparison.png`

### p076_fig8_primary_sampleA_revision

- Title: Saturation index (primary) for SampleA
- Axes: HCT cycles (weeks), linear, 0..160; Saturation index (dimensionless), linear, -50..10
- Series: si_Anorthite:114; si_Albite:114; si_K-mica:114; si_Chlorite(14A):114; si_Biotite_FeMg:114
- Issue summary: main differences are expected from fonts, ticks, legend placement, and marker style
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p076_fig8_primary_sampleA_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p076_fig8_primary_sampleA_revision_comparison.png`

### p076_fig8_secondary_sampleA_revision

- Title: Saturation index (secondary) for SampleA
- Axes: HCT cycles (weeks), linear, 0..160; Saturation index (dimensionless), linear, -1..1.5
- Series: si_Hydrobasaluminite:103; si_Jarosite-K:113; si_Fe(OH)3(a):114
- Issue summary: main differences are expected from fonts, ticks, legend placement, and marker style
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p076_fig8_secondary_sampleA_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p076_fig8_secondary_sampleA_revision_comparison.png`

### p077_fig9_primary_sampleB_revision

- Title: Saturation index (primary) for SampleB
- Axes: HCT cycles (weeks), linear, 0..160; Saturation index (dimensionless), linear, -60..20
- Series: si_Anorthite:114; si_Albite:109; si_K-mica:114; si_Chlorite(14A):114; si_Biotite_FeMg:114; si_Dolomite:114
- Issue summary: main differences are expected from fonts, ticks, legend placement, and marker style
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p077_fig9_primary_sampleB_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p077_fig9_primary_sampleB_revision_comparison.png`

### p077_fig9_secondary_sampleB_revision

- Title: Saturation index (secondary) for SampleB
- Axes: HCT cycles (weeks), linear, 0..160; Saturation index (dimensionless), linear, -16..2
- Series: si_Hydrobasaluminite:114; si_Jarosite-K:114; si_Fe(OH)3(a):114
- Issue summary: main differences are expected from fonts, ticks, legend placement, and marker style
- Fix summary: use manually verified axis tick pixels for publication-grade extraction | preserve original plotting style metadata when layout fidelity is required
- Redraw: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/redrawn_charts/p077_fig9_secondary_sampleB_revision_redrawn.png`
- Comparison: `openminer/plugins/report/academic-figure-data-extraction-reactive-geochemical-2026-05-31-v3-final/redraw_comparison/comparison_panels/p077_fig9_secondary_sampleB_revision_comparison.png`
