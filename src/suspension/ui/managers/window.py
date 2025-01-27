# src/suspension/ui/managers/window.py
"""
Window manager for the Suspension Calculator.
Handles window state, geometry, and component coordination.
"""

from typing import Optional, TypedDict
from PyQt6.QtCore import QObject, pyqtSignal, QSettings
from PyQt6.QtWidgets import QMainWindow, QToolBar


class WindowState(TypedDict):
    """Type-safe state definition for window configuration."""

    geometry: bytes
    state: bytes  # Window state including toolbars
    maximized: bool
    fullscreen: bool


class WindowManager(QObject):
    """
    Manages the application window state and coordinates window-level components.
    Handles window geometry, state persistence, and component visibility.
    """

    # Signals
    state_changed = pyqtSignal()
    status_message = pyqtSignal(str, int)  # message, timeout

    def __init__(self, window: QMainWindow) -> None:
        """
        Initialize the window manager.

        Args:
            window: The application's main window instance
        """
        super().__init__()
        self._window = window
        self._settings = QSettings()

        # Connect window signals
        self._window.windowStateChanged.connect(self._handle_state_changed)

    def save_state(self) -> None:
        """Save current window state to settings."""
        state: WindowState = {
            "geometry": bytes(self._window.saveGeometry()),
            "state": bytes(self._window.saveState()),
            "maximized": self._window.isMaximized(),
            "fullscreen": self._window.isFullScreen(),
        }

        self._settings.setValue("window/state", state)

    def restore_state(self) -> None:
        """Restore window state from settings."""
        state = self._settings.value("window/state")
        if not isinstance(state, dict):
            return

        # Restore geometry first
        if geometry := state.get("geometry"):
            self._window.restoreGeometry(geometry)

        # Restore window state (toolbars, etc)
        if window_state := state.get("state"):
            self._window.restoreState(window_state)

        # Restore window mode
        if state.get("maximized"):
            self._window.showMaximized()
        elif state.get("fullscreen"):
            self._window.showFullScreen()

    def _handle_state_changed(self) -> None:
        """Handle window state changes."""
        self.state_changed.emit()
        self.save_state()

    def show_status_message(self, message: str, timeout: int = 5000) -> None:
        """
        Show a message in the status bar.

        Args:
            message: Message to display
            timeout: Display duration in milliseconds
        """
        status_bar = self._window.statusBar()
        if status_bar is not None:
            status_bar.showMessage(message, timeout)

    def toggle_maximized(self) -> None:
        """Toggle window maximized state."""
        if self._window.isMaximized():
            self._window.showNormal()
        else:
            self._window.showMaximized()

    def toggle_fullscreen(self) -> None:
        """Toggle window fullscreen state."""
        if self._window.isFullScreen():
            self._window.showNormal()
        else:
            self._window.showFullScreen()

    def get_toolbar(self, name: str) -> Optional[QToolBar]:
        """
        Get a toolbar by name.

        Args:
            name: Name of the toolbar to retrieve

        Returns:
            The toolbar if found, None otherwise
        """
        toolbars = self._window.findChildren(QToolBar)
        for toolbar in toolbars:
            if toolbar.objectName() == name:
                return toolbar
        return None

    def set_window_title(self, title: str) -> None:
        """
        Set the window title.

        Args:
            title: New window title
        """
        self._window.setWindowTitle(title)


# src/suspension/ui/models/window.py
"""
Window-related models for the Suspension Calculator.
"""

from enum import Enum
from pydantic import BaseModel


class WindowMode(str, Enum):
    """Window display modes."""

    NORMAL = "normal"
    MAXIMIZED = "maximized"
    FULLSCREEN = "fullscreen"


class WindowPreferences(BaseModel):
    """User preferences for window behavior."""

    remember_geometry: bool = True
    remember_state: bool = True
    startup_mode: WindowMode = WindowMode.NORMAL
    status_message_duration: int = 5000  # milliseconds
