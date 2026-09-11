# Supervisor code-review guide

**Purpose:** navigate the archived implementation associated with the completed EHR/Flower experiment. This is a newly prepared guide, not a new experimental implementation, an execution authorisation, or a claim that a clean-machine reproduction has been completed.

## Start here

The source archive is `EHR_FL_Main_Experiments_Package_v1_0_3.zip`. Its top-level directory is `EHR_FL_Main_Experiments_Package_v1_0_3/`. All code paths below are relative to that directory. Keep that directory intact; add review documentation outside it.

The archive SHA-256 is:

`433a26789afd362dad4316c96379017d2808969925fa5df1d61e332d94cb6c84`

The SHA-256 of its `PACKAGE_SHA256SUMS.txt` is:

`0e4bc1175bf97a766d46aa60f02c4c891c483d3870957b3ae6ac52ea7734dc88`

All 215 entries in that manifest were checked against the supplied archive when preparing this guide. The archive has no additional regular files except the manifest itself. This verifies the supplied source archive against its internal manifest; it does not authenticate a GitHub upload or independently inspect the researcher's live WSL campaign.

The completed campaign was recorded as `20260909T142009Z_2ad79bf6`. The experiment compared A (pooled centralised), B (Flower FedAvg), and C (FedAvg with SecAgg+ in a locally modified Flower build), with Reference and controlled Non-IID conditions and seeds 11, 29, 47, 71 and 97. `MAIN_IMPLEMENTATION.md` describes the executed design and its boundaries.

**Historical instructions:** the frozen package's `README.md` describes the repair-preparation stage at the time of release. Do not treat its `PrepareRepair` instructions as a command to start reviewing completed results. Do not rerun training or final evaluation in the completed campaign.

## Recommended reading route

| Review question | Exact source path | Entry points or content |
|---|---|---|
| What was fixed in the design? | `MAIN_IMPLEMENTATION.md`; `protocol/decisions/config/main_protocol_decisions.json`; `protocol/decisions/config/main_run_order.csv` | Scientific choices, checkpoint rule, calibration, evaluation, execution order and limits. |
| What is the neural model and loss? | `app/pilot_core/model.py` | `CompactLSTMAutoencoder` (line 30), `session_losses` (line 64), `new_optimiser` (line 89). The directory name is inherited; this module is used by the main implementation. |
| How are events encoded? | `app/ehr_preprocessing/pipeline.py`; `config/encoding_schema.json`; `main_study/test_inputs.py` | Training-side feature functions and scaler; the approved schema; test encoding and final-input loading without refitting. |
| How are client draws and the pooled baseline constructed? | `main_study/design.py` | `make_draws`, `pooled_round`, `cell_config`, `stage_cell`; generated job configuration is distinct from inherited timing-pilot configuration. |
| Where is main centralised training? | `main_study/central.py` | `fit_epoch` (line 15), `run_central` (line 35). |
| Where is standard federated training? | `app/ehr_fedavg/client_app.py`; `app/ehr_fedavg/server_app.py`; `app/ehr_fedavg/task.py`; `app/ehr_fedavg/strategy.py` | Client and server entry points, `fit_one_client`, and the aggregation/evaluation strategy. |
| What changes in the secured configuration? | `app/ehr_secagg/client_app.py`; `app/ehr_secagg/server_app.py`; `app/ehr_secagg/workflow.py`; `app/ehr_secagg/wire.py` | SecAgg+ client mod, server workflow, message-boundary guards and local training integration. |
| What is the locally modified Flower dependency? | `validation_support/NOTICE.md`; `validation_support/CHANGE_MANIFEST.json`; `validation_support/prg_validation/build.py`; `validation_support/sources/backport_secaggplus_utils.py` | Attribution, pinned inputs, local wheel construction and the exact helper change. |
| How are checkpoints and thresholds linked to results? | `main_study/evaluation.py`; `main_study/final_evaluator.py` | `calibrate_validation`, `join_scores_labels`, `score_endpoints`, `paired_summary`; model validation, scoring and final evaluation. |
| What is actually counted as overhead? | `app/mai_measurement.py`; `main_study/costs.py` | Instrumented timing and application record-content accounting; not complete network-wire bytes or isolated cryptographic CPU cost. |
| How are experiments orchestrated? | `scripts/run_on_wsl.sh`; `scripts/main_cli.py`; `main_study/campaign.py`; `main_study/common.py` | Preparation, staged training blocks, model sealing, separate evaluation authorisation and file integrity checks. |
| How was correctness checked? | `tests/`; `tests_main/`; `scripts/run_main_tests.py` | Test fixtures, boundary checks and main-study regression tests. Test results and native execution claims must be distinguished. |

The function locations above were identified by parsing the archive's Python files without importing or executing them. Line numbers refer only to this frozen source version.

## Evidence to deliver alongside the source

The supervisor should receive an indexed, access-reviewed copy of the completed run evidence: the preparation report; ten main-block reports; the completion report including `selected_models_manifest.json`; the final evaluation report; and the final score-audit report and arithmetic code. Report identifiers should connect configuration, distribution, seed, source identity, checkpoint digest, calibration digest and metric file.

`EHR_FL_Final_Score_Audit_Review_v1_0.zip` contains the separate post-evaluation arithmetic audit, including `audit_scores.py` and `test_audit_metrics.py`. It is not the trainer or a new model. `EHR_FL_Results_and_Discussion_v1_0.zip` contains the writing, tables and figures layer, not the experimental source.

The 30 selected checkpoints and their calibration files should be indexed separately. Provide model parameters rather than any client secret state or individual local-update collection. Availability of these files on the researcher's machine is not equivalent to their inclusion in this guide.

## Three different review/reproduction tasks

**Code inspection.** Browse the paths above and follow one A/B/C block through its recorded evidence. No training is necessary.

**Metric reproduction.** Recompute the reported metrics from the already saved scores and calibration evidence using the arithmetic audit. This checks metric calculation and joins; it does not reproduce training or model inference.

**Full independent rerun.** Requires the original benchmark or approved prepared inputs, schema/scaler, frozen client membership and draw schedules or their verified derivation, pinned environment including the local Flower build, and a documented path to initialise a new campaign. The existing launcher relies on earlier preprocessing/inference/accepted-environment paths and campaign-specific records. A GitHub clone alone does not supply these assets. Validate a clean setup before describing it as a one-command reproduction. Any later portability wrapper is a post-experiment addition and must not overwrite the archived experimental source or completed outputs.

The original data generator was not established as available in the accepted provenance record. File-based reproduction must not be described as independently verified regeneration of the synthetic benchmark.

## Local Flower build and attribution

The archived dependency identity is `1.22.0+mai.prg7570.1`, not an ordinary stock Flower installation. The stored change manifest identifies the upstream contributor revision `e87804ad00c46bff6dc3f058b73de81529e50bc0`. Preserve the attribution, Apache notices and exact patch/build inputs supplied with the archive. The historic PR status in its manifest is a record of that review, not a claim about the PR's current status.

Do not relabel the patch as a new cryptographic protocol or an official Flower release. The main implementation does not include TLS or local-only experiments. Its local guards and hashes are not formal privacy certification, OS isolation or remote attestation.

## Presentation and result integrity

Retain all planned seeds, both test sets, negative findings, and the documented history of unsuccessful runs and repairs. Do not backdate a new Git history to simulate a contemporaneous development record. Distinguish project integration, third-party implementations and programming assistance in the contribution statement.

For a short review meeting, trace the model and loss, then one client fit, the B/C workflow difference, validation-only calibration, and the final metric calculation. Show an observed limitation as well as a successful execution. A saved result shown in a demonstration must be labelled as saved output, not as a fresh training run.
