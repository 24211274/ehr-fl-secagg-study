# Session Check

A public research demonstration of the retained C / Reference / seed 11 LSTM model. The model, encoding schema, training-time scaler and per-client calibration are the original project files.

Visitors upload one complete CSV session, choose C1/C2/C3, and run inference. Results include the raw reconstruction score, the original client threshold, event contributions, an optional review and a browser-side JSON download.

Each visitor has a separate temporary session. Uploaded contents, results and review notes stay in server memory temporarily and are not written to a database or uploaded-file directory. Session expiry, eviction and service restart discard this temporary state. Use synthetic or de-identified test data.

The score is reconstruction error, not a threat probability. This demonstration does not establish clinical validity. No training or recalibration runs from the interface.

## Hosting

The Docker image runs Python 3.12 with CPU-only PyTorch and one inference worker. Set the hosting port through `PORT`; the default is 10000. Render supplies `RENDER_EXTERNAL_HOSTNAME` for origin validation. `COOKIE_SECURE=1` is the public HTTPS setting; local HTTP tests explicitly use 0. Health is reported at `/healthz` after the model loads.

Use the Free web-service plan. Free services may sleep while inactive and need time to wake. No paid instance or persistent disk is required for this demo.

## Verification

The container build runs `self_test.py` against bundled synthetic samples and verifies all original scientific file hashes. The API tests cover per-visitor isolation, CSRF, request limits, actual model scores and transient review state.

The local and portable project versions remain separate from this hosted adaptation.
