# src/suspension/ui/managers/layout.py

from typing import ClassVar, Dict, Optional

from PyQt6.QtCore import QObject, QSettings, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QWidget

from ...exceptions import PanelLayoutError, PanelStateError
from ...utils.logging import StructuredLogger, app_logger
from ..models.state.state_dict import ComponentState


class LayoutManager(QObject):
    """
    Manages UI component layout states.

    Responsibilities:
    - Component size and position management
    - Layout state persistence
    - Dock/float state management
    """

    logger: ClassVar[StructuredLogger] = app_logger

    # Signals
    layout_changed = pyqtSignal(str)  # component_id

    def __init__(self, window: QMainWindow) -> None:
        super().__init__()
        self._window = window
        self._settings = QSettings()
        self._component_states: Dict[str, ComponentState] = {}
        self._context = {"component": "LayoutManager"}

        self.logger.info("Initializing layout manager", self._context)

    def save_component_state(self, component_id: str, state: ComponentState) -> None:
        """Save layout state for a component."""
        try:
            self._component_states[component_id] = state
            self._settings.setValue(f"layout/components/{component_id}", state)
            self.layout_changed.emit(component_id)

            self.logger.debug(
                "Saved component state",
                {**self._context, "component_id": component_id, "state": state},
            )
        except Exception as e:
            self.logger.error("Failed to save component state", e, self._context)
            raise PanelStateError(
                f"Failed to save state for component {component_id}: {str(e)}"
            )

    def get_component_state(self, component_id: str) -> Optional[ComponentState]:
        """Get saved layout state for a component."""
        return self._settings.value(f"layout/components/{component_id}")

    def restore_component_state(self, component_id: str, widget: QWidget) -> None:
        """Restore saved layout state to a component."""
        try:
            if state := self._settings.value(f"layout/components/{component_id}"):
                if isinstance(state, dict):
                    self._apply_state_to_widget(widget, state)
                    self._component_states[component_id] = state

                    self.logger.debug(
                        "Restored component state",
                        {**self._context, "component_id": component_id},
                    )
        except Exception as e:
            self.logger.error("Failed to restore component state", e, self._context)
            raise PanelStateError(
                f"Failed to restore state for component {component_id}: {str(e)}"
            )

    def save_component_size(self, component_id: str, size_dict: dict) -> None:
        """Save component size information.

        Args:
            component_id: Identifier for the component
            size_dict: Dictionary containing size information (e.g. width, height)

        Raises:
            PanelStateError: If component state cannot be saved
        """
        try:
            state = self._component_states.get(
                component_id,
                ComponentState(
                    dock_area=None,
                    floating=False,
                    width=None,
                    collapsed=False,
                    size_ratio=None,
                    geometry=None,
                ),
            )

            if "width" in size_dict:
                state["width"] = size_dict["width"]

            self.save_component_state(component_id, state)

            self.logger.debug(
                "Saved component size",
                {**self._context, "component_id": component_id, "size": size_dict},
            )
        except Exception as e:
            self.logger.error("Failed to save component size", e, self._context)
            raise PanelStateError(
                f"Failed to save size for component {component_id}: {str(e)}"
            )

    def _apply_state_to_widget(self, widget: QWidget, state: Dict) -> None:
        """Apply a saved state to a widget."""
        try:
            if "width" in state:
                widget.setFixedWidth(state["width"])
            if "geometry" in state and state["geometry"]:
                widget.restoreGeometry(state["geometry"])
        except Exception as e:
            self.logger.error("Failed to apply widget state", e, self._context)
            raise PanelLayoutError(f"Failed to apply state to widget: {str(e)}")
