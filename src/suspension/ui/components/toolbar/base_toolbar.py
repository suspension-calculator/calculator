# # src/suspension/ui/components/toolbar/base_toolbar.pys
"""
Base toolbar component providing common functionality.
"""

import qtawesome as qta  # type: ignore
from typing import Optional, Dict, Any

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QWidget, QToolBar

from ...constants.icons import AppIcon


class BaseToolBar(QToolBar):
    """
    Base toolbar component with common functionality.

    Features:
    - Icon support (QtAwesome and AppIcon)
    - Standard styling
    - Action management
    - State persistence
    """

    action_triggered = pyqtSignal(str)  # Emitted when an action is triggered

    def __init__(
        self,
        name: str,
        parent: Optional[QWidget] = None,
        movable: bool = False,
        floatable: bool = False,
    ) -> None:
        """Initialize the toolbar."""
        super().__init__(name, parent)

        self.setObjectName(name)
        self.setMovable(movable)
        self.setFloatable(floatable)

        # Store actions by ID for easy access
        self._actions: Dict[str, QAction] = {}

    def add_action(
        self,
        action_id: str,
        text: str,
        icon_name: Optional[str] = None,
        shortcut: Optional[str] = None,
        checkable: bool = False,
        tooltip: Optional[str] = None,
        status_tip: Optional[str] = None,
    ) -> QAction:
        """
        Add an action to the toolbar.

        Args:
            action_id: Unique identifier for the action
            text: Display text
            icon_name: Name of icon (FontAwesome or AppIcon)
            shortcut: Keyboard shortcut
            checkable: Whether action can be toggled
            tooltip: Hover tooltip text
            status_tip: Status bar tip text
        """
        action = QAction(text, self)

        if icon_name:
            if icon_name.startswith("fa"):
                action.setIcon(qta.icon(icon_name))
            else:
                icon = AppIcon(icon_name).to_icon()
                action.setIcon(icon)

        if shortcut:
            action.setShortcut(shortcut)
        if checkable:
            action.setCheckable(checkable)
        if tooltip:
            action.setToolTip(tooltip)
        if status_tip:
            action.setStatusTip(status_tip)

        # Connect the action
        action.triggered.connect(lambda: self._handle_action(action_id))

        # Store and add the action
        self._actions[action_id] = action
        super().addAction(action)

        return action

    def add_separator(self) -> None:
        """Add a separator to the toolbar."""
        super().addSeparator()

    def add_widget(self, widget: QWidget) -> None:
        """Add a widget to the toolbar."""
        super().addWidget(widget)

    def get_action(self, action_id: str) -> Optional[QAction]:
        """Get an action by its ID."""
        return self._actions.get(action_id)

    def _handle_action(self, action_id: str) -> None:
        """Handle action triggers."""
        self.action_triggered.emit(action_id)

    def save_state(self) -> Dict[str, Any]:
        """Save toolbar state."""
        state = {
            "visible": self.isVisible(),
            "actions": {
                action_id: action.isChecked() if action.isCheckable() else None
                for action_id, action in self._actions.items()
            },
        }
        return state

    def restore_state(self, state: Dict[str, Any]) -> None:
        """Restore toolbar state."""
        if state.get("visible") is not None:
            self.setVisible(state["visible"])

        for action_id, checked in state.get("actions", {}).items():
            action = self._actions.get(action_id)
            if action and action.isCheckable() and checked is not None:
                action.setChecked(checked)
