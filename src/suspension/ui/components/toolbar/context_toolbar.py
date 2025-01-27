# src/suspension/ui/components/toolbar/context_toolbar.py

"""
Context-sensitive toolbar.
"""

from typing import Optional

from PyQt6.QtWidgets import QWidget, QMenu, QLabel

from .base_toolbar import BaseToolBar


class ContextToolbar(BaseToolBar):
    """
    Context-sensitive toolbar that updates based on current view/selection.

    Features:
    - Quick tools (G, L, S, A)
    - Context title
    - Tools menu
    - Compare functionality
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Initialize the context toolbar."""
        super().__init__("Context Toolbar", parent, movable=False, floatable=False)
        self._setup_actions()
        self._context_label = self._setup_context_label()

    def _setup_actions(self) -> None:
        """Setup toolbar actions."""
        # Quick tools
        self.add_action(
            "geometry",
            "Geometry",
            "fa5s.ruler",
            shortcut="G",
            tooltip="Geometry tools",
            status_tip="Access geometry tools",
        )

        self.add_action(
            "links",
            "Links",
            "fa5s.link",
            shortcut="L",
            tooltip="Link configuration",
            status_tip="Configure suspension links",
        )

        self.add_action(
            "springs",
            "Springs",
            "fa5s.compress",
            shortcut="S",
            tooltip="Spring settings",
            status_tip="Configure spring parameters",
        )

        self.add_action(
            "analysis",
            "Analysis",
            "fa5s.chart-line",
            shortcut="A",
            tooltip="Analysis tools",
            status_tip="Access analysis tools",
        )

        self.add_separator()

        # Add context label
        self.add_widget(self._context_label)

        self.add_separator()

        # Tools menu
        tools_menu = QMenu("Tools", self)
        tools_menu.addAction(
            self.add_action(
                "measure", "Measure", "fa5s.ruler", tooltip="Measurement tools"
            )
        )
        tools_menu.addAction(
            self.add_action(
                "calculate", "Calculate", "fa5s.calculator", tooltip="Calculation tools"
            )
        )

        tools_btn = self.add_action(
            "tools", "Tools", "fa5s.tools", tooltip="Access tools"
        )
        tools_btn.setMenu(tools_menu)

        # Compare button
        self.add_action(
            "compare",
            "Compare",
            "fa5s.columns",
            tooltip="Compare configurations",
            status_tip="Compare different configurations",
        )

    def _setup_context_label(self) -> QLabel:
        """Create the context label."""
        label = QLabel("Front Geometry")
        label.setStyleSheet("font-weight: bold; padding: 0 10px;")
        return label

    def set_context(self, context: str) -> None:
        """Update the context label."""
        self._context_label.setText(context)
