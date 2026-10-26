# Reproduction materials

Start with [the online file and download guide](AVAILABILITY.md). The release supplies the original audit inputs, all 30 selected model records, raw/frozen preparation inputs, dependency wheels and replay controls. File inventories and hashes distinguish these materials from newly generated outputs.

## Integrity inspection

Run the two standard-library verifiers in the root README. The original executed 215-file source and PACKAGE_SHA256SUMS.txt remain unchanged. The historical handover manifest is retained under evidence/historical; the current handover manifest covers the enlarged repository and corrects the pre-existing README checksum drift.

## Saved-score arithmetic

The audit package supplies all five inputs required by analysis/final_score_audit/audit_scores.py. Its numerical-fixture tests and an actual file-only arithmetic pass are recorded separately from model inference or training. Use the package's instructions and a new output directory.

## New-session inference

The inference directory contains its own model, calibration, preprocessing assets, dependency files, template and samples. Its self-test checks the fixed C/Reference/seed11 example. It does not retrain or recalibrate the model.

## Full training replay

The archived ME06 control files and offline Python 3.12 Linux wheels are supplied, including the local Flower build. Historical absolute paths and predecessor identity guards remain visible. Restore into a new workspace and review those path bindings before execution. Availability of the materials is not a claim of new independent-host training validation or a newly tested one-command launcher.

This online publication step performs integrity checks, score arithmetic and demo tests only; it does not repeat the benchmark training or change the thesis results.
