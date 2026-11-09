# Provenance and transformation

Scientific freeze SHA256: `4892e75b09ee72f35077b32f12b00c93c59ea1f481a11657b739e7ef0cafefeb`. Original sources are project-generated results under `results/rvpw_v1_5/`; hashes below identify input files, not licences. CSV extraction retained the original numerical strings and row order, discarded schedule-hash columns where present, and normalized CSV encoding/line endings. The 111 support table is a field selection from the Stage-B summary. No source files were changed.

| Release data | Source relative to results/rvpw_v1_5 | Source SHA256 |
|---|---|---|
| `data/isolated_risk.csv` | `p1_gen1_stage_a_isolated_2026_11_05/isolated_schedule_risk.csv` | `3f126e757e868af58eeff19346dbf39fac0c374f28628d2845f2547ac6b7ae22` |
| `data/decision_tension.csv` | `p1_gen1_stage_a_isolated_2026_11_05/decision_tension.csv` | `072b08a17408073c56a5c1ee3124232f9360b81c0baf3c63dc7df955b4817bff` |
| `data/compound_111.csv` | `p1_gen1_stage_b_transport_2026_11_05/compound_111_schedule_risk.csv` | `231783b6c7e30b171eed59e5cfdcd69bb1086761c840131fa86369bc2c60567e` |
| `data/metrics_111.csv` | `p1_gen1_stage_b_transport_2026_11_05/transport_metrics.csv` | `0c81e8e3e9f197170a85bc4b87edab00553929484d8ca8e9fb7a4ba18f00bc67` |
| `data/bootstrap_111.csv` | `p1_gen1_stage_b_transport_2026_11_05/bootstrap_rmse_ratio.csv` | `ce04f7be50134a026d1adedf82639094998799eb804c1a524774d2851c51153b` |
| `data/compound_pairwise.csv` | `p1_gen1_stage_c_crosscell_2026_11_05/pairwise_compound_schedule_risk.csv` | `33e87388ce47638826242fa2390ab8393771f9cf5e32297b0deac32665f8ae4c` |
| `data/metrics_pairwise.csv` | `p1_gen1_stage_c_crosscell_2026_11_05/crosscell_transport_metrics.csv` | `be695efd9e3fe03e216151eb2dac95e89aeda20d8d40379ac71aa59c421ab94d` |
| `data/bootstrap_pairwise.csv` | `p1_gen1_stage_c_crosscell_2026_11_05/crosscell_bootstrap_rmse_ratio.csv` | `00a199fce8ba358d9c47a55ef5344cc831129a97619599247236a5bcdbca272a` |
| `data/support_pairwise.csv` | `p1_gen1_stage_c_crosscell_2026_11_05/crosscell_extrapolation.csv` | `e1160df691a4ecdc58917976795c5653c7abf34e5d3a385222d7a416151e87e2` |
| `data/transport_figure_table.csv` | `p3_gen1_manuscript_integration_2026_11_06/transport_plot_source.csv` | `c6e2284bab3b2609c67a85c45c6e36459616a6147e9a14bb1f1987bc6a52cd61` |
| `data/support_111.csv` | `p1_gen1_stage_b_transport_2026_11_05/stage_b_summary.json` | `64d2ac19c5b5ff33105e67630f4f85550b8631459369b55481ba44d3a2d2f5fa` |

The 111 comparison was prospectively specified; the pairwise comparisons were selected after its positive result and specified before their own outcomes. These summaries do not claim an independently replicated or end-to-end simulation workflow. Licensing for the released project-created files is specified in `LICENSES.md`; benchmark material is excluded.
