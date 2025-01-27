# src/suspension/ui/windows/main_window.py

"""
Main application window for the Suspension Calculator.
"""
from typing import cast

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QSplitter,
    QStatusBar,
)

from ..components.navigation.menu.main_menu import MainMenu
from ..components.navigation.tree_view import NavigationTree
from ..components.toolbar.context_toolbar import ContextToolbar
from ..components.toolbar.main_toolbar import MainToolbar
from ..managers.navigation import NavigationManager
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
    nav_tree: NavigationTree
    main_toolbar: MainToolbar
    context_toolbar: ContextToolbar
    main_splitter: QSplitter
    data_panel: QWidget
    plot_panel: QWidget
    logger: StructuredLogger
    _context: dict[str, str]
    main_menu: MainMenu

    def __init__(self) -> None:
        """Initialize the main window."""
        super().__init__()

        # Initialize managers
        self.theme_manager = ThemeManager()
        self.nav_manager = NavigationManager()
        self.window_manager = WindowManager(self)  # Add window manager

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
        # Create splitter for resizable panels
        self.main_splitter = QSplitter(Qt.Orientation.Horizontal)

        # Navigation tree (left panel)
        self.nav_tree = NavigationTree(self.nav_manager)
        self.main_splitter.addWidget(self.nav_tree)

        # Content area (center + right panels)
        content_splitter = QSplitter(Qt.Orientation.Horizontal)

        # Data entry panel
        self.data_panel = QWidget()  # TODO: Replace with proper data entry panel
        content_splitter.addWidget(self.data_panel)

        # Plot view panel
        self.plot_panel = QWidget()  # TODO: Replace with proper plot panel
        content_splitter.addWidget(self.plot_panel)

        # Add content splitter to main splitter
        self.main_splitter.addWidget(content_splitter)

        # Set stretch factors
        self.main_splitter.setStretchFactor(0, 0)  # Navigation tree doesn't stretch
        self.main_splitter.setStretchFactor(1, 1)  # Content area stretches

        # Add to central widget - with proper type checking
        central = self.centralWidget()
        if central is not None:
            layout = central.layout()
            if layout is not None:
                layout = cast(QVBoxLayout, layout)
                layout.addWidget(self.main_splitter)

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
            self.logger.info("Saved window state", context=self._context)
            event.accept()
        except Exception as e:
            self.logger.error(
                "Failed to save window state", error=e, context=self._context
            )
            event.accept()
