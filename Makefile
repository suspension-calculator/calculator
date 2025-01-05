.PHONY: start build clean dev setup

start:
	./dist/Calculator/Calculator

build:
	pyinstaller Calculator.spec

clean:
	rm -rf build dist *.egg-info __pycache__

dev:
	python -m src.suspension.main

setup:
	pip install -e .