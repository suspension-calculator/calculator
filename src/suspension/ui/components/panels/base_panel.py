# src/suspension/ui/components/panels/base_panel.py

"""
Base panel component providing common panel functionality.
"""

from typing import Optional, Dict, Any
from PyQt6.QtCore import pyqtSignal, QSettings, Qt, QByteArray
from PyQt6.QtWidgets import (
    QDockWidget,
    QWidget,
    QVBoxLayout,
    QFrame,
    QLabel,
    QToolButton,
    QHBoxLayout,
)

from ...constants.icons import AppIcon
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

    state_changed = pyqtSignal()
    visibility_changed = pyqtSignal(bool)

    def __init__(
        self,
        title: str,
        panel_id: str,
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

        # Set the object name using the panel_id
        self.setObjectName(panel_id)

        self.panel_id = panel_id
        self._settings = QSettings()
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

    def save_state(self) -> Dict[str, Any]:
        """
        Save panel state.

        Returns:
            Dictionary containing panel state
        """
        state = {
            "geometry": self.saveGeometry().data(),  # Convert QByteArray to bytes
            "floating": self.isFloating(),
            "visible": self.isVisible(),
            "features": self.features().value,  # Get raw enum value
            "dock_area": self.get_dock_area().value,  # Get raw enum value
        }
        return state

    def restore_state(self, state: Dict[str, Any]) -> None:
        """
        Restore panel state.

        Args:
            state: Dictionary containing panel state
        """
        if geometry := state.get("geometry"):
            self.restoreGeometry(QByteArray(geometry))

        if floating := state.get("floating"):
            self.setFloating(bool(floating))

        if visible := state.get("visible"):
            self.setVisible(bool(visible))

        if features := state.get("features"):
            self.setFeatures(QDockWidget.DockWidgetFeature(features))

        if dock_area := state.get("dock_area"):
            self.set_dock_area(Qt.DockWidgetArea(dock_area))

    def _handle_state_changed(self) -> None:
        """Handle panel state changes."""
        self.state_changed.emit()
        self._save_panel_state()

    def _handle_visibility_changed(self, visible: bool) -> None:
        """Handle panel visibility changes."""
        self.visibility_changed.emit(visible)
        self._save_panel_state()

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
        self._save_panel_state()

    def defaultDockArea(self) -> Qt.DockWidgetArea:
        """
        Get the default dock area for this panel.
        Can be overridden by subclasses to specify different default locations.

        Returns:
            Default dock area for the panel
        """
        return self._dock_area
