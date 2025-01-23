# src/suspension/ui/components/link_input_panel.py
from typing import Protocol, Optional
import tkinter as tk
from ..base.models import InputField
from .input_grid import InputGrid
from ...core.models.link_models import LinkPosition, SuspensionConfig


class LinkInputPanel(tk.Frame):
    """Panel for link mounting point inputs"""

    def __init__(
        self, master, title: str, link_type: str, on_change: Optional[callable] = None
    ):
        super().__init__(master)
        self.title = title
        self.link_type = link_type
        self.on_change = on_change
        self._setup_ui()

    def _setup_ui(self):
        # Header
        header = tk.Label(self, text=self.title, font=("Arial", 20))
        header.grid(row=0, column=0, columnspan=3, sticky="ew", pady=(0, 10))

        # Create input fields
        fields = {
            f"{self.link_type}_frame_x": InputField(label="Frame X:", unit="mm"),
            f"{self.link_type}_frame_y": InputField(label="Frame Y:", unit="mm"),
            f"{self.link_type}_frame_z": InputField(label="Frame Z:", unit="mm"),
            f"{self.link_type}_axle_x": InputField(label="Axle X:", unit="mm"),
            f"{self.link_type}_axle_y": InputField(label="Axle Y:", unit="mm"),
            f"{self.link_type}_axle_z": InputField(label="Axle Z:", unit="mm"),
        }

        self.input_grid = InputGrid(self, fields)
        self.input_grid.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        if self.on_change:
            self.input_grid.bind_to_changes(self.on_change)

    def get_position(self) -> LinkPosition:
        """Get current link position from inputs"""
        values = self.input_grid.get_values()
        return LinkPosition(
            frame_x=values[f"{self.link_type}_frame_x"],
            frame_y=values[f"{self.link_type}_frame_y"],
            frame_z=values[f"{self.link_type}_frame_z"],
            axle_x=values[f"{self.link_type}_axle_x"],
            axle_y=values[f"{self.link_type}_axle_y"],
            axle_z=values[f"{self.link_type}_axle_z"],
        )

    def set_position(self, position: LinkPosition):
        """Set link position in inputs"""
        self.input_grid.set_values(
            {
                f"{self.link_type}_frame_x": position.frame_x,
                f"{self.link_type}_frame_y": position.frame_y,
                f"{self.link_type}_frame_z": position.frame_z,
                f"{self.link_type}_axle_x": position.axle_x,
                f"{self.link_type}_axle_y": position.axle_y,
                f"{self.link_type}_axle_z": position.axle_z,
            }
        )
