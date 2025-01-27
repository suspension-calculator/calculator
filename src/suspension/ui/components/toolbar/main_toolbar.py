# src/suspension/ui/components/toolbar/main_toolbar.py

"""
Main application toolbar.
"""

from typing import Optional
from PyQt6.QtWidgets import QWidget, QLineEdit, QMenu

from .base_toolbar import BaseToolBar
from ...constants.icons import AppIcon


class MainToolbar(BaseToolBar):
    """
    Main application toolbar providing primary navigation and tools.

    Features:
    - Main section buttons (Vehicle Setup, Suspension, Analysis, Reports)
    - Quick Actions menu
    - Search functionality
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Initialize the main toolbar."""
        super().__init__("Main Toolbar", parent, movable=False, floatable=False)
        self._setup_actions()

    def _setup_actions(self) -> None:
        """Setup toolbar actions."""
        # Main section buttons
        self.add_action(
            "vehicle_setup",
            "Vehicle Setup",
            AppIcon.GEOMETRY.value,
            tooltip="Configure vehicle setup",
            status_tip="Open vehicle setup configuration",
        )

        self.add_action(
            "suspension",
            "Suspension",
            AppIcon.SUSPENSION.value,
            tooltip="Suspension settings",
            status_tip="Configure suspension parameters",
        )

        self.add_action(
            "analysis",
            "Analysis",
            AppIcon.ANALYSIS.value,
            tooltip="Run analysis",
            status_tip="Open analysis tools",
        )

        self.add_action(
            "reports",
            "Reports",
            "fa5s.file-alt",
            tooltip="View reports",
            status_tip="Generate and view reports",
        )

        self.add_separator()

        # Quick Actions menu
        quick_actions = QMenu("Quick Actions", self)
        quick_actions.addAction(
            self.add_action(
                "new_analysis",
                "New Analysis",
                "fa5s.plus",
                tooltip="Start new analysis",
            )
        )
        quick_actions.addAction(
            self.add_action(
                "import_data",
                "Import Data",
                "fa5s.file-import",
                tooltip="Import external data",
            )
        )
        quick_actions.addAction(
            self.add_action(
                "export_results",
                "Export Results",
                "fa5s.file-export",
                tooltip="Export analysis results",
            )
        )

        quick_actions_btn = self.add_action(
            "quick_actions",
            "Quick Actions",
            "fa5s.bolt",
            tooltip="Quick access to common actions",
        )
        quick_actions_btn.setMenu(quick_actions)

        self.add_separator()

        # Search box
        search = QLineEdit(self)
        search.setPlaceholderText("Search...")
        search.setMaximumWidth(200)
        self.add_widget(search)
