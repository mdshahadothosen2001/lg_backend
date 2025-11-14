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
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata engage/accounts/fixtures/m-user.json
python manage.py loaddata engage/accounts/fixtures/g-user.json

python manage.py loaddata engage/locations/fixtures/division.json
python manage.py loaddata engage/locations/fixtures/district.json
python manage.py loaddata engage/locations/fixtures/upazila.json
python manage.py loaddata engage/locations/fixtures/union.json

python manage.py loaddata engage/local_govt/fixtures/member.json
python manage.py loaddata engage/local_govt/fixtures/contribution.json

python manage.py loaddata engage/request/fixtures/respond.json
python manage.py loaddata engage/service/fixtures/service.json
echo Starting Django development server on 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000
