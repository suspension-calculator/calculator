# src/suspension/ui/tabs/link_tab.py
from typing import Dict, Optional
import tkinter as tk
from ..base import BaseTab
from ..components.link_input_panel import LinkInputPanel
from ..components.navigation import NavigationBar
from ...core.models.link_models import LinkPosition, SuspensionConfig, SuspensionResults
from ...core.services.geometry_service import GeometryService
from ...utils.events import Event, EventBus


class LinkTab(BaseTab):
    """
    Tab for suspension link configuration and analysis
    """

    def __init__(self, master):
        super().__init__(master)
        self.geometry_service = GeometryService()
        self.event_bus = EventBus()

        # Subscribe to events
        self.event_bus.subscribe("geometry_updated", self.handle_geometry_update)

        self.setup_ui()

    def setup_ui(self):
        # Create main layout frames
        self.setup_navigation()
        self.setup_input_panels()
        self.setup_plots()
        self.setup_results()

    def setup_navigation(self):
        """Setup navigation buttons"""
        nav_buttons = [
            {"text": "Save", "command": self.save_data},
            {"text": "Load", "command": self.load_data},
            {"text": "Calculate", "command": self.calculate},
        ]
        self.nav_bar = NavigationBar(self, nav_buttons)
        self.nav_bar.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=5)

    def setup_input_panels(self):
        """Setup input panels for front and rear suspension"""
        # Front suspension inputs
        self.front_panel = tk.Frame(self)
        self.front_panel.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        self.front_upper = LinkInputPanel(
            self.front_panel,
            "Front Upper Link",
            "front_upper",
            self.handle_input_change,
        )
        self.front_upper.grid(row=0, column=0, sticky="nsew")

        self.front_lower = LinkInputPanel(
            self.front_panel,
            "Front Lower Link",
            "front_lower",
            self.handle_input_change,
        )
        self.front_lower.grid(row=1, column=0, sticky="nsew")

        # Similar setup for rear suspension...

    def handle_input_change(self):
        """Handle changes in any input field"""
        self.event_bus.publish(Event("geometry_updated", self.get_current_geometry()))

    def handle_geometry_update(self, geometry: Dict):
        """Handle geometry updates"""
        # Update calculations and plots
        results = self.geometry_service.calculate_geometry(geometry)
        self.update_plots(results)
        self.update_results(results)

    def get_current_geometry(self) -> Dict:
        """Get current geometry from all inputs"""
        return {
            "front": {
                "upper": self.front_upper.get_position(),
                "lower": self.front_lower.get_position(),
            },
            "rear": {
                "upper": self.rear_upper.get_position(),
                "lower": self.rear_lower.get_position(),
            },
        }
