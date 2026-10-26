# EHR federated anomaly detection study

Code, data, trained models and supporting evidence for the executed study are indexed in the [online availability guide](docs/AVAILABILITY.md). Download the versioned packages from [study-artifacts-v1.30](https://github.com/24211274/ehr-fl-secagg-study/releases/tag/study-artifacts-v1.30). This repository is private; GitHub read access is required.

## Start here

- [Availability and download instructions](docs/AVAILABILITY.md)
- [Evidence supporting the thesis appendices](supplementary/README.md)
- [Original supervisor code guide](docs/original_handover_guide/SUPERVISOR_CODE_GUIDE.md)
- [Run the English inference demonstration](inference/README.md) or [open the hosted app](https://session-check-demo.onrender.com)
- [Current thesis and concise appendices](manuscript/README.md)

## Contents

| Location | Contents |
| --- | --- |
| `executed/` | Original executed source: 215 manifested files preserved byte for byte. |
| `analysis/` and `results/` | Metric audit, five-seed result tables and figures. |
| `supplementary/` | Evidence Companion, metric derivations, replay/security/repair records, literature records and diagnostics. |
| `inference/` | Relocatable new-session application, selected C/Reference/11 model, schema, scaler, calibration and samples. |
| `docs/` | Access, reproduction and user instructions. |
| `manuscript/` | Thesis and condensed appendices with online links. |
| Release assets | Complete audit inputs, replay inputs and all selected models, offline runtime, replay controls and records. |

## Verify the download

```console
python -I -B tools/verify_handover.py
python -I -B tools/verify_online_assets.py --directory downloads --require-all
```

The first command checks the checkout and the original source manifest. The second checks downloaded release packages by size and SHA-256; it does not run training. See [availability](docs/AVAILABILITY.md) for the separate arithmetic and inference checks.

## Study and history

Campaign `20260909T142009Z_2ad79bf6` compares pooled centralised training, Flower FedAvg and FedAvg with SecAgg+ across three simulated clients, two sampling conditions and five seeds, producing 30 selected models and 60 model/test evaluations. The detector uses 119 input dimensions. Reported poor detection of unusual legitimate activity remains part of the results; no equivalence or comprehensive privacy claim is introduced by this archive.

Git history begins with the post-experiment handover. The later online packaging and inference demonstration are identified additions; they are not a reconstructed development history. The deployment branch and original executed scientific source remain distinct.

Dataset origin and redistribution rights remain unverified. This private archive grants no new blanket licence; see [data access](docs/DATA_ACCESS.md), [reproduction](docs/REPRODUCIBILITY.md) and [contributions](docs/CONTRIBUTIONS.md).
