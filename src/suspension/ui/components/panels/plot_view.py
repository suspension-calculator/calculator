# src/suspension/ui/components/panels/plot_view.py

"""
Plot view panel with support for multiple plot types and real-time updates.
"""

from typing import Any, ClassVar, Dict, Optional

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget

from suspension.utils import StructuredLogger, app_logger

from ...managers.layout import LayoutManager
from .base_panel import BasePanel


class PlotViewPanel(BasePanel):
    """
    Plot view panel supporting multiple plot types and real-time updates.

    Features:
    - Dynamic plot component injection
    - Real-time plot updates
    - State persistence
    - Plot state management via Redux
    - Multi-plot support

    Signals:
        plot_changed: Emitted when plot component changes
        view_state_changed: Emitted when view state changes (zoom, pan, etc)
    """

    logger: ClassVar[StructuredLogger] = app_logger
    plot_changed = pyqtSignal()  # Emitted when plot component changes
    view_state_changed = pyqtSignal(dict)  # View state changes

    def __init__(
        self,
        panel_id: str,
        layout_manager: LayoutManager,
        initial_plot: Optional[QWidget] = None,
        parent: Optional[QWidget] = None,
    ) -> None:
        """
        Initialize the plot view panel.

        Args:
            panel_id: Unique identifier for the panel
            initial_plot: Initial plot widget to display
            parent: Parent widget
        """
        super().__init__(
            title="Plot View",
            panel_id=panel_id,
            layout_manager=layout_manager,
            parent=parent,
            allow_close=True,
            allow_float=True,
        )
        self._current_plot: Optional[QWidget] = None
        self._view_state: Dict[str, Any] = {}

        # Set initial plot if provided
        if initial_plot:
            self.set_plot(initial_plot)

    def set_plot(self, plot: QWidget) -> None:
        """
        Set the current plot component.

        Args:
            plot: Plot widget to display
        """
        self.set_content(plot)
        self._current_plot = plot
        self.plot_changed.emit()

    def get_current_plot(self) -> Optional[QWidget]:
        """
        Get the currently displayed plot.

        Returns:
            Current plot widget or None if no plot is set
        """
        return self._current_plot

    def set_view_state(self, state: Dict[str, Any]) -> None:
        """
        Update the view state (zoom, pan, etc).

        Args:
            state: New view state
        """
        self._view_state.update(state)
        self.view_state_changed.emit(self._view_state)

    def get_view_state(self) -> Dict[str, Any]:
        """
        Get current view state.

        Returns:
            Current view state
        """
        return self._view_state.copy()
