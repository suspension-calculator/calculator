# src/suspension/ui/base/tab.py
import tkinter as tk
from typing import Dict

from .models import TabState, PlotConfig, PlotData
from .plot_container import PlotContainer


class BaseTab(tk.Frame):
    """
    Base class for all tabs in the application with type-safe state management.
    """

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.state = TabState(tab_name=self.__class__.__name__)
        self.plot_containers: Dict[str, PlotContainer] = {}

        # Configure grid
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Initialize UI components
        self.setup_header()
        self.setup_ui()
        self.setup_events()

    def create_plot(self, plot_id: str, config: PlotConfig) -> PlotContainer:
        """Create a new plot with type-safe configuration"""
        plot = PlotContainer(self, config)
        self.plot_containers[plot_id] = plot
        self.state.plot_configs[plot_id] = config
        return plot

    def update_plot(self, plot_id: str, data: PlotData):
        """Update a plot with type-safe data"""
        if plot_id in self.plot_containers:
            self.plot_containers[plot_id].update(data)
            if plot_id not in self.state.plot_data:
                self.state.plot_data[plot_id] = []
            self.state.plot_data[plot_id].append(data)

    def save_state(self) -> TabState:
        """Save the current tab state"""
        return self.state

    def load_state(self, state: TabState):
        """Load a tab state"""
        self.state = state
        # Recreate plots and update with saved data
        for plot_id, config in state.plot_configs.items():
            plot = self.create_plot(plot_id, config)
            if plot_id in state.plot_data:
                for data in state.plot_data[plot_id]:
                    plot.update(data)
