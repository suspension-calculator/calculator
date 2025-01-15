# src/suspension/ui/tabs/driveshaft.py

# IO Imports
from tool_io.variables import S, x, y, z
from tool_io.initialize_IO import *
from tool_io.save_suspension import save_susp, save_as_susp
from tool_io.load_suspension import load_susp

# Core Imports
from core.calculations.driveshaft import run_driveshaft

# UI Imports
from ui.styles import *

# Library Imports
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class driveshaftPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.config(background=bgColor)
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        # self.rowconfigure(2,weight=1)

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
                fg=buttonColor,
                bg=pressedButtonColor,
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

        frontFrame = tk.Frame(self, bg=bgColor)
        frontFrame.grid(row=2, column=1, sticky="nse")
        frontFrame.rowconfigure([0, 1], weight=1)
        # frontFrame.columnconfigure([0,1],weight=1)
        rearFrame = tk.Frame(self, bg=bgColor)
        rearFrame.grid(row=2, column=0, sticky="nsw")
        rearFrame.rowconfigure([0, 1], weight=1)
        # rearFrame.columnconfigure([0,1],weight=1)

        if True:  # Plot Area Setup
            self.figF_pinion, self.axF_Pinion_Angle = plt.subplots(1, 1)
            self.figF_pinion.subplots_adjust(bottom=0.12)
            self.figF_pinion.set_facecolor(bgColor)

            self.figF_T_Case_Joint, self.axF_T_Case_Joint = plt.subplots(1, 1)
            self.figF_T_Case_Joint.subplots_adjust(bottom=0.12)
            self.figF_T_Case_Joint.set_facecolor(bgColor)

            self.figF_Pinion_Joint, self.axF_Pinion_Joint = plt.subplots(1, 1)
            self.figF_Pinion_Joint.subplots_adjust(bottom=0.12)
            self.figF_Pinion_Joint.set_facecolor(bgColor)

            self.figR_pinion, self.axR_Pinion_Angle = plt.subplots(1, 1)
            self.figR_pinion.subplots_adjust(bottom=0.12)
            self.figR_pinion.set_facecolor(bgColor)

            self.figR_T_Case_Joint, self.axR_T_Case_Joint = plt.subplots(1, 1)
            self.figR_T_Case_Joint.subplots_adjust(bottom=0.12)
            self.figR_T_Case_Joint.set_facecolor(bgColor)

            self.figR_Pinion_Joint, self.axR_Pinion_Joint = plt.subplots(1, 1)
            self.figR_Pinion_Joint.subplots_adjust(bottom=0.12)
            self.figR_Pinion_Joint.set_facecolor(bgColor)

            self.F_Pinion_Angle = FigureCanvasTkAgg(self.figF_pinion, frontFrame)
            self.F_Pinion_Angle.get_tk_widget().grid(row=0, column=1, sticky="nesw")
            self.F_T_Case_Joint = FigureCanvasTkAgg(self.figF_T_Case_Joint, frontFrame)
            self.F_T_Case_Joint.get_tk_widget().grid(row=1, column=0, sticky="nesw")
            self.F_Pinion_Joint = FigureCanvasTkAgg(self.figF_Pinion_Joint, frontFrame)
            self.F_Pinion_Joint.get_tk_widget().grid(row=1, column=1, sticky="nesw")

            self.R_Pinion_Angle = FigureCanvasTkAgg(self.figR_pinion, rearFrame)
            self.R_Pinion_Angle.get_tk_widget().grid(row=0, column=0, sticky="nesw")
            self.R_T_Case_Joint = FigureCanvasTkAgg(self.figR_T_Case_Joint, rearFrame)
            self.R_T_Case_Joint.get_tk_widget().grid(row=1, column=0, sticky="nesw")
            self.R_Pinion_Joint = FigureCanvasTkAgg(self.figR_Pinion_Joint, rearFrame)
            self.R_Pinion_Joint.get_tk_widget().grid(row=1, column=1, sticky="nesw")

        if True:  # Front Inputs
            label = tk.Label(
                self,
                text="Front",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 30),
                justify=tk.CENTER,
            )
            label.grid(row=1, column=1, pady=1)
            label.bind("<1>", lambda event: update_outputs())

            front_text = tk.Frame(frontFrame, bg=bgColor)
            front_text.grid(row=0, column=0)

            i_row = 1

            label = tk.Label(
                front_text,
                text="Pinion Location Method:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            F_method = tk.StringVar()
            if inputs.F.pinion_location_method == 1:
                default = "XYZ"
            else:
                default = "Hypoid and Length"
            F_method.set(default)
            F_method_menu = tk.OptionMenu(
                front_text, F_method, "XYZ", "Hypoid and Length"
            )
            F_method_menu.grid(row=i_row, column=2, columnspan=2)
            F_method_menu.config(bg=textEntryColor)
            F_method_menu.config(fg=entryTextColor)
            F_method_menu.config(width=17)
            F_method_menu.config(highlightthickness=0)
            F_method_menu.config(font=(fontType, 17))
            F_method_menu.nametowidget(F_method_menu.menuname).config(
                font=(fontType, 17)
            )

            i_row = 2

            label = tk.Label(
                front_text,
                text="X",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=6,
            )
            label.grid(row=i_row, column=1, sticky="nesw")
            label.bind("<1>", lambda event: update_outputs())

            label = tk.Label(
                front_text,
                text="Y",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=6,
            )
            label.grid(row=i_row, column=2, sticky="nesw")
            label.bind("<1>", lambda event: update_outputs())

            label = tk.Label(
                front_text,
                text="Z",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=6,
            )
            label.grid(row=i_row, column=3, sticky="nesw")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 3

            label = tk.Label(
                front_text,
                text="Transfer Case Yoke:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.T_case[x])
            F_TC_x = tk.Entry(
                front_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            F_TC_x.grid(row=i_row, column=1)
            F_TC_x.config(bg=textEntryColor)
            F_TC_x.config(fg=entryTextColor)
            F_TC_x.bind("<Return>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.T_case[y])
            F_TC_y = tk.Entry(
                front_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            F_TC_y.grid(row=i_row, column=2)
            F_TC_y.config(bg=textEntryColor)
            F_TC_y.config(fg=entryTextColor)
            F_TC_y.bind("<Return>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.T_case[z])
            F_TC_z = tk.Entry(
                front_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            F_TC_z.grid(row=i_row, column=3)
            F_TC_z.config(bg=textEntryColor)
            F_TC_z.config(fg=entryTextColor)
            F_TC_z.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                front_text,
                text="{}".format(S.position_units),
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=4, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 4

            label = tk.Label(
                front_text,
                text="Pinion Yoke:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.pinion[x])
            F_pinion_x = tk.Entry(
                front_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            F_pinion_x.grid(row=i_row, column=1)
            F_pinion_x.config(bg=textEntryColor)
            F_pinion_x.config(fg=entryTextColor)
            F_pinion_x.bind("<Return>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.pinion[y])
            F_pinion_y = tk.Entry(
                front_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            F_pinion_y.grid(row=i_row, column=2)
            F_pinion_y.config(bg=textEntryColor)
            F_pinion_y.config(fg=entryTextColor)
            F_pinion_y.bind("<Return>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.pinion[z])
            F_pinion_z = tk.Entry(
                front_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            F_pinion_z.grid(row=i_row, column=3)
            F_pinion_z.config(bg=textEntryColor)
            F_pinion_z.config(fg=entryTextColor)
            F_pinion_z.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                front_text,
                text="{}".format(S.position_units),
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=4, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 5

            label = tk.Label(
                front_text,
                text="Hypoid Offset:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.pinion_hypoid)
            F_hypoid = tk.Entry(
                front_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            F_hypoid.grid(row=i_row, column=2)
            F_hypoid.config(bg=textEntryColor)
            F_hypoid.config(fg=entryTextColor)
            F_hypoid.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                front_text,
                text="{}".format(S.position_units),
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=3, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 6

            label = tk.Label(
                front_text,
                text="Pinion Length:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.pinion_length)
            F_length = tk.Entry(
                front_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            F_length.grid(row=i_row, column=2)
            F_length.config(bg=textEntryColor)
            F_length.config(fg=entryTextColor)
            F_length.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                front_text,
                text="{}".format(S.position_units),
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=3, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 7

            label = tk.Label(
                front_text,
                text="Side View Transer Case Angle:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.T_case_side_angle)
            F_SV_TC = tk.Entry(
                front_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            F_SV_TC.grid(row=i_row, column=2)
            F_SV_TC.config(bg=textEntryColor)
            F_SV_TC.config(fg=entryTextColor)
            F_SV_TC.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                front_text,
                text="\u00b0",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=3, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 8

            label = tk.Label(
                front_text,
                text="Top View Transfer Case Angle:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.T_case_top_angle)
            F_TV_TC = tk.Entry(
                front_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            F_TV_TC.grid(row=i_row, column=2)
            F_TV_TC.config(bg=textEntryColor)
            F_TV_TC.config(fg=entryTextColor)
            F_TV_TC.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                front_text,
                text="\u00b0",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=3, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 9

            label = tk.Label(
                front_text,
                text="Pinion Angle:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.pinion_angle)
            F_pinion_angle = tk.Entry(
                front_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            F_pinion_angle.grid(row=i_row, column=2)
            F_pinion_angle.config(bg=textEntryColor)
            F_pinion_angle.config(fg=entryTextColor)
            F_pinion_angle.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                front_text,
                text="\u00b0",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=3, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 10

            label = tk.Label(
                front_text,
                text="a",
                background=bgColor,
                foreground=bgColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            if inputs.F.pinion_location_method == 1:
                F_pinion_x.config(fg=entryTextColor)
                F_pinion_z.config(fg=entryTextColor)
                F_hypoid.config(fg=bgColor)
                F_length.config(fg=bgColor)
            else:
                F_pinion_x.config(fg=bgColor)
                F_pinion_z.config(fg=bgColor)
                F_hypoid.config(fg=entryTextColor)
                F_length.config(fg=entryTextColor)

        if True:  # Front Outputs
            i_row = 11

            label = tk.Label(
                front_text,
                text="Maximum Length:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            label_F_max_length = tk.Label(
                front_text,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label_F_max_length.grid(row=i_row, column=2, columnspan=2, sticky="w")
            label_F_max_length.bind("<1>", lambda event: update_outputs())

            i_row = 12

            label = tk.Label(
                front_text,
                text="Ride Length:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            label_F_ride_length = tk.Label(
                front_text,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label_F_ride_length.grid(row=i_row, column=2, columnspan=2, sticky="w")
            label_F_ride_length.bind("<1>", lambda event: update_outputs())

            i_row = 13

            label = tk.Label(
                front_text,
                text="Minimum Length:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            label_F_min_length = tk.Label(
                front_text,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label_F_min_length.grid(row=i_row, column=2, columnspan=2, sticky="w")
            label_F_min_length.bind("<1>", lambda event: update_outputs())

            i_row = 14

            label = tk.Label(
                front_text,
                text="Driveshaft Travel:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            label_F_travel = tk.Label(
                front_text,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label_F_travel.grid(row=i_row, column=2, columnspan=2, sticky="w")
            label_F_travel.bind("<1>", lambda event: update_outputs())

        if True:  # Rear Inputs
            label = tk.Label(
                self,
                text="Rear",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 30),
                justify=tk.CENTER,
            )
            label.grid(row=1, column=0, pady=1)
            label.bind("<1>", lambda event: update_outputs())

            rear_text = tk.Frame(rearFrame, bg=bgColor)
            rear_text.grid(row=0, column=1)

            i_row = 1

            label = tk.Label(
                rear_text,
                text="Pinion Location Method:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            R_method = tk.StringVar()
            if inputs.R.pinion_location_method == 1:
                default = "XYZ"
            else:
                default = "Hypoid and Length"
            R_method.set(default)
            R_method_menu = tk.OptionMenu(
                rear_text, R_method, "XYZ", "Hypoid and Length"
            )
            R_method_menu.grid(row=i_row, column=2, columnspan=2)
            R_method_menu.config(bg=textEntryColor)
            R_method_menu.config(fg=entryTextColor)
            R_method_menu.config(width=17)
            R_method_menu.config(highlightthickness=0)
            R_method_menu.config(font=(fontType, 17))
            R_method_menu.nametowidget(R_method_menu.menuname).config(
                font=(fontType, 17)
            )

            i_row = 2

            label = tk.Label(
                rear_text,
                text="X",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=6,
            )
            label.grid(row=i_row, column=1, sticky="nesw")
            label.bind("<1>", lambda event: update_outputs())

            label = tk.Label(
                rear_text,
                text="Y",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=6,
            )
            label.grid(row=i_row, column=2, sticky="nesw")
            label.bind("<1>", lambda event: update_outputs())

            label = tk.Label(
                rear_text,
                text="Z",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=6,
            )
            label.grid(row=i_row, column=3, sticky="nesw")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 3

            label = tk.Label(
                rear_text,
                text="Transfer Case Yoke:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.R.T_case[x])
            R_TC_x = tk.Entry(
                rear_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            R_TC_x.grid(row=i_row, column=1)
            R_TC_x.config(bg=textEntryColor)
            R_TC_x.config(fg=entryTextColor)
            R_TC_x.bind("<Return>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.R.T_case[y])
            R_TC_y = tk.Entry(
                rear_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            R_TC_y.grid(row=i_row, column=2)
            R_TC_y.config(bg=textEntryColor)
            R_TC_y.config(fg=entryTextColor)
            R_TC_y.bind("<Return>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.R.T_case[z])
            R_TC_z = tk.Entry(
                rear_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            R_TC_z.grid(row=i_row, column=3)
            R_TC_z.config(bg=textEntryColor)
            R_TC_z.config(fg=entryTextColor)
            R_TC_z.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                rear_text,
                text="{}".format(S.position_units),
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=4, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 4

            label = tk.Label(
                rear_text,
                text="Pinion Yoke:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.R.pinion[x])
            R_pinion_x = tk.Entry(
                rear_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            R_pinion_x.grid(row=i_row, column=1)
            R_pinion_x.config(bg=textEntryColor)
            R_pinion_x.config(fg=entryTextColor)
            R_pinion_x.bind("<Return>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.R.pinion[y])
            R_pinion_y = tk.Entry(
                rear_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            R_pinion_y.grid(row=i_row, column=2)
            R_pinion_y.config(bg=textEntryColor)
            R_pinion_y.config(fg=entryTextColor)
            R_pinion_y.bind("<Return>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.R.pinion[z])
            R_pinion_z = tk.Entry(
                rear_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            R_pinion_z.grid(row=i_row, column=3)
            R_pinion_z.config(bg=textEntryColor)
            R_pinion_z.config(fg=entryTextColor)
            R_pinion_z.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                rear_text,
                text="{}".format(S.position_units),
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=4, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 5

            label = tk.Label(
                rear_text,
                text="Hypoid Offset:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.R.pinion_hypoid)
            R_hypoid = tk.Entry(
                rear_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            R_hypoid.grid(row=i_row, column=2)
            R_hypoid.config(bg=textEntryColor)
            R_hypoid.config(fg=entryTextColor)
            R_hypoid.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                rear_text,
                text="{}".format(S.position_units),
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=3, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 6

            label = tk.Label(
                rear_text,
                text="Pinion Length:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.R.pinion_length)
            R_length = tk.Entry(
                rear_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            R_length.grid(row=i_row, column=2)
            R_length.config(bg=textEntryColor)
            R_length.config(fg=entryTextColor)
            R_length.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                rear_text,
                text="{}".format(S.position_units),
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=3, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 7

            label = tk.Label(
                rear_text,
                text="Side View Transer Case Angle:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.R.T_case_side_angle)
            R_SV_TC = tk.Entry(
                rear_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            R_SV_TC.grid(row=i_row, column=2)
            R_SV_TC.config(bg=textEntryColor)
            R_SV_TC.config(fg=entryTextColor)
            R_SV_TC.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                rear_text,
                text="\u00b0",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=3, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 8

            label = tk.Label(
                rear_text,
                text="Top View Transfer Case Angle:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.R.T_case_top_angle)
            R_TV_TC = tk.Entry(
                rear_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            R_TV_TC.grid(row=i_row, column=2)
            R_TV_TC.config(bg=textEntryColor)
            R_TV_TC.config(fg=entryTextColor)
            R_TV_TC.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                rear_text,
                text="\u00b0",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=3, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 9

            label = tk.Label(
                rear_text,
                text="Pinion Angle:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.R.pinion_angle)
            R_pinion_angle = tk.Entry(
                rear_text,
                font=(fontType, 17),
                justify=tk.CENTER,
                width=10,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            R_pinion_angle.grid(row=i_row, column=2)
            R_pinion_angle.config(bg=textEntryColor)
            R_pinion_angle.config(fg=entryTextColor)
            R_pinion_angle.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                rear_text,
                text="\u00b0",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=3, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 10

            label = tk.Label(
                rear_text,
                text="a",
                background=bgColor,
                foreground=bgColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            if inputs.R.pinion_location_method == 1:
                R_pinion_x.config(fg=entryTextColor)
                R_pinion_z.config(fg=entryTextColor)
                R_hypoid.config(fg=bgColor)
                R_length.config(fg=bgColor)
            else:
                R_pinion_x.config(fg=bgColor)
                R_pinion_z.config(fg=bgColor)
                R_hypoid.config(fg=entryTextColor)
                R_length.config(fg=entryTextColor)

        if True:  # Rear Outputs
            i_row = 11

            label = tk.Label(
                rear_text,
                text="Maximum Length:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            label_R_max_length = tk.Label(
                rear_text,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label_R_max_length.grid(row=i_row, column=2, columnspan=2, sticky="w")
            label_R_max_length.bind("<1>", lambda event: update_outputs())

            i_row = 12

            label = tk.Label(
                rear_text,
                text="Ride Length:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            label_R_ride_length = tk.Label(
                rear_text,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label_R_ride_length.grid(row=i_row, column=2, columnspan=2, sticky="w")
            label_R_ride_length.bind("<1>", lambda event: update_outputs())

            i_row = 13

            label = tk.Label(
                rear_text,
                text="Minimum Length:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            label_R_min_length = tk.Label(
                rear_text,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label_R_min_length.grid(row=i_row, column=2, columnspan=2, sticky="w")
            label_R_min_length.bind("<1>", lambda event: update_outputs())

            i_row = 14

            label = tk.Label(
                rear_text,
                text="Driveshaft Travel:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, columnspan=2, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            label_R_travel = tk.Label(
                rear_text,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 17),
                justify=tk.RIGHT,
            )
            label_R_travel.grid(row=i_row, column=2, columnspan=2, sticky="w")
            label_R_travel.bind("<1>", lambda event: update_outputs())

        def update_outputs(*args):
            self.focus_set()
            plots_changed = False

            if self.opening:
                plots_changed = True
                self.opening = False
            else:  # Clear Plots
                self.axF_Pinion_Angle.clear()
                self.axF_T_Case_Joint.clear()
                self.axF_Pinion_Joint.clear()

                self.axR_Pinion_Angle.clear()
                self.axR_T_Case_Joint.clear()
                self.axR_Pinion_Joint.clear()

                linkLine = 3.5
                dottedLine = 2.5
                travelLine = 2.5
                markerSize = 7

            if True:  # Get Front Inputs
                if F_method.get() == "XYZ" and inputs.F.pinion_location_method == 0:
                    inputs.F.pinion_location_method = 1
                    plots_changed = True
                    F_pinion_x.config(fg=entryTextColor)
                    F_pinion_z.config(fg=entryTextColor)
                    F_hypoid.config(fg=bgColor)
                    F_length.config(fg=bgColor)
                    inputs.F.pinion[x] = float(F_pinion_x.get())
                    inputs.F.pinion[z] = float(F_pinion_z.get())
                elif (
                    F_method.get() == "Hypoid and Length"
                    and inputs.F.pinion_location_method == 1
                ):
                    inputs.F.pinion_location_method = 0
                    plots_changed = True
                    F_pinion_x.config(fg=bgColor)
                    F_pinion_z.config(fg=bgColor)
                    F_hypoid.config(fg=entryTextColor)
                    F_length.config(fg=entryTextColor)
                    inputs.F.pinion_hypoid = float(F_hypoid.get())
                    inputs.F.pinion_length = float(F_length.get())

                if inputs.F.T_case[x] != float(F_TC_x.get()):
                    inputs.F.T_case[x] = float(F_TC_x.get())
                    plots_changed = True
                if inputs.F.T_case[y] != float(F_TC_y.get()):
                    inputs.F.T_case[y] = float(F_TC_y.get())
                    plots_changed = True
                if inputs.F.T_case[z] != float(F_TC_z.get()):
                    inputs.F.T_case[z] = float(F_TC_z.get())
                    plots_changed = True
                if inputs.F.pinion[x] != float(F_pinion_x.get()):
                    inputs.F.pinion[x] = float(F_pinion_x.get())
                    plots_changed = True
                if inputs.F.pinion[y] != float(F_pinion_y.get()):
                    inputs.F.pinion[y] = float(F_pinion_y.get())
                    plots_changed = True
                if inputs.F.pinion[z] != float(F_pinion_z.get()):
                    inputs.F.pinion[z] = float(F_pinion_z.get())
                    plots_changed = True
                if inputs.F.pinion_hypoid != float(F_hypoid.get()):
                    inputs.F.pinion_hypoid = float(F_hypoid.get())
                    plots_changed = True
                if inputs.F.pinion_length != float(F_length.get()):
                    inputs.F.pinion_length = float(F_length.get())
                    plots_changed = True
                if inputs.F.T_case_side_angle != float(F_SV_TC.get()):
                    inputs.F.T_case_side_angle = float(F_SV_TC.get())
                    plots_changed = True
                if inputs.F.T_case_top_angle != float(F_TV_TC.get()):
                    inputs.F.T_case_top_angle = float(F_TV_TC.get())
                    plots_changed = True
                if inputs.F.pinion_angle != float(F_pinion_angle.get()):
                    inputs.F.pinion_angle = float(F_pinion_angle.get())
                    plots_changed = True

            if True:  # Get Rear Inputs
                if R_method.get() == "XYZ" and inputs.R.pinion_location_method == 0:
                    inputs.R.pinion_location_method = 1
                    plots_changed = True
                    R_pinion_x.config(fg=entryTextColor)
                    R_pinion_z.config(fg=entryTextColor)
                    R_hypoid.config(fg=bgColor)
                    R_length.config(fg=bgColor)
                    inputs.R.pinion[x] = float(R_pinion_x.get())
                    inputs.R.pinion[z] = float(R_pinion_z.get())
                elif (
                    R_method.get() == "Hypoid and Length"
                    and inputs.R.pinion_location_method == 1
                ):
                    inputs.R.pinion_location_method = 0
                    plots_changed = True
                    R_pinion_x.config(fg=bgColor)
                    R_pinion_z.config(fg=bgColor)
                    R_hypoid.config(fg=entryTextColor)
                    R_length.config(fg=entryTextColor)
                    inputs.R.pinion_hypoid = float(R_hypoid.get())
                    inputs.R.pinion_length = float(R_length.get())

                if inputs.R.T_case[x] != float(R_TC_x.get()):
                    inputs.R.T_case[x] = float(R_TC_x.get())
                    plots_changed = True
                if inputs.R.T_case[y] != float(R_TC_y.get()):
                    inputs.R.T_case[y] = float(R_TC_y.get())
                    plots_changed = True
                if inputs.R.T_case[z] != float(R_TC_z.get()):
                    inputs.R.T_case[z] = float(R_TC_z.get())
                    plots_changed = True
                if inputs.R.pinion[x] != float(R_pinion_x.get()):
                    inputs.R.pinion[x] = float(R_pinion_x.get())
                    plots_changed = True
                if inputs.R.pinion[y] != float(R_pinion_y.get()):
                    inputs.R.pinion[y] = float(R_pinion_y.get())
                    plots_changed = True
                if inputs.R.pinion[z] != float(R_pinion_z.get()):
                    inputs.R.pinion[z] = float(R_pinion_z.get())
                    plots_changed = True
                if inputs.R.pinion_hypoid != float(R_hypoid.get()):
                    inputs.R.pinion_hypoid = float(R_hypoid.get())
                    plots_changed = True
                if inputs.R.pinion_length != float(R_length.get()):
                    inputs.R.pinion_length = float(R_length.get())
                    plots_changed = True
                if inputs.R.T_case_side_angle != float(R_SV_TC.get()):
                    inputs.R.T_case_side_angle = float(R_SV_TC.get())
                    plots_changed = True
                if inputs.R.T_case_top_angle != float(R_TV_TC.get()):
                    inputs.R.T_case_top_angle = float(R_TV_TC.get())
                    plots_changed = True
                if inputs.R.pinion_angle != float(R_pinion_angle.get()):
                    inputs.R.pinion_angle = float(R_pinion_angle.get())
                    plots_changed = True

            if plots_changed:
                run_driveshaft()

                if True:  # Update Front
                    if True:  # Update Front Plots
                        self.axF_Pinion_Angle.plot(
                            -outputs.F.Pinion_Change + inputs.F.pinion_angle,
                            outputs.F.Travel,
                            color=plotMainColor,
                        )
                        self.axF_Pinion_Angle.set_xlabel(
                            "Pinion Angle [\u00b0] Positive is up"
                        )
                        self.axF_Pinion_Angle.set_ylabel(
                            "Travel [{}]".format(S.position_units)
                        )
                        self.axF_Pinion_Angle.grid(linewidth=0.5, color=bgColor)
                        self.axF_Pinion_Angle.set_facecolor(textEntryColor)
                        self.axF_Pinion_Angle.xaxis.label.set_color(entryTextColor)
                        self.axF_Pinion_Angle.yaxis.label.set_color(entryTextColor)
                        self.axF_Pinion_Angle.spines[
                            ["top", "bottom", "left", "right"]
                        ].set_color(entryTextColor)
                        self.axF_Pinion_Angle.tick_params(
                            axis="x", colors=entryTextColor
                        )
                        self.axF_Pinion_Angle.tick_params(
                            axis="y", colors=entryTextColor
                        )
                        self.axF_Pinion_Angle.text(
                            -outputs.F.Pinion_Change[0] + inputs.F.pinion_angle,
                            outputs.F.Travel[0],
                            "{:.1f}".format(
                                -outputs.F.Pinion_Change[0] + inputs.F.pinion_angle
                            ),
                            color=plotMainColor,
                        )
                        self.axF_Pinion_Angle.text(
                            -outputs.F.Pinion_Change[S.sample_points]
                            + inputs.F.pinion_angle,
                            outputs.F.Travel[S.sample_points],
                            "{:.1f}".format(
                                -outputs.F.Pinion_Change[S.sample_points]
                                + inputs.F.pinion_angle
                            ),
                            color=plotMainColor,
                        )
                        self.axF_Pinion_Angle.text(
                            -outputs.F.Pinion_Change[S.sample_points * 2]
                            + inputs.F.pinion_angle,
                            outputs.F.Travel[S.sample_points * 2],
                            "{:.1f}".format(
                                -outputs.F.Pinion_Change[S.sample_points * 2]
                                + inputs.F.pinion_angle
                            ),
                            color=plotMainColor,
                        )

                        self.axF_T_Case_Joint.plot(
                            outputs.F.T_Case_U_Joint,
                            outputs.F.Travel,
                            color=plotSecondaryColor,
                        )
                        self.axF_T_Case_Joint.set_xlabel(
                            "Transfer Case U-joint Angle [\u00b0]"
                        )
                        self.axF_T_Case_Joint.set_ylabel(
                            "Travel [{}]".format(S.position_units)
                        )
                        self.axF_T_Case_Joint.grid(linewidth=0.5, color=bgColor)
                        self.axF_T_Case_Joint.set_facecolor(textEntryColor)
                        self.axF_T_Case_Joint.xaxis.label.set_color(entryTextColor)
                        self.axF_T_Case_Joint.yaxis.label.set_color(entryTextColor)
                        self.axF_T_Case_Joint.spines[
                            ["top", "bottom", "left", "right"]
                        ].set_color(entryTextColor)
                        self.axF_T_Case_Joint.tick_params(
                            axis="x", colors=entryTextColor
                        )
                        self.axF_T_Case_Joint.tick_params(
                            axis="y", colors=entryTextColor
                        )
                        self.axF_T_Case_Joint.text(
                            outputs.F.T_Case_U_Joint[0],
                            outputs.F.Travel[0],
                            "{:.1f}".format(outputs.F.T_Case_U_Joint[0]),
                            color=plotSecondaryColor,
                        )
                        self.axF_T_Case_Joint.text(
                            outputs.F.T_Case_U_Joint[S.sample_points],
                            outputs.F.Travel[S.sample_points],
                            "{:.1f}".format(outputs.F.T_Case_U_Joint[S.sample_points]),
                            color=plotSecondaryColor,
                        )
                        self.axF_T_Case_Joint.text(
                            outputs.F.T_Case_U_Joint[S.sample_points * 2],
                            outputs.F.Travel[S.sample_points * 2],
                            "{:.1f}".format(
                                outputs.F.T_Case_U_Joint[S.sample_points * 2]
                            ),
                            color=plotSecondaryColor,
                        )

                        self.axF_Pinion_Joint.plot(
                            outputs.F.Pinion_U_Joint,
                            outputs.F.Travel,
                            color=plotMainColor,
                        )
                        self.axF_Pinion_Joint.set_xlabel(
                            "Pinion U-joint Angle [\u00b0]"
                        )
                        self.axF_Pinion_Joint.set_ylabel(
                            "Travel [{}]".format(S.position_units)
                        )
                        self.axF_Pinion_Joint.grid(linewidth=0.5, color=bgColor)
                        self.axF_Pinion_Joint.set_facecolor(textEntryColor)
                        self.axF_Pinion_Joint.xaxis.label.set_color(entryTextColor)
                        self.axF_Pinion_Joint.yaxis.label.set_color(entryTextColor)
                        self.axF_Pinion_Joint.spines[
                            ["top", "bottom", "left", "right"]
                        ].set_color(entryTextColor)
                        self.axF_Pinion_Joint.tick_params(
                            axis="x", colors=entryTextColor
                        )
                        self.axF_Pinion_Joint.tick_params(
                            axis="y", colors=entryTextColor
                        )
                        self.axF_Pinion_Joint.text(
                            outputs.F.Pinion_U_Joint[0],
                            outputs.F.Travel[0],
                            "{:.1f}".format(outputs.F.Pinion_U_Joint[0]),
                            color=plotMainColor,
                        )
                        self.axF_Pinion_Joint.text(
                            outputs.F.Pinion_U_Joint[S.sample_points],
                            outputs.F.Travel[S.sample_points],
                            "{:.1f}".format(outputs.F.Pinion_U_Joint[S.sample_points]),
                            color=plotMainColor,
                        )
                        self.axF_Pinion_Joint.text(
                            outputs.F.Pinion_U_Joint[S.sample_points * 2],
                            outputs.F.Travel[S.sample_points * 2],
                            "{:.1f}".format(
                                outputs.F.Pinion_U_Joint[S.sample_points * 2]
                            ),
                            color=plotMainColor,
                        )

                    if True:  # Update Front Text
                        label_F_max_length.config(
                            text="{:.1f} {}".format(
                                outputs.F.Max_Length, S.position_units
                            )
                        )
                        label_F_ride_length.config(
                            text="{:.1f} {}".format(
                                outputs.F.Ride_Length, S.position_units
                            )
                        )
                        label_F_min_length.config(
                            text="{:.1f} {}".format(
                                outputs.F.Min_Length, S.position_units
                            )
                        )
                        label_F_travel.config(
                            text="{:.1f} {}".format(
                                outputs.F.Driveshaft_Travel, S.position_units
                            )
                        )

                if True:  # Update Rear
                    if True:  # Update Rear Plots
                        self.axR_Pinion_Angle.plot(
                            outputs.R.Pinion_Change + inputs.R.pinion_angle,
                            outputs.R.Travel,
                            color=plotMainColor,
                        )
                        self.axR_Pinion_Angle.set_xlabel(
                            "Pinion Angle [\u00b0] Positive is up"
                        )
                        self.axR_Pinion_Angle.set_ylabel(
                            "Travel [{}]".format(S.position_units)
                        )
                        self.axR_Pinion_Angle.grid(linewidth=0.5, color=bgColor)
                        self.axR_Pinion_Angle.set_facecolor(textEntryColor)
                        self.axR_Pinion_Angle.xaxis.label.set_color(entryTextColor)
                        self.axR_Pinion_Angle.yaxis.label.set_color(entryTextColor)
                        self.axR_Pinion_Angle.spines[
                            ["top", "bottom", "left", "right"]
                        ].set_color(entryTextColor)
                        self.axR_Pinion_Angle.tick_params(
                            axis="x", colors=entryTextColor
                        )
                        self.axR_Pinion_Angle.tick_params(
                            axis="y", colors=entryTextColor
                        )
                        self.axR_Pinion_Angle.text(
                            outputs.R.Pinion_Change[0] + inputs.R.pinion_angle,
                            outputs.R.Travel[0],
                            "{:.1f}".format(
                                -outputs.R.Pinion_Change[0] + inputs.R.pinion_angle
                            ),
                            color=plotMainColor,
                        )
                        self.axR_Pinion_Angle.text(
                            outputs.R.Pinion_Change[S.sample_points]
                            + inputs.R.pinion_angle,
                            outputs.R.Travel[S.sample_points],
                            "{:.1f}".format(
                                -outputs.R.Pinion_Change[S.sample_points]
                                + inputs.R.pinion_angle
                            ),
                            color=plotMainColor,
                        )
                        self.axR_Pinion_Angle.text(
                            outputs.R.Pinion_Change[S.sample_points * 2]
                            + inputs.R.pinion_angle,
                            outputs.R.Travel[S.sample_points * 2],
                            "{:.1f}".format(
                                -outputs.R.Pinion_Change[S.sample_points * 2]
                                + inputs.R.pinion_angle
                            ),
                            color=plotMainColor,
                        )

                        self.axR_T_Case_Joint.plot(
                            outputs.R.T_Case_U_Joint,
                            outputs.R.Travel,
                            color=plotSecondaryColor,
                        )
                        self.axR_T_Case_Joint.set_xlabel(
                            "Transfer Case U-joint Angle [\u00b0]"
                        )
                        self.axR_T_Case_Joint.set_ylabel(
                            "Travel [{}]".format(S.position_units)
                        )
                        self.axR_T_Case_Joint.grid(linewidth=0.5, color=bgColor)
                        self.axR_T_Case_Joint.set_facecolor(textEntryColor)
                        self.axR_T_Case_Joint.xaxis.label.set_color(entryTextColor)
                        self.axR_T_Case_Joint.yaxis.label.set_color(entryTextColor)
                        self.axR_T_Case_Joint.spines[
                            ["top", "bottom", "left", "right"]
                        ].set_color(entryTextColor)
                        self.axR_T_Case_Joint.tick_params(
                            axis="x", colors=entryTextColor
                        )
                        self.axR_T_Case_Joint.tick_params(
                            axis="y", colors=entryTextColor
                        )
                        self.axR_T_Case_Joint.text(
                            outputs.R.T_Case_U_Joint[0],
                            outputs.R.Travel[0],
                            "{:.1f}".format(outputs.R.T_Case_U_Joint[0]),
                            color=plotSecondaryColor,
                        )
                        self.axR_T_Case_Joint.text(
                            outputs.R.T_Case_U_Joint[S.sample_points],
                            outputs.R.Travel[S.sample_points],
                            "{:.1f}".format(outputs.R.T_Case_U_Joint[S.sample_points]),
                            color=plotSecondaryColor,
                        )
                        self.axR_T_Case_Joint.text(
                            outputs.R.T_Case_U_Joint[S.sample_points * 2],
                            outputs.R.Travel[S.sample_points * 2],
                            "{:.1f}".format(
                                outputs.R.T_Case_U_Joint[S.sample_points * 2]
                            ),
                            color=plotSecondaryColor,
                        )

                        self.axR_Pinion_Joint.plot(
                            outputs.R.Pinion_U_Joint,
                            outputs.R.Travel,
                            color=plotMainColor,
                        )
                        self.axR_Pinion_Joint.set_xlabel(
                            "Pinion U-joint Angle [\u00b0]"
                        )
                        self.axR_Pinion_Joint.set_ylabel(
                            "Travel [{}]".format(S.position_units)
                        )
                        self.axR_Pinion_Joint.grid(linewidth=0.5, color=bgColor)
                        self.axR_Pinion_Joint.set_facecolor(textEntryColor)
                        self.axR_Pinion_Joint.xaxis.label.set_color(entryTextColor)
                        self.axR_Pinion_Joint.yaxis.label.set_color(entryTextColor)
                        self.axR_Pinion_Joint.spines[
                            ["top", "bottom", "left", "right"]
                        ].set_color(entryTextColor)
                        self.axR_Pinion_Joint.tick_params(
                            axis="x", colors=entryTextColor
                        )
                        self.axR_Pinion_Joint.tick_params(
                            axis="y", colors=entryTextColor
                        )
                        self.axR_Pinion_Joint.text(
                            outputs.R.Pinion_U_Joint[0],
                            outputs.R.Travel[0],
                            "{:.1f}".format(outputs.R.Pinion_U_Joint[0]),
                            color=plotMainColor,
                        )
                        self.axR_Pinion_Joint.text(
                            outputs.R.Pinion_U_Joint[S.sample_points],
                            outputs.R.Travel[S.sample_points],
                            "{:.1f}".format(outputs.R.Pinion_U_Joint[S.sample_points]),
                            color=plotMainColor,
                        )
                        self.axR_Pinion_Joint.text(
                            outputs.R.Pinion_U_Joint[S.sample_points * 2],
                            outputs.R.Travel[S.sample_points * 2],
                            "{:.1f}".format(
                                outputs.R.Pinion_U_Joint[S.sample_points * 2]
                            ),
                            color=plotMainColor,
                        )

                    if True:  # Update Rear Text
                        label_R_max_length.config(
                            text="{:.1f} {}".format(
                                outputs.R.Max_Length, S.position_units
                            )
                        )
                        label_R_ride_length.config(
                            text="{:.1f} {}".format(
                                outputs.R.Ride_Length, S.position_units
                            )
                        )
                        label_R_min_length.config(
                            text="{:.1f} {}".format(
                                outputs.R.Min_Length, S.position_units
                            )
                        )
                        label_R_travel.config(
                            text="{:.1f} {}".format(
                                outputs.R.Driveshaft_Travel, S.position_units
                            )
                        )

                if True:  # Draw Plots
                    self.F_Pinion_Angle.draw()
                    self.F_T_Case_Joint.draw()
                    self.F_Pinion_Joint.draw()

                    self.R_Pinion_Angle.draw()
                    self.R_T_Case_Joint.draw()
                    self.R_Pinion_Joint.draw()

        if True:  # Detect out of input click
            self.bind("<1>", lambda event: update_outputs())

        if True:  # Update with option menu change
            F_method.trace_add("write", update_outputs)
            R_method.trace_add("write", update_outputs)

        update_outputs()

        def load_from_file():
            load_susp()
            master.switch_frame("driveshaft")
