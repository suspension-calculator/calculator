# src/suspension/ui/components/plot_frame.py

import tkinter as tk
from suspension.ui.components.base.plot_container import PlotContainer
from suspension.ui.components.base.models import PlotConfig


class PlotFrame(tk.Frame):
    """Reusable container for plots"""

    def __init__(self, master, config: PlotConfig):
        self.plot = PlotContainer(self, config)
