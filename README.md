# lg_backend

A Django backend for the LG project.

## Build & Run

This project uses Django. The repository includes helper scripts for Linux and Windows to set up a virtual environment, install dependencies, run migrations, collect static files, and start the development server.

Linux (recommended for development)

Using the included `Makefile` (requires `make` and `python3`):

```bash
# create venv, install deps, run migrations and start server
make start

# or run steps individually
make install   # create venv and install requirements
make migrate
make collectstatic
make run       # start server on 0.0.0.0:8000
```

Windows (Batch)

Run the provided batch script from a Command Prompt (uses the `python` on PATH):

```bat
run_windows.bat
```

Windows (PowerShell)

Run the PowerShell script from PowerShell. If execution policy blocks running scripts, you can bypass it for the invocation:

```powershell
powershell -ExecutionPolicy Bypass -File run_windows.ps1
```

Notes
- The scripts create a virtual environment in `.venv` in the repository root.
- They install packages listed in `requirements.txt`.
- Development server listens on port 8000 bound to all interfaces (0.0.0.0). Adjust as needed.

If you need more advanced deployment (production WSGI server, Docker, systemd, etc.), I can add a Dockerfile and systemd unit in a follow-up.
# lg_backend