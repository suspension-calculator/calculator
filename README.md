# Suspension Calculator

This project is a Python-based suspension calculator for vehicle suspension design.

## Prerequisites

- Python 3.13+
- pip (Python package installer)
- make (for using Makefile commands)

## Project Setup

1. Clone the repository:
```bash
git clone [repository-url]
cd calculator
```

2. Create and activate virtual environment:
```bash
make venv
```
This will:
- Create a Python 3.13 virtual environment in `venv/` directory
- Install the package and development dependencies

## Available Make Commands

- `make venv`: Create virtual environment and install dependencies
- `make setup`: Install package in editable mode with development dependencies
- `make start`: Run the compiled calculator application 
- `make build`: Build the application using PyInstaller
- `make clean`: Remove build artifacts and cache files
- `make dev`: Run the calculator in development mode
- `make test`: Run pytest test suite
- `make coverage`: Run tests with coverage report

## Development

1. Install in development mode:
```bash
make setup
```

2. Run tests:
```bash
make test
```

3. Check test coverage:
```bash
make coverage
```
This generates:
- Terminal output with line-by-line coverage
- HTML coverage report in `htmlcov/` directory

4. Run in development mode:
```bash
make dev
```

## Building

To create a distributable version:

```bash
make build
```

This creates the executable in `dist/Calculator/`

## Project Structure

```
calculator/
├── src/
│   └── suspension/        # Main package directory
│       ├── core/         # Core calculations
│       ├── io/           # Input/Output handling
│       └── ui/          # User interface
├── tests/               # Test files
├── resources/          # Additional resources
├── Calculator.spec    # PyInstaller spec file
├── pyproject.toml    # Project metadata and dependencies
└── Makefile         # Build and development commands
```

## Running Tests

Tests are written using pytest. To run:

- Basic test run: `make test`
- With coverage: `make coverage`

The coverage report will be available in:
- Terminal output
- HTML format in `htmlcov/index.html`

## Dependencies

Core dependencies:
- matplotlib
- PyInstaller

Development dependencies:
- pytest
- coverage[toml]
- pytest-cov

## Configuration Files

### pyproject.toml
```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "suspension-calculator"
version = "0.1.0"
description = "A suspension calculator application"
requires-python = ">=3.10"
dependencies = [
    "matplotlib",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "coverage[toml]>=7.0.0",
    "pytest-cov>=4.0.0",
]

[tool.setuptools]
package-dir = {"" = "src"}
packages = {find = {where = ["src"]}}

[tool.coverage.run]
source = ["src"]
omit = [
    "tests/*",
    "**/__init__.py",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if __name__ == .__main__.:",
    "raise NotImplementedError",
    "if False:",
    "if typing.TYPE_CHECKING:",
]
```

### Makefile
```makefile
.PHONY: start build clean dev setup venv test coverage

PYTHON = ./venv/bin/python
PIP = ./venv/bin/pip

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

setup:
	$(PIP) install -e ".[dev]"

test:
	$(PYTHON) -m pytest tests/ -v

coverage:
	$(PYTHON) -m pytest --cov=suspension tests/ --cov-report=term-missing --cov-report=html
```