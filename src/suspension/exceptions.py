class SuspensionError(Exception):
    """Base exception for all application errors."""

    pass


class ThemeError(SuspensionError):
    """Theme-related errors."""

    pass


class ConfigurationError(SuspensionError):
    """Configuration-related errors."""

    pass


class NavigationError(SuspensionError):
    """Base class for navigation-related errors."""

    pass


class InvalidNavigationItemError(NavigationError):
    """Raised when attempting to interact with an invalid navigation item."""

    pass


class NavigationStateError(NavigationError):
    """Raised when navigation state becomes invalid or inconsistent."""

    pass


class NavigationPersistenceError(NavigationError):
    """Raised when there are issues saving or loading navigation state."""

    pass


class PanelError(SuspensionError):
    """Base class for panel-related errors."""

    pass


class InvalidPanelError(PanelError):
    """Raised when attempting to interact with an invalid or non-existent panel."""

    pass


class PanelStateError(PanelError):
    """Raised when panel state becomes invalid or inconsistent."""

    pass


class PanelPersistenceError(PanelError):
    """Raised when there are issues saving or loading panel state."""

    pass


class PanelLayoutError(PanelError):
    """Raised when there are issues with panel layout or docking."""

    pass
