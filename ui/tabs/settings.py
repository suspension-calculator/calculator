# src/suspension/ui/tabs/settings.py

# IO Imports
from tool_io.variables import S
from tool_io.initialize_IO import *
from tool_io.IO_Conversion.convert_all_inputs import unit_change
from tool_io.IO_Conversion.x_direction_change import flip_front_x
from tool_io.save_suspension import save_susp, save_as_susp
from tool_io.load_suspension import load_susp

# UI Imports
from ui.styles import *

# Library Imports
import tkinter as tk

class settingsPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.rowconfigure(2, weight=1)

        self.opening = True

        self.tk.call(
            "tk",
            "scaling",
            min(
                self.winfo_screenwidth() / 2560,
                self.winfo_screenheight() / 1440,
            )
        )

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
                fg=buttonColor,
                bg=pressedButtonColor,
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
                fg=pressedButtonColor,
                bg=buttonColor,
                command=lambda: master.switch_frame("pitch"),
                height=1,
                width=12,
                font=(fontType, 13),
            )
            button5.grid(row=0, column=10, padx=5)

        if True:  # Settings Frame
            settings = tk.Frame(self, bg=bgColor)
            settings.grid(row=1, column=0)

            i_row = 0

            label = tk.Label(
                settings,
                text="Unit System:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            Unit = tk.StringVar()
            if S.units == "Imperial":
                default = "Imperial"
            else:
                default = "Metric"
            Unit.set(default)
            Unit_menu = tk.OptionMenu(settings, Unit, "Imperial", "Metric")
            Unit_menu.grid(row=i_row, column=1)
            Unit_menu.config(bg=textEntryColor)
            Unit_menu.config(fg=entryTextColor)
            Unit_menu.config(highlightthickness=0)
            Unit_menu.config(font=(fontType, 17))
            Unit_menu.nametowidget(Unit_menu.menuname).config(font=(fontType, 17))

            i_row = 1

            label = tk.Label(
                settings,
                text="Invert front X?",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            invert_front = tk.StringVar()
            if S.reversed_front_x == 1:
                default = "Yes"
            else:
                default = "No"
            invert_front.set(default)
            invert_front_menu = tk.OptionMenu(settings, invert_front, "Yes", "No")
            invert_front_menu.grid(row=i_row, column=1)
            invert_front_menu.config(bg=textEntryColor)
            invert_front_menu.config(fg=entryTextColor)
            invert_front_menu.config(highlightthickness=0)
            invert_front_menu.config(font=(fontType, 17))
            invert_front_menu.nametowidget(invert_front_menu.menuname).config(
                font=(fontType, 17)
            )

            i_row = 2

            label = tk.Label(
                settings,
                text="Model tire loading?",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            tire_loading = tk.StringVar()
            if S.simulate_tire_loading:
                default = "Yes"
            else:
                default = "No"
            tire_loading.set(default)
            tire_loading_menu = tk.OptionMenu(settings, tire_loading, "Yes", "No")
            tire_loading_menu.grid(row=i_row, column=1)
            tire_loading_menu.config(bg=textEntryColor)
            tire_loading_menu.config(fg=entryTextColor)
            tire_loading_menu.config(highlightthickness=0)
            tire_loading_menu.config(font=(fontType, 17))
            tire_loading_menu.nametowidget(tire_loading_menu.menuname).config(
                font=(fontType, 17)
            )

            i_row = 3

            label = tk.Label(
                settings,
                text="Sample points:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(S.sample_points)
            sample_points = tk.Entry(
                settings,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=4,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            sample_points.grid(row=i_row, column=1)
            sample_points.config(bg=textEntryColor)
            sample_points.config(fg=entryTextColor)
            sample_points.bind("<Return>", lambda event: update_outputs())

        def update_outputs(*args):
            self.focus_set()

            if Unit.get() == "Imperial" and S.units == "metric":
                S.units = "Imperial"
                unit_change()
            elif Unit.get() == "Metric" and S.units == "Imperial":
                S.units = "metric"
                unit_change()

            if invert_front.get() == "Yes" and S.reversed_front_x == False:
                S.reversed_front_x = True
                flip_front_x()
            elif invert_front.get() == "No" and S.reversed_front_x == True:
                S.reversed_front_x = False
                flip_front_x()

            if tire_loading.get() == "Yes" and S.simulate_tire_loading == False:
                S.simulate_tire_loading = True
            elif tire_loading.get() == "No" and S.simulate_tire_loading == True:
                S.simulate_tire_loading = False

            if S.sample_points != float(sample_points.get()):
                S.sample_points = round(float(sample_points.get()))
                if S.sample_points < 1:
                    S.sample_points = 1

        if True:  # Detect out of input click
            self.bind("<1>", lambda event: update_outputs())

        if True:  # Update with option menu change
            Unit.trace_add("write", update_outputs)
            invert_front.trace_add("write", update_outputs)
            tire_loading.trace_add("write", update_outputs)

        update_outputs()

        def load_from_file():
            load_susp()
            master.switch_frame("settings")
