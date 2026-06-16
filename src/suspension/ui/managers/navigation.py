from typing import Any, Dict, List, Optional, Set

from PyQt6.QtCore import QObject, QSettings, pyqtSignal

from suspension import (
    InvalidNavigationItemError,
    NavigationError,
    NavigationPersistenceError,
    NavigationStateError,
)
from suspension.utils import app_logger


class NavigationManager(QObject):
    """
    Manages navigation state using Qt signals/slots.

    Features:
    - Tree item selection/expansion
    - Navigation pane visibility
    - Navigation history
    - State persistence
    - Error logging and recovery
    """

    # Signal definitions
    item_selected = pyqtSignal(str)  # Item ID
    item_expanded = pyqtSignal(str)  # Item ID
    item_collapsed = pyqtSignal(str)  # Item ID
    nav_visibility_changed = pyqtSignal(bool)
    drawer_state_changed = pyqtSignal(bool)

    def __init__(self) -> None:
        """Initialize the navigation manager and load persistent state."""
        super().__init__()

        # Create logger context
        self.logger = app_logger
        self._context = {"component": "NavigationManager"}

        # Initialize state
        self._settings = QSettings()
        self._selected_item_id: Optional[str] = None
        self._expanded_item_ids: Set[str] = set()
        self._drawer_visible = True
        self._nav_pane_visible: bool = True
        self._history: List[str] = []
        self._current_index: int = -1

        # Valid navigation items (could be loaded from configuration)
        self._valid_items = {
            "suspension",
            "suspension-geometry",
            "suspension-springs",
            "suspension-dampers",
            "suspension-links",
            "suspension-pitch",
            "suspension-driveshaft",
            "materials",
            "settings",
        }

        try:
            self._load_state()
            self.logger.info(
                "Navigation manager initialized successfully", self._context
            )
        except Exception as e:
            self.logger.error(
                "Failed to initialize navigation manager",
                error=e,
                context=self._context,
            )
            raise NavigationError("Failed to initialize navigation") from e

    def get_drawer_state(self) -> bool:
        """Get the current drawer visibility state."""
        return self._drawer_visible

    def set_drawer_visible(self, visible: bool) -> None:
        """Set drawer visibility state."""
        try:
            if self._drawer_visible != visible:
                self._drawer_visible = visible
                self._settings.setValue("navigation/drawer/visible", visible)
                self.drawer_state_changed.emit(visible)

                self.logger.debug(
                    "Set drawer visibility",
                    {**self._context, "visible": visible},
                )
        except Exception as e:
            self.logger.error("Failed to set drawer visibility", e, self._context)
            raise

    def _load_state(self) -> None:
        """Load navigation state from settings."""
        try:
            # Load existing navigation state
            self._expanded_item_ids = set(
                self._settings.value("navigation/expanded_items", [], type=list)
            )
            self._selected_item_id = self._settings.value(
                "navigation/selected_item", None, type=str
            )
            # Add drawer state loading
            self._drawer_visible = self._settings.value(
                "navigation/drawer/visible", True, type=bool
            )

            self.logger.debug(
                "Loaded navigation state",
                {
                    **self._context,
                    "expanded_items": list(self._expanded_item_ids),
                    "drawer_visible": self._drawer_visible,
                },
            )
        except Exception as e:
            self.logger.error("Failed to load navigation state", e, self._context)
            raise

    def _save_state(self) -> None:
        """Save current navigation state to persistent storage."""
        try:
            self._settings.setValue(
                "navigation/expanded_items", list(self._expanded_item_ids)
            )
            self._settings.setValue("navigation/pane_visible", self._nav_pane_visible)
            self.logger.debug(
                "Saved navigation state",
                context={
                    **self._context,
                    "expanded_items": list(self._expanded_item_ids),
                },
            )
        except Exception as e:
            self.logger.error(
                "Failed to save navigation state", error=e, context=self._context
            )
            raise NavigationPersistenceError("Failed to save navigation state") from e

    def _validate_item_id(self, item_id: str) -> None:
        """
        Validate that an item ID exists in the navigation tree.

        Raises:
            InvalidNavigationItemError: If the item ID is invalid
        """
        if item_id not in self._valid_items:
            self.logger.error(
                f"Invalid navigation item: {item_id}",
                context={**self._context, "item_id": item_id},
            )
            raise InvalidNavigationItemError(f"Invalid navigation item: {item_id}")

    @property
    def selected_item_id(self) -> Optional[str]:
        """Currently selected navigation item ID."""
        return self._selected_item_id

    @property
    def expanded_item_ids(self) -> Set[str]:
        """Set of currently expanded item IDs."""
        return self._expanded_item_ids.copy()

    @property
    def nav_pane_visible(self) -> bool:
        """Navigation pane visibility state."""
        return self._nav_pane_visible

    def set_selected_item(self, item_id: str) -> None:
        """
        Set the selected navigation item.

        Args:
            item_id: Identifier of the item to select

        Raises:
            InvalidNavigationItemError: If the item ID is invalid
        """
        try:
            self._validate_item_id(item_id)

            if item_id != self._selected_item_id:
                self._selected_item_id = item_id
                self._history = self._history[: self._current_index + 1]
                self._history.append(item_id)
                self._current_index = len(self._history) - 1
                self.item_selected.emit(item_id)

                self.logger.info(
                    f"Selected navigation item: {item_id}",
                    context={**self._context, "item_id": item_id},
                )
        except Exception as e:
            self.logger.error(
                "Failed to set selected item",
                error=e,
                context={**self._context, "item_id": item_id},
            )
            raise

    def toggle_item_expanded(self, item_id: str) -> None:
        """
        Toggle the expanded state of a navigation item.

        Args:
            item_id: Identifier of the item to toggle

        Raises:
            InvalidNavigationItemError: If the item ID is invalid
        """
        try:
            self._validate_item_id(item_id)

            if item_id in self._expanded_item_ids:
                self._expanded_item_ids.remove(item_id)
                self.item_collapsed.emit(item_id)
            else:
                self._expanded_item_ids.add(item_id)
                self.item_expanded.emit(item_id)

            self._save_state()
            self.logger.debug(
                f"Toggled item expansion: {item_id}",
                context={
                    **self._context,
                    "item_id": item_id,
                    "expanded": item_id in self._expanded_item_ids,
                },
            )
        except Exception as e:
            self.logger.error(
                "Failed to toggle item expansion",
                error=e,
                context={**self._context, "item_id": item_id},
            )
            raise

    def set_nav_pane_visible(self, visible: bool) -> None:
        """
        Set navigation pane visibility.

        Args:
            visible: Whether the navigation pane should be visible
        """
        try:
            if visible != self._nav_pane_visible:
                self._nav_pane_visible = visible
                self.nav_visibility_changed.emit(visible)
                self._save_state()

                self.logger.debug(
                    "Set navigation pane visibility",
                    context={**self._context, "visible": visible},
                )
        except Exception as e:
            self.logger.error(
                "Failed to set navigation pane visibility",
                error=e,
                context={**self._context, "visible": visible},
            )
            raise NavigationStateError("Failed to set navigation visibility") from e

    def can_go_back(self) -> bool:
        """Check if backward navigation is possible."""
        return self._current_index > 0

    def can_go_forward(self) -> bool:
        """Check if forward navigation is possible."""
        return self._current_index < len(self._history) - 1

    def go_back(self) -> None:
        """
        Navigate to the previous item in history.

        Raises:
            NavigationStateError: If there is no previous item
        """
        try:
            if self.can_go_back():
                self._current_index -= 1
                item_id = self._history[self._current_index]
                self._selected_item_id = item_id
                self.item_selected.emit(item_id)
                self.logger.debug(
                    "Navigated back", context={**self._context, "item_id": item_id}
                )
            else:
                raise NavigationStateError("Cannot navigate back: at start of history")
        except Exception as e:
            self.logger.error("Failed to navigate back", error=e, context=self._context)
            raise

    def go_forward(self) -> None:
        """
        Navigate to the next item in history.

        Raises:
            NavigationStateError: If there is no next item
        """
        try:
            if self.can_go_forward():
                self._current_index += 1
                item_id = self._history[self._current_index]
                self._selected_item_id = item_id
                self.item_selected.emit(item_id)
                self.logger.debug(
                    "Navigated forward", context={**self._context, "item_id": item_id}
                )
            else:
                raise NavigationStateError("Cannot navigate forward: at end of history")
        except Exception as e:
            self.logger.error(
                "Failed to navigate forward", error=e, context=self._context
            )
            raise

    def clear_history(self) -> None:
        """Clear navigation history."""
        try:
            self._history = []
            self._current_index = -1
            self.logger.debug("Cleared navigation history", context=self._context)
        except Exception as e:
            self.logger.error(
                "Failed to clear navigation history", error=e, context=self._context
            )
            raise NavigationStateError("Failed to clear navigation history") from e

    def get_state_snapshot(self) -> Dict[str, Any]:
        """
        Get a snapshot of the current navigation state.
        Useful for debugging and state restoration.

        Returns:
            Dict containing the current navigation state
        """
        return {
            "selected_item": self._selected_item_id,
            "expanded_items": list(self._expanded_item_ids),
            "nav_pane_visible": self._nav_pane_visible,
            "history": self._history,
            "current_index": self._current_index,
        }

    def restore_state_snapshot(self, snapshot: Dict[str, Any]) -> None:
        """
        Restore navigation state from a snapshot.

        Args:
            snapshot: State snapshot from get_state_snapshot()

        Raises:
            NavigationStateError: If the snapshot is invalid
        """
        try:
            # Validate snapshot
            required_keys = {
                "selected_item",
                "expanded_items",
                "nav_pane_visible",
                "history",
                "current_index",
            }
            if not all(key in snapshot for key in required_keys):
                raise NavigationStateError(
                    "Invalid state snapshot: missing required keys"
                )

            # Restore state
            if snapshot["selected_item"]:
                self._validate_item_id(snapshot["selected_item"])
            self._selected_item_id = snapshot["selected_item"]

            for item_id in snapshot["expanded_items"]:
                self._validate_item_id(item_id)
            self._expanded_item_ids = set(snapshot["expanded_items"])

            self._nav_pane_visible = bool(snapshot["nav_pane_visible"])
            self._history = list(snapshot["history"])
            self._current_index = int(snapshot["current_index"])

            # Emit signals for state changes
            if self._selected_item_id:
                self.item_selected.emit(self._selected_item_id)
            for item_id in self._expanded_item_ids:
                self.item_expanded.emit(item_id)
            self.nav_visibility_changed.emit(self._nav_pane_visible)

            self._save_state()
            self.logger.info(
                "Restored navigation state from snapshot",
                context={**self._context, "snapshot": snapshot},
            )
        except Exception as e:
            self.logger.error(
                "Failed to restore navigation state",
                error=e,
                context={**self._context, "snapshot": snapshot},
            )
            raise
