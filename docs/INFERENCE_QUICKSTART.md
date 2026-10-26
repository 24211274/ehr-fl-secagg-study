# Run the session demonstration

Use the [hosted website](https://session-check-demo.onrender.com) for the simplest trial. For the screen controls, read the [English user guide](user_guides/Session_Check_User_Guide_EN.pdf). The downloadable code is in `inference/`.

## Local Python setup

Use 64-bit Python 3.12. From the `inference` directory, create a new virtual environment and activate it using the command for your platform.

```console
python -m venv .venv
```

Windows PowerShell activation:

```powershell
.venv\Scripts\Activate.ps1
```

Linux activation:

```sh
. .venv/bin/activate
```

Install the pinned files into that environment:

```console
python -m pip install --no-deps -r requirements_runtime.txt
python -m pip install --no-deps --index-url https://download.pytorch.org/whl/cpu -r requirements_torch.txt
python -m pip install -r requirements_web.txt
python -m pip check
python self_test.py
```

For local HTTP, start the service in PowerShell with:

```powershell
$env:COOKIE_SECURE = "0"
$env:PUBLIC_ORIGIN = "http://127.0.0.1:10000"
python -m uvicorn web_app:app --host 127.0.0.1 --port 10000 --workers 1
```

Or on Linux:

```sh
COOKIE_SECURE=0 PUBLIC_ORIGIN=http://127.0.0.1:10000 python -m uvicorn web_app:app --host 127.0.0.1 --port 10000 --workers 1
```

Open `http://127.0.0.1:10000`. Choose one synthetic sample under `samples/`, select a client and run inference. This setting binds local HTTP to your own computer. The hosted HTTPS service uses its original secure-cookie setting.

## Docker alternative

From `inference/`:

```console
docker build -t session-check .
docker run --rm -p 127.0.0.1:10000:10000 -e COOKIE_SECURE=0 -e PUBLIC_ORIGIN=http://127.0.0.1:10000 session-check
```

The Docker build runs the bundled inference self-test. First-time dependency installation requires Internet access. The separate offline Linux package supplies the historical training/replay runtime, rather than a portable offline web-server installer for every platform.
