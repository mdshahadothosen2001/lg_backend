@echo off
REM Windows batch script to create venv, install requirements, run migrations and start server

SET VENV_DIR=.venv
IF NOT EXIST "%VENV_DIR%\Scripts\activate" (
    echo Creating virtual environment in %VENV_DIR%
    python -m venv %VENV_DIR%
)

call %VENV_DIR%\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
echo Starting Django development server on 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000
