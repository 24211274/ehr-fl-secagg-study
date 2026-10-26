# Study evidence index

Current online index for release [study-artifacts-v1.30](https://github.com/24211274/ehr-fl-secagg-study/releases/tag/study-artifacts-v1.30). Repository read access is required.

## Results and evidence

| Material | Files |
| --- | --- |
| Saved-score metrics and scenario derivations | [Traceability package](Result_Traceability_Evidence.zip), [instructions](README_Result_Traceability.md) |
| Same-host computational replay | [ME06 evidence](ME06_Evidence.zip) |
| Original security validation | [Seven-group evidence](Security_Validation_Evidence.zip) |
| Separate input-validation correction and retest | [SV05 repair evidence](SV05_Repair_Evidence.zip) |
| Post-test diagnostics | [Code and records](Supplementary_Diagnostics.zip) |
| Literature search and source-access records | [Search update](Literature_Refresh_ME04_ME05_20261011.zip), [access inventory](Source_Access_Update.json) |
| Original supplement file identities | [Preserved v1.18 manifest](Artifact_Manifest.json) |

The traceability package contains 60 saved-score CSVs, 30 calibration records and archived evaluation inputs. These are existing results, not newly generated predictions.

## Security validation

Use both the original seven-group package and the separate SV05 correction package. The original 101 cases, later 59 targeted cases, 12 guard cases and 75 unit/regression tests retain their different counting units.

## Reproduction downloads

| Package | Purpose |
| --- | --- |
| [Audit inputs](https://github.com/24211274/ehr-fl-secagg-study/releases/download/study-artifacts-v1.30/Study_Audit_Inputs_Original.zip) | Five inputs for the unchanged score-arithmetic audit, including the original benchmark snapshot and byte-preserved source members. |
| [Replay inputs and selected models](https://github.com/24211274/ehr-fl-secagg-study/releases/download/study-artifacts-v1.30/Study_Replay_Inputs_And_Selected_Models.zip) | Raw/frozen inputs, selected checkpoints, calibration and validation records. |
| [Offline Linux runtime](https://github.com/24211274/ehr-fl-secagg-study/releases/download/study-artifacts-v1.30/Study_Offline_Runtime_Linux_Python312.zip) | Pinned Python 3.12 dependency wheels, including the local Flower build. |
| [Replay controls and records](https://github.com/24211274/ehr-fl-secagg-study/releases/download/study-artifacts-v1.30/Study_Replay_Controls_And_Records.zip) | Preprocessing and replay source, locks, controls and historical execution records. |

See the [complete availability and verification guide](../docs/AVAILABILITY.md) and [release checksum manifest](../evidence/ONLINE_RELEASE_ASSETS.json).

## Historical records

[Original v1.18 index](Evidence_Companion.md) and [historical narrative](Historical_Evidence_Companion.md) retain their original text. The publication copies of three archives withhold the author’s declaration identifier in editorial and extracted page-text records; [the redaction record](../evidence/PUBLICATION_REDACTIONS.json) identifies affected members and original/current hashes. Scientific source, data, models and numeric results are unchanged. The v1.18 artifact manifest describes the original packages; the current handover manifest describes these publication copies. Their historical local paths and earlier availability statements describe their original revision, not the current online inventory. Compatibility copies repair three historical links without rewriting those records.

The supplied benchmark's origin and redistribution rights remain unverified. This controlled-access archive does not establish a public data licence, ethics clearance or a new clinical validation.
