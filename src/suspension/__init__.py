# src/suspension/__init__.py
"""
Suspension Calculator
A comprehensive tool for suspension geometry analysis and optimization.
"""

# Version information
__version__ = "0.1.0"
__author__ = "Your Name"
__license__ = "MIT"

from .constants import (
    LogLevel,
    APP_NAME,
    DEFAULT_CONFIG_PATH,
    MAX_RECENT_FILES,
)

from .exceptions import (
    SuspensionError,
    ThemeError,
    ConfigurationError,
    NavigationError,
    InvalidNavigationItemError,
    NavigationStateError,
    NavigationPersistenceError,
)

from .types import (
    PathLike,
    ColorValue,
    JsonDict,
    T,
)

__all__ = [
    # Version info
    "__version__",
    "__author__",
    "__license__",
    # Constants
    "LogLevel",
    "APP_NAME",
    "DEFAULT_CONFIG_PATH",
    "MAX_RECENT_FILES",
    # Exceptions
    "SuspensionError",
    "ThemeError",
    "ConfigurationError",
    "NavigationError",
    "InvalidNavigationItemError",
    "NavigationStateError",
    "NavigationPersistenceError",
    # Types
    "PathLike",
    "ColorValue",
    "JsonDict",
    "T",
]
