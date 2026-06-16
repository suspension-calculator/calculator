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
