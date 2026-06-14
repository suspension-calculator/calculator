# src/suspension/ui/app.py
import tkinter as tk
import matplotlib.pyplot as plt
from ui.styles import *  # Using the new styles module instead of visual_scheme


class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame("linkCalc")

        self.configure(bg=buttonColor)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.title(calcVersion)
        self.geometry("%dx%d" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        self.state("zoomed")

    def switch_frame(self, page_name):
        from main import tabs  # Import here to avoid circular import

        cls = tabs[page_name]
        plt.close("all")
        new_frame = cls(master=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0, column=0, sticky="nsew")
        self._frame.config(bg=bgColor)
