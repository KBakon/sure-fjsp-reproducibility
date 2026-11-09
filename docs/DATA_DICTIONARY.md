# Data dictionary

CSV values are UTF-8, one header row, comma separated. `regime`/`severity` is LOW or HIGH; `base_id` identifies a published benchmark instance; `strategy_id` is the existing schedule label. These labels do not contain machine assignments or operation sequences. `cell` encodes activation of processing, breakdown and release disturbances, respectively. `nominal_makespan` is the deterministic schedule makespan. CVaR90 is empirical conditional value at risk of makespan; `Y` is log(CVaR90 / nominal makespan). Predictions and errors are on that normalized log scale unless explicitly marked absolute. Errors are prediction minus observation. `X_log` is the corresponding additive isolated-response predictor. `Q` is RMSE(D1)/RMSE(D0_LOG); CI fields are 2.5th/97.5th percentiles of whole-base bootstrap draws. All 10,000 draws per cell/regime use seed 20261105. `D0_RAW` is the historical secondary comparator.

- `isolated_risk.csv`: 160 schedule rows, isolated response and predicted scores.
- `decision_tension.csv`: 40 regime/base contexts, selected strategies and predicted absolute-score margins.
- `compound_111.csv`: 160 schedule-level triple-cell observed risks and model predictions/errors.
- `compound_pairwise.csv`: 480 pairwise-cell schedule-level observations and predictions/errors.
- `metrics_111.csv`, `metrics_pairwise.csv`: frozen analysis summaries for each model.
- `bootstrap_111.csv`, `bootstrap_pairwise.csv`: 20,000 and 60,000 ratio draws.
- `support_111.csv`, `support_pairwise.csv`: original DEV scalar-predictor ranges and target sample coverage; this diagnostic does not establish multivariate support.
- `transport_figure_table.csv`: eight unrounded forest/table records including RMSE, Q and bootstrap intervals.

Scientific numbers and labels are retained from source tables; schedule hash columns were removed and CSV line endings normalized. No raw benchmark data or schedules are included.
