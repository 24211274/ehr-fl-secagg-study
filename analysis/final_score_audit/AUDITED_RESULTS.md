# Final stored-score audit and verified detection results

**Campaign:** `20260909T142009Z_2ad79bf6`  
**Decision:** arithmetic audit passed; retain the original final evaluation. This decision validates the recalculation from the supplied scores, not deployment readiness, cryptographic security, external label validity or a new model evaluation.

## 1. Audit scope and evidence

The supplied export contains 60 existing score CSV files and 30 frozen calibration files. The 90,270 score rows correspond to 3,009 distinct session identifiers evaluated by 30 models, not 90,270 independent observations. The two tests contain 2,364 and 645 sessions, respectively. The 94 payload files match the export manifest; the manifest itself is the 95th archive member. The original final-report manifest, stage status and source-integrity record match the previously supplied final report. The selected-model manifest is byte-identical to the pre-evaluation completion record.

All score-file session identifiers, clients, partitions, binary labels, scenario identifiers and primary classes match `labels.csv` in the preserved synthetic benchmark. There are no duplicate session identifiers within any score file, no overlap between the two tests, and no overlap with development session identifiers. `TRUE` maps to threat label 1 and `FALSE` to legitimate label 0. These are internal consistency checks, not independent adjudication of the synthetic labels or a comprehensive leakage audit.

AP was independently calculated by grouping equal scores in descending order and summing precision at the score cut-offs, weighted by the increments in recall. AUROC was independently calculated from positive–negative score comparisons, counting ties as one half. Both calculations were cross-checked against scikit-learn. The audit recalculated 300 distinct ranking groups (600 AP/AUROC values), 720 decision-metric groups at the three frozen quantiles, 63,000 scenario-count groups including repeated quantiles, 144 method–endpoint summaries, 96 paired contrasts and 16 predeclared exploratory intervals. The largest difference in a ranking/decision metric versus the original report was `3.3306690738754696e-16`; no discrepancy exceeded the absolute tolerance `1e-12`.

The original score direction and all raw thresholds were retained. The primary global ranking uses the client-specific validation transformation `(loss − validation median) / validation scale`. Per-client ranking uses raw loss. Secondary pooled raw-score metrics were also recalculated. Decision metrics use the fixed client threshold and the strict `>` operator. Positive affine calibration preserved ranking within every client; the decision in raw and transformed coordinates agreed for all stored scores and all three quantiles. No probability calibration is implied.

## 2. Original primary test: `test_held_out`

This test comprises 189 labelled `low_and_slow_misuse` threat sessions, 1,986 routine legitimate sessions and 189 unusual legitimate `longitudinal_follow_up` sessions. The threat prevalence is 7.9949%. Each entry below summarises the five fixed training seeds (11, 29, 47, 71, 97). `±` denotes sample standard deviation across seeds. Decision metrics use the frozen 0.99 validation quantile, not a threshold selected on the test.

A = pooled centralised reference; B = Flower FedAvg; C = FedAvg with SecAgg+ in the approved locally patched build.

| Condition | Method | AP, mean ± SD | AUROC, mean ± SD | Precision | Recall | FPR |
|---|---|---:|---:|---:|---:|---:|
| Reference | A | 0.4858 ± 0.1175 | 0.9537 ± 0.0111 | 51.05% | 98.84% | 8.34% |
| Reference | B | 0.4161 ± 0.0491 | 0.9430 ± 0.0093 | 45.93% | 84.87% | 8.75% |
| Reference | C | 0.4208 ± 0.0536 | 0.9437 ± 0.0094 | 46.00% | 84.97% | 8.74% |
| Controlled Non-IID | A | 0.4055 ± 0.0356 | 0.9432 ± 0.0064 | 48.72% | 96.83% | 8.93% |
| Controlled Non-IID | B | 0.4293 ± 0.0240 | 0.9459 ± 0.0054 | 49.57% | 81.38% | 7.19% |
| Controlled Non-IID | C | 0.4294 ± 0.0250 | 0.9457 ± 0.0056 | 49.85% | 82.01% | 7.16% |

## 3. Original secondary test: `test_known`

This test comprises 378 threat sessions and 267 unusual legitimate sessions, with **no routine legitimate background**. Threat prevalence is 58.6047%. Its composition differs from `test_held_out`; it is not pooled with that test. All below-chance AUROC values in the original report were reproduced from the stored scores. Neither labels nor score direction were reversed to improve them.

| Condition | Method | AP, mean ± SD | AUROC, mean ± SD | Precision | Recall | FPR |
|---|---|---:|---:|---:|---:|---:|
| Reference | A | 0.4766 ± 0.0526 | 0.3365 ± 0.1303 | 58.86% | 99.68% | 98.65% |
| Reference | B | 0.4025 ± 0.0069 | 0.1377 ± 0.0260 | 53.04% | 78.94% | 98.80% |
| Reference | C | 0.4040 ± 0.0074 | 0.1432 ± 0.0274 | 52.65% | 77.67% | 98.58% |
| Controlled Non-IID | A | 0.4724 ± 0.0218 | 0.3298 ± 0.0528 | 58.95% | 99.58% | 98.20% |
| Controlled Non-IID | B | 0.4107 ± 0.0075 | 0.1670 ± 0.0260 | 50.21% | 69.47% | 96.40% |
| Controlled Non-IID | C | 0.4113 ± 0.0074 | 0.1692 ± 0.0254 | 50.61% | 70.74% | 96.40% |

The low AUROC is not solely an artefact of pooling client-specific scales. For method C, the pooled raw-score AUROC means are 0.142786 (Reference) and 0.168936 (Non-IID), compared with calibrated-score means of 0.143240 and 0.169213. All 30 per-client C AUROC values in `test_known` are below 0.5; their range is 0.099608–0.221241. Thus the ranking problem remains within individual clients using the untransformed scores.

## 4. Post-test descriptive error analysis — not a revised primary endpoint

The following diagnostics were computed after viewing the original evaluation. They explain the recorded errors without selecting new thresholds, fitting a new model, excluding difficult cases from the primary results or claiming a new confirmatory experiment.

| Legitimate session group | Sessions per model | C Reference FPR | C Non-IID FPR |
|---|---:|---:|---:|
| Held-out: routine legitimate | 1,986 | 1.26% | 1.36% |
| Held-out: unusual legitimate follow-up | 189 | 87.30% | 68.15% |
| Known: unusual legitimate | 267 | 98.58% | 96.40% |

The distinction between unusual-but-authorised behaviour and misuse is weak in these scores. For example, unusual legitimate sessions in `test_known` include approved troubleshooting, emergency access, cross-department cover and authorised long sessions. These are source-provided synthetic categories, not validated observations of actual hospital practice.

| Positive-versus-negative comparison, method C | Reference AUROC | Non-IID AUROC |
|---|---:|---:|
| Held-out threats vs routine legitimate | 0.9925 | 0.9899 |
| Held-out threats vs unusual legitimate | 0.4307 | 0.4805 |
| Known threats vs unusual legitimate | 0.1432 | 0.1692 |

The held-out global AUROC is a negative-class-weighted combination of the two comparisons: the 1,986 routine negatives dominate the 189 unusual legitimate negatives. The weighted identity was checked for all 30 models in raw and calibrated coordinates (60 checks). The high aggregate AUROC therefore coexists with poor discrimination against the unusual legitimate subgroup. This calculation explains an observed metric pattern; it does not establish whether architecture, feature representation or synthetic scenario construction is the principal cause.

### Predeclared threshold sensitivity

| Test | Condition | Frozen quantile | C recall | C FPR |
|---|---|---:|---:|---:|
| test_held_out | reference | 0.98 | 89.52% | 9.63% |
| test_held_out | reference | 0.99 | 84.97% | 8.74% |
| test_held_out | reference | 0.995 | 76.19% | 7.83% |
| test_held_out | noniid | 0.98 | 88.99% | 8.71% |
| test_held_out | noniid | 0.99 | 82.01% | 7.16% |
| test_held_out | noniid | 0.995 | 74.18% | 6.36% |
| test_known | reference | 0.98 | 89.89% | 99.63% |
| test_known | reference | 0.99 | 77.67% | 98.58% |
| test_known | reference | 0.995 | 50.21% | 92.58% |
| test_known | noniid | 0.98 | 87.83% | 98.95% |
| test_known | noniid | 0.99 | 70.74% | 96.40% |
| test_known | noniid | 0.995 | 42.17% | 86.29% |

These are the already specified sensitivity settings, not a new threshold search. They do not replace 0.99 as the primary setting. At 0.995, the known-test FPR remains high while recall falls; changing a decision threshold also cannot reorder fixed anomaly scores.

## 5. Predeclared paired comparisons

| Test | Condition | Endpoint | Contrast | Mean difference | Exploratory 95% interval |
|---|---|---|---|---:|---|
| test_held_out | reference | Global AP | B − A | -0.069672 | [-0.237533, +0.098189] |
| test_held_out | reference | Global AP | C − B | +0.004652 | [-0.001834, +0.011137] |
| test_known | reference | Global AP | B − A | -0.074188 | [-0.143647, -0.004728] |
| test_known | reference | Global AP | C − B | +0.001543 | [-0.001514, +0.004600] |
| test_held_out | noniid | Global AP | B − A | +0.023826 | [-0.036166, +0.083818] |
| test_held_out | noniid | Global AP | C − B | +0.000139 | [-0.004262, +0.004540] |
| test_known | noniid | Global AP | B − A | -0.061700 | [-0.091239, -0.032161] |
| test_known | noniid | Global AP | C − B | +0.000582 | [-0.000767, +0.001930] |

These intervals reproduce the frozen five-seed paired Student-t calculation. They are exploratory and conditional on the fixed benchmark; nominal coverage with five seeds is not established. They are not equivalence tests and are not intervals over independent hospitals. B does not show consistent superiority to A on the held-out test. The observed C−B AP differences are small, but a claim of mathematical identity, no effect under all conditions, or privacy certification is not supported.

### Worst-client AP

| Test | Condition | A | B | C |
|---|---|---:|---:|---:|
| test_held_out | reference | 0.4594 ± 0.1158 | 0.3938 ± 0.0419 | 0.3975 ± 0.0464 |
| test_held_out | noniid | 0.3918 ± 0.0336 | 0.4077 ± 0.0199 | 0.4071 ± 0.0175 |
| test_known | reference | 0.4727 ± 0.0506 | 0.4010 ± 0.0050 | 0.4022 ± 0.0050 |
| test_known | noniid | 0.4653 ± 0.0212 | 0.4094 ± 0.0096 | 0.4096 ± 0.0093 |

Each seed contributes the minimum of its three client AP values before aggregation across seeds; this is not the minimum of client means. Full per-client values are retained in the CSV files.

## 6. Reporting decision and remaining limits

**Accept the arithmetic of the final detection results, including the negative findings. Do not rescore, reverse the anomaly-score direction, retune the model, relabel the benchmark or change thresholds to improve these test results.** The audit does not justify deploying the detector as a reliable threat/legitimacy discriminator. Retain the completed campaign and the already disclosed source, licence, test-exposure and security limitations.

The raw score files were not listed in the original final-report hash manifest. The new export fixes their hashes, and the recomputation shows consistency with the original aggregate and scenario results; this is not an independent rerun from model weights. Validation medians, scales and quantile estimates were not refitted because the underlying validation-score arrays are absent, although the calibration files match the completion record and their use was checked for every test score. No new cryptographic claim or claim of real-hospital generalisation follows from this work.

The next reporting task is Chapter 4: document the fixed protocol, the two different test compositions, all A/B/C results, per-client variation, the paired comparisons and the false-positive failure analysis; then relate the detection results to the separately audited time and application-payload costs in the discussion. The research contribution must be stated as bounded implementation and empirical evaluation, not a successful elimination of false alarms or a certified privacy-preserving system.

## 7. Reproducibility and contents

`audit_scores.py` reads supplied archives and writes only to a new audit output directory. It imports no study model or Flower runtime. `test_audit_metrics.py` supplies 12 fixtures for score ordering, ties, class absence, monotonic transformation, decision denominators and non-finite-input rejection. All 12 passed. Two complete arithmetic runs gave byte-identical shared CSV results. No user-side command is required to continue writing.

Sources are the following user-provided archives and preserved members; no external literature was used to substitute for missing experimental evidence.

- **scores:** `8dd948ee-36ee-4857-98c5-2369906fe735.zip`, SHA-256 `6bd4d752c12730d6d93143c2e8bd184622b5e5c2778d244a1327ddc1657d6dcf`.

- **report:** `7e7c3043-b7fe-4a9f-848d-f384f1bdd962.zip`, SHA-256 `fe66ff79196f2936605ce873689821a0716fa7bf7c7c99323ad5af26e8497ecd`.

- **completion:** `a4eabf5e-947f-45b5-a072-4f5c2c50bb47.zip`, SHA-256 `9adc12c476b689c92e2e2daa2e0333f1439cc7ab09483e8983cc11cfd0c2e879`.

- **source:** `EHR_FL_Main_Experiments_Package_v1_0_3.zip`, SHA-256 `433a26789afd362dad4316c96379017d2808969925fa5df1d61e332d94cb6c84`.

- **benchmark:** `EHR_FL_Benchmark_Publication_Package_v1_0.zip`, SHA-256 `b551bfdbe515ba40fc5b147163aad619788566062d5e571339aa9ef60d06700e`.

The authoritative audit record is `Final_Score_Arithmetic_Audit.json`. The aggregate CSVs are analytical outputs, not additional participants, runs or model predictions.
