# src/suspension/ui/components/navigation.py
import tkinter as tk
from typing import List, Dict

from ..base.models import NavButtonConfig


class NavigationBar(tk.Frame):
    def __init__(self, master, buttons: List[NavButtonConfig]):
        super().__init__(master)
        self.buttons: Dict[str, tk.Button] = {}
        self.setup_buttons(buttons)

    def setup_buttons(self, buttons: List[NavButtonConfig]):
        """Create navigation buttons"""
        for i, btn_config in enumerate(buttons):
            button = tk.Button(
                self,
                text=btn_config.text,
                command=btn_config.command,
                width=btn_config.width,
                state="normal" if btn_config.enabled else "disabled",
            )
            button.grid(row=0, column=i, padx=5, pady=5)
            self.buttons[btn_config.text] = button

    def set_button_state(self, button_text: str, enabled: bool):
        """Enable or disable a button by its text"""
        if button_text in self.buttons:
            self.buttons[button_text].configure(
                state="normal" if enabled else "disabled"
            )
