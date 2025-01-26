# src/suspension/constants.py
from enum import Enum
from pathlib import Path


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


APP_NAME = "Suspension Calculator"
DEFAULT_CONFIG_PATH = Path.home() / ".suspension"
MAX_RECENT_FILES = 10
