SHELL := /bin/bash

.PHONY: help venv install migrate collectstatic run start clean

VENV_DIR := .venv
PIP := $(VENV_DIR)/bin/pip
PY := $(VENV_DIR)/bin/python

help:
	@echo "Makefile targets:"
	@echo "  make venv           # create a virtualenv in $(VENV_DIR)"
	@echo "  make install        # create venv and install requirements"
	@echo "  make migrate        # run Django migrations"
	@echo "  make collectstatic  # collect static files"
	@echo "  make run            # run Django development server"
	@echo "  make start          # install, migrate, collectstatic and run"
	@echo "  make clean          # remove virtualenv"

venv:
	@test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

migrate:
	$(PY) manage.py migrate

collectstatic:
	$(PY) manage.py collectstatic --noinput

run:
	$(PY) manage.py runserver 0.0.0.0:8000

start: install migrate collectstatic run

clean:
	rm -rf $(VENV_DIR)
