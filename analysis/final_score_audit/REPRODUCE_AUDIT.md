# Reproducing this file-only audit

No model or Flower runtime is imported. No training, model inference, resampling or threshold fitting is performed.
The audit writes only to a newly named output directory. The main campaign is never accessed.

Audit environment used:
Python 3.13.5; NumPy 2.3.5; pandas 2.2.3; SciPy 1.17.0; scikit-learn 1.8.0.
This is an analysis environment, not a replacement for the frozen training environment.

Run `python -B -m unittest -v test_audit_metrics` to execute the 12 arithmetic fixtures.

The recorded full audit invocation was:

```sh
python -B audit_scores.py \
  --scores /mnt/data/8dd948ee-36ee-4857-98c5-2369906fe735.zip \
  --report /mnt/data/7e7c3043-b7fe-4a9f-848d-f384f1bdd962.zip \
  --completion /mnt/data/a4eabf5e-947f-45b5-a072-4f5c2c50bb47.zip \
  --source /mnt/data/EHR_FL_Main_Experiments_Package_v1_0_3.zip \
  --benchmark /mnt/data/EHR_FL_Benchmark_Publication_Package_v1_0.zip \
  --output /mnt/data/_final_score_audit_work/run2
```

These `/mnt/data` paths are the audit environment paths, **not paths on the researcher's Windows machine**.
Input file hashes, not attachment names alone, identify the sources. Use the corresponding preserved archives
and a new output directory for any independent reproduction. Do not run Python with optimisation (`-O`),
because assertions implement several data-integrity checks in this audit script.

This package does not redistribute raw event data, per-session score rows, model weights, or protocol secrets.
Its CSV outputs are numerical audit/summary tables, not extra experimental runs. Null metric values indicate
that the required denominator or class is absent, as specified in the original frozen evaluator.
