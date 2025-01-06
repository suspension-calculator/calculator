.PHONY: start build clean dev setup venv

PYTHON = ./venv/bin/python
PIP = ./venv/bin/pip

venv:
	python3.13 -m venv venv
	$(PIP) install -e .

start:
	./dist/Calculator/Calculator

build:
	pyinstaller Calculator.spec

clean:
	rm -rf build dist *.egg-info __pycache__

dev:
	$(PYTHON) -m suspension.main

setup:
	$(PIP) install -e .