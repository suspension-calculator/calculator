# src/suspension/ui/components/navigation/tree_view.py

from typing import Optional

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QTreeWidget,
    QTreeWidgetItem,
    QWidget,
)

from ...constants.icons import AppIcon
from ...managers.navigation import NavigationManager


class NavigationTree(QTreeWidget):
    """
    Custom tree widget for application navigation.

    Works with NavigationManager to maintain state and handle user interactions.
    Supports:
    - Item selection
    - Expansion state
    - Visual styling
    - Icon management
    """

    def __init__(
        self, nav_manager: NavigationManager, parent: QWidget | None = None
    ) -> None:
        """Initialize the navigation tree.

        Args:
            nav_manager: Navigation state manager
            parent: Parent widget
        """
        super().__init__(parent)
        self.nav_manager = nav_manager

        # Configure tree widget
        self.setHeaderHidden(True)
        self.setRootIsDecorated(False)
        self.setIndentation(16)
        self.setVerticalScrollMode(QTreeWidget.ScrollMode.ScrollPerPixel)
        self.setHorizontalScrollMode(QTreeWidget.ScrollMode.ScrollPerPixel)
        self.setUniformRowHeights(True)
        self.setAnimated(False)

        # Connect to navigation manager signals
        self.nav_manager.item_selected.connect(self._handle_item_selected)
        self.nav_manager.item_expanded.connect(self._handle_item_expanded)
        self.nav_manager.item_collapsed.connect(self._handle_item_collapsed)

        # Connect tree signals to manager
        self.itemClicked.connect(self._handle_item_click)

        # Initial setup
        self._setup_tree_items()
        self._restore_state()

    def _setup_tree_items(self) -> None:
        """Create the initial tree structure."""
        # Suspension section
        suspension = QTreeWidgetItem()
        suspension.setIcon(0, AppIcon.SUSPENSION.to_icon())
        suspension.setText(0, "Suspension")
        suspension.setData(0, Qt.ItemDataRole.UserRole, "suspension")
        self.addTopLevelItem(suspension)

        # Child items
        children = [
            ("Geometry", "suspension-geometry"),
            ("Springs", "suspension-springs"),
            ("Dampers", "suspension-dampers"),
            ("Links", "suspension-links"),
            ("Pitch", "suspension-pitch"),
            ("Driveshaft", "suspension-driveshaft"),
        ]

        for text, item_id in children:
            child = QTreeWidgetItem(suspension)
            child.setText(0, text)
            child.setData(0, Qt.ItemDataRole.UserRole, item_id)

        # Other top-level items
        other_items = [
            ("Materials", "materials", AppIcon.GEOMETRY),
            ("Settings", "settings", AppIcon.SETTINGS),
        ]

        for text, item_id, icon in other_items:
            item = QTreeWidgetItem()
            item.setText(0, text)
            item.setIcon(0, icon.to_icon())
            item.setData(0, Qt.ItemDataRole.UserRole, item_id)
            self.addTopLevelItem(item)

    def _restore_state(self) -> None:
        """Restore tree state from navigation manager."""
        # Restore expanded states
        for item_id in self.nav_manager.expanded_item_ids:
            item = self._find_item_by_id(item_id)
            if item:
                item.setExpanded(True)
                self._update_chevron(item)

        # Restore selection if any
        if self.nav_manager.selected_item_id:
            item = self._find_item_by_id(self.nav_manager.selected_item_id)
            if item:
                self.setCurrentItem(item)

    def _handle_item_click(self, item: QTreeWidgetItem, column: int) -> None:
        """Handle item clicks and update navigation manager."""
        item_id = item.data(0, Qt.ItemDataRole.UserRole)
        self.nav_manager.set_selected_item(item_id)  # Always handle selection

        # Expand/collapse on single click if item has children
        if item.childCount() > 0:
            item.setExpanded(not item.isExpanded())
            self.nav_manager.toggle_item_expanded(item_id)

    def _handle_item_selected(self, item_id: str) -> None:
        """Handle selection change from navigation manager."""
        item = self._find_item_by_id(item_id)
        if item:
            self.setCurrentItem(item)

    def _handle_item_expanded(self, item_id: str) -> None:
        """Handle item expansion from navigation manager."""
        item = self._find_item_by_id(item_id)
        if item:
            item.setExpanded(True)
            self._update_chevron(item)

    def _handle_item_collapsed(self, item_id: str) -> None:
        """Handle item collapse from navigation manager."""
        item = self._find_item_by_id(item_id)
        if item:
            item.setExpanded(False)
            self._update_chevron(item)

    def _find_item_by_id(self, item_id: str) -> Optional[QTreeWidgetItem]:
        """Find a tree item by its ID."""

        def search_item(root_item: QTreeWidgetItem) -> Optional[QTreeWidgetItem]:
            if root_item.data(0, Qt.ItemDataRole.UserRole) == item_id:
                return root_item

            for i in range(root_item.childCount()):
                result = search_item(root_item.child(i))
                if result:
                    return result
            return None

        for i in range(self.topLevelItemCount()):
            result = search_item(self.topLevelItem(i))
            if result:
                return result
        return None

    def _update_chevron(self, item: QTreeWidgetItem) -> None:
        """Update chevron icon based on expansion state."""
        if item.childCount() > 0:
            icon = AppIcon.MINIMIZE if item.isExpanded() else AppIcon.MAXIMIZE
            item.setIcon(0, icon.to_icon())
