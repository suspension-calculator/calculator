# src/suspension/ui/components/navigation/menu/__init__.py
"""
Base menu component providing common functionality.
"""

from typing import Optional, Dict, Any
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu, QWidget

from ....constants.icons import AppIcon


class BaseMenu(QMenu):
    """
    Base menu component with common functionality.

    Features:
    - Icon support (QtAwesome and AppIcon)
    - Action management
    - Submenu support
    - State persistence
    """

    action_triggered = pyqtSignal(str)  # Emitted when an action is triggered

    def __init__(
        self,
        title: str,
        parent: Optional[QWidget] = None,
    ) -> None:
        """Initialize the menu."""
        super().__init__(title, parent)

        # Store actions and submenus by ID
        self._actions: Dict[str, QAction] = {}
        self._submenus: Dict[str, "BaseMenu"] = {}

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
        Add an action to the menu.

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
                import qtawesome as qta

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

    def add_submenu(
        self,
        menu_id: str,
        title: str,
        icon_name: Optional[str] = None,
    ) -> "BaseMenu":
        """
        Add a submenu.

        Args:
            menu_id: Unique identifier for the submenu
            title: Display text
            icon_name: Name of icon (FontAwesome or AppIcon)
        """
        submenu = BaseMenu(title, self)

        if icon_name:
            if icon_name.startswith("fa"):
                import qtawesome as qta

                submenu.setIcon(qta.icon(icon_name))
            else:
                icon = AppIcon(icon_name).to_icon()
                submenu.setIcon(icon)

        # Connect submenu actions
        submenu.action_triggered.connect(self.action_triggered.emit)

        # Store and add the submenu
        self._submenus[menu_id] = submenu
        self.addMenu(submenu)

        return submenu

    def add_separator(self) -> None:
        """Add a separator to the menu."""
        super().addSeparator()

    def get_action(self, action_id: str) -> Optional[QAction]:
        """Get an action by its ID."""
        return self._actions.get(action_id)

    def get_submenu(self, menu_id: str) -> Optional["BaseMenu"]:
        """Get a submenu by its ID."""
        return self._submenus.get(menu_id)

    def _handle_action(self, action_id: str) -> None:
        """Handle action triggers."""
        self.action_triggered.emit(action_id)

    def save_state(self) -> Dict[str, Any]:
        """Save menu state."""
        state = {
            "visible": self.isVisible(),
            "actions": {
                action_id: action.isChecked() if action.isCheckable() else None
                for action_id, action in self._actions.items()
            },
            "submenus": {
                menu_id: menu.save_state() for menu_id, menu in self._submenus.items()
            },
        }
        return state

    def restore_state(self, state: Dict[str, Any]) -> None:
        """Restore menu state."""
        if state.get("visible") is not None:
            self.setVisible(state["visible"])

        for action_id, checked in state.get("actions", {}).items():
            action = self._actions.get(action_id)
            if action and action.isCheckable() and checked is not None:
                action.setChecked(checked)

        for menu_id, menu_state in state.get("submenus", {}).items():
            submenu = self._submenus.get(menu_id)
            if submenu:
                submenu.restore_state(menu_state)
