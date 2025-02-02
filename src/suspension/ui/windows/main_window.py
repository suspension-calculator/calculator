# src/suspension/ui/windows/main_window.py

"""
Main application window for the Suspension Calculator.
"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QSplitter,
    QStatusBar,
    QToolBar,
)

from ..components.base.placeholder import PlaceholderWidget
from ..components.navigation import Drawer, NavigationTree
from ..components.navigation.menu import MainMenu
from ..components.panels import DataEntryPanel, PlotViewPanel
from ..components.toolbar import ContextToolbar, MainToolbar
from ..managers.navigation import NavigationManager
from ..managers.panel import PanelManager
from ..managers.theme import ThemeManager
from ..managers.window import WindowManager
from ..models.theme import Theme
from ...utils.logging import app_logger, StructuredLogger


class MainWindow(QMainWindow):
    """
    Main application window providing core UI structure.

    Layout:
    - Menu bar (File, Edit, View, Analysis, Help)
    - Main toolbar (Vehicle Setup, Suspension, Analysis, Reports)
    - Context toolbar
    - Three-panel layout:
        - Navigation tree (collapsible)
        - Data entry
        - Plot view
    - Status bar
    """

    theme_manager: ThemeManager
    nav_manager: NavigationManager
    window_manager: WindowManager
    panel_manager: PanelManager
    nav_tree: NavigationTree
    main_toolbar: MainToolbar
    context_toolbar: ContextToolbar
    main_splitter: QSplitter
    data_panel: DataEntryPanel
    plot_panel: PlotViewPanel
    logger: StructuredLogger
    _context: dict[str, str]
    main_menu: MainMenu

    def __init__(self) -> None:
        """Initialize the main window."""
        super().__init__()

        # Initialize managers
        self.theme_manager = ThemeManager()
        self.nav_manager = NavigationManager()
        self.window_manager = WindowManager(self)
        self.panel_manager = PanelManager(self)

        # Setup logging
        self.logger = app_logger
        self._context = {"component": "MainWindow"}

        try:
            self._initialize_window()
            self.logger.info("Main window initialized", context=self._context)
        except Exception as e:
            self.logger.error(
                "Failed to initialize main window", error=e, context=self._context
            )
            raise

    def _handle_theme_error(self, error_msg: str) -> None:
        """Handle theme-related errors."""
        self.window_manager.show_status_message(f"Theme Error: {error_msg}", 5000)
        self.logger.error(
            "Theme error occurred", context={**self._context, "error": error_msg}
        )

    def _initialize_window(self) -> None:
        """Initialize the window layout and components."""
        # Set window properties
        self.setWindowTitle("Suspension Calculator")
        self.resize(1200, 800)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Create core UI components
        self._setup_menu()
        self._setup_toolbars()
        self._setup_main_layout()
        self._setup_status_bar()

        # Restore window state
        self._restore_window_state()

        # Connect theme manager
        self.theme_manager.theme_changed.connect(self._handle_theme_changed)
        self.theme_manager.error_occurred.connect(self._handle_theme_error)

    def _setup_menu(self) -> None:
        """Setup the main menu bar."""
        self.main_menu = MainMenu(self)
        self.setMenuBar(self.main_menu)
        # Connect menu actions
        # TODO: Implement menu action handlers

    def _setup_toolbars(self) -> None:
        """Setup the main and context toolbars."""
        # Main toolbar
        self.main_toolbar = MainToolbar(self)
        self.addToolBar(self.main_toolbar)
        # TODO: Connect main toolbar actions

        # Context toolbar
        self.context_toolbar = ContextToolbar(self)
        self.addToolBar(self.context_toolbar)
        # TODO: Connect context toolbar actions

    def _setup_main_layout(self) -> None:
        """Create the main three-panel layout."""
        self._setup_central_widget()
        self._setup_navigation_drawer()
        self._setup_panels()

    def _setup_central_widget(self) -> None:
        """Setup the central widget and its layout."""
        main_content = QWidget()
        main_layout = QVBoxLayout(main_content)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(main_content)

    def _setup_navigation_drawer(self) -> None:
        """Setup the navigation drawer with tree view."""
        # Create the navigation tree first
        nav_tree = NavigationTree(self.nav_manager)

        # Get animation duration with a safe default
        animation_duration = (
            self.theme_manager.theme.animation_duration_normal
            if self.theme_manager.theme is not None
            else 200
        )

        # Create the drawer containing the navigation tree
        self.nav_drawer = Drawer(
            content=nav_tree,
            parent=self,
            width=250,
            animation_duration=animation_duration,
        )

        # Position the toggle button absolutely in the top-left corner
        self.nav_drawer.toggle_button.setFixedSize(32, 32)  # Make button bigger
        self.nav_drawer.toggle_button.move(4, 4)  # Position it with some padding

        # Connect to theme system
        self.theme_manager.theme_changed.connect(
            lambda theme: self.nav_drawer.apply_theme(theme)
        )
        if current_theme := self.theme_manager.theme:
            self.nav_drawer.apply_theme(current_theme)

        # Add the drawer to the main window
        main_content = self.centralWidget()
        if isinstance(main_content, QWidget):
            layout = main_content.layout()
            if isinstance(layout, QVBoxLayout):
                layout.insertWidget(0, self.nav_drawer)

    def _create_navigation_container(self) -> QWidget:
        """Create and setup the navigation container widget."""
        nav_container = QWidget()
        nav_container.setObjectName("nav_container")
        nav_container_layout = QVBoxLayout(nav_container)
        nav_container_layout.setContentsMargins(0, 0, 0, 0)

        self.nav_tree = NavigationTree(self.nav_manager)
        nav_container_layout.addWidget(self.nav_tree)

        nav_container.setFixedWidth(250)
        nav_container.setStyleSheet(
            """
            QWidget#nav_container {
                border-right: 1px solid palette(mid);
                background-color: palette(window);
            }
        """
        )

        return nav_container

    def _add_navigation_toggle(self, nav_toolbar: QToolBar) -> None:
        """Add the navigation toggle button to main toolbar."""
        nav_toggle = self.main_toolbar.add_action(
            "toggle_nav",
            "Toggle Navigation",
            "fa5s.bars",
            tooltip="Toggle Navigation Panel",
            checkable=True,
        )
        nav_toggle.setChecked(True)
        nav_toggle.triggered.connect(lambda checked: nav_toolbar.setVisible(checked))

    def _setup_panels(self) -> None:
        """Setup the data entry and plot view panels."""
        # Create panels
        self.data_panel = self._create_data_panel()
        self.plot_panel = self._create_plot_panel()

        # Add to window
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.data_panel)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.plot_panel)

    def _create_data_panel(self) -> DataEntryPanel:
        """Create and initialize the data entry panel."""
        panel = self.panel_manager.create_data_entry_panel("data_entry", "Data Entry")
        placeholder = PlaceholderWidget("Data Entry Panel\nNo form loaded")
        panel.set_content(placeholder)
        return panel

    def _create_plot_panel(self) -> PlotViewPanel:
        """Create and initialize the plot view panel."""
        panel = self.panel_manager.create_plot_panel("plot_view", "Plot View")
        placeholder = PlaceholderWidget("Plot View Panel\nNo plot loaded")
        panel.set_content(placeholder)
        return panel

    def _setup_status_bar(self) -> None:
        """Setup the status bar."""
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage("Ready")

    def _restore_window_state(self) -> None:
        """Restore saved window state and geometry."""
        self.window_manager.restore_state()

    def _handle_theme_changed(self, theme: Theme) -> None:
        """Handle theme changes."""
        # Apply component-specific styles
        stylesheet = self.theme_manager.get_component_stylesheet("navigation")
        if stylesheet:
            self.nav_tree.setStyleSheet(stylesheet)

        toolbar_style = self.theme_manager.get_component_stylesheet("toolbar")
        if toolbar_style:
            self.main_toolbar.setStyleSheet(toolbar_style)
            self.context_toolbar.setStyleSheet(toolbar_style)

    def closeEvent(self, event: QCloseEvent | None) -> None:
        """Handle window close event."""
        if event is None:
            return

        try:
            self.window_manager.save_state()
            self.panel_manager.save_state()
            self.logger.info("Saved window state", context=self._context)
            event.accept()
        except Exception as e:
            self.logger.error(
                "Failed to save window state", error=e, context=self._context
            )
            event.accept()
