# src/suspension/ui/tabs_original/pitch.py

import tkinter as tk
from suspension.io.initialize_IO import *
from suspension.ui.styles import *
from suspension.io.save_suspension import save_susp, save_as_susp
from suspension.io.load_suspension import load_susp


class pitchPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.rowconfigure(2, weight=1)

        self.opening = True

        self.tk.call("tk", "scaling", self.winfo_screenwidth() / 2560)

        if True:  # Page Selection
            calc_page_sel = tk.Frame(self, background=bgColor)
            calc_page_sel.grid(row=0, column=0, columnspan=3, sticky="w", padx=10)

            label = tk.Label(
                calc_page_sel,
                text=calcVersion,
                font=(fontType, 20),
                background=bgColor,
                foreground=entryTextColor,
            )
            label.grid(row=0, column=0, padx=5)
            label.bind("<1>", lambda event: update_outputs())

            button1 = tk.Button(
                calc_page_sel,
                text="Save As",
                fg=pressedButtonColor,
                bg=buttonColor,
                command=lambda: save_as_susp(),
                height=1,
                width=7,
                font=(fontType, 13),
            )
            button1.grid(row=0, column=1, padx=5)

            button1 = tk.Button(
                calc_page_sel,
                text="Save",
                fg=pressedButtonColor,
                bg=buttonColor,
                command=lambda: save_susp(),
                height=1,
                width=4,
                font=(fontType, 13),
            )
            button1.grid(row=0, column=2, padx=5)

            button1 = tk.Button(
                calc_page_sel,
                text="Load",
                fg=pressedButtonColor,
                bg=buttonColor,
                command=lambda: load_from_file(),
                height=1,
                width=4,
                font=(fontType, 13),
            )
            button1.grid(row=0, column=3, padx=5)

            button2 = tk.Button(
                calc_page_sel,
                text="Settings",
                fg=pressedButtonColor,
                bg=buttonColor,
                command=lambda: master.switch_frame("settings"),
                height=1,
                width=8,
                font=(fontType, 13),
            )
            button2.grid(row=0, column=4, padx=5)

            button2 = tk.Button(
                calc_page_sel,
                text="About",
                fg=pressedButtonColor,
                bg=buttonColor,
                command=lambda: master.switch_frame("about"),
                height=1,
                width=8,
                font=(fontType, 13),
            )
            button2.grid(row=0, column=5, padx=5)

            button1 = tk.Button(
                calc_page_sel,
                text="Link Calculator",
                fg=pressedButtonColor,
                bg=buttonColor,
                command=lambda: master.switch_frame("linkCalc"),
                height=1,
                width=12,
                font=(fontType, 13),
            )
            button1.grid(row=0, column=6, padx=5)

            button2 = tk.Button(
                calc_page_sel,
                text="Link Sizing",
                fg=pressedButtonColor,
                bg=buttonColor,
                command=lambda: master.switch_frame("linkSizing"),
                height=1,
                width=12,
                font=(fontType, 13),
            )
            button2.grid(row=0, column=7, padx=5)

            button3 = tk.Button(
                calc_page_sel,
                text="Driveshafts",
                fg=pressedButtonColor,
                bg=buttonColor,
                command=lambda: master.switch_frame("driveshaft"),
                height=1,
                width=12,
                font=(fontType, 13),
            )
            button3.grid(row=0, column=8, padx=5)

            button4 = tk.Button(
                calc_page_sel,
                text="Shocks",
                fg=pressedButtonColor,
                bg=buttonColor,
                command=lambda: master.switch_frame("shocks"),
                height=1,
                width=12,
                font=(fontType, 13),
            )
            button4.grid(row=0, column=9, padx=5)

            button5 = tk.Button(
                calc_page_sel,
                text="Vehicle Pitch",
                fg=buttonColor,
                bg=pressedButtonColor,
                command=lambda: master.switch_frame("pitch"),
                height=1,
                width=12,
                font=(fontType, 13),
            )
            button5.grid(row=0, column=10, padx=5)

        if True:  # User Pitch
            if True:  # Set up inputs
                a = 1

            if True:  # Plot
                a = 1

            if True:  # Text
                a = 1

        if True:  # 50% Rear Pitch
            if True:  # Plot
                a = 1

            if True:  # Text
                a = 1

        if True:  # 50% Front Pitch
            if True:  # Plot
                a = 1

            if True:  # Text
                a = 1

        if True:  # 100% Rear Pitch
            if True:  # Plot
                a = 1

            if True:  # Text
                a = 1

        if True:  # 100% Front Pitch
            if True:  # Plot
                a = 1

            if True:  # Text
                a = 1

        if True:  # 100% Up Travel
            if True:  # Plot
                a = 1

            if True:  # Text
                a = 1

        if True:  # 100% Down Travel
            if True:  # Plot
                a = 1

            if True:  # Text
                a = 1

        if True:  # Pitch Predictions
            if True:  # Set up inputs
                a = 1
            if True:  # Outputs
                a = 1

        def update_outputs(*args):
            self.focus_set()
            plots_changed = False

            if self.opening:
                plots_changed = True
                self.opening = False
            else:  # Clear Plots
                a = 1

            if True:  # Get Inputs
                a = 1

            if plots_changed:
                if True:  # User Pitch
                    a = 1

                if True:  # Pitch Predictions
                    a = 1

        if True:  # Detect out of input click
            self.bind("<1>", lambda event: update_outputs())

        if True:  # Update with option menu change
            # F_U_solid.trace_add("write", update_outputs)
            a = 1

        update_outputs()

        def load_from_file():
            load_susp()
            master.switch_frame("Pitch")
