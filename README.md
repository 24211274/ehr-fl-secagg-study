# EHR federated anomaly-detection study — supervisor review

A post-experiment handover of the implementation and audited results for campaign `20260909T142009Z_2ad79bf6`. The Git history starts at handover; it is **not** a reconstructed or backdated development history.

**Start with [the supervisor code guide](docs/original_handover_guide/SUPERVISOR_CODE_GUIDE.md)** and [the evidence index](evidence/INDEX.md).

## What is included

| Directory | Purpose |
| --- | --- |
| [`executed/EHR_FL_Main_Experiments_Package_v1_0_3/`](executed/EHR_FL_Main_Experiments_Package_v1_0_3/) | Complete, byte-preserved executed source package, including its original integrity manifest, configuration, tests, historical review records and third-party notices. |
| [`analysis/final_score_audit/`](analysis/final_score_audit/) | Separate post-evaluation arithmetic audit, its code, tests and audited aggregate/per-model/per-client metric tables. Not a new detector. |
| [`results/tables/`](results/tables/) | Existing tables used in preparing the Results and Discussion chapters, including all five seeds and both conditions. |
| [`results/figures/`](results/figures/) | Existing PNG/SVG figures derived from those tables. |
| [`docs/`](docs/) | Reading guide, data-access limits, reproducibility boundaries and contribution disclosure. |
| [`evidence/`](evidence/) | Source identities, copied evidence summaries and handover file manifest. |
| [`tools/verify_handover.py`](tools/verify_handover.py) | New, standard-library-only handover checksum verifier; does not train or score models. |

## Executed design and outcome

The executed comparison comprises A (centralised reference), B (Flower FedAvg) and C (FedAvg with SecAgg+ in a locally modified Flower build), three simulated clients, Reference and controlled Non-IID conditions, and seeds 11, 29, 47, 71 and 97. There are 30 trained/selected models and 60 final model–test-set evaluations in the accepted campaign record. The primary model is the compact LSTM autoencoder with 119 input dimensions.

The accepted implementation has **no local-only experiment and no TLS experiment**. Do not infer either from older research proposals or from general descriptions of federated learning. The local Flower identity is `1.22.0+mai.prg7570.1`; attribution and modification notices are retained in the executed package.

**Negative findings are retained:** the detector frequently flags unusual legitimate activity, and performance on `test_known` is poor. Small observed B/C differences are not an equivalence proof. Instrumented execution time is not isolated cryptographic time; application record-content volume is not complete network traffic. See [the audited findings](analysis/final_score_audit/AUDITED_RESULTS.md).

## Review safely

For a read-only integrity check, from this repository root run:

```console
python -I -B tools/verify_handover.py
```

This does not install dependencies or contact a service. Do **not** start `PrepareRepair`, `TrainNextBlock` or `Evaluate` in the completed original campaign just to demonstrate the project. Instructions inside the frozen source README describe its historical preparation stage, not a new review task.

A fresh clone supports code and result inspection. It does **not** contain the raw benchmark, individual saved score files, selected checkpoints, fitted scaler arrays, local virtual environments or all campaign reports. Metric reproduction and full retraining require separately authorised assets; see [REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md).

## Sharing and attribution

This handover is intended for a **private** repository. It does not grant a new blanket software or dataset licence. Third-party notices remain applicable; public release of the benchmark is not established. See [DATA_ACCESS.md](docs/DATA_ACCESS.md) and [CONTRIBUTIONS.md](docs/CONTRIBUTIONS.md).
