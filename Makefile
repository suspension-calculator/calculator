.PHONY: start build clean dev setup venv coverage-report format lint fix typecheck check-types

PYTHON = ./venv/bin/python
PIP = ./venv/bin/pip
MYPY = ./venv/bin/mypy

activate-pip:
	source venv/bin/activate

venv:
	python3.13 -m venv venv
	$(PIP) install -e ".[dev]"

start:
	./dist/Calculator/Calculator

build:
	pyinstaller Calculator.spec

clean:
	rm -rf build dist *.egg-info __pycache__

dev:
	$(PYTHON) -m suspension.main

clean-pre-commit:
	rm -rf ~/.cache/pre-commit
	rm -rf .git/hooks/pre-commit

setup-pre-commit: clean-pre-commit
	$(PIP) install pre-commit --upgrade
	$(PIP) install -e ".[dev]"
	./venv/bin/pre-commit install

pre-commit: clean-pre-commit
	./venv/bin/pre-commit run --all-files


setup:
	$(PIP) install -e ".[dev]"

test:
	$(PYTHON) -m pytest tests/ -v

coverage:
	$(PYTHON) -m pytest --cov=suspension tests/ --cov-report=term-missing --cov-report=html

coverage-report:
	$(PYTHON) -m webbrowser "file://$(PWD)/htmlcov/index.html"

format:
	$(PYTHON) -m black src tests

lint:
	$(PYTHON) -m ruff check src tests
	$(PYTHON) -m ruff format --check src tests

fix:
	$(PYTHON) -m black src tests
	$(PYTHON) -m ruff check --fix src tests
	$(PYTHON) -m ruff format src tests

typecheck:
	$(PYTHON) -m mypy src tests
	$(PYTHON) -m pyright src tests

check-types: typecheck
