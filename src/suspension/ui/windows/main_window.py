"""
Main application window for the Suspension Calculator.
"""

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QToolBar,
    QStatusBar,
    QSplitter,
)
from PyQt6.QtCore import Qt, QSettings

from ..components.navigation.tree_view import NavigationTree
from ..managers.theme import ThemeManager
from ..managers.navigation import NavigationManager
from ...utils.logging import app_logger


class MainWindow(QMainWindow):
    """
    Main application window providing core UI structure.

    Layout:
    - Menu bar (File, Edit, View, Analysis, Help)
    - Main toolbar (Vehicle Setup, Suspension, Analysis, Reports)
    - Breadcrumb navigation
    - Context toolbar
    - Three-panel layout:
        - Navigation tree (collapsible)
        - Data entry
        - Plot view
    - Status bar
    """

    def __init__(self) -> None:
        """Initialize the main window."""
        super().__init__()

        # Initialize managers
        self.theme_manager = ThemeManager()
        self.nav_manager = NavigationManager()

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
        self._create_menu_bar()
        self._create_main_toolbar()
        self._create_breadcrumb()
        self._create_context_toolbar()
        self._create_main_layout()
        self._create_status_bar()

        # Restore window state
        self._restore_window_state()

        # Connect theme manager
        self.theme_manager.theme_changed.connect(self._handle_theme_changed)
        self.theme_manager.error_occurred.connect(self._handle_theme_error)

    def _create_menu_bar(self) -> None:
        """Create the main menu bar."""
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("&File")
        # TODO: Add file menu actions

        # Edit menu
        edit_menu = menu_bar.addMenu("&Edit")
        # TODO: Add edit menu actions

        # View menu
        view_menu = menu_bar.addMenu("&View")
        # TODO: Add view menu actions

        # Analysis menu
        analysis_menu = menu_bar.addMenu("&Analysis")
        # TODO: Add analysis menu actions

        # Help menu
        help_menu = menu_bar.addMenu("&Help")
        # TODO: Add help menu actions

    def _create_main_toolbar(self) -> None:
        """Create the main toolbar."""
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        self.addToolBar(toolbar)

        # TODO: Add toolbar actions
        # - Vehicle Setup
        # - Suspension
        # - Analysis
        # - Reports
        # - Quick Actions
        # - Search

    def _create_breadcrumb(self) -> None:
        """Create the breadcrumb navigation."""
        breadcrumb_bar = QToolBar()
        breadcrumb_bar.setMovable(False)
        breadcrumb_bar.setFloatable(False)
        self.addToolBar(breadcrumb_bar)

        # TODO: Add breadcrumb navigation
        # Connect to navigation manager for updates

    def _create_context_toolbar(self) -> None:
        """Create the context-sensitive toolbar."""
        context_toolbar = QToolBar()
        context_toolbar.setMovable(False)
        context_toolbar.setFloatable(False)
        self.addToolBar(context_toolbar)

        # TODO: Add context actions
        # - Will be updated based on current view/selection

    def _create_main_layout(self) -> None:
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

        # Add to central widget
        self.centralWidget().layout().addWidget(self.main_splitter)

    def _create_status_bar(self) -> None:
        """Create the status bar."""
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage("Ready")

    def _restore_window_state(self) -> None:
        """Restore saved window state and geometry."""
        settings = QSettings()

        # Restore window geometry
        geometry = settings.value("mainwindow/geometry")
        if geometry:
            self.restoreGeometry(geometry)

        # Restore window state (toolbar positions, etc)
        state = settings.value("mainwindow/state")
        if state:
            self.restoreState(state)

        # Restore splitter states
        nav_splitter_state = settings.value("mainwindow/nav_splitter")
        if nav_splitter_state:
            self.main_splitter.restoreState(nav_splitter_state)

    def closeEvent(self, event) -> None:
        """Handle window close event."""
        try:
            # Save window state
            settings = QSettings()
            settings.setValue("mainwindow/geometry", self.saveGeometry())
            settings.setValue("mainwindow/state", self.saveState())
            settings.setValue("mainwindow/nav_splitter", self.main_splitter.saveState())

            self.logger.info("Saved window state", context=self._context)
            event.accept()
        except Exception as e:
            self.logger.error(
                "Failed to save window state", error=e, context=self._context
            )
            event.accept()

    def _handle_theme_changed(self, theme) -> None:
        """Handle theme changes."""
        # Apply component-specific styles
        self.nav_tree.setStyleSheet(
            self.theme_manager.get_component_stylesheet("navigation")
        )
        # TODO: Apply other component-specific styles

    def _handle_theme_error(self, error_msg: str) -> None:
        """Handle theme-related errors."""
        self.statusBar().showMessage(
            f"Theme Error: {error_msg}", 5000
        )  # Show for 5 seconds
        self.logger.error(
            "Theme error occurred", context={**self._context, "error": error_msg}
        )
