# src/suspension/ui/managers/panel_manager.py

"""
Panel management for the Suspension Calculator.
Handles panel lifecycle, state, and coordination.
"""

from typing import Dict, Optional, Set, TypedDict

from PyQt6.QtCore import QObject, pyqtSignal, QSettings, Qt
from PyQt6.QtWidgets import QMainWindow

from ..components.panels import BasePanel, DataEntryPanel, PlotViewPanel
from ..models.theme import Theme
from ...exceptions import PanelError, PanelStateError, PanelLayoutError
from ...utils.logging import app_logger, StructuredLogger


class PanelState(TypedDict):
    """Type-safe panel state definition."""

    layout: Dict[str, Dict[str, int]]  # panel_id -> {dock_area, index}
    visible: Set[str]  # Set of visible panel IDs


class PanelManager(QObject):
    """
    Manages application panels and their states.

    Features:
    - Panel registration and lifecycle management
    - State persistence
    - Layout coordination
    - Theme integration
    - Visibility management
    - Logging and error tracking
    """

    # Signals
    panel_added = pyqtSignal(str)  # panel_id
    panel_removed = pyqtSignal(str)  # panel_id
    panel_state_changed = pyqtSignal(str)  # panel_id
    layout_changed = pyqtSignal()
    error_occurred = pyqtSignal(str)  # error message

    def __init__(self, window: QMainWindow) -> None:
        """
        Initialize the panel manager.

        Args:
            window: Main window instance to manage panels for
        """
        super().__init__()
        self._window = window
        self._settings = QSettings()
        self._panels: Dict[str, BasePanel] = {}
        self._visible_panels: Set[str] = set()

        # Setup logging
        self.logger: StructuredLogger = app_logger
        self._context = {"component": "PanelManager"}

        # Initialize state
        try:
            self._restore_state()
            self.logger.info("Panel manager initialized", context=self._context)
        except Exception as e:
            self.logger.error(
                "Failed to initialize panel manager", error=e, context=self._context
            )
            self.error_occurred.emit(str(e))
            raise PanelError("Failed to initialize panel manager") from e

    def create_data_entry_panel(
        self, panel_id: str, title: Optional[str] = None
    ) -> DataEntryPanel:
        """
        Create and register a new data entry panel.

        Args:
            panel_id: Unique identifier for the panel
            title: Optional custom title for the panel

        Returns:
            New data entry panel instance

        Raises:
            PanelError: If panel ID already exists
        """
        try:
            panel = DataEntryPanel(
                panel_id=panel_id,
                parent=self._window,
            )
            if title:
                panel.setWindowTitle(title)

            self.register_panel(panel)
            return panel

        except Exception as e:
            self.logger.error(
                "Failed to create data entry panel",
                error=e,
                context={**self._context, "panel_id": panel_id},
            )
            raise PanelError(f"Failed to create data entry panel: {panel_id}") from e

    def create_plot_panel(
        self, panel_id: str, title: Optional[str] = None
    ) -> PlotViewPanel:
        """
        Create and register a new plot panel.

        Args:
            panel_id: Unique identifier for the panel
            title: Optional custom title for the panel

        Returns:
            New plot panel instance

        Raises:
            PanelError: If panel ID already exists
        """
        try:
            panel = PlotViewPanel(
                panel_id=panel_id,
                parent=self._window,
            )
            if title:
                panel.setWindowTitle(title)

            self.register_panel(panel)
            return panel

        except Exception as e:
            self.logger.error(
                "Failed to create plot panel",
                error=e,
                context={**self._context, "panel_id": panel_id},
            )
            raise PanelError(f"Failed to create plot panel: {panel_id}") from e

    def register_panel(self, panel: BasePanel) -> None:
        """
        Register a panel with the manager.

        Args:
            panel: Panel instance to register

        Raises:
            PanelError: If panel already exists
        """
        try:
            panel_id = panel.panel_id
            if panel_id in self._panels:
                raise PanelError(f"Panel already registered: {panel_id}")

            # Connect panel signals
            panel.state_changed.connect(
                lambda: self._handle_panel_state_changed(panel_id)
            )
            panel.visibility_changed.connect(
                lambda visible: self._handle_panel_visibility_changed(panel_id, visible)
            )

            # Add to window and tracking
            self._window.addDockWidget(panel.defaultDockArea(), panel)
            self._panels[panel_id] = panel

            # Restore panel state if available
            self._restore_panel_state(panel)

            self.panel_added.emit(panel_id)
            self.layout_changed.emit()

            self.logger.info(
                f"Registered panel: {panel_id}",
                context={**self._context, "panel_id": panel_id},
            )

        except Exception as e:
            self.logger.error(
                "Failed to register panel",
                error=e,
                context={**self._context, "panel_id": panel.panel_id},
            )
            raise PanelError(f"Failed to register panel: {panel.panel_id}") from e

    def get_panel(self, panel_id: str) -> Optional[BasePanel]:
        """
        Get a panel by ID.

        Args:
            panel_id: ID of panel to retrieve

        Returns:
            Panel instance if found, None otherwise
        """
        return self._panels.get(panel_id)

    def apply_theme(self, theme: Theme) -> None:
        """
        Apply theme to all panels.

        Args:
            theme: Theme to apply
        """
        try:
            for panel in self._panels.values():
                panel.apply_theme(theme)

            self.logger.debug(
                "Applied theme to all panels",
                context={**self._context, "theme": theme.metadata.name},
            )

        except Exception as e:
            self.logger.error(
                "Failed to apply theme to panels",
                error=e,
                context={**self._context, "theme": theme.metadata.name},
            )
            raise PanelError("Failed to apply theme to panels") from e

    def arrange_panels(self, layout: Dict[str, Dict[str, int]]) -> None:
        """
        Arrange panels according to layout specification.

        Args:
            layout: Dictionary mapping panel IDs to dock areas and indices
        """
        try:
            for panel_id, position in layout.items():
                if panel := self.get_panel(panel_id):
                    area = Qt.DockWidgetArea(position["dock_area"])
                    self._window.addDockWidget(area, panel)

            self.layout_changed.emit()
            self.logger.debug(
                "Arranged panels", context={**self._context, "layout": layout}
            )

        except Exception as e:
            self.logger.error(
                "Failed to arrange panels",
                error=e,
                context={**self._context, "layout": layout},
            )
            raise PanelLayoutError("Failed to arrange panels") from e

    def save_state(self) -> None:
        """Save current panel states and layout to settings."""
        try:
            # Save individual panel states
            for panel in self._panels.values():
                self._save_panel_state(panel)

            # Save overall layout state
            layout_state = {
                panel_id: {
                    # Change this line to get the integer value from the DockWidgetArea
                    "dock_area": panel.get_dock_area().value,  # Access the enum's value
                    "index": idx,
                }
                for idx, (panel_id, panel) in enumerate(self._panels.items())
            }

            state: PanelState = {
                "layout": layout_state,
                "visible": self._visible_panels,
            }

            self._settings.setValue("panels/state", state)
            self.logger.debug("Saved panel states", context=self._context)

        except Exception as e:
            self.logger.error(
                "Failed to save panel states", error=e, context=self._context
            )
            raise PanelStateError("Failed to save panel states") from e

    def _restore_state(self) -> None:
        """Restore panel states from settings."""
        try:
            if state := self._settings.value("panels/state"):
                if isinstance(state, dict):
                    # Restore layout
                    if layout := state.get("layout"):
                        self.arrange_panels(layout)

                    # Restore visibility
                    if visible := state.get("visible"):
                        self._visible_panels = set(visible)
                        for panel_id in visible:
                            if panel := self.get_panel(panel_id):
                                panel.setVisible(True)

            self.logger.debug(
                "Restored panel states",
                context={**self._context, "visible_panels": list(self._visible_panels)},
            )

        except Exception as e:
            self.logger.error(
                "Failed to restore panel states", error=e, context=self._context
            )
            raise PanelStateError("Failed to restore panel states") from e

    def _save_panel_state(self, panel: BasePanel) -> None:
        """Save state for a specific panel."""
        state = panel.save_state()
        self._settings.setValue(f"panels/{panel.panel_id}/state", state)

    def _restore_panel_state(self, panel: BasePanel) -> None:
        """Restore state for a specific panel."""
        if state := self._settings.value(f"panels/{panel.panel_id}/state"):
            panel.restore_state(state)

    def _handle_panel_state_changed(self, panel_id: str) -> None:
        """Handle panel state changes."""
        if panel := self.get_panel(panel_id):
            self._save_panel_state(panel)
            self.panel_state_changed.emit(panel_id)
            self.layout_changed.emit()

    def _handle_panel_visibility_changed(self, panel_id: str, visible: bool) -> None:
        """Handle panel visibility changes."""
        if visible:
            self._visible_panels.add(panel_id)
        else:
            self._visible_panels.discard(panel_id)
        # Change this line from self._save_state() to:
        self.save_state()
