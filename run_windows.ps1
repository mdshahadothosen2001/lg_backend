<#
PowerShell script to create venv, install requirements, run migrations and start server on Windows.
Run with: powershell -ExecutionPolicy Bypass -File run_windows.ps1
#>

$VenvDir = ".venv"
if (-not (Test-Path "$VenvDir/Scripts/Activate.ps1")) {
    Write-Output "Creating virtual environment in $VenvDir"
    python -m venv $VenvDir
}

# Activate the venv for the current session
& "$PSScriptRoot\$VenvDir\Scripts\Activate.ps1"

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
Write-Output "Starting Django development server on 0.0.0.0:8000"
python manage.py runserver 0.0.0.0:8000
