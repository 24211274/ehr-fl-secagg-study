# Result traceability evidence

The two missing supplementary trace records have been reconstructed from preserved test scores, source-assigned labels and saved validation calibration records. This is a new post-test derivation, not recovery of historical missing files, an independent dataset validation or a new training experiment.

## Main records

- `outputs/worst_client_by_seed_reconstructed.csv`: 60 model–condition–seed–test records, including 30 primary held-out records. Each row retains C1/C2/C3 average precision (AP), the within-seed minimum, every exactly tied minimum-client identity, counts and source hashes. AP is non-interpolated and computed from raw loss, grouping tied scores. Display rounding is not used to define ties. There are no exact minimum-AP ties in these records.
- `outputs/scenario_error_by_seed_reconstructed.csv`: 44,220 descriptive records at all-client and individual-client scopes, grouped separately by preserved scenario identifier, primary class, legitimate subtype and threat family. It retains TP/TN/FP/FN, denominators, applicable rates and the frozen threshold range. Many scenario identifiers denote individual scenario instances, not distinct threat families. A blank preserved scenario identifier is not renamed or imputed.

The grouping families and global/client scopes overlap. Do not add all rows together or treat repeated sessions across models/seeds as independent samples. For positive-only groups, alert rate is recall and FPR is undefined; for negative-only groups, alert rate is FPR and recall is undefined. Undefined values are empty CSV cells, not zeros. Scenario AP/AUROC are not computed. `threshold_min` and `threshold_max` delimit the participating clients' saved thresholds; a global row does not imply use of a single pooled threshold.

## Inputs and decision rules

The package retains the exact score-export and original evaluation archives, the labels extracted from the supplied benchmark snapshot, the preserved descriptive summary, the original evaluation source, the two manuscript tables and source lineage. There are 60 score files, 30 validation calibration records, 90,270 scored rows and 3,009 distinct evaluated sessions. The latter appear repeatedly across 30 trained models.

The alert decision is `raw loss > saved client validation threshold at q=0.99`. All thresholds were retained as supplied. No training, inference, checkpoint selection, threshold fitting, score reversal or test-driven tuning was performed. These results concern the supplied source labels and fixed dataset, and do not establish the labels' independent clinical/security validity, data-generation provenance, redistribution rights or ethics clearance.

## Verification

- Every saved score/label binding was checked against the supplied labels and stable model membership.
- All 180 client AP values, all 60 minimum AP values and identities, and original per-client/global confusion counts were reconciled. Maximum client AP discrepancy from the original preserved evaluation is 3.3306690738754696e-16, a floating-point arithmetic difference.
- All 21,000 original global scenario count records matched. All 108 preserved descriptive summaries matched using round-trip float parsing.
- All 24 formatted mean/sample-SD fields in Table 4.8 and all six FPR mean/sample-SD fields in Table 4.10 matched, including session denominators 1,986, 189 and 267.
- Separate implementations independently recomputed AP and scenario counts. Cross-checks covered all 60 worst-client rows and all 44,220 scenario records, including undefined-rate handling. Independent derivation is a numerical check on the same preserved data, not an external replication.

`outputs/Derivation_Receipt.json`, `outputs/Numerical_Reconciliation.json`, the independent cross-check receipts, source hashes and the retained execution log document these assertions. Duplicate copies of the score export are byte-identical and were not counted as independent evidence sources.

## Re-run the derivation

Use Python with NumPy and pandas. The executed environment was Python 3.12.14, NumPy 2.3.5 and pandas 3.0.1 on Windows. No scikit-learn installation is needed by the derivation script.

```text
python derive_traces.py --input-dir inputs --output-dir reproduced_outputs
```

Use a new output directory so that the delivered records remain intact. JSON execution timestamps/platform strings can differ; scientific CSV contents and numeric checks should match. Input archive/member hashes and the input-lineage file identify the preserved source snapshot. The original generator is not provided because it was not established in the supplied records. The independent checking scripts retain their actual execution paths in their receipts; the main script above is the portable reproduction entry point.

## Reading the revised Word files

Revision 1.14 updates §4.6, §4.8.1, Appendix C.4 and the note below Table C.6. Scientific table values and figures are unchanged. Yellow highlights identify corrected availability statements; green identifies the added derivation/evidence explanation; cyan identifies the new evidence link. Margin comments explain each of the four edits. The clean copy has identical text without highlights/comments.

The earlier Evidence Companion and annotated revision are retained as historical records. Statements there that a file was not located describe the earlier audit state, not the availability of this newly reconstructed supplementary record. Current data-source, licence and ethics limitations remain unchanged pending original documentation.

This is a private local evidence package. Its creation grants no new permission to redistribute underlying data or previous project evidence.
