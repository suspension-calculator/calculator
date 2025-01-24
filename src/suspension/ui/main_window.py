# src/suspension/ui/main_window.py
from typing import Set

import qtawesome as qta
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTreeWidget,
    QTreeWidgetItem,
    QStatusBar,
    QDockWidget,
    QStackedWidget,
    QHBoxLayout,
)

from suspension.infrastructure.state.observers.navigation import NavigationStore
from suspension.infrastructure.state.types.navigation import NavigationState
from suspension.ui.components.navigation_header import NavigationHeader
from suspension.ui.components.navigation_item import NavigationItem
from suspension.ui.components.navigation_strip import NavigationStrip
from suspension.ui.styles.theme import Theme


class MainWindow(QMainWindow):
    """Main application window that implements the Observer protocol"""

    def __init__(self, nav_store: NavigationStore):
        super().__init__()
        self.setWindowTitle("Suspension Calculator")
        self.resize(1200, 800)

        # Store the injected navigation store
        self.nav_store = nav_store
        self.nav_store.add_observer(self)

        self._setup_ui()
        self._create_actions()
        self._create_toolbar()
        self._create_status_bar()

    def _setup_ui(self):
        """Sets up the main UI layout with a specific dock widget configuration."""
        base_widget = QWidget()
        self.setCentralWidget(base_widget)

        base_layout = QHBoxLayout(base_widget)
        base_layout.setContentsMargins(0, 0, 0, 0)
        base_layout.setSpacing(0)

        self.content_stack = QStackedWidget()
        base_layout.addWidget(self.content_stack, 1)

        # Create navigation strip
        self.nav_strip = NavigationStrip(self)
        strip_dock = QDockWidget(self)
        strip_dock.setWidget(self.nav_strip)
        strip_dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        strip_dock.setTitleBarWidget(QWidget())
        strip_dock.setFixedWidth(40)
        strip_dock.setStyleSheet(
            """
            QDockWidget {
                border: none;
                background: transparent;
            }
        """
        )

        # Create navigation dock
        self.nav_dock = QDockWidget(self)
        self.nav_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable)

        # Create the navigation content
        nav_content = QWidget()
        nav_layout = QVBoxLayout(nav_content)
        nav_layout.setContentsMargins(0, 0, 0, 0)
        nav_layout.setSpacing(0)

        # Setup header
        theme = Theme.current()
        self.nav_header = NavigationHeader(self.nav_dock, theme)
        self.nav_dock.setTitleBarWidget(self.nav_header)

        # Setup tree
        self.nav_tree = QTreeWidget()
        self.nav_tree.setHeaderHidden(True)
        self.nav_tree.setRootIsDecorated(False)
        self.nav_tree.setIndentation(16)
        self.nav_tree.setVerticalScrollMode(QTreeWidget.ScrollMode.ScrollPerPixel)
        self.nav_tree.setHorizontalScrollMode(QTreeWidget.ScrollMode.ScrollPerPixel)
        self.nav_tree.setUniformRowHeights(True)
        self.nav_tree.setAnimated(False)

        self.nav_tree.setStyleSheet(
            """
            QTreeWidget {
                border: none;
                background-color: transparent;
                outline: none;
            }
            QTreeWidget::item {
                padding: 4px;
            }
            QTreeWidget::item:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
            QTreeWidget::item:selected {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """
        )

        self.nav_tree.itemClicked.connect(self._handle_item_click)
        self.nav_tree.setAttribute(Qt.WidgetAttribute.WA_MacShowFocusRect, False)
        self.nav_tree.setFrameStyle(0)

        # Create items and add to layout
        self._create_nav_items()
        nav_layout.addWidget(self.nav_tree)

        # Set content widget
        self.nav_dock.setWidget(nav_content)

        # Add dock widgets
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, strip_dock)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.nav_dock)
        self.splitDockWidget(strip_dock, self.nav_dock, Qt.Orientation.Horizontal)

        # Prevent docks from tabbing
        self.setDockNestingEnabled(False)

        # Connect navigation components
        self.nav_strip.nav_button.clicked.connect(self._toggle_navigation)
        self.nav_dock.visibilityChanged.connect(self._on_dock_visibility_changed)

    def _handle_item_click(self, item: QTreeWidgetItem, column: int):
        """Handle item clicks using store actions"""
        item_id = item.data(0, Qt.ItemDataRole.UserRole)
        current_state = self.nav_store.state

        if item.childCount() > 0:
            # Update expanded state in store
            new_expanded_ids = current_state.expanded_item_ids.copy()
            if item_id in new_expanded_ids:
                new_expanded_ids.remove(item_id)
            else:
                new_expanded_ids.add(item_id)

            new_state = NavigationState(
                **{**current_state.dict(), "expanded_item_ids": new_expanded_ids}
            )
            self.nav_store.set_state(new_state)
            self._update_chevron(item)
        else:
            # Update selected item and page in store
            new_state = NavigationState(
                **{
                    **current_state.dict(),
                    "selected_item_id": item_id,
                    "current_page": item.text(column),
                }
            )
            self.nav_store.set_state(new_state)
            self.status_bar.showMessage(f"Selected: {item.text(column)}")

    def _create_actions(self):
        self.open_action = QAction("Open...", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)

        self.save_action = QAction("Save", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)

        self.save_as_action = QAction("Save As...", self)
        self.save_as_action.setShortcut("Ctrl+Shift+S")
        self.save_action.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)

    def _create_toolbar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.setAsDockMenu()

        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.save_as_action)

    def _create_status_bar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")

    def _create_nav_items(self):
        # Create suspension item with ID
        suspension = QTreeWidgetItem()
        suspension.setIcon(0, qta.icon("fa5s.chevron-right"))
        suspension_widget = NavigationItem("Suspension")
        suspension.setData(0, Qt.ItemDataRole.UserRole, "suspension")
        self.nav_tree.addTopLevelItem(suspension)
        self.nav_tree.setItemWidget(suspension, 0, suspension_widget)

        # Create child items with IDs
        child_items = ["Geometry", "Springs", "Dampers", "Links", "Pitch", "Driveshaft"]
        for item_text in child_items:
            child = QTreeWidgetItem(suspension)
            child_widget = NavigationItem(item_text, is_child=True)
            # Create a kebab-case ID from the text
            item_id = f"suspension-{item_text.lower()}"
            child.setData(0, Qt.ItemDataRole.UserRole, item_id)
            self.nav_tree.setItemWidget(child, 0, child_widget)

        # Create other top-level items with IDs
        for item_text in ["Materials", "Settings"]:
            item = QTreeWidgetItem()
            item_widget = NavigationItem(item_text)
            # Create kebab-case ID
            item_id = item_text.lower()
            item.setData(0, Qt.ItemDataRole.UserRole, item_id)
            self.nav_tree.addTopLevelItem(item)
            self.nav_tree.setItemWidget(item, 0, item_widget)

    def _update_chevron(self, item):
        """Update chevron icon based on expansion state"""
        if item.childCount() > 0:
            is_expanded = item.isExpanded()
            item.setIcon(
                0, qta.icon(f"fa5s.chevron-{'down' if is_expanded else 'right'}")
            )

    def _toggle_navigation(self, checked: bool):
        """Toggle navigation pane visibility"""
        current_state = self.nav_store.state
        new_state = NavigationState(
            **{**current_state.dict(), "nav_pane_visible": checked}
        )
        self.nav_store.set_state(new_state)

    def _on_dock_visibility_changed(self, visible: bool):
        """Handle dock visibility changes"""
        current_state = self.nav_store.state
        new_state = NavigationState(
            **{**current_state.dict(), "nav_pane_visible": visible}
        )
        self.nav_store.set_state(new_state)
        self.nav_strip.nav_button.setChecked(visible)

    def on_state_changed(self, state: NavigationState):
        """Observer method to handle state changes"""
        # Update UI based on navigation state changes
        self.nav_dock.setVisible(state.nav_pane_visible)

        # Update selected items
        if state.selected_item_id:
            self._update_selected_item(state.selected_item_id)

        # Update expanded items
        self._update_expanded_items(state.expanded_item_ids)

        # Update current page if changed
        if state.current_page:
            self._update_current_page(state.current_page)

    def _update_selected_item(self, selected_id: str):
        """Update the selected item in the navigation tree"""
        self._clear_selection()

        def find_and_select_item(root_item: QTreeWidgetItem) -> bool:
            # Check the current item
            item_id = root_item.data(0, Qt.ItemDataRole.UserRole)
            if item_id == selected_id:
                root_item.setSelected(True)
                return True

            # Check children
            for i in range(root_item.childCount()):
                if find_and_select_item(root_item.child(i)):
                    return True
            return False

        # Search through top-level items
        for i in range(self.nav_tree.topLevelItemCount()):
            if find_and_select_item(self.nav_tree.topLevelItem(i)):
                break

    def _clear_selection(self):
        """Clear all selected items in the tree"""
        for item in self.nav_tree.selectedItems():
            item.setSelected(False)

    def _update_expanded_items(self, expanded_ids: Set[str]):
        """Update the expansion state of all items in the tree"""

        def update_item_expansion(item: QTreeWidgetItem):
            item_id = item.data(0, Qt.ItemDataRole.UserRole)
            if item_id:
                is_expanded = item_id in expanded_ids
                item.setExpanded(is_expanded)
                self._update_chevron(item)

            # Process children
            for i in range(item.childCount()):
                update_item_expansion(item.child(i))

        # Update all top-level items
        for i in range(self.nav_tree.topLevelItemCount()):
            update_item_expansion(self.nav_tree.topLevelItem(i))

    def _update_current_page(self, page_name: str):
        """Update the current page in the content stack"""
        # TODO: Implement page switching logic when content pages are added
        self.status_bar.showMessage(f"Current page: {page_name}")

    def closeEvent(self, event):
        """Handle window close event"""
        # Clean up observers
        self.nav_store.remove_observer(self)
        super().closeEvent(event)
