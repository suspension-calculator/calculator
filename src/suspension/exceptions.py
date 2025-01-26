# src/suspension/exceptions.py
class SuspensionError(Exception):
    """Base exception for all application errors."""

    pass


class ThemeError(SuspensionError):
    """Theme-related errors."""

    pass


class ConfigurationError(SuspensionError):
    """Configuration-related errors."""

    pass
