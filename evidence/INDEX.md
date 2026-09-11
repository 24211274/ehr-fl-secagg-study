# Evidence index

## Source identity

The original executed archive is `EHR_FL_Main_Experiments_Package_v1_0_3.zip`.

SHA-256: `433a26789afd362dad4316c96379017d2808969925fa5df1d61e332d94cb6c84`.

Original manifest SHA-256: `0e4bc1175bf97a766d46aa60f02c4c891c483d3870957b3ae6ac52ea7734dc88`.

The repository preserves its 215 manifested files **plus the manifest file itself** under `executed/EHR_FL_Main_Experiments_Package_v1_0_3/`. See the original guide's `source_identity.json` for the per-file inventory.

## Results and audit

- `analysis/final_score_audit/AUDITED_RESULTS.md`: audited findings, including negative results.
- `analysis/final_score_audit/Final_Score_Arithmetic_Audit.json`: recorded independent arithmetic audit and its limits.
- `results/tables/selected_models_and_validation_loss.csv`: model selection and routine-validation summaries.
- `results/tables/system_cost_run_values.csv`: per-run cost values.
- `results/tables/recomputed_rank_metrics.csv` and `recomputed_decision_metrics.csv`: all supplied recomputed metric cells, not only favourable runs.
- `completion_status.json` and `system_cost_analysis.json`: existing completion and cost summaries from the writing package.
- `Table_and_Figure_Source_Map.csv` and `writing_source_register.json`: existing provenance for the writing layer. Some original paths are historic local references, not files supplied by this repository.

The ten full main-block ZIPs, the full final-evaluation report, individual score evidence and model checkpoint files are **not uploaded by this handover tool**. Keep them in the original research archive. Their filenames/digests in the supplied provenance are pointers, not proof that those assets are included here.

`HANDOVER_FILES_SHA256.json` is newly generated for this repository. It binds the copied files and new documentation; it does not alter the original experiment's integrity manifest.
