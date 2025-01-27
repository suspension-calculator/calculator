# src/suspension/ui/components/navigation/menu/main_menu.py
"""
Main application menu providing primary navigation and actions.
"""

from typing import Optional
from PyQt6.QtWidgets import QWidget, QMenuBar

from .base_menu import BaseMenu


class MainMenu(QMenuBar):
    """
    Main application menu bar.

    Features:
    - File menu (New, Open, Save, Export)
    - Edit menu (Undo, Redo, Preferences)
    - View menu (Panels, Themes)
    - Analysis menu (Run, Stop, Export)
    - Help menu (Documentation, About)
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Initialize the main menu."""
        super().__init__(parent)
        self._setup_menus()

    def _setup_menus(self) -> None:
        """Setup all main menus."""
        self._setup_file_menu()
        self._setup_edit_menu()
        self._setup_view_menu()
        self._setup_analysis_menu()
        self._setup_help_menu()

    def _setup_file_menu(self) -> None:
        """Setup the File menu."""
        file_menu = BaseMenu("&File", self)
        self.addMenu(file_menu)

        file_menu.add_action(
            "new",
            "New",
            "fa5s.file",
            shortcut="Ctrl+N",
            tooltip="Create new configuration",
            status_tip="Create a new suspension configuration",
        )

        file_menu.add_action(
            "open",
            "Open",
            "fa5s.folder-open",
            shortcut="Ctrl+O",
            tooltip="Open configuration",
            status_tip="Open an existing configuration",
        )

        file_menu.add_action(
            "save",
            "Save",
            "fa5s.save",
            shortcut="Ctrl+S",
            tooltip="Save configuration",
            status_tip="Save current configuration",
        )

        file_menu.add_separator()

        file_menu.add_action(
            "export",
            "Export",
            "fa5s.file-export",
            shortcut="Ctrl+E",
            tooltip="Export configuration",
            status_tip="Export configuration to file",
        )

        file_menu.add_separator()

        file_menu.add_action(
            "exit",
            "Exit",
            "fa5s.times",
            shortcut="Alt+F4",
            tooltip="Exit application",
            status_tip="Exit the application",
        )

    def _setup_edit_menu(self) -> None:
        """Setup the Edit menu."""
        edit_menu = BaseMenu("&Edit", self)
        self.addMenu(edit_menu)

        edit_menu.add_action(
            "undo",
            "Undo",
            "fa5s.undo",
            shortcut="Ctrl+Z",
            tooltip="Undo last action",
            status_tip="Undo the last action",
        )

        edit_menu.add_action(
            "redo",
            "Redo",
            "fa5s.redo",
            shortcut="Ctrl+Y",
            tooltip="Redo last action",
            status_tip="Redo the last undone action",
        )

        edit_menu.add_separator()

        edit_menu.add_action(
            "preferences",
            "Preferences",
            "fa5s.cog",
            tooltip="Open preferences",
            status_tip="Open application preferences",
        )

    def _setup_view_menu(self) -> None:
        """Setup the View menu."""
        view_menu = BaseMenu("&View", self)
        self.addMenu(view_menu)

        # Panel visibility toggles
        view_menu.add_action(
            "toggle_navigation",
            "Navigation Panel",
            "fa5s.bars",
            checkable=True,
            tooltip="Toggle navigation panel",
            status_tip="Show/hide the navigation panel",
        )

        view_menu.add_action(
            "toggle_plot",
            "Plot Panel",
            "fa5s.chart-line",
            checkable=True,
            tooltip="Toggle plot panel",
            status_tip="Show/hide the plot panel",
        )

        view_menu.add_separator()

        # Theme submenu
        themes_menu = view_menu.add_submenu("themes", "Themes", "fa5s.palette")

        themes_menu.add_action(
            "theme_light",
            "Light",
            "fa5s.sun",
            checkable=True,
            tooltip="Use light theme",
            status_tip="Switch to light theme",
        )

        themes_menu.add_action(
            "theme_dark",
            "Dark",
            "fa5s.moon",
            checkable=True,
            tooltip="Use dark theme",
            status_tip="Switch to dark theme",
        )

        themes_menu.add_action(
            "theme_system",
            "System",
            "fa5s.desktop",
            checkable=True,
            tooltip="Use system theme",
            status_tip="Follow system theme",
        )

    def _setup_analysis_menu(self) -> None:
        """Setup the Analysis menu."""
        analysis_menu = BaseMenu("&Analysis", self)
        self.addMenu(analysis_menu)

        analysis_menu.add_action(
            "run_analysis",
            "Run Analysis",
            "fa5s.play",
            shortcut="F5",
            tooltip="Run analysis",
            status_tip="Run suspension analysis",
        )

        analysis_menu.add_action(
            "stop_analysis",
            "Stop",
            "fa5s.stop",
            shortcut="F6",
            tooltip="Stop analysis",
            status_tip="Stop current analysis",
        )

        analysis_menu.add_separator()

        analysis_menu.add_action(
            "export_results",
            "Export Results",
            "fa5s.file-export",
            tooltip="Export analysis results",
            status_tip="Export analysis results to file",
        )

    def _setup_help_menu(self) -> None:
        """Setup the Help menu."""
        help_menu = BaseMenu("&Help", self)
        self.addMenu(help_menu)

        help_menu.add_action(
            "documentation",
            "Documentation",
            "fa5s.book",
            shortcut="F1",
            tooltip="Open documentation",
            status_tip="View application documentation",
        )

        help_menu.add_action(
            "about",
            "About",
            "fa5s.info-circle",
            tooltip="About application",
            status_tip="Show application information",
        )
