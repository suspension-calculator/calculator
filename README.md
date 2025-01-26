# Suspension Calculator

This project is a Python-based suspension calculator for vehicle suspension design.

## Prerequisites

- Python 3.13+ (Python 3.10+ may work but is not officially supported)
- pip (Python package installer)
- make (build automation tool - see OS-specific installation instructions below)

## Operating System Setup

### Windows Setup

#### Installing Make (choose one method):

1. **Using Chocolatey (Recommended):**
   ```bash
   # Install Chocolatey (PowerShell Admin)
   Set-ExecutionPolicy Bypass -Scope Process -Force
   [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
   iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

   # Install make
   choco install make
   ```

2. **Using Scoop:**
   ```bash
   # Install Scoop (PowerShell)
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   irm get.scoop.sh | iex

   # Install make
   scoop install make
   ```

3. **Using Git Bash:**
    - Download and install Git for Windows from https://gitforwindows.org/
    - During installation, select "Use Git and optional Unix tools from the Command Prompt"

#### Without Make (Alternative Windows Commands)

If you prefer not to install Make, use these equivalent commands:

```bash
# Instead of 'make venv'
python -m venv venv
.\venv\Scripts\activate
pip install -e ".[dev]"

# Instead of 'make dev'
python -m suspension.main

# Instead of 'make build'
pyinstaller Calculator.spec

# Instead of 'make clean'
rmdir /s /q build dist *.egg-info __pycache__
```

### MacOS Setup

```bash
# Install make if not present
brew install make
```

### Linux Setup

```bash
# Ubuntu/Debian
sudo apt-get install make

# Fedora
sudo dnf install make

# Arch Linux
sudo pacman -S make
```

## Project Setup

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd calculator
   ```

2. Create and activate virtual environment:
   ```bash
   # Create venv and install dependencies
   make venv

   # Activate virtual environment
   # Windows (CMD):        .\venv\Scripts\activate.bat
   # Windows (PowerShell): .\venv\Scripts\Activate.ps1
   # Unix/MacOS:          source venv/bin/activate
   ```

## Available Make Commands

| Command         | Description                                            | Alternative (Windows without Make)                                                     |
|-----------------|--------------------------------------------------------|----------------------------------------------------------------------------------------|
| `make venv`     | Create virtual environment and install dependencies    | `python -m venv venv && .\venv\Scripts\activate && pip install -e ".[dev]"`            |
| `make setup`    | Install package in editable mode with dev dependencies | `pip install -e ".[dev]"`                                                              |
| `make start`    | Run the compiled calculator application                | `.\dist\Calculator\Calculator.exe`                                                     |
| `make build`    | Build application using PyInstaller                    | `pyinstaller Calculator.spec`                                                          |
| `make clean`    | Remove build artifacts and cache                       | `rmdir /s /q build dist *.egg-info __pycache__`                                        |
| `make dev`      | Run calculator in development mode                     | `python -m suspension.main`                                                            |
| `make test`     | Run pytest test suite                                  | `python -m pytest tests/ -v`                                                           |
| `make coverage` | Run tests with coverage report                         | `python -m pytest --cov=suspension tests/ --cov-report=term-missing --cov-report=html` |

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

### Platform-Specific Notes

#### Windows

- The executable will have `.exe` extension
- Users may need to allow the application through Windows Defender
- Right-click and "Run as Administrator" if required

#### MacOS

- Users may need to allow the application in Security & Privacy settings
- Application is not code signed by default
- Use `chmod +x` if execute permission is needed:
  ```bash
  chmod +x dist/Calculator/Calculator
  ```

#### Linux

- Ensure execute permissions are set
- Dependencies like GTK might be required
- Consider using AppImage for broader compatibility

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

## Troubleshooting

### Common Issues

1. **Python Version Issues:**
    - Use `python --version` to verify Python 3.13+ is installed
    - Consider using pyenv to manage Python versions

2. **Make Command Not Found:**
    - Windows: Restart terminal after installing make
    - Check installation: `make --version`

3. **Virtual Environment Issues:**
    - Ensure you're in the project root directory
    - Check if venv is activated (should see `(venv)` in prompt)
    - Try removing and recreating: `rm -rf venv && make venv`

4. **Build Errors:**
    - Ensure all dependencies are installed: `make setup`
    - Check PyInstaller installation: `pip install pyinstaller`
    - Verify spec file exists in project root

### Still Having Issues?

- Check the project's issue tracker for similar problems
- Ensure all prerequisites are correctly installed
- Try running commands without make (see Windows alternative commands)

## Configuration Files

See `pyproject.toml` for project configuration and dependencies.
