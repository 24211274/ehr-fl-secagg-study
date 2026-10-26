# Code data and artifact availability

The study archive is hosted at [https://github.com/24211274/ehr-fl-secagg-study](https://github.com/24211274/ehr-fl-secagg-study). The versioned download is [study-artifacts-v1.30](https://github.com/24211274/ehr-fl-secagg-study/releases/tag/study-artifacts-v1.30). It is a private repository: readers must sign in with a GitHub account that has been granted read access. A private link alone does not grant permission.

## Find the required files

| Task | Required material |
| --- | --- |
| Inspect the original implementation | [Executed source](../executed/EHR_FL_Main_Experiments_Package_v1_0_3/), [source manifest](../executed/EHR_FL_Main_Experiments_Package_v1_0_3/PACKAGE_SHA256SUMS.txt) |
| Read the reported results | [Metric tables](../results/tables/), [figures](../results/figures/), [arithmetic audit](../analysis/final_score_audit/AUDITED_RESULTS.md) |
| Read appendix evidence | [Current evidence index](../supplementary/README.md) |
| Recalculate metrics from saved scores | Audit-input release package and [the unchanged audit script](../analysis/final_score_audit/audit_scores.py) |
| Score a new session | [Inference application](../inference/), [user guide](user_guides/Session_Check_User_Guide_EN.pdf), [synthetic samples](user_guides/Session_Check_Test_Samples.zip) |
| Inspect or restore the training/replay inputs | Replay-input/model, offline-runtime and replay-control release packages |

The inference demonstration uses the original C / Reference / seed 11 / selected round 30 checkpoint. The separate replay-model package contains all 30 selected study checkpoints; the demo is not all 30 models.

## Download the larger packages

Open the release page and download the four named ZIP assets. For authenticated command-line download, use GitHub CLI:

```console
gh release download study-artifacts-v1.30 --repo 24211274/ehr-fl-secagg-study --dir downloads
python -I -B tools/verify_online_assets.py --directory downloads --require-all
```

To restore all packages into a new directory, run:

```console
python -I -B tools/restore_online_assets.py --directory downloads --output restored
```

This verifies the ZIP and member hashes without starting training.

Every release ZIP contains its own file inventory. Package-specific metadata filenames permit extracting the packages into the same new workspace without metadata collisions. Extract into a new directory, preserving the completed historical campaign.

## Recalculate the saved-score metrics

Install the analysis dependencies described in [the audit instructions](../analysis/final_score_audit/REPRODUCE_AUDIT.md). Extract `Study_Audit_Inputs_Original.zip`, or restore all four packages as above. Then run from the repository root:

```console
python -B tools/run_stored_score_audit.py --restored restored --output ../metric-output
```

This wrapper passes the five files under `audit_inputs/` to the unchanged audit script: `saved_scores_original.zip`, `final_evaluation_original.zip`, `training_completion_original.zip`, `frozen_source_original.zip` and `benchmark_original.zip`. The source archive is a new ZIP container around the exact 215 original source members and their unchanged manifest. Its container bytes are not described as the unavailable original source ZIP.

The audit reads existing scores and source labels and verifies the complete benchmark's bytes. It does not train a model, perform inference or refit thresholds. Use a new output directory.

## Run the new-session demonstration

See [the local inference quick start](INFERENCE_QUICKSTART.md) and [inference README](../inference/README.md). The hosted demonstration is [Session Check](https://session-check-demo.onrender.com). Its deployment branch remains `codex/public-demo`; this archive does not change that deployment configuration.

## Training and replay records

The release includes the archived inputs, models, runtime wheels and replay/preprocessing controls identified in the manifests. Historical replay controls contain the original author's absolute paths. Restoring those controls requires mapping their recorded paths into a new workspace; their inclusion alone is not a tested one-command training path on an independent host. Python and the operating system are installation prerequisites, not bundled virtual environments.

The verification record distinguishes archive integrity, score arithmetic and demonstration inference from new full training. No new benchmark training is required to inspect this archive.

## Rights and historical statements

This is a controlled-access research archive. Dataset creator, original generation rules and redistribution rights remain unverified. Uploading a snapshot to this private repository does not establish a public dataset release or grant a new licence. Third-party notices in the executed source, preprocessing source and dependency wheels remain applicable.

Historical evidence packages are preserved as dated records. Their old local-only availability descriptions are superseded for current file location by this page; their scientific results and limitations remain unchanged.
