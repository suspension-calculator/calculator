# src/suspension/ui/components/navigation/navigation_menu.py

from typing import ClassVar, Dict, Optional

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem, QWidget

from ....utils.logging import StructuredLogger, app_logger
from ...constants.icons import AppIcon
from ...managers.navigation import NavigationManager
from ...models.navigation import DEFAULT_NAVIGATION, NavigationItem, NavigationStructure


class NavigationTree(QTreeWidget):
    """
    Navigation menu component.

    Features:
    - Hierarchical menu structure
    - State management via NavigationManager
    - Visual styling and icon management
    - Theme integration
    """

    logger: ClassVar[StructuredLogger] = app_logger

    def __init__(
        self,
        nav_manager: NavigationManager,
        structure: NavigationStructure = DEFAULT_NAVIGATION,
        parent: Optional[QWidget] = None,
    ) -> None:
        """Initialize the navigation menu.

        Args:
            nav_manager: Navigation state manager
            structure: Menu structure configuration
            parent: Parent widget
        """
        super().__init__(parent)
        self._context = {"component": "NavigationMenu"}
        self.logger.info("Initializing navigation menu", self._context)

        self.nav_manager = nav_manager
        self._structure = structure
        self._items: Dict[str, QTreeWidgetItem] = {}

        self._setup_widget()
        self._setup_connections()
        self._build_menu_structure()
        self._restore_state()

    def _setup_widget(self) -> None:
        """Configure widget properties."""
        try:
            self.setHeaderHidden(True)
            self.setRootIsDecorated(False)
            self.setIndentation(16)
            self.setVerticalScrollMode(QTreeWidget.ScrollMode.ScrollPerPixel)
            self.setHorizontalScrollMode(QTreeWidget.ScrollMode.ScrollPerPixel)
            self.setUniformRowHeights(True)
            self.setAnimated(False)
        except Exception as e:
            self.logger.error("Failed to setup widget", e, self._context)
            raise

    def _restore_state(self) -> None:
        """Restore tree state from navigation manager."""
        try:
            # Restore expanded states
            for item_id in self.nav_manager.expanded_item_ids:
                if item := self._items.get(item_id):
                    item.setExpanded(True)
                    self._update_chevron(item)

            # Restore selection if any
            if selected_id := self.nav_manager.selected_item_id:
                if item := self._items.get(selected_id):
                    self.setCurrentItem(item)

            self.logger.debug(
                "Restored tree state",
                {
                    **self._context,
                    "expanded_items": list(self.nav_manager.expanded_item_ids),
                    "selected_item": self.nav_manager.selected_item_id,
                },
            )
        except Exception as e:
            self.logger.error("Failed to restore tree state", e, self._context)
            raise

    def _setup_connections(self) -> None:
        """Setup signal connections."""
        try:
            # Connect to navigation manager signals
            self.nav_manager.item_selected.connect(self._handle_item_selected)
            self.nav_manager.item_expanded.connect(self._handle_item_expanded)
            self.nav_manager.item_collapsed.connect(self._handle_item_collapsed)

            # Connect tree signals
            self.itemClicked.connect(self._handle_item_click)
        except Exception as e:
            self.logger.error("Failed to setup connections", e, self._context)
            raise

    def _handle_item_click(self, item: QTreeWidgetItem, column: int) -> None:
        """Handle item clicks and update navigation manager."""
        try:
            item_id = item.data(0, Qt.ItemDataRole.UserRole)
            self.nav_manager.set_selected_item(item_id)

            # Expand/collapse on single click if item has children
            if item.childCount() > 0:
                item.setExpanded(not item.isExpanded())
                self.nav_manager.toggle_item_expanded(item_id)

            self.logger.debug(
                "Item clicked",
                {**self._context, "item_id": item_id, "expanded": item.isExpanded()},
            )
        except Exception as e:
            self.logger.error("Failed to handle item click", e, self._context)
            raise

    def _build_menu_structure(self) -> None:
        """Build menu structure from configuration."""
        try:
            for item in self._structure.items:
                tree_item = self._create_tree_item(item)
                self.addTopLevelItem(tree_item)
                self._items[item.item_id] = tree_item
        except Exception as e:
            self.logger.error("Failed to build menu structure", e, self._context)
            raise

    def _create_tree_item(
        self, nav_item: NavigationItem, parent: Optional[QTreeWidgetItem] = None
    ) -> QTreeWidgetItem:
        """Create a tree widget item from navigation item."""
        item = QTreeWidgetItem(parent)
        item.setText(0, nav_item.text)
        item.setData(0, Qt.ItemDataRole.UserRole, nav_item.item_id)

        if nav_item.icon:
            icon = getattr(AppIcon, nav_item.icon, None)
            if icon:
                item.setIcon(0, icon.to_icon())

        # Create child items
        for child in nav_item.children:
            child_item = self._create_tree_item(child, item)
            self._items[child.item_id] = child_item

        return item

    def _handle_item_selected(self, item_id: str) -> None:
        """Handle selection change from navigation manager."""
        try:
            if item := self._items.get(item_id):
                self.setCurrentItem(item)
                self.logger.debug(
                    "Item selected", {**self._context, "item_id": item_id}
                )
        except Exception as e:
            self.logger.error("Failed to handle item selection", e, self._context)
            raise

    def _handle_item_expanded(self, item_id: str) -> None:
        """Handle item expansion from navigation manager."""
        try:
            if item := self._items.get(item_id):
                item.setExpanded(True)
                self._update_chevron(item)
                self.logger.debug(
                    "Item expanded", {**self._context, "item_id": item_id}
                )
        except Exception as e:
            self.logger.error("Failed to handle item expansion", e, self._context)
            raise

    def _handle_item_collapsed(self, item_id: str) -> None:
        """Handle item collapse from navigation manager."""
        try:
            if item := self._items.get(item_id):
                item.setExpanded(False)
                self._update_chevron(item)
                self.logger.debug(
                    "Item collapsed", {**self._context, "item_id": item_id}
                )
        except Exception as e:
            self.logger.error("Failed to handle item collapse", e, self._context)
            raise

    def _update_chevron(self, item: QTreeWidgetItem) -> None:
        """Update chevron icon based on expansion state."""
        try:
            if item.childCount() > 0:
                icon = AppIcon.MINIMIZE if item.isExpanded() else AppIcon.MAXIMIZE
                item.setIcon(0, icon.to_icon())
        except Exception as e:
            self.logger.error("Failed to update chevron", e, self._context)
            raise
