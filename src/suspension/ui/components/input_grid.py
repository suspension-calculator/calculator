# src/suspension/ui/components/input_grid.py
import tkinter as tk
from typing import Dict

from suspension.ui.components.base.models import InputField


class InputGrid(tk.Frame):
    def __init__(self, master, fields: Dict[str, InputField]):
        super().__init__(master)
        self.fields = fields
        self.entries: Dict[str, tk.Entry] = {}
        self.setup_grid()

    def setup_grid(self):
        """Create the grid of labels and entry fields"""
        for i, (field_name, field_config) in enumerate(self.fields.items()):
            # Create label
            label = tk.Label(self, text=field_config.label, justify=tk.RIGHT)
            label.grid(row=i, column=0, sticky="e", padx=5, pady=2)

            # Create entry
            entry = tk.Entry(self, width=field_config.width, justify=tk.CENTER)
            entry.insert(0, str(field_config.default))
            entry.grid(row=i, column=1, sticky="w", padx=5, pady=2)
            self.entries[field_name] = entry

            # Add unit label if specified
            if field_config.unit:
                unit_label = tk.Label(self, text=field_config.unit, justify=tk.LEFT)
                unit_label.grid(row=i, column=2, sticky="w", padx=5, pady=2)

    def get_values(self) -> Dict[str, float]:
        """Get all current values as a dictionary"""
        values = {}
        for field_name, entry in self.entries.items():
            try:
                value = float(entry.get())
                if self.fields[field_name].validator:
                    if self.fields[field_name].validator(value):
                        values[field_name] = value
                else:
                    values[field_name] = value
            except ValueError:
                values[field_name] = self.fields[field_name].default
        return values

    def set_values(self, values: Dict[str, float]):
        """Set values for all fields"""
        for field_name, value in values.items():
            if field_name in self.entries:
                self.entries[field_name].delete(0, tk.END)
                self.entries[field_name].insert(0, str(value))
