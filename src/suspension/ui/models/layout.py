# src/suspension/ui/models/layout.py
"""
Layout configuration models for the Suspension Calculator.
Defines type-safe models for window and panel layouts.
"""

from enum import Enum
from typing import TypedDict

from pydantic import BaseModel


class PanelType(str, Enum):
    """Types of panels in the application."""

    NAVIGATION = "navigation"
    DATA_ENTRY = "data_entry"
    PLOT_VIEW = "plot_view"


class PanelState(TypedDict):
    """Type-safe state definition for a panel."""

    visible: bool
    size: int  # Size in pixels
    position: int  # Index in splitter


class LayoutState(TypedDict):
    """Type-safe state definition for the entire layout."""

    nav_panel: PanelState
    data_panel: PanelState
    plot_panel: PanelState
    navigation_visible: bool
    toolbar_state: bytes
    geometry: bytes


class PanelConfig(BaseModel):
    """Configuration for a panel."""

    panel_type: PanelType
    min_size: int
    max_size: int
    default_size: int
    resizable: bool = True
    collapsible: bool = True


# src/suspension/ui/managers/layout.py
"""
Layout manager for the Suspension Calculator.
Handles panel layouts, visibility, and state persistence.
"""

from typing import Dict, Optional
from PyQt6.QtCore import QObject, pyqtSignal, QSettings
from PyQt6.QtWidgets import QSplitter

from ..models.layout import LayoutState, PanelState, PanelType, PanelConfig


class LayoutManager(QObject):
    """
    Manages application layout state and panel configurations.
    Handles panel visibility, sizes, and state persistence.
    """

    # Signals
    layout_changed = pyqtSignal()
    panel_visibility_changed = pyqtSignal(PanelType, bool)

    def __init__(self, main_splitter: QSplitter) -> None:
        """Initialize the layout manager."""
        super().__init__()
        self._settings = QSettings()
        self._main_splitter = main_splitter
        self._panel_configs: Dict[PanelType, PanelConfig] = {}

        # Initialize with default configurations
        self._initialize_panel_configs()

    def _initialize_panel_configs(self) -> None:
        """Set up default panel configurations."""
        self._panel_configs = {
            PanelType.NAVIGATION: PanelConfig(
                panel_type=PanelType.NAVIGATION,
                min_size=200,
                max_size=400,
                default_size=250,
                collapsible=True,
            ),
            PanelType.DATA_ENTRY: PanelConfig(
                panel_type=PanelType.DATA_ENTRY,
                min_size=300,
                max_size=800,
                default_size=400,
            ),
            PanelType.PLOT_VIEW: PanelConfig(
                panel_type=PanelType.PLOT_VIEW,
                min_size=400,
                max_size=1200,
                default_size=600,
            ),
        }

    def save_layout_state(self) -> None:
        """Save current layout state to settings."""
        splitter = self._main_splitter

        state: LayoutState = {
            "nav_panel": self._get_panel_state(PanelType.NAVIGATION),
            "data_panel": self._get_panel_state(PanelType.DATA_ENTRY),
            "plot_panel": self._get_panel_state(PanelType.PLOT_VIEW),
            "navigation_visible": not splitter.widget(0).isHidden(),
            "toolbar_state": bytes(splitter.saveState()),
            "geometry": bytes(splitter.saveGeometry()),
        }

        self._settings.setValue("layout/state", state)

    def _get_panel_state(self, panel_type: PanelType) -> PanelState:
        """Get the current state of a panel."""
        index = self._get_panel_index(panel_type)
        widget = self._main_splitter.widget(index)
        if widget is None:
            raise ValueError(f"Panel not found: {panel_type}")

        return {
            "visible": not widget.isHidden(),
            "size": self._main_splitter.sizes()[index],
            "position": index,
        }

    def _get_panel_index(self, panel_type: PanelType) -> int:
        """Get the index of a panel in the splitter."""
        if panel_type == PanelType.NAVIGATION:
            return 0
        elif panel_type == PanelType.DATA_ENTRY:
            return 1
        else:
            return 2

    def restore_layout_state(self) -> None:
        """Restore layout state from settings."""
        state = self._settings.value("layout/state")
        if not isinstance(state, dict):
            return

        # Restore panel states
        for panel_type in PanelType:
            self._restore_panel_state(panel_type, state)

        # Restore splitter state
        if toolbar_state := state.get("toolbar_state"):
            self._main_splitter.restoreState(toolbar_state)

    def _restore_panel_state(self, panel_type: PanelType, state: dict) -> None:
        """Restore state for a specific panel."""
        panel_key = f"{panel_type.value}_panel"
        if panel_state := state.get(panel_key):
            index = self._get_panel_index(panel_type)
            widget = self._main_splitter.widget(index)
            if widget is not None:
                widget.setVisible(panel_state.get("visible", True))

    def toggle_panel(self, panel_type: PanelType) -> None:
        """Toggle visibility of a specific panel."""
        index = self._get_panel_index(panel_type)
        widget = self._main_splitter.widget(index)
        if widget is not None:
            widget.setVisible(not widget.isVisible())
            self.panel_visibility_changed.emit(panel_type, widget.isVisible())
            self.save_layout_state()

    def get_panel_config(self, panel_type: PanelType) -> Optional[PanelConfig]:
        """Get configuration for a specific panel."""
        return self._panel_configs.get(panel_type)
