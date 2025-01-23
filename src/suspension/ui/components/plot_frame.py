# src/suspension/ui/components/plot_frame.py

from typing import Optional, Dict, Any
import tkinter as tk
from ..base.plot_container import PlotContainer
from ..base.models import PlotConfig


class PlotFrame(tk.Frame):
    """Reusable container for plots"""

    def __init__(self, master, config: PlotConfig):
        self.plot = PlotContainer(self, config)
