# Reproducibility boundaries

## 1. Inspect code and existing results

Read the root README, supervisor guide and evidence index. Run `python -I -B tools/verify_handover.py` to check the handover files against the supplied SHA-256 manifest and the original source manifest. This verifies file consistency, not research validity or cryptographic security.

## 2. Reproduce metric arithmetic

Use `analysis/final_score_audit/REPRODUCE_AUDIT.md` with separately authorised saved-score/calibration evidence, the final evaluation report and original source labels. The audit can recalculate AP, AUROC and decision metrics without retraining. This repository includes the audit code and outputs, but not all its private inputs. Tests on numerical fixtures are not repeat training runs.

## 3. Reproduce training/inference from a new host

This has not been established as a one-command path by this handover. The frozen launcher depends on earlier preprocessing and validation evidence, fitted transforms, initial states/draws or their verified generation, campaign-specific files and the pinned local Flower build `1.22.0+mai.prg7570.1`. Inspect the retained build provenance; do not substitute the latest stock Flower release.

An independent rerun needs an approved asset transfer and a new workspace, preserving the completed campaign. A later portability wrapper must be identified as a post-experiment addition and must not overwrite the original executed source or claim to have produced the original results.

No training, inference, threshold refitting or score-direction change was performed when preparing this GitHub handover. Test data have already been evaluated; new development must not be represented as blind tuning on untouched test sets.
