# src/suspension/ui/managers/panel_manager.py

"""
Panel management for the Suspension Calculator.
Handles panel lifecycle, state, and coordination.
"""
from typing import Dict, Optional, Set

from PyQt6.QtCore import QObject, QSettings, Qt, pyqtSignal
from PyQt6.QtWidgets import QMainWindow

from ...exceptions import PanelError, PanelLayoutError, PanelStateError
from ...utils.logging import StructuredLogger, app_logger
from ..components.panels import BasePanel, DataEntryPanel, PlotViewPanel
from ..models.state import PanelState
from ..models.theme import Theme
from .layout import LayoutManager


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

    def __init__(self, window: QMainWindow, layout_manager: LayoutManager) -> None:
        """
        Initialize the panel manager.

        Args:
            window: Main window instance to manage panels for
        """
        super().__init__()
        self._window = window
        self._layout_manager = layout_manager
        self._settings = QSettings()
        self._panels: Dict[str, BasePanel] = {}
        self._visible_panels: Set[str] = set()

        # Setup logging
        self.logger: StructuredLogger = app_logger
        self._context = {"component": "PanelManager"}

        # Initialize state
        try:
            # Load saved state if it exists
            if saved_state := self._settings.value("panels/state"):
                self.restore_state(saved_state)

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
                layout_manager=self._layout_manager,  # Add this line
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
                layout_manager=self._layout_manager,  # Add this line
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

    def save_state(self) -> PanelState:
        """
        Save current panel states and layout to settings.

        Returns:
            PanelState containing the current state of all panels

        Raises:
            PanelStateError: If saving state fails
        """
        try:
            # Create layout state with proper typing
            layout_state: Dict[str, Dict[str, int]] = {
                str(panel_id): {  # Ensure key is str
                    "dock_area": panel.get_dock_area().value,  # type: ignore # int from enum
                    "index": i,
                }
                for i, (panel_id, panel) in enumerate(self._panels.items())
            }

            state: PanelState = {
                "layout": layout_state,
                "visible": set(
                    str(id) for id in self._visible_panels
                ),  # Ensure Set[str]
            }

            self._settings.setValue("panels/state", state)
            self.logger.debug(
                "Saved panel states",
                {
                    **self._context,
                    "layout": layout_state,
                    "visible_panels": list(self._visible_panels),
                },
            )
            return state

        except Exception as e:
            self.logger.error(
                "Failed to save panel states", error=e, context=self._context
            )
            raise PanelStateError("Failed to save panel states") from e

    def restore_state(self, state: PanelState) -> None:
        """
        Restore panel states from saved state.

        Args:
            state: PanelState containing the panel states to restore

        Raises:
            PanelStateError: If restoring state fails
        """
        try:
            # Restore layout
            for panel_id, layout_info in state["layout"].items():
                if panel := self._panels.get(panel_id):
                    dock_area = layout_info["dock_area"]
                    self._window.addDockWidget(Qt.DockWidgetArea(dock_area), panel)

            # Restore visibility
            self._visible_panels = state["visible"]
            for panel_id in self._panels:
                if panel := self._panels.get(panel_id):
                    panel.setVisible(panel_id in self._visible_panels)

            self.logger.debug(
                "Restored panel states",
                {
                    **self._context,
                    "restored_panels": list(state["layout"].keys()),
                    "visible_panels": list(self._visible_panels),
                },
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
        """
        Restore state for a specific panel.
        State restoration failures are logged but don't prevent panel registration.
        """
        try:
            if state := self._settings.value(f"panels/{panel.panel_id}/state"):
                try:
                    panel.restore_state(state)
                    self.logger.debug(
                        "Restored panel state successfully",
                        context={**self._context, "panel_id": panel.panel_id},
                    )
                except PanelStateError as e:
                    # Log the error but continue with default state
                    self.logger.warning(
                        "Failed to restore panel state, using defaults",
                        error=e,
                        context={**self._context, "panel_id": panel.panel_id},
                    )
                    # Set default state
                    panel.setVisible(True)
                    panel.setFloating(False)
                    panel.set_dock_area(panel.defaultDockArea())
        except Exception as e:
            # Log any other errors but don't prevent panel registration
            self.logger.error(
                "Unexpected error during panel state restoration",
                error=e,
                context={**self._context, "panel_id": panel.panel_id},
            )

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
