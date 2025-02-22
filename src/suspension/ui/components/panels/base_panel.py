# src/suspension/ui/components/panels/base_panel.py

"""
Base panel component providing common panel functionality.
"""
from base64 import b64decode, b64encode
from typing import ClassVar, Optional

from PyQt6.QtCore import QByteArray, Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QDockWidget,
    QFrame,
    QHBoxLayout,
    QLabel,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

from suspension.exceptions import PanelStateError
from suspension.utils import StructuredLogger, app_logger

from ...constants.icons import AppIcon
from ...managers.layout import LayoutManager
from ...models.state import ComponentState
from ...models.theme import Theme


class BasePanel(QDockWidget):
    """
    Base panel component with common functionality.

    Features:
    - Custom title bar with actions
    - State persistence
    - Theme support
    - Dock/float/close capabilities
    - Content area management

    Signals:
        state_changed: Emitted when panel state changes (docked, floating, hidden)
        visibility_changed: Emitted when panel visibility changes
    """

    logger: ClassVar[StructuredLogger] = app_logger
    state_changed = pyqtSignal()
    visibility_changed = pyqtSignal(bool)

    def __init__(
        self,
        title: str,
        panel_id: str,
        layout_manager: LayoutManager,
        parent: Optional[QWidget] = None,
        allow_close: bool = True,
        allow_float: bool = True,
        dock_area: Optional[Qt.DockWidgetArea] = None,
    ) -> None:
        """
        Initialize the panel.

        Args:
            title: Panel title
            panel_id: Unique identifier for the panel
            parent: Parent widget
            allow_close: Whether panel can be closed
            allow_float: Whether panel can be floated
            dock_area: Default dock area for the panel
        """
        super().__init__(title, parent)
        self._context = {"component": "BasePanel", "panel_id": panel_id}
        self.logger.info("Initializing panel", self._context)

        self.setObjectName(panel_id)
        self.panel_id = panel_id
        self._layout_manager = layout_manager
        self._allow_close = allow_close
        self._allow_float = allow_float
        self._dock_area = dock_area or Qt.DockWidgetArea.LeftDockWidgetArea

        # Initialize UI
        self._setup_ui()
        self._setup_title_bar()
        self._setup_content_area()

        # Connect signals
        self.dockLocationChanged.connect(self._handle_state_changed)
        self.topLevelChanged.connect(self._handle_state_changed)
        self.visibilityChanged.connect(self._handle_visibility_changed)

    def _setup_ui(self) -> None:
        """Setup the panel UI."""
        # Set features based on configuration
        features = QDockWidget.DockWidgetFeature.DockWidgetMovable

        if self._allow_float:
            features |= QDockWidget.DockWidgetFeature.DockWidgetFloatable

        if self._allow_close:
            features |= QDockWidget.DockWidgetFeature.DockWidgetClosable

        self.setFeatures(features)

    def _setup_title_bar(self) -> None:
        """Setup custom title bar."""
        title_bar = QFrame(self)
        title_bar.setObjectName("panelTitleBar")
        layout = QHBoxLayout(title_bar)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(4)

        # Title label
        title_label = QLabel(self.windowTitle(), title_bar)
        title_label.setObjectName("panelTitle")
        layout.addWidget(title_label)

        # Add stretch to push buttons to the right
        layout.addStretch()

        # Float button if allowed
        if self._allow_float:
            float_btn = QToolButton(title_bar)
            float_btn.setIcon(AppIcon.MAXIMIZE.to_icon())
            float_btn.setToolTip("Float panel")
            float_btn.clicked.connect(self._toggle_floating)
            layout.addWidget(float_btn)

        # Close button if allowed
        if self._allow_close:
            close_btn = QToolButton(title_bar)
            close_btn.setIcon(AppIcon.MINIMIZE.to_icon())
            close_btn.setToolTip("Close panel")
            close_btn.clicked.connect(self.close)
            layout.addWidget(close_btn)

        self.setTitleBarWidget(title_bar)

    def _setup_content_area(self) -> None:
        """Setup the main content area."""
        content = QFrame(self)
        content.setObjectName("panelContent")

        layout = QVBoxLayout(content)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setWidget(content)

    def set_content(self, widget: QWidget) -> None:
        """
        Set the main content widget.

        Args:
            widget: Widget to use as panel content
        """
        if content_frame := self.widget():
            if isinstance(content_frame, QFrame):
                if layout := content_frame.layout():
                    # Clear existing content
                    while layout.count():
                        if item := layout.takeAt(0):
                            if old_widget := item.widget():
                                old_widget.deleteLater()
                    # Add new content
                    layout.addWidget(widget)

    def apply_theme(self, theme: Theme) -> None:
        """
        Apply theme to the panel.

        Args:
            theme: Theme to apply
        """
        # Title bar styling
        if title_bar := self.titleBarWidget():
            title_bar.setStyleSheet(
                f"""
                QFrame#panelTitleBar {{
                    background-color: {theme.colors.toolbar};
                    border-bottom: 1px solid {theme.colors.border};
                }}
                QLabel#panelTitle {{
                    color: {theme.colors.toolbar_text};
                    font-weight: bold;
                }}
            """
            )

        # Content area styling
        if content := self.widget():
            content.setStyleSheet(
                f"""
                QFrame#panelContent {{
                    background-color: {theme.colors.surface};
                    border: none;
                }}
            """
            )

    def save_state(self) -> ComponentState:
        """
        Save panel state.

        Returns:
            ComponentState containing the panel's current state

        Raises:
            PanelStateError: If saving state fails
        """
        try:
            geometry_bytes = self.saveGeometry().data()
            # Convert bytes to base64 string for JSON serialization
            geometry_b64 = b64encode(geometry_bytes).decode("utf-8")

            state: ComponentState = {
                "visible": self.isVisible(),
                "dock_area": self.get_dock_area().value,
                "floating": self.isFloating(),
                "width": self.width(),
                "collapsed": False,  # Base panels aren't collapsible
                "size_ratio": None,  # Base panels don't use size ratios
                "geometry": geometry_b64,  # Add to ComponentState definition
            }
            return state
        except Exception as e:
            self.logger.error(
                "Failed to save panel state",
                error=e,
                context={**self._context, "panel_id": self.panel_id},
            )
            raise PanelStateError(
                f"Failed to save state for panel: {self.panel_id}"
            ) from e

    def restore_state(self, state: ComponentState) -> None:
        """
        Restore panel state.

        Args:
            state: ComponentState containing panel state

        Raises:
            PanelStateError: If restoring critical state fails
        """
        try:
            # Restore geometry if available
            if geometry_b64 := state.get("geometry"):
                try:
                    # Add padding if necessary
                    padding_needed = len(geometry_b64) % 4
                    if padding_needed:
                        geometry_b64 += "=" * padding_needed

                    # Attempt to decode and restore geometry
                    geometry_bytes = b64decode(geometry_b64)
                    self.restoreGeometry(QByteArray(geometry_bytes))
                except Exception as e:
                    # Log geometry restoration failure but continue
                    self.logger.warning(
                        "Failed to restore panel geometry",
                        error=e,
                        context={"panel_id": self.panel_id},
                    )
                    # Don't raise here - continue with other state restoration

            # Restore other state properties
            self.setVisible(state["visible"])
            self.setFloating(state["floating"])

            if dock_area := state["dock_area"]:
                self.set_dock_area(Qt.DockWidgetArea(dock_area))

            if width := state.get("width"):
                self.setFixedWidth(width)

        except Exception as e:
            self.logger.error(
                "Failed to restore panel state",
                error=e,
                context={"panel_id": self.panel_id},
            )
            raise PanelStateError(
                f"Failed to restore state for panel: {self.panel_id}"
            ) from e

    def _handle_state_changed(self) -> None:
        """Handle panel state changes."""
        try:
            state = self.save_state()
            self._layout_manager.save_component_state(self.panel_id, state)
            self.state_changed.emit()

            self.logger.debug(
                "Panel state changed",
                {**self._context, "state": state},
            )
        except Exception as e:
            self.logger.error("Failed to handle state change", e, self._context)
            raise

    def _handle_visibility_changed(self, visible: bool) -> None:
        """Handle panel visibility changes."""
        self.visibility_changed.emit(visible)
        state = self.save_state()
        self._layout_manager.save_component_state(self.panel_id, state)

    def _save_panel_state(self) -> None:
        """Save panel state to settings."""
        state = self.save_state()
        self._settings.setValue(f"panels/{self.panel_id}/state", state)

    def _toggle_floating(self) -> None:
        """Toggle panel floating state."""
        self.setFloating(not self.isFloating())

    def get_dock_area(self) -> Qt.DockWidgetArea:
        """
        Get the current dock area of the panel.

        Returns:
            Current dock area
        """
        return self._dock_area

    def set_dock_area(self, area: Qt.DockWidgetArea) -> None:
        """
        Set the dock area for the panel.

        Args:
            area: New dock area
        """
        self._dock_area = area
        self.state_changed.emit()
        state = self.save_state()
        self._layout_manager.save_component_state(self.panel_id, state)

    def defaultDockArea(self) -> Qt.DockWidgetArea:
        """
        Get the default dock area for this panel.
        Can be overridden by subclasses to specify different default locations.

        Returns:
            Default dock area for the panel
        """
        return self._dock_area
