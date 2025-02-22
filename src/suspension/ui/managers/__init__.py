# src/suspension/ui/managers/__init__.py
"""
Manager components for the Suspension Calculator UI.

This module provides access to the core managers that handle various
aspects of the application's state and behavior:

- NavigationManager: Handles navigation state and history
- ThemeManager: Manages application theming and styles
- WindowManager: Controls window state and geometry
"""

from .layout import LayoutManager
from .navigation import NavigationManager
from .panel import PanelManager
from .theme import ThemeManager
from .window import WindowManager

__all__ = [
    "NavigationManager",
    "LayoutManager",
    "PanelManager",
    "ThemeManager",
    "WindowManager",
]
