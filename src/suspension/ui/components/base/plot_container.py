# src/suspension/ui/base/plot_container.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from typing import Optional
from .models import PlotConfig, PlotData, PlotStyle
from suspension.ui.styles import *


class PlotContainer:
    """
    Base class for managing individual plots with type-safe configuration and updates.
    """

    def __init__(self, parent, config: PlotConfig):
        self.parent = parent
        self.config = config
        self.figure = None
        self.canvas = None
        self.axes = None
        self.setup_plot()

    def setup_plot(self):
        """Initialize matplotlib figure and canvas with typed configuration"""
        self.figure, self.axes = plt.subplots(
            figsize=self.config.style.figsize, dpi=self.config.style.dpi
        )
        self.figure.set_facecolor(self.config.style.face_color)

        # Create canvas
        self.canvas = FigureCanvasTkAgg(self.figure, self.parent)

        # Configure axes
        self.configure_axes()

        # Apply plot-specific configuration
        if self.config.title:
            self.axes.set_title(self.config.title, color=self.config.style.text_color)
        if self.config.xlabel:
            self.axes.set_xlabel(self.config.xlabel, color=self.config.style.text_color)
        if self.config.ylabel:
            self.axes.set_ylabel(self.config.ylabel, color=self.config.style.text_color)

    def _configure_single_axes(self, ax):
        """Configure a single axes object with typed styling"""
        style = self.config.style
        ax.set_facecolor(style.face_color)
        ax.xaxis.label.set_color(style.text_color)
        ax.yaxis.label.set_color(style.text_color)
        ax.tick_params(axis="both", colors=style.text_color)
        for spine in ax.spines.values():
            spine.set_color(style.edge_color)

    def update(self, plot_data: PlotData):
        """Update the plot with type-safe plot data"""
        self.axes.plot(
            plot_data.x, plot_data.y, label=plot_data.label, **plot_data.style
        )
        if plot_data.label:
            self.axes.legend()
        self.draw()
