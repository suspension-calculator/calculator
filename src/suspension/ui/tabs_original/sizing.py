# src/suspension/ui/tabs_original/sizing.py

import tkinter as tk


from suspension.core.calculations.link_sizing import run_link_sizing
from suspension.io.initialize_IO import *
from suspension.io.load_suspension import load_susp
from suspension.io.save_suspension import save_susp, save_as_susp
from suspension.io.variables import constant, S
from suspension.ui.styles import *


class sizingPage(tk.Frame):
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
                fg=buttonColor,
                bg=pressedButtonColor,
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

        if True:  # Front Inputs
            calc_front = tk.Frame(self, background=bgColor)
            calc_front.grid(row=1, column=2, sticky="n")
            front_upper = tk.Frame(calc_front, background=bgColor)
            front_upper.grid(row=1, column=0, stick="nesw")
            front_lower = tk.Frame(calc_front, background=bgColor)
            front_lower.grid(row=2, column=0, stick="nesw")
            front_panhard = tk.Frame(calc_front, background=bgColor)
            front_panhard.grid(row=3, column=0, stick="nesw")

            label = tk.Label(
                calc_front,
                text="Front",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 25),
                justify=tk.CENTER,
            )
            label.grid(row=0, column=0, pady=1)
            label.bind("<1>", lambda event: update_outputs())

            if True:  # Upper

                label = tk.Label(
                    front_upper,
                    text="Upper",
                    background=upperColor,
                    foreground=entryTextColor,
                    font=(fontType, 20),
                    justify=tk.CENTER,
                )
                label.grid(row=0, column=0, columnspan=3, stick="nesw")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 1

                label = tk.Label(
                    front_upper,
                    text="Outside Diameter:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                text = tk.StringVar()
                text.set(inputs.F.U_OD)
                F_U_OD = tk.Entry(
                    front_upper,
                    font=(fontType, 15),
                    justify=tk.CENTER,
                    width=13,
                    textvariable=text,
                    insertbackground=entryTextColor,
                )
                F_U_OD.grid(row=i_row, column=1)
                F_U_OD.config(bg=textEntryColor)
                F_U_OD.config(fg=entryTextColor)
                F_U_OD.bind("<Return>", lambda event: update_outputs())

                label = tk.Label(
                    front_upper,
                    text="{}".format(S.position_units),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 2

                label = tk.Label(
                    front_upper,
                    text="Solid Link?",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                F_U_solid = tk.StringVar()
                if inputs.F.U_solid:
                    default = "Yes"
                else:
                    default = "No"
                F_U_solid.set(default)
                F_U_solid_menu = tk.OptionMenu(front_upper, F_U_solid, "Yes", "No")
                F_U_solid_menu.grid(row=i_row, column=1)
                F_U_solid_menu.config(bg=textEntryColor)
                F_U_solid_menu.config(fg=entryTextColor)
                F_U_solid_menu.config(highlightthickness=0)
                F_U_solid_menu.config(width=3)
                F_U_solid_menu.config(font=(fontType, 15))
                F_U_solid_menu.nametowidget(F_U_solid_menu.menuname).config(
                    font=(fontType, 15)
                )

                i_row = 3

                label = tk.Label(
                    front_upper,
                    text="Wall Thickness:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                text = tk.StringVar()
                text.set(inputs.F.U_wall)
                F_U_thickness = tk.Entry(
                    front_upper,
                    font=(fontType, 15),
                    justify=tk.CENTER,
                    width=13,
                    textvariable=text,
                    insertbackground=entryTextColor,
                )
                F_U_thickness.grid(row=i_row, column=1)
                F_U_thickness.config(bg=textEntryColor)
                F_U_thickness.config(fg=entryTextColor)
                F_U_thickness.bind("<Return>", lambda event: update_outputs())

                label = tk.Label(
                    front_upper,
                    text="{}".format(S.position_units),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 4

                label = tk.Label(
                    front_upper,
                    text="Material Used:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                F_U_material = tk.StringVar()
                F_U_material.set(inputs.F.U_material)
                F_U_material_menu = tk.OptionMenu(
                    front_upper, F_U_material, *constant.materials.name
                )
                F_U_material_menu.grid(row=i_row, column=1)
                F_U_material_menu.config(bg=textEntryColor)
                F_U_material_menu.config(fg=entryTextColor)
                F_U_material_menu.config(highlightthickness=0)
                F_U_material_menu.config(width=20)
                F_U_material_menu.config(font=(fontType, 15))
                F_U_material_menu.nametowidget(F_U_material_menu.menuname).config(
                    font=(fontType, 15)
                )

                i_row = 5

                label = tk.Label(
                    front_upper,
                    text="Rod End:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                F_U_RE = tk.StringVar()
                F_U_RE.set(inputs.F.U_rod_end)
                F_U_RE_menu = tk.OptionMenu(
                    front_upper, F_U_RE, *constant.rod_ends.name
                )
                F_U_RE_menu.grid(row=i_row, column=1)
                F_U_RE_menu.config(bg=textEntryColor)
                F_U_RE_menu.config(fg=entryTextColor)
                F_U_RE_menu.config(highlightthickness=0)
                F_U_RE_menu.config(width=20)
                F_U_RE_menu.config(font=(fontType, 15))
                F_U_RE_menu.nametowidget(F_U_RE_menu.menuname).config(
                    font=(fontType, 15)
                )

            if True:  # Lower

                label = tk.Label(
                    front_lower,
                    text="Lower",
                    background=lowerColor,
                    foreground=textEntryColor,
                    font=(fontType, 20),
                    justify=tk.CENTER,
                )
                label.grid(row=0, column=0, columnspan=3, stick="nesw")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 1

                label = tk.Label(
                    front_lower,
                    text="Outside Diameter:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                text = tk.StringVar()
                text.set(inputs.F.L_OD)
                F_L_OD = tk.Entry(
                    front_lower,
                    font=(fontType, 15),
                    justify=tk.CENTER,
                    width=13,
                    textvariable=text,
                    insertbackground=entryTextColor,
                )
                F_L_OD.grid(row=i_row, column=1)
                F_L_OD.config(bg=textEntryColor)
                F_L_OD.config(fg=entryTextColor)
                F_L_OD.bind("<Return>", lambda event: update_outputs())

                label = tk.Label(
                    front_lower,
                    text="{}".format(S.position_units),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 2

                label = tk.Label(
                    front_lower,
                    text="Solid Link?",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                F_L_solid = tk.StringVar()
                if inputs.F.L_solid:
                    default = "Yes"
                else:
                    default = "No"
                F_L_solid.set(default)
                F_L_solid_menu = tk.OptionMenu(front_lower, F_L_solid, "Yes", "No")
                F_L_solid_menu.grid(row=i_row, column=1)
                F_L_solid_menu.config(bg=textEntryColor)
                F_L_solid_menu.config(fg=entryTextColor)
                F_L_solid_menu.config(highlightthickness=0)
                F_L_solid_menu.config(width=3)
                F_L_solid_menu.config(font=(fontType, 15))
                F_L_solid_menu.nametowidget(F_L_solid_menu.menuname).config(
                    font=(fontType, 15)
                )

                i_row = 3

                label = tk.Label(
                    front_lower,
                    text="Wall Thickness:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                text = tk.StringVar()
                text.set(inputs.F.L_wall)
                F_L_thickness = tk.Entry(
                    front_lower,
                    font=(fontType, 15),
                    justify=tk.CENTER,
                    width=13,
                    textvariable=text,
                    insertbackground=entryTextColor,
                )
                F_L_thickness.grid(row=i_row, column=1)
                F_L_thickness.config(bg=textEntryColor)
                F_L_thickness.config(fg=entryTextColor)
                F_L_thickness.bind("<Return>", lambda event: update_outputs())

                label = tk.Label(
                    front_lower,
                    text="{}".format(S.position_units),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 4

                label = tk.Label(
                    front_lower,
                    text="Material Used:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                F_L_material = tk.StringVar()
                F_L_material.set(inputs.F.L_material)
                F_L_material_menu = tk.OptionMenu(
                    front_lower, F_L_material, *constant.materials.name
                )
                F_L_material_menu.grid(row=i_row, column=1)
                F_L_material_menu.config(bg=textEntryColor)
                F_L_material_menu.config(fg=entryTextColor)
                F_L_material_menu.config(highlightthickness=0)
                F_L_material_menu.config(width=20)
                F_L_material_menu.config(font=(fontType, 15))
                F_L_material_menu.nametowidget(F_L_material_menu.menuname).config(
                    font=(fontType, 15)
                )

                i_row = 5

                label = tk.Label(
                    front_lower,
                    text="Rod End:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                F_L_RE = tk.StringVar()
                F_L_RE.set(inputs.F.L_rod_end)
                F_L_RE_menu = tk.OptionMenu(
                    front_lower, F_L_RE, *constant.rod_ends.name
                )
                F_L_RE_menu.grid(row=i_row, column=1)
                F_L_RE_menu.config(bg=textEntryColor)
                F_L_RE_menu.config(fg=entryTextColor)
                F_L_RE_menu.config(highlightthickness=0)
                F_L_RE_menu.config(width=20)
                F_L_RE_menu.config(font=(fontType, 15))
                F_L_RE_menu.nametowidget(F_L_RE_menu.menuname).config(
                    font=(fontType, 15)
                )

            if True:  # Panhard

                label = tk.Label(
                    front_panhard,
                    text="Panhard",
                    background=panhardColor,
                    foreground=textEntryColor,
                    font=(fontType, 20),
                    justify=tk.CENTER,
                )
                label.grid(row=0, column=0, columnspan=3, stick="nesw")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 1

                label = tk.Label(
                    front_panhard,
                    text="Outside Diameter:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                text = tk.StringVar()
                text.set(inputs.F.P_OD)
                F_P_OD = tk.Entry(
                    front_panhard,
                    font=(fontType, 15),
                    justify=tk.CENTER,
                    width=13,
                    textvariable=text,
                    insertbackground=entryTextColor,
                )
                F_P_OD.grid(row=i_row, column=1)
                F_P_OD.config(bg=textEntryColor)
                F_P_OD.config(fg=entryTextColor)
                F_P_OD.bind("<Return>", lambda event: update_outputs())

                label = tk.Label(
                    front_panhard,
                    text="{}".format(S.position_units),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 2

                label = tk.Label(
                    front_panhard,
                    text="Solid Link?",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                F_P_solid = tk.StringVar()
                if inputs.F.P_solid:
                    default = "Yes"
                else:
                    default = "No"
                F_P_solid.set(default)
                F_P_solid_menu = tk.OptionMenu(front_panhard, F_P_solid, "Yes", "No")
                F_P_solid_menu.grid(row=i_row, column=1)
                F_P_solid_menu.config(bg=textEntryColor)
                F_P_solid_menu.config(fg=entryTextColor)
                F_P_solid_menu.config(highlightthickness=0)
                F_P_solid_menu.config(width=3)
                F_P_solid_menu.config(font=(fontType, 15))
                F_P_solid_menu.nametowidget(F_P_solid_menu.menuname).config(
                    font=(fontType, 15)
                )

                i_row = 3

                label = tk.Label(
                    front_panhard,
                    text="Wall Thickness:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                text = tk.StringVar()
                text.set(inputs.F.P_wall)
                F_P_thickness = tk.Entry(
                    front_panhard,
                    font=(fontType, 15),
                    justify=tk.CENTER,
                    width=13,
                    textvariable=text,
                    insertbackground=entryTextColor,
                )
                F_P_thickness.grid(row=i_row, column=1)
                F_P_thickness.config(bg=textEntryColor)
                F_P_thickness.config(fg=entryTextColor)
                F_P_thickness.bind("<Return>", lambda event: update_outputs())

                label = tk.Label(
                    front_panhard,
                    text="{}".format(S.position_units),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 4

                label = tk.Label(
                    front_panhard,
                    text="Material Used:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                F_P_material = tk.StringVar()
                F_P_material.set(inputs.F.P_material)
                F_P_material_menu = tk.OptionMenu(
                    front_panhard, F_P_material, *constant.materials.name
                )
                F_P_material_menu.grid(row=i_row, column=1)
                F_P_material_menu.config(bg=textEntryColor)
                F_P_material_menu.config(fg=entryTextColor)
                F_P_material_menu.config(highlightthickness=0)
                F_P_material_menu.config(width=20)
                F_P_material_menu.config(font=(fontType, 15))
                F_P_material_menu.nametowidget(F_P_material_menu.menuname).config(
                    font=(fontType, 15)
                )

                i_row = 5

                label = tk.Label(
                    front_panhard,
                    text="Rod End:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                F_P_RE = tk.StringVar()
                F_P_RE.set(inputs.F.P_rod_end)
                F_P_RE_menu = tk.OptionMenu(
                    front_panhard, F_P_RE, *constant.rod_ends.name
                )
                F_P_RE_menu.grid(row=i_row, column=1)
                F_P_RE_menu.config(bg=textEntryColor)
                F_P_RE_menu.config(fg=entryTextColor)
                F_P_RE_menu.config(highlightthickness=0)
                F_P_RE_menu.config(width=20)
                F_P_RE_menu.config(font=(fontType, 15))
                F_P_RE_menu.nametowidget(F_P_RE_menu.menuname).config(
                    font=(fontType, 15)
                )

                if not constant.F.panhard:
                    F_P_OD.config(fg=bgColor)
                    F_P_solid_menu.config(fg=bgColor)
                    F_P_thickness.config(fg=bgColor)
                    F_P_material_menu.config(fg=bgColor)
                    F_P_RE_menu.config(fg=bgColor)

        if True:  # Front Outputs
            if True:  # Upper
                i_row = 6

                label = tk.Label(
                    front_upper,
                    text="Rod End Thread:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_U_RE_thread = tk.Label(
                    front_upper,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_U_RE_thread.grid(row=i_row, column=1, sticky="w")
                label_F_U_RE_thread.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_upper,
                    text="Top View Rod End Angle: {:.0f}\u00b0".format(
                        outputs.F.U_top_view_angle
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_upper,
                    text="Rod End Hole:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_U_RE_hole = tk.Label(
                    front_upper,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_U_RE_hole.grid(row=i_row, column=1, sticky="w")
                label_F_U_RE_hole.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_upper,
                    text="Side View Axle Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.F.UA_side_view_angle_range[0],
                        outputs.F.UA_side_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                    width=45,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_upper,
                    text="Rod End Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_U_RE_weight = tk.Label(
                    front_upper,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_U_RE_weight.grid(row=i_row, column=1, sticky="w")
                label_F_U_RE_weight.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_upper,
                    text="Side View Frame Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.F.UF_side_view_angle_range[0],
                        outputs.F.UF_side_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_upper,
                    text="Link Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_U_link_weight = tk.Label(
                    front_upper,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_U_link_weight.grid(row=i_row, column=1, sticky="w")
                label_F_U_link_weight.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_upper,
                    text="Single Link Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_U_weight = tk.Label(
                    front_upper,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_U_weight.grid(row=i_row, column=1, sticky="w")
                label_F_U_weight.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_upper,
                    text="Factor of Safety Yield:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_U_FS_yield = tk.Label(
                    front_upper,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_U_FS_yield.grid(row=i_row, column=1, sticky="nesw")
                label_F_U_FS_yield.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_upper,
                    text="(link stretching)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_upper,
                    text="Factor of Safety Buckling:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_U_FS_buckling = tk.Label(
                    front_upper,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_U_FS_buckling.grid(row=i_row, column=1, stick="nesw")
                label_F_U_FS_buckling.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_upper,
                    text="(link buckling under braking)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_upper,
                    text="Factor of Safety Bending:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_U_FS_bending = tk.Label(
                    front_upper,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_U_FS_bending.grid(row=i_row, column=1, stick="nesw")
                label_F_U_FS_bending.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_upper,
                    text="(somewhat irrelevant for an UPPER link)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_upper,
                    text="Factor of Safety Rod End:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_U_FS_RE = tk.Label(
                    front_upper,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_U_FS_RE.grid(row=i_row, column=1, stick="nesw")
                label_F_U_FS_RE.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_upper,
                    text="(rod end breaking)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_upper,
                    text="Dent Resistance:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_U_dent_resist = tk.Label(
                    front_upper,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_U_dent_resist.grid(row=i_row, column=1, sticky="nesw")
                label_F_U_dent_resist.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_upper,
                    text='(compared to 0.25" thick 1018 steel)',
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

            if True:  # Lower
                i_row = 6

                label = tk.Label(
                    front_lower,
                    text="Rod End Thread:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_L_RE_thread = tk.Label(
                    front_lower,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_L_RE_thread.grid(row=i_row, column=1, sticky="w")
                label_F_L_RE_thread.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_lower,
                    text="Top View Rod End Angle: {:.0f}\u00b0".format(
                        outputs.F.L_top_view_angle
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_lower,
                    text="Rod End Hole:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_L_RE_hole = tk.Label(
                    front_lower,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_L_RE_hole.grid(row=i_row, column=1, sticky="w")
                label_F_L_RE_hole.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_lower,
                    text="Side View Axle Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.F.LA_side_view_angle_range[0],
                        outputs.F.LA_side_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                    width=45,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_lower,
                    text="Rod End Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_L_RE_weight = tk.Label(
                    front_lower,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_L_RE_weight.grid(row=i_row, column=1, sticky="w")
                label_F_L_RE_weight.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_lower,
                    text="Side View Frame Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.F.LF_side_view_angle_range[0],
                        outputs.F.LF_side_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_lower,
                    text="Link Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_L_link_weight = tk.Label(
                    front_lower,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_L_link_weight.grid(row=i_row, column=1, sticky="w")
                label_F_L_link_weight.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_lower,
                    text="Single Link Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_L_weight = tk.Label(
                    front_lower,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_L_weight.grid(row=i_row, column=1, sticky="w")
                label_F_L_weight.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_lower,
                    text="Factor of Safety Yield:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_L_FS_yield = tk.Label(
                    front_lower,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_L_FS_yield.grid(row=i_row, column=1, stick="nesw")
                label_F_L_FS_yield.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_lower,
                    text="(link stretching)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_lower,
                    text="Factor of Safety Buckling:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_L_FS_buckling = tk.Label(
                    front_lower,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_L_FS_buckling.grid(row=i_row, column=1, stick="nesw")
                label_F_L_FS_buckling.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_lower,
                    text="(link buckling under acceleration)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_lower,
                    text="Factor of Safety Bending:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_L_FS_bending = tk.Label(
                    front_lower,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_L_FS_bending.grid(row=i_row, column=1, stick="nesw")
                label_F_L_FS_bending.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_lower,
                    text="(link bending with 1/2 the vehicle's weight on it)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_lower,
                    text="Factor of Safety Rod End:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_L_FS_RE = tk.Label(
                    front_lower,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_L_FS_RE.grid(row=i_row, column=1, stick="nesw")
                label_F_L_FS_RE.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_lower,
                    text="(rod end breaking)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_lower,
                    text="Dent Resistance:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_L_dent_resist = tk.Label(
                    front_lower,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_L_dent_resist.grid(row=i_row, column=1, sticky="nesw")
                label_F_L_dent_resist.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_lower,
                    text='(compared to 0.25" thick 1018 steel)',
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

            if True:  # Panhard
                i_row = 6

                label = tk.Label(
                    front_panhard,
                    text="Rod End Thread:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_P_RE_thread = tk.Label(
                    front_panhard,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_P_RE_thread.grid(row=i_row, column=1, sticky="w")
                label_F_P_RE_thread.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_panhard,
                    text="Top View Axle Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.F.PA_top_view_angle_range[0],
                        outputs.F.PA_top_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                    width=45,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_panhard,
                    text="Rod End Hole:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_P_RE_hole = tk.Label(
                    front_panhard,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_P_RE_hole.grid(row=i_row, column=1, sticky="w")
                label_F_P_RE_hole.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_panhard,
                    text="Top View Frame Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.F.PF_top_view_angle_range[0],
                        outputs.F.PF_top_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                    width=45,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_panhard,
                    text="Rod End Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_P_RE_weight = tk.Label(
                    front_panhard,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_P_RE_weight.grid(row=i_row, column=1, sticky="w")
                label_F_P_RE_weight.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_panhard,
                    text="Front View Axle Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.F.PA_front_view_angle_range[0],
                        outputs.F.PA_front_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                    width=45,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_panhard,
                    text="Link Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_P_link_weight = tk.Label(
                    front_panhard,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_P_link_weight.grid(row=i_row, column=1, sticky="w")
                label_F_P_link_weight.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_panhard,
                    text="Front View Frame Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.F.PF_front_view_angle_range[0],
                        outputs.F.PF_front_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                    width=45,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_panhard,
                    text="Single Link Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_P_weight = tk.Label(
                    front_panhard,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_P_weight.grid(row=i_row, column=1, sticky="w")
                label_F_P_weight.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_panhard,
                    text="Factor of Safety Yield:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_P_FS_yield = tk.Label(
                    front_panhard,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_P_FS_yield.grid(row=i_row, column=1, stick="nesw")
                label_F_P_FS_yield.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_panhard,
                    text="(link stretching)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_panhard,
                    text="Factor of Safety Buckling:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_P_FS_buckling = tk.Label(
                    front_panhard,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_P_FS_buckling.grid(row=i_row, column=1, stick="nesw")
                label_F_P_FS_buckling.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_panhard,
                    text="(link buckling under side force)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_panhard,
                    text="Factor of Safety Bending:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_P_FS_bending = tk.Label(
                    front_panhard,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_P_FS_bending.grid(row=i_row, column=1, stick="nesw")
                label_F_P_FS_bending.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_panhard,
                    text="(link bending with the vehicle's weight on it)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_panhard,
                    text="Factor of Safety Rod End:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_P_FS_RE = tk.Label(
                    front_panhard,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_P_FS_RE.grid(row=i_row, column=1, stick="nesw")
                label_F_P_FS_RE.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_panhard,
                    text="(rod end breaking)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    front_panhard,
                    text="Dent Resistance:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_F_P_dent_resist = tk.Label(
                    front_panhard,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_F_P_dent_resist.grid(row=i_row, column=1, sticky="nesw")
                label_F_P_dent_resist.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    front_panhard,
                    text='(compared to 0.25" thick 1018 steel)',
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

        if True:  # Rear Inputs
            calc_rear = tk.Frame(self, background=bgColor)
            calc_rear.grid(row=1, column=0, sticky="n")
            rear_upper = tk.Frame(calc_rear, background=bgColor)
            rear_upper.grid(row=1, column=0, stick="nesw")
            rear_lower = tk.Frame(calc_rear, background=bgColor)
            rear_lower.grid(row=2, column=0, stick="nesw")
            rear_panhard = tk.Frame(calc_rear, background=bgColor)
            rear_panhard.grid(row=3, column=0, stick="nesw")

            label = tk.Label(
                calc_rear,
                text="Rear",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 25),
                justify=tk.CENTER,
            )
            label.grid(row=0, column=0, pady=1)
            label.bind("<1>", lambda event: update_outputs())

            if True:  # Upper

                label = tk.Label(
                    rear_upper,
                    text="Upper",
                    background=upperColor,
                    foreground=entryTextColor,
                    font=(fontType, 20),
                    justify=tk.CENTER,
                )
                label.grid(row=0, column=0, columnspan=3, stick="nesw")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 1

                label = tk.Label(
                    rear_upper,
                    text="Outside Diameter:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                text = tk.StringVar()
                text.set(inputs.R.U_OD)
                R_U_OD = tk.Entry(
                    rear_upper,
                    font=(fontType, 15),
                    justify=tk.CENTER,
                    width=13,
                    textvariable=text,
                    insertbackground=entryTextColor,
                )
                R_U_OD.grid(row=i_row, column=1)
                R_U_OD.config(bg=textEntryColor)
                R_U_OD.config(fg=entryTextColor)
                R_U_OD.bind("<Return>", lambda event: update_outputs())

                label = tk.Label(
                    rear_upper,
                    text="{}".format(S.position_units),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 2

                label = tk.Label(
                    rear_upper,
                    text="Solid Link?",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                R_U_solid = tk.StringVar()
                if inputs.R.U_solid:
                    default = "Yes"
                else:
                    default = "No"
                R_U_solid.set(default)
                R_U_solid_menu = tk.OptionMenu(rear_upper, R_U_solid, "Yes", "No")
                R_U_solid_menu.grid(row=i_row, column=1)
                R_U_solid_menu.config(bg=textEntryColor)
                R_U_solid_menu.config(fg=entryTextColor)
                R_U_solid_menu.config(highlightthickness=0)
                R_U_solid_menu.config(width=3)
                R_U_solid_menu.config(font=(fontType, 15))
                R_U_solid_menu.nametowidget(R_U_solid_menu.menuname).config(
                    font=(fontType, 15)
                )

                i_row = 3

                label = tk.Label(
                    rear_upper,
                    text="Wall Thickness:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                text = tk.StringVar()
                text.set(inputs.R.U_wall)
                R_U_thickness = tk.Entry(
                    rear_upper,
                    font=(fontType, 15),
                    justify=tk.CENTER,
                    width=13,
                    textvariable=text,
                    insertbackground=entryTextColor,
                )
                R_U_thickness.grid(row=i_row, column=1)
                R_U_thickness.config(bg=textEntryColor)
                R_U_thickness.config(fg=entryTextColor)
                R_U_thickness.bind("<Return>", lambda event: update_outputs())

                label = tk.Label(
                    rear_upper,
                    text="{}".format(S.position_units),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 4

                label = tk.Label(
                    rear_upper,
                    text="Material Used:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                R_U_material = tk.StringVar()
                R_U_material.set(inputs.R.U_material)
                R_U_material_menu = tk.OptionMenu(
                    rear_upper, R_U_material, *constant.materials.name
                )
                R_U_material_menu.grid(row=i_row, column=1)
                R_U_material_menu.config(bg=textEntryColor)
                R_U_material_menu.config(fg=entryTextColor)
                R_U_material_menu.config(highlightthickness=0)
                R_U_material_menu.config(width=20)
                R_U_material_menu.config(font=(fontType, 15))
                R_U_material_menu.nametowidget(R_U_material_menu.menuname).config(
                    font=(fontType, 15)
                )

                i_row = 5

                label = tk.Label(
                    rear_upper,
                    text="Rod End:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                R_U_RE = tk.StringVar()
                R_U_RE.set(inputs.R.U_rod_end)
                R_U_RE_menu = tk.OptionMenu(rear_upper, R_U_RE, *constant.rod_ends.name)
                R_U_RE_menu.grid(row=i_row, column=1)
                R_U_RE_menu.config(bg=textEntryColor)
                R_U_RE_menu.config(fg=entryTextColor)
                R_U_RE_menu.config(highlightthickness=0)
                R_U_RE_menu.config(width=20)
                R_U_RE_menu.config(font=(fontType, 15))
                R_U_RE_menu.nametowidget(R_U_RE_menu.menuname).config(
                    font=(fontType, 15)
                )

            if True:  # Lower

                label = tk.Label(
                    rear_lower,
                    text="Lower",
                    background=lowerColor,
                    foreground=textEntryColor,
                    font=(fontType, 20),
                    justify=tk.CENTER,
                )
                label.grid(row=0, column=0, columnspan=3, stick="nesw")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 1

                label = tk.Label(
                    rear_lower,
                    text="Outside Diameter:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                text = tk.StringVar()
                text.set(inputs.R.L_OD)
                R_L_OD = tk.Entry(
                    rear_lower,
                    font=(fontType, 15),
                    justify=tk.CENTER,
                    width=13,
                    textvariable=text,
                    insertbackground=entryTextColor,
                )
                R_L_OD.grid(row=i_row, column=1)
                R_L_OD.config(bg=textEntryColor)
                R_L_OD.config(fg=entryTextColor)
                R_L_OD.bind("<Return>", lambda event: update_outputs())

                label = tk.Label(
                    rear_lower,
                    text="{}".format(S.position_units),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 2

                label = tk.Label(
                    rear_lower,
                    text="Solid Link?",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                R_L_solid = tk.StringVar()
                if inputs.R.L_solid:
                    default = "Yes"
                else:
                    default = "No"
                R_L_solid.set(default)
                R_L_solid_menu = tk.OptionMenu(rear_lower, R_L_solid, "Yes", "No")
                R_L_solid_menu.grid(row=i_row, column=1)
                R_L_solid_menu.config(bg=textEntryColor)
                R_L_solid_menu.config(fg=entryTextColor)
                R_L_solid_menu.config(highlightthickness=0)
                R_L_solid_menu.config(width=3)
                R_L_solid_menu.config(font=(fontType, 15))
                R_L_solid_menu.nametowidget(R_L_solid_menu.menuname).config(
                    font=(fontType, 15)
                )

                i_row = 3

                label = tk.Label(
                    rear_lower,
                    text="Wall Thickness:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                text = tk.StringVar()
                text.set(inputs.R.L_wall)
                R_L_thickness = tk.Entry(
                    rear_lower,
                    font=(fontType, 15),
                    justify=tk.CENTER,
                    width=13,
                    textvariable=text,
                    insertbackground=entryTextColor,
                )
                R_L_thickness.grid(row=i_row, column=1)
                R_L_thickness.config(bg=textEntryColor)
                R_L_thickness.config(fg=entryTextColor)
                R_L_thickness.bind("<Return>", lambda event: update_outputs())

                label = tk.Label(
                    rear_lower,
                    text="{}".format(S.position_units),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 4

                label = tk.Label(
                    rear_lower,
                    text="Material Used:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                R_L_material = tk.StringVar()
                R_L_material.set(inputs.R.L_material)
                R_L_material_menu = tk.OptionMenu(
                    rear_lower, R_L_material, *constant.materials.name
                )
                R_L_material_menu.grid(row=i_row, column=1)
                R_L_material_menu.config(bg=textEntryColor)
                R_L_material_menu.config(fg=entryTextColor)
                R_L_material_menu.config(highlightthickness=0)
                R_L_material_menu.config(width=20)
                R_L_material_menu.config(font=(fontType, 15))
                R_L_material_menu.nametowidget(R_L_material_menu.menuname).config(
                    font=(fontType, 15)
                )

                i_row = 5

                label = tk.Label(
                    rear_lower,
                    text="Rod End:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                R_L_RE = tk.StringVar()
                R_L_RE.set(inputs.R.L_rod_end)
                R_L_RE_menu = tk.OptionMenu(rear_lower, R_L_RE, *constant.rod_ends.name)
                R_L_RE_menu.grid(row=i_row, column=1)
                R_L_RE_menu.config(bg=textEntryColor)
                R_L_RE_menu.config(fg=entryTextColor)
                R_L_RE_menu.config(highlightthickness=0)
                R_L_RE_menu.config(width=20)
                R_L_RE_menu.config(font=(fontType, 15))
                R_L_RE_menu.nametowidget(R_L_RE_menu.menuname).config(
                    font=(fontType, 15)
                )

            if True:  # Panhard

                label = tk.Label(
                    rear_panhard,
                    text="Panhard",
                    background=panhardColor,
                    foreground=textEntryColor,
                    font=(fontType, 20),
                    justify=tk.CENTER,
                )
                label.grid(row=0, column=0, columnspan=3, stick="nesw")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 1

                label = tk.Label(
                    rear_panhard,
                    text="Outside Diameter:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                text = tk.StringVar()
                text.set(inputs.R.P_OD)
                R_P_OD = tk.Entry(
                    rear_panhard,
                    font=(fontType, 15),
                    justify=tk.CENTER,
                    width=13,
                    textvariable=text,
                    insertbackground=entryTextColor,
                )
                R_P_OD.grid(row=i_row, column=1)
                R_P_OD.config(bg=textEntryColor)
                R_P_OD.config(fg=entryTextColor)
                R_P_OD.bind("<Return>", lambda event: update_outputs())

                label = tk.Label(
                    rear_panhard,
                    text="{}".format(S.position_units),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 2

                label = tk.Label(
                    rear_panhard,
                    text="Solid Link?",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                R_P_solid = tk.StringVar()
                if inputs.R.P_solid:
                    default = "Yes"
                else:
                    default = "No"
                R_P_solid.set(default)
                R_P_solid_menu = tk.OptionMenu(rear_panhard, R_P_solid, "Yes", "No")
                R_P_solid_menu.grid(row=i_row, column=1)
                R_P_solid_menu.config(bg=textEntryColor)
                R_P_solid_menu.config(fg=entryTextColor)
                R_P_solid_menu.config(highlightthickness=0)
                R_P_solid_menu.config(width=3)
                R_P_solid_menu.config(font=(fontType, 15))
                R_P_solid_menu.nametowidget(R_P_solid_menu.menuname).config(
                    font=(fontType, 15)
                )

                i_row = 3

                label = tk.Label(
                    rear_panhard,
                    text="Wall Thickness:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                text = tk.StringVar()
                text.set(inputs.R.P_wall)
                R_P_thickness = tk.Entry(
                    rear_panhard,
                    font=(fontType, 15),
                    justify=tk.CENTER,
                    width=13,
                    textvariable=text,
                    insertbackground=entryTextColor,
                )
                R_P_thickness.grid(row=i_row, column=1)
                R_P_thickness.config(bg=textEntryColor)
                R_P_thickness.config(fg=entryTextColor)
                R_P_thickness.bind("<Return>", lambda event: update_outputs())

                label = tk.Label(
                    rear_panhard,
                    text="{}".format(S.position_units),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = 4

                label = tk.Label(
                    rear_panhard,
                    text="Material Used:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                R_P_material = tk.StringVar()
                R_P_material.set(inputs.R.P_material)
                R_P_material_menu = tk.OptionMenu(
                    rear_panhard, R_P_material, *constant.materials.name
                )
                R_P_material_menu.grid(row=i_row, column=1)
                R_P_material_menu.config(bg=textEntryColor)
                R_P_material_menu.config(fg=entryTextColor)
                R_P_material_menu.config(highlightthickness=0)
                R_P_material_menu.config(width=20)
                R_P_material_menu.config(font=(fontType, 15))
                R_P_material_menu.nametowidget(R_P_material_menu.menuname).config(
                    font=(fontType, 15)
                )

                i_row = 5

                label = tk.Label(
                    rear_panhard,
                    text="Rod End:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                R_P_RE = tk.StringVar()
                R_P_RE.set(inputs.R.P_rod_end)
                R_P_RE_menu = tk.OptionMenu(
                    rear_panhard, R_P_RE, *constant.rod_ends.name
                )
                R_P_RE_menu.grid(row=i_row, column=1)
                R_P_RE_menu.config(bg=textEntryColor)
                R_P_RE_menu.config(fg=entryTextColor)
                R_P_RE_menu.config(highlightthickness=0)
                R_P_RE_menu.config(width=20)
                R_P_RE_menu.config(font=(fontType, 15))
                R_P_RE_menu.nametowidget(R_P_RE_menu.menuname).config(
                    font=(fontType, 15)
                )

                if not constant.R.panhard:
                    R_P_OD.config(fg=bgColor)
                    R_P_solid_menu.config(fg=bgColor)
                    R_P_thickness.config(fg=bgColor)
                    R_P_material_menu.config(fg=bgColor)
                    R_P_RE_menu.config(fg=bgColor)

        if True:  # Rear Outputs
            if True:  # Upper
                i_row = 6

                label = tk.Label(
                    rear_upper,
                    text="Rod End Thread:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_U_RE_thread = tk.Label(
                    rear_upper,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_U_RE_thread.grid(row=i_row, column=1, sticky="w")
                label_R_U_RE_thread.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_upper,
                    text="Top View Rod End Angle: {:.0f}\u00b0".format(
                        outputs.R.U_top_view_angle
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_upper,
                    text="Rod End Hole:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_U_RE_hole = tk.Label(
                    rear_upper,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_U_RE_hole.grid(row=i_row, column=1, sticky="w")
                label_R_U_RE_hole.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_upper,
                    text="Side View Axle Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.R.UA_side_view_angle_range[0],
                        outputs.R.UA_side_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                    width=45,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_upper,
                    text="Rod End Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_U_RE_weight = tk.Label(
                    rear_upper,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_U_RE_weight.grid(row=i_row, column=1, sticky="w")
                label_R_U_RE_weight.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_upper,
                    text="Side View Frame Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.R.UF_side_view_angle_range[0],
                        outputs.R.UF_side_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_upper,
                    text="Link Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_U_link_weight = tk.Label(
                    rear_upper,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_U_link_weight.grid(row=i_row, column=1, sticky="w")
                label_R_U_link_weight.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_upper,
                    text="Single Link Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_U_weight = tk.Label(
                    rear_upper,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_U_weight.grid(row=i_row, column=1, sticky="w")
                label_R_U_weight.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_upper,
                    text="Factor of Safety Yield:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_U_FS_yield = tk.Label(
                    rear_upper,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_U_FS_yield.grid(row=i_row, column=1, stick="nesw")
                label_R_U_FS_yield.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_upper,
                    text="(link stretching)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_upper,
                    text="Factor of Safety Buckling:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_U_FS_buckling = tk.Label(
                    rear_upper,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_U_FS_buckling.grid(row=i_row, column=1, stick="nesw")
                label_R_U_FS_buckling.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_upper,
                    text="(link buckling under acceleration)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_upper,
                    text="Factor of Safety Bending:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_U_FS_bending = tk.Label(
                    rear_upper,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_U_FS_bending.grid(row=i_row, column=1, stick="nesw")
                label_R_U_FS_bending.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_upper,
                    text="(somewhat irrelevant for an UPPER link)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_upper,
                    text="Factor of Safety Rod End:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_U_FS_RE = tk.Label(
                    rear_upper,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_U_FS_RE.grid(row=i_row, column=1, stick="nesw")
                label_R_U_FS_RE.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_upper,
                    text="(rod end breaking)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_upper,
                    text="Dent Resistance:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_U_dent_resist = tk.Label(
                    rear_upper,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_U_dent_resist.grid(row=i_row, column=1, sticky="nesw")
                label_R_U_dent_resist.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_upper,
                    text='(compared to 0.25" thick 1018 steel)',
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

            if True:  # Lower
                i_row = 6

                label = tk.Label(
                    rear_lower,
                    text="Rod End Thread:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_L_RE_thread = tk.Label(
                    rear_lower,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_L_RE_thread.grid(row=i_row, column=1, sticky="w")
                label_R_L_RE_thread.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_lower,
                    text="Top View Rod End Angle: {:.0f}\u00b0".format(
                        outputs.R.L_top_view_angle
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_lower,
                    text="Rod End Hole:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_L_RE_hole = tk.Label(
                    rear_lower,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_L_RE_hole.grid(row=i_row, column=1, sticky="w")
                label_R_L_RE_hole.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_lower,
                    text="Side View Axle Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.R.LA_side_view_angle_range[0],
                        outputs.R.LA_side_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                    width=45,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_lower,
                    text="Rod End Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_L_RE_weight = tk.Label(
                    rear_lower,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_L_RE_weight.grid(row=i_row, column=1, sticky="w")
                label_R_L_RE_weight.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_lower,
                    text="Side View Frame Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.R.LF_side_view_angle_range[0],
                        outputs.R.LF_side_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_lower,
                    text="Link Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_L_link_weight = tk.Label(
                    rear_lower,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_L_link_weight.grid(row=i_row, column=1, sticky="w")
                label_R_L_link_weight.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_lower,
                    text="Single Link Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_L_weight = tk.Label(
                    rear_lower,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_L_weight.grid(row=i_row, column=1, sticky="w")
                label_R_L_weight.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_lower,
                    text="Factor of Safety Yield:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_L_FS_yield = tk.Label(
                    rear_lower,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_L_FS_yield.grid(row=i_row, column=1, stick="nesw")
                label_R_L_FS_yield.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_lower,
                    text="(link stretching)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_lower,
                    text="Factor of Safety Buckling:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_L_FS_buckling = tk.Label(
                    rear_lower,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_L_FS_buckling.grid(row=i_row, column=1, stick="nesw")
                label_R_L_FS_buckling.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_lower,
                    text="(link buckling under braking)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_lower,
                    text="Factor of Safety Bending:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_L_FS_bending = tk.Label(
                    rear_lower,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_L_FS_bending.grid(row=i_row, column=1, stick="nesw")
                label_R_L_FS_bending.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_lower,
                    text="(link bending with 1/2 the vehicle's weight on it)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_lower,
                    text="Factor of Safety Rod End:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_L_FS_RE = tk.Label(
                    rear_lower,
                    text="",
                    background=FSPassColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_L_FS_RE.grid(row=i_row, column=1, stick="nesw")
                label_R_L_FS_RE.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_lower,
                    text="(rod end breaking)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_lower,
                    text="Dent Resistance:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_L_dent_resist = tk.Label(
                    rear_lower,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_L_dent_resist.grid(row=i_row, column=1, sticky="nesw")
                label_R_L_dent_resist.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_lower,
                    text='(compared to 0.25" thick 1018 steel)',
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

            if True:  # Panhard
                i_row = 6

                label = tk.Label(
                    rear_panhard,
                    text="Rod End Thread:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_P_RE_thread = tk.Label(
                    rear_panhard,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_P_RE_thread.grid(row=i_row, column=1, sticky="w")
                label_R_P_RE_thread.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_panhard,
                    text="Top View Axle Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.R.PA_top_view_angle_range[0],
                        outputs.R.PA_top_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                    width=45,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_panhard,
                    text="Rod End Hole:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_P_RE_hole = tk.Label(
                    rear_panhard,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_P_RE_hole.grid(row=i_row, column=1, sticky="w")
                label_R_P_RE_hole.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_panhard,
                    text="Top View Frame Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.R.PF_top_view_angle_range[0],
                        outputs.R.PF_top_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                    width=45,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_panhard,
                    text="Rod End Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_P_RE_weight = tk.Label(
                    rear_panhard,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_P_RE_weight.grid(row=i_row, column=1, sticky="w")
                label_R_P_RE_weight.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_panhard,
                    text="Rear View Axle Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.R.PA_rear_view_angle_range[0],
                        outputs.R.PA_rear_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                    width=45,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_panhard,
                    text="Link Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_P_link_weight = tk.Label(
                    rear_panhard,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_P_link_weight.grid(row=i_row, column=1, sticky="w")
                label_R_P_link_weight.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_panhard,
                    text="Rear View Frame Rod End Angle Range: {:.0f}\u00b0 to {:.0f}\u00b0".format(
                        outputs.R.PF_rear_view_angle_range[0],
                        outputs.R.PF_rear_view_angle_range[1],
                    ),
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                    width=45,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_panhard,
                    text="Single Link Weight:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_P_weight = tk.Label(
                    rear_panhard,
                    text="",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_P_weight.grid(row=i_row, column=1, sticky="w")
                label_R_P_weight.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_panhard,
                    text="Factor of Safety Yield:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_P_FS_yield = tk.Label(
                    rear_panhard,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_P_FS_yield.grid(row=i_row, column=1, stick="nesw")
                label_R_P_FS_yield.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_panhard,
                    text="(link stretching)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_panhard,
                    text="Factor of Safety Buckling:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_P_FS_buckling = tk.Label(
                    rear_panhard,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_P_FS_buckling.grid(row=i_row, column=1, stick="nesw")
                label_R_P_FS_buckling.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_panhard,
                    text="(link buckling under side force)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_panhard,
                    text="Factor of Safety Bending:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_P_FS_bending = tk.Label(
                    rear_panhard,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_P_FS_bending.grid(row=i_row, column=1, stick="nesw")
                label_R_P_FS_bending.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_panhard,
                    text="(link bending with the vehicle's weight on it)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_panhard,
                    text="Factor of Safety Rod End:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_P_FS_RE = tk.Label(
                    rear_panhard,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_P_FS_RE.grid(row=i_row, column=1, stick="nesw")
                label_R_P_FS_RE.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_panhard,
                    text="(rod end breaking)",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

                i_row = i_row + 1

                label = tk.Label(
                    rear_panhard,
                    text="Dent Resistance:",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=0, sticky="e")
                label.bind("<1>", lambda event: update_outputs())

                label_R_P_dent_resist = tk.Label(
                    rear_panhard,
                    text="",
                    background=bgColor,
                    foreground=textEntryColor,
                    font=(fontType, 15),
                    anchor="w",
                )
                label_R_P_dent_resist.grid(row=i_row, column=1, sticky="nesw")
                label_R_P_dent_resist.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    rear_panhard,
                    text='(compared to 0.25" thick 1018 steel)',
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    justify=tk.RIGHT,
                )
                label.grid(row=i_row, column=2, sticky="w")
                label.bind("<1>", lambda event: update_outputs())

        if True:  # Vehicle Inputs
            calc_vehicle = tk.Frame(self, background=bgColor)
            calc_vehicle.grid(row=1, column=1, sticky="n")
            calc_IO = tk.Frame(calc_vehicle, background=bgColor)
            calc_IO.grid(row=1, column=0, sticky="n")
            calc_RE_table = tk.Frame(calc_vehicle, background=bgColor)
            calc_RE_table.grid(row=2, column=0, sticky="n")
            calc_material_table = tk.Frame(calc_vehicle, background=bgColor)
            calc_material_table.grid(row=4, column=0, sticky="n")

            label = tk.Label(
                calc_vehicle,
                text="Vehicle Sizing Results",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 25),
                justify=tk.CENTER,
            )
            label.grid(row=0, column=0, pady=1)
            label.bind("<1>", lambda event: update_outputs())

            i_row = 1

            label = tk.Label(
                calc_IO,
                text="Desired Factor of Safety for Yield:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(constant.V.Desired_FS_Yield)
            V_FS_yield = tk.Entry(
                calc_IO,
                font=(fontType, 15),
                justify=tk.CENTER,
                width=13,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            V_FS_yield.grid(row=i_row, column=1)
            V_FS_yield.config(bg=textEntryColor)
            V_FS_yield.config(fg=entryTextColor)
            V_FS_yield.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                calc_IO,
                text="Yield is affected most by wall thickness",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=2, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 2

            label = tk.Label(
                calc_IO,
                text="Desired Factor of Safety for Buckling:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(constant.V.Desired_FS_Buckling)
            V_FS_buckling = tk.Entry(
                calc_IO,
                font=(fontType, 15),
                justify=tk.CENTER,
                width=13,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            V_FS_buckling.grid(row=i_row, column=1)
            V_FS_buckling.config(bg=textEntryColor)
            V_FS_buckling.config(fg=entryTextColor)
            V_FS_buckling.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                calc_IO,
                text="Buckling is affected most by outside diameter",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=2, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 3

            label = tk.Label(
                calc_IO,
                text="Desired Factor of Safety for Bending:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(constant.V.Desired_FS_Bending)
            V_FS_bending = tk.Entry(
                calc_IO,
                font=(fontType, 15),
                justify=tk.CENTER,
                width=13,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            V_FS_bending.grid(row=i_row, column=1)
            V_FS_bending.config(bg=textEntryColor)
            V_FS_bending.config(fg=entryTextColor)
            V_FS_bending.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                calc_IO,
                text="Bending is most affected by oustide diameter",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=2, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            i_row = 4

            label = tk.Label(
                calc_IO,
                text="Desired Factor of Safety for Rod End:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(constant.V.Desired_FS_RE)
            V_FS_RE = tk.Entry(
                calc_IO,
                font=(fontType, 15),
                justify=tk.CENTER,
                width=13,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            V_FS_RE.grid(row=i_row, column=1)
            V_FS_RE.config(bg=textEntryColor)
            V_FS_RE.config(fg=entryTextColor)
            V_FS_RE.bind("<Return>", lambda event: update_outputs())

            i_row = 5

            label = tk.Label(
                calc_IO,
                text="Desired Ratio for Denting:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(constant.V.Desired_FS_Dent)
            V_FS_Dent = tk.Entry(
                calc_IO,
                font=(fontType, 15),
                justify=tk.CENTER,
                width=13,
                textvariable=text,
                insertbackground=entryTextColor,
            )
            V_FS_Dent.grid(row=i_row, column=1)
            V_FS_Dent.config(bg=textEntryColor)
            V_FS_Dent.config(fg=entryTextColor)
            V_FS_Dent.bind("<Return>", lambda event: update_outputs())

            label = tk.Label(
                calc_IO,
                text="Denting is most affected by wall thickness",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=2, sticky="w")
            label.bind("<1>", lambda event: update_outputs())

            buttonRE = tk.Button(
                calc_vehicle,
                text="Add Rod End",
                fg=pressedButtonColor,
                bg=buttonColor,
                command=lambda: master.switch_frame("rodEnds"),
                height=1,
                width=11,
                font=(fontType, 13),
            )
            buttonRE.grid(row=3, column=0, padx=2)

            buttonMaterial = tk.Button(
                calc_vehicle,
                text="Add Material",
                fg=pressedButtonColor,
                bg=buttonColor,
                command=lambda: master.switch_frame("materials"),
                height=1,
                width=11,
                font=(fontType, 13),
            )
            buttonMaterial.grid(row=5, column=0, padx=2)

        if True:  # Vehicle outputs
            i_row = 0
            label = tk.Label(
                calc_IO,
                text="Total Link Weight:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                justify=tk.RIGHT,
            )
            label.grid(row=i_row, column=0, sticky="e")
            label.bind("<1>", lambda event: update_outputs())

            label_V_total_weight = tk.Label(
                calc_IO,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label_V_total_weight.grid(row=i_row, column=1, sticky="w")
            label_V_total_weight.bind("<1>", lambda event: update_outputs())

            if True:  # Rod end Table
                label = tk.Label(
                    calc_RE_table,
                    text="Rod End",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="center",
                    borderwidth=1,
                    relief="groove",
                    width=15,
                )
                label.grid(row=0, column=0, sticky="nesw")
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    calc_RE_table,
                    text="Radial Load",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="center",
                    borderwidth=1,
                    relief="groove",
                    width=10,
                )
                label.grid(row=0, column=1, sticky="nesw")
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    calc_RE_table,
                    text="Weight",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="center",
                    borderwidth=1,
                    relief="groove",
                    width=7,
                )
                label.grid(row=0, column=2, sticky="nesw")
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    calc_RE_table,
                    text="Through Hole\nDiameter",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="center",
                    borderwidth=1,
                    relief="groove",
                    width=11,
                )
                label.grid(row=0, column=3, sticky="nesw")
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    calc_RE_table,
                    text="Shank\nDiameter",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="center",
                    borderwidth=1,
                    relief="groove",
                    width=8,
                )
                label.grid(row=0, column=4, sticky="nesw")
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    calc_RE_table,
                    text="Shank\nThread",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="center",
                    borderwidth=1,
                    relief="groove",
                    width=10,
                )
                label.grid(row=0, column=5, sticky="nesw")
                label.bind("<1>", lambda event: update_outputs())

                for row in range(1, len(constant.rod_ends.name) + 1):
                    label = tk.Label(
                        calc_RE_table,
                        text=constant.rod_ends.name[row - 1],
                        background=bgColor,
                        foreground=entryTextColor,
                        font=(fontType, 15),
                        anchor="w",
                        borderwidth=1,
                        relief="groove",
                    )
                    label.grid(row=row, column=0, sticky="nesw")
                    label.bind("<1>", lambda event: update_outputs())

                    label = tk.Label(
                        calc_RE_table,
                        text="{:,.0f} lb ".format(
                            constant.rod_ends.radial_load[row - 1]
                        ),
                        background=bgColor,
                        foreground=entryTextColor,
                        font=(fontType, 15),
                        anchor="e",
                        borderwidth=1,
                        relief="groove",
                    )
                    label.grid(row=row, column=1, sticky="nesw")
                    label.bind("<1>", lambda event: update_outputs())

                    label = tk.Label(
                        calc_RE_table,
                        text="{:.2f} lb ".format(constant.rod_ends.weight[row - 1]),
                        background=bgColor,
                        foreground=entryTextColor,
                        font=(fontType, 15),
                        anchor="e",
                        borderwidth=1,
                        relief="groove",
                    )
                    label.grid(row=row, column=2, sticky="nesw")
                    label.bind("<1>", lambda event: update_outputs())

                    label = tk.Label(
                        calc_RE_table,
                        text="{:s} in ".format(
                            constant.rod_ends.hole_diameter[row - 1]
                        ),
                        background=bgColor,
                        foreground=entryTextColor,
                        font=(fontType, 15),
                        anchor="e",
                        borderwidth=1,
                        relief="groove",
                    )
                    label.grid(row=row, column=3, sticky="nesw")
                    label.bind("<1>", lambda event: update_outputs())

                    label = tk.Label(
                        calc_RE_table,
                        text="{:,.3f} in ".format(
                            constant.rod_ends.shank_diameter[row - 1]
                        ),
                        background=bgColor,
                        foreground=entryTextColor,
                        font=(fontType, 15),
                        anchor="e",
                        borderwidth=1,
                        relief="groove",
                    )
                    label.grid(row=row, column=4, sticky="nesw")
                    label.bind("<1>", lambda event: update_outputs())

                    label = tk.Label(
                        calc_RE_table,
                        text=constant.rod_ends.thread[row - 1],
                        background=bgColor,
                        foreground=entryTextColor,
                        font=(fontType, 15),
                        anchor="e",
                        borderwidth=1,
                        relief="groove",
                    )
                    label.grid(row=row, column=5, sticky="nesw")
                    label.bind("<1>", lambda event: update_outputs())

            if True:  # Materials Table
                label = tk.Label(
                    calc_material_table,
                    text="Material",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="center",
                    borderwidth=1,
                    relief="groove",
                    width=20,
                )
                label.grid(row=0, column=0, sticky="nesw")
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    calc_material_table,
                    text="Elastic Modulus",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="center",
                    borderwidth=1,
                    relief="groove",
                    width=13,
                )
                label.grid(row=0, column=1, sticky="nesw")
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    calc_material_table,
                    text="Yield Strength",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="center",
                    borderwidth=1,
                    relief="groove",
                    width=12,
                )
                label.grid(row=0, column=2, sticky="nesw")
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    calc_material_table,
                    text="Density",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="center",
                    borderwidth=1,
                    relief="groove",
                    width=11,
                )
                label.grid(row=0, column=3, sticky="nesw")
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(
                    calc_material_table,
                    text="Notes",
                    background=bgColor,
                    foreground=entryTextColor,
                    font=(fontType, 15),
                    anchor="center",
                    borderwidth=1,
                    relief="groove",
                    width=50,
                )
                label.grid(row=0, column=4, sticky="nesw")
                label.bind("<1>", lambda event: update_outputs())

                for row in range(1, len(constant.materials.name) + 1):
                    label = tk.Label(
                        calc_material_table,
                        text=constant.materials.name[row - 1],
                        background=bgColor,
                        foreground=entryTextColor,
                        font=(fontType, 15),
                        anchor="w",
                        borderwidth=1,
                        relief="groove",
                    )
                    label.grid(row=row, column=0, sticky="nesw")
                    label.bind("<1>", lambda event: update_outputs())

                    label = tk.Label(
                        calc_material_table,
                        text="{:,.0f} psi ".format(
                            constant.materials.modulus_elasticity[row - 1]
                        ),
                        background=bgColor,
                        foreground=entryTextColor,
                        font=(fontType, 15),
                        anchor="e",
                        borderwidth=1,
                        relief="groove",
                    )
                    label.grid(row=row, column=1, sticky="nesw")
                    label.bind("<1>", lambda event: update_outputs())

                    label = tk.Label(
                        calc_material_table,
                        text="{:,.0f} psi ".format(
                            constant.materials.yield_strength[row - 1]
                        ),
                        background=bgColor,
                        foreground=entryTextColor,
                        font=(fontType, 15),
                        anchor="e",
                        borderwidth=1,
                        relief="groove",
                    )
                    label.grid(row=row, column=2, sticky="nesw")
                    label.bind("<1>", lambda event: update_outputs())

                    label = tk.Label(
                        calc_material_table,
                        text="{:.3f} lbs/in\u00B3 ".format(
                            constant.materials.density[row - 1]
                        ),
                        background=bgColor,
                        foreground=entryTextColor,
                        font=(fontType, 15),
                        anchor="e",
                        borderwidth=1,
                        relief="groove",
                    )
                    label.grid(row=row, column=3, sticky="nesw")
                    label.bind("<1>", lambda event: update_outputs())

                    label = tk.Label(
                        calc_material_table,
                        text=constant.materials.notes[row - 1],
                        background=bgColor,
                        foreground=entryTextColor,
                        font=(fontType, 15),
                        anchor="w",
                        borderwidth=1,
                        relief="groove",
                    )
                    label.grid(row=row, column=4, sticky="nesw")
                    label.bind("<1>", lambda event: update_outputs())

        def update_outputs(*args):
            self.focus_set()
            plots_changed = False

            if self.opening:
                plots_changed = True
                self.opening = False
            else:
                if True:  # Get Front Inputs
                    if True:  # Upper
                        if inputs.F.U_OD != float(F_U_OD.get()):
                            inputs.F.U_OD = float(F_U_OD.get())
                            plots_changed = True
                        if F_U_solid.get() == "Yes" and inputs.F.U_solid == False:
                            inputs.F.U_solid = True
                            plots_changed = True
                        elif F_U_solid.get() == "No" and inputs.F.U_solid == True:
                            inputs.F.U_solid = False
                            inputs.F.U_wall = float(F_U_thickness.get())
                            plots_changed = True
                        if (
                            inputs.F.U_wall != float(F_U_thickness.get())
                            and inputs.F.U_solid == False
                        ):
                            inputs.F.U_wall = float(F_U_thickness.get())
                            plots_changed = True
                        if inputs.F.U_material != F_U_material.get():
                            inputs.F.U_material = F_U_material.get()
                            plots_changed = True
                        if inputs.F.U_rod_end != F_U_RE.get():
                            inputs.F.U_rod_end = F_U_RE.get()
                            plots_changed = True

                    if True:  # Lower
                        if inputs.F.L_OD != float(F_L_OD.get()):
                            inputs.F.L_OD = float(F_L_OD.get())
                            plots_changed = True
                        if F_L_solid.get() == "Yes" and inputs.F.L_solid == False:
                            inputs.F.L_solid = True
                            plots_changed = True
                        elif F_L_solid.get() == "No" and inputs.F.L_solid == True:
                            inputs.F.L_solid = False
                            inputs.F.L_wall = float(F_L_thickness.get())
                            plots_changed = True
                        if (
                            inputs.F.L_wall != float(F_L_thickness.get())
                            and inputs.F.L_solid == False
                        ):
                            inputs.F.L_wall = float(F_L_thickness.get())
                            plots_changed = True
                        if inputs.F.L_material != F_L_material.get():
                            inputs.F.L_material = F_L_material.get()
                            plots_changed = True
                        if inputs.F.L_rod_end != F_L_RE.get():
                            inputs.F.L_rod_end = F_L_RE.get()
                            plots_changed = True

                    if constant.F.panhard:  # Panhard
                        if inputs.F.P_OD != float(F_P_OD.get()):
                            inputs.F.P_OD = float(F_P_OD.get())
                            plots_changed = True
                        if F_P_solid.get() == "Yes" and inputs.F.P_solid == False:
                            inputs.F.P_solid = True
                            plots_changed = True
                        elif F_P_solid.get() == "No" and inputs.F.P_solid == True:
                            inputs.F.P_solid = False
                            inputs.F.P_wall = float(F_P_thickness.get())
                            plots_changed = True
                        if (
                            inputs.F.P_wall != float(F_P_thickness.get())
                            and inputs.F.P_solid == False
                        ):
                            inputs.F.P_wall = float(F_P_thickness.get())
                            plots_changed = True
                        if inputs.F.P_material != F_P_material.get():
                            inputs.F.P_material = F_P_material.get()
                            plots_changed = True
                        if inputs.F.P_rod_end != F_P_RE.get():
                            inputs.F.P_rod_end = F_P_RE.get()
                            plots_changed = True

                if True:  # Get Rear Inputs
                    if True:  # Upper
                        if inputs.R.U_OD != float(R_U_OD.get()):
                            inputs.R.U_OD = float(R_U_OD.get())
                            plots_changed = True
                        if R_U_solid.get() == "Yes" and inputs.R.U_solid == False:
                            inputs.R.U_solid = True
                            plots_changed = True
                        elif R_U_solid.get() == "No" and inputs.R.U_solid == True:
                            inputs.R.U_solid = False
                            inputs.R.U_wall = float(R_U_thickness.get())
                            plots_changed = True
                        if (
                            inputs.R.U_wall != float(R_U_thickness.get())
                            and inputs.R.U_solid == False
                        ):
                            inputs.R.U_wall = float(R_U_thickness.get())
                            plots_changed = True
                        if inputs.R.U_material != R_U_material.get():
                            inputs.R.U_material = R_U_material.get()
                            plots_changed = True
                        if inputs.R.U_rod_end != R_U_RE.get():
                            inputs.R.U_rod_end = R_U_RE.get()
                            plots_changed = True

                    if True:  # Lower
                        if inputs.R.L_OD != float(R_L_OD.get()):
                            inputs.R.L_OD = float(R_L_OD.get())
                            plots_changed = True
                        if R_L_solid.get() == "Yes" and inputs.R.L_solid == False:
                            inputs.R.L_solid = True
                            plots_changed = True
                        elif R_L_solid.get() == "No" and inputs.R.L_solid == True:
                            inputs.R.L_solid = False
                            inputs.R.L_wall = float(R_L_thickness.get())
                            plots_changed = True
                        if (
                            inputs.R.L_wall != float(R_L_thickness.get())
                            and inputs.R.L_solid == False
                        ):
                            inputs.R.L_wall = float(R_L_thickness.get())
                            plots_changed = True
                        if inputs.R.L_material != R_L_material.get():
                            inputs.R.L_material = R_L_material.get()
                            plots_changed = True
                        if inputs.R.L_rod_end != R_L_RE.get():
                            inputs.R.L_rod_end = R_L_RE.get()
                            plots_changed = True

                    if constant.R.panhard:  # Panhard
                        if inputs.R.P_OD != float(R_P_OD.get()):
                            inputs.R.P_OD = float(R_P_OD.get())
                            plots_changed = True
                        if R_P_solid.get() == "Yes" and inputs.R.P_solid == False:
                            inputs.R.P_solid = True
                            plots_changed = True
                        elif R_P_solid.get() == "No" and inputs.R.P_solid == True:
                            inputs.R.P_solid = False
                            inputs.R.P_wall = float(R_P_thickness.get())
                            plots_changed = True
                        if (
                            inputs.R.P_wall != float(R_P_thickness.get())
                            and inputs.R.P_solid == False
                        ):
                            inputs.R.P_wall = float(R_P_thickness.get())
                            plots_changed = True
                        if inputs.R.P_material != R_P_material.get():
                            inputs.R.P_material = R_P_material.get()
                            plots_changed = True
                        if inputs.R.P_rod_end != R_P_RE.get():
                            inputs.R.P_rod_end = R_P_RE.get()
                            plots_changed = True

            if True:  # Get Vehicle Inputs
                if inputs.V.Desired_FS_Yield != float(V_FS_yield.get()):
                    inputs.V.Desired_FS_Yield = float(V_FS_yield.get())
                    plots_changed = True
                if inputs.V.Desired_FS_Buckling != float(V_FS_buckling.get()):
                    inputs.V.Desired_FS_Buckling = float(V_FS_buckling.get())
                    plots_changed = True
                if inputs.V.Desired_FS_Bending != float(V_FS_bending.get()):
                    inputs.V.Desired_FS_Bending = float(V_FS_bending.get())
                    plots_changed = True
                if inputs.V.Desired_FS_RE != float(V_FS_RE.get()):
                    inputs.V.Desired_FS_RE = float(V_FS_RE.get())
                    plots_changed = True
                if inputs.V.Desired_FS_Dent != float(V_FS_Dent.get()):
                    inputs.V.Desired_FS_Dent = float(V_FS_Dent.get())
                    plots_changed = True

            run_link_sizing()

            if True:  # Darken unavailable options
                if inputs.F.U_solid:
                    F_U_thickness.config(fg=bgColor)
                else:
                    F_U_thickness.config(fg=entryTextColor)
                if inputs.F.L_solid:
                    F_L_thickness.config(fg=bgColor)
                else:
                    F_L_thickness.config(fg=entryTextColor)
                if constant.F.panhard:
                    if inputs.F.P_solid:
                        F_P_thickness.config(fg=bgColor)
                    else:
                        F_P_thickness.config(fg=entryTextColor)

                if inputs.R.U_solid:
                    R_U_thickness.config(fg=bgColor)
                else:
                    R_U_thickness.config(fg=entryTextColor)
                if inputs.R.L_solid:
                    R_L_thickness.config(fg=bgColor)
                else:
                    R_L_thickness.config(fg=entryTextColor)
                if constant.R.panhard:
                    if inputs.R.P_solid:
                        R_P_thickness.config(fg=bgColor)
                    else:
                        R_P_thickness.config(fg=entryTextColor)

            if plots_changed:
                if True:  # Update Text Outputs
                    if True:  # Front Upper
                        label_F_U_RE_thread.config(text="{}".format(outputs.F.U_Thread))
                        label_F_U_RE_hole.config(text="{}".format(outputs.F.U_Hole))
                        label_F_U_RE_weight.config(
                            text="{:.1f} {}".format(outputs.F.U_RE_Weight, S.mass_units)
                        )
                        label_F_U_link_weight.config(
                            text="{:.1f} {}".format(
                                outputs.F.U_Link_Weight, S.mass_units
                            )
                        )
                        label_F_U_weight.config(
                            text="{:.1f} {}".format(outputs.F.U_Weight, S.mass_units)
                        )
                        label_F_U_FS_yield.config(
                            text="{:.2f}".format(outputs.F.U_FS_Yield)
                        )
                        label_F_U_FS_buckling.config(
                            text="{:.2f}".format(outputs.F.U_FS_buckling)
                        )
                        label_F_U_FS_bending.config(
                            text="{:.2f}".format(outputs.F.U_FS_bending)
                        )
                        label_F_U_FS_RE.config(text="{:.2f}".format(outputs.F.U_FS_RE))
                        label_F_U_dent_resist.config(
                            text="{:.2f}".format(outputs.F.U_Dent_Resistance)
                        )
                    if True:  # Front Lower
                        label_F_L_RE_thread.config(text="{}".format(outputs.F.L_Thread))
                        label_F_L_RE_hole.config(text="{}".format(outputs.F.L_Hole))
                        label_F_L_RE_weight.config(
                            text="{:.1f} {}".format(outputs.F.L_RE_Weight, S.mass_units)
                        )
                        label_F_L_link_weight.config(
                            text="{:.1f} {}".format(
                                outputs.F.L_Link_Weight, S.mass_units
                            )
                        )
                        label_F_L_weight.config(
                            text="{:.1f} {}".format(outputs.F.L_Weight, S.mass_units)
                        )
                        label_F_L_FS_yield.config(
                            text="{:.2f}".format(outputs.F.L_FS_Yield)
                        )
                        label_F_L_FS_buckling.config(
                            text="{:.2f}".format(outputs.F.L_FS_buckling)
                        )
                        label_F_L_FS_bending.config(
                            text="{:.2f}".format(outputs.F.L_FS_bending)
                        )
                        label_F_L_FS_RE.config(text="{:.2f}".format(outputs.F.L_FS_RE))
                        label_F_L_dent_resist.config(
                            text="{:.2f}".format(outputs.F.L_Dent_Resistance)
                        )
                    if constant.F.panhard:  # Front Panhard
                        label_F_P_RE_thread.config(text="{}".format(outputs.F.P_Thread))
                        label_F_P_RE_hole.config(text="{}".format(outputs.F.P_Hole))
                        label_F_P_RE_weight.config(
                            text="{:.1f} {}".format(outputs.F.P_RE_Weight, S.mass_units)
                        )
                        label_F_P_link_weight.config(
                            text="{:.1f} {}".format(
                                outputs.F.P_Link_Weight, S.mass_units
                            )
                        )
                        label_F_P_weight.config(
                            text="{:.1f} {}".format(outputs.F.P_Weight, S.mass_units)
                        )
                        label_F_P_FS_yield.config(
                            text="{:.2f}".format(outputs.F.P_FS_Yield)
                        )
                        label_F_P_FS_buckling.config(
                            text="{:.2f}".format(outputs.F.P_FS_buckling)
                        )
                        label_F_P_FS_bending.config(
                            text="{:.2f}".format(outputs.F.P_FS_bending)
                        )
                        label_F_P_FS_RE.config(text="{:.2f}".format(outputs.F.P_FS_RE))
                        label_F_P_dent_resist.config(
                            text="{:.2f}".format(outputs.F.P_Dent_Resistance)
                        )
                    if True:  # Rear Upper
                        label_R_U_RE_thread.config(text="{}".format(outputs.R.U_Thread))
                        label_R_U_RE_hole.config(text="{}".format(outputs.R.U_Hole))
                        label_R_U_RE_weight.config(
                            text="{:.1f} {}".format(outputs.R.U_RE_Weight, S.mass_units)
                        )
                        label_R_U_link_weight.config(
                            text="{:.1f} {}".format(
                                outputs.R.U_Link_Weight, S.mass_units
                            )
                        )
                        label_R_U_weight.config(
                            text="{:.1f} {}".format(outputs.R.U_Weight, S.mass_units)
                        )
                        label_R_U_FS_yield.config(
                            text="{:.2f}".format(outputs.R.U_FS_Yield)
                        )
                        label_R_U_FS_buckling.config(
                            text="{:.2f}".format(outputs.R.U_FS_buckling)
                        )
                        label_R_U_FS_bending.config(
                            text="{:.2f}".format(outputs.R.U_FS_bending)
                        )
                        label_R_U_FS_RE.config(text="{:.2f}".format(outputs.R.U_FS_RE))
                        label_R_U_dent_resist.config(
                            text="{:.2f}".format(outputs.R.U_Dent_Resistance)
                        )
                    if True:  # Rear Lower
                        label_R_L_RE_thread.config(text="{}".format(outputs.R.L_Thread))
                        label_R_L_RE_hole.config(text="{}".format(outputs.R.L_Hole))
                        label_R_L_RE_weight.config(
                            text="{:.1f} {}".format(outputs.R.L_RE_Weight, S.mass_units)
                        )
                        label_R_L_link_weight.config(
                            text="{:.1f} {}".format(
                                outputs.R.L_Link_Weight, S.mass_units
                            )
                        )
                        label_R_L_weight.config(
                            text="{:.1f} {}".format(outputs.R.L_Weight, S.mass_units)
                        )
                        label_R_L_FS_yield.config(
                            text="{:.2f}".format(outputs.R.L_FS_Yield)
                        )
                        label_R_L_FS_buckling.config(
                            text="{:.2f}".format(outputs.R.L_FS_buckling)
                        )
                        label_R_L_FS_bending.config(
                            text="{:.2f}".format(outputs.R.L_FS_bending)
                        )
                        label_R_L_FS_RE.config(text="{:.2f}".format(outputs.R.L_FS_RE))
                        label_R_L_dent_resist.config(
                            text="{:.2f}".format(outputs.R.L_Dent_Resistance)
                        )
                    if constant.R.panhard:  # Rear Panhard
                        label_R_P_RE_thread.config(text="{}".format(outputs.R.P_Thread))
                        label_R_P_RE_hole.config(text="{}".format(outputs.R.P_Hole))
                        label_R_P_RE_weight.config(
                            text="{:.1f} {}".format(outputs.R.P_RE_Weight, S.mass_units)
                        )
                        label_R_P_link_weight.config(
                            text="{:.1f} {}".format(
                                outputs.R.P_Link_Weight, S.mass_units
                            )
                        )
                        label_R_P_weight.config(
                            text="{:.1f} {}".format(outputs.R.P_Weight, S.mass_units)
                        )
                        label_R_P_FS_yield.config(
                            text="{:.2f}".format(outputs.R.P_FS_Yield)
                        )
                        label_R_P_FS_buckling.config(
                            text="{:.2f}".format(outputs.R.P_FS_buckling)
                        )
                        label_R_P_FS_bending.config(
                            text="{:.2f}".format(outputs.R.P_FS_bending)
                        )
                        label_R_P_FS_RE.config(text="{:.2f}".format(outputs.R.P_FS_RE))
                        label_R_P_dent_resist.config(
                            text="{:.2f}".format(outputs.R.P_Dent_Resistance)
                        )
                    label_V_total_weight.config(
                        text="{:.1f} {}".format(
                            outputs.V.Combined_Link_Weight, S.mass_units
                        )
                    )

                if True:  # Update FS box colors
                    if outputs.F.U_FS_Yield > inputs.V.Desired_FS_Yield:
                        label_F_U_FS_yield.config(bg=FSPassColor)
                    else:
                        label_F_U_FS_yield.config(bg=FSFailColor)
                    if outputs.F.U_FS_buckling > inputs.V.Desired_FS_Buckling:
                        label_F_U_FS_buckling.config(bg=FSPassColor)
                    else:
                        label_F_U_FS_buckling.config(bg=FSFailColor)
                    if outputs.F.U_FS_bending > inputs.V.Desired_FS_Bending:
                        label_F_U_FS_bending.config(bg=FSPassColor)
                    else:
                        label_F_U_FS_bending.config(bg=FSFailColor)
                    if outputs.F.U_FS_RE > inputs.V.Desired_FS_RE:
                        label_F_U_FS_RE.config(bg=FSPassColor)
                    else:
                        label_F_U_FS_RE.config(bg=FSFailColor)
                    if outputs.F.U_Dent_Resistance > inputs.V.Desired_FS_Dent:
                        label_F_U_dent_resist.config(bg=FSPassColor)
                    else:
                        label_F_U_dent_resist.config(bg=FSFailColor)

                    if outputs.F.L_FS_Yield > inputs.V.Desired_FS_Yield:
                        label_F_L_FS_yield.config(bg=FSPassColor)
                    else:
                        label_F_L_FS_yield.config(bg=FSFailColor)
                    if outputs.F.L_FS_buckling > inputs.V.Desired_FS_Buckling:
                        label_F_L_FS_buckling.config(bg=FSPassColor)
                    else:
                        label_F_L_FS_buckling.config(bg=FSFailColor)
                    if outputs.F.L_FS_bending > inputs.V.Desired_FS_Bending:
                        label_F_L_FS_bending.config(bg=FSPassColor)
                    else:
                        label_F_L_FS_bending.config(bg=FSFailColor)
                    if outputs.F.L_FS_RE > inputs.V.Desired_FS_RE:
                        label_F_L_FS_RE.config(bg=FSPassColor)
                    else:
                        label_F_L_FS_RE.config(bg=FSFailColor)
                    if outputs.F.L_Dent_Resistance > inputs.V.Desired_FS_Dent:
                        label_F_L_dent_resist.config(bg=FSPassColor)
                    else:
                        label_F_L_dent_resist.config(bg=FSFailColor)

                    if constant.F.panhard:
                        if outputs.F.P_FS_Yield > inputs.V.Desired_FS_Yield:
                            label_F_P_FS_yield.config(bg=FSPassColor)
                        else:
                            label_F_P_FS_yield.config(bg=FSFailColor)
                        if outputs.F.P_FS_buckling > inputs.V.Desired_FS_Buckling:
                            label_F_P_FS_buckling.config(bg=FSPassColor)
                        else:
                            label_F_P_FS_buckling.config(bg=FSFailColor)
                        if outputs.F.P_FS_bending > inputs.V.Desired_FS_Bending:
                            label_F_P_FS_bending.config(bg=FSPassColor)
                        else:
                            label_F_P_FS_bending.config(bg=FSFailColor)
                        if outputs.F.P_FS_RE > inputs.V.Desired_FS_RE:
                            label_F_P_FS_RE.config(bg=FSPassColor)
                        else:
                            label_F_P_FS_RE.config(bg=FSFailColor)
                        if outputs.F.P_Dent_Resistance > inputs.V.Desired_FS_Dent:
                            label_F_P_dent_resist.config(bg=FSPassColor)
                        else:
                            label_F_P_dent_resist.config(bg=FSFailColor)

                    if outputs.R.U_FS_Yield > inputs.V.Desired_FS_Yield:
                        label_R_U_FS_yield.config(bg=FSPassColor)
                    else:
                        label_R_U_FS_yield.config(bg=FSFailColor)
                    if outputs.R.U_FS_buckling > inputs.V.Desired_FS_Buckling:
                        label_R_U_FS_buckling.config(bg=FSPassColor)
                    else:
                        label_R_U_FS_buckling.config(bg=FSFailColor)
                    if outputs.R.U_FS_bending > inputs.V.Desired_FS_Bending:
                        label_R_U_FS_bending.config(bg=FSPassColor)
                    else:
                        label_R_U_FS_bending.config(bg=FSFailColor)
                    if outputs.R.U_FS_RE > inputs.V.Desired_FS_RE:
                        label_R_U_FS_RE.config(bg=FSPassColor)
                    else:
                        label_R_U_FS_RE.config(bg=FSFailColor)
                    if outputs.R.U_Dent_Resistance > inputs.V.Desired_FS_Dent:
                        label_R_U_dent_resist.config(bg=FSPassColor)
                    else:
                        label_R_U_dent_resist.config(bg=FSFailColor)

                    if outputs.R.L_FS_Yield > inputs.V.Desired_FS_Yield:
                        label_R_L_FS_yield.config(bg=FSPassColor)
                    else:
                        label_R_L_FS_yield.config(bg=FSFailColor)
                    if outputs.R.L_FS_buckling > inputs.V.Desired_FS_Buckling:
                        label_R_L_FS_buckling.config(bg=FSPassColor)
                    else:
                        label_R_L_FS_buckling.config(bg=FSFailColor)
                    if outputs.R.L_FS_bending > inputs.V.Desired_FS_Bending:
                        label_R_L_FS_bending.config(bg=FSPassColor)
                    else:
                        label_R_L_FS_bending.config(bg=FSFailColor)
                    if outputs.R.L_FS_RE > inputs.V.Desired_FS_RE:
                        label_R_L_FS_RE.config(bg=FSPassColor)
                    else:
                        label_R_L_FS_RE.config(bg=FSFailColor)
                    if outputs.R.L_Dent_Resistance > inputs.V.Desired_FS_Dent:
                        label_R_L_dent_resist.config(bg=FSPassColor)
                    else:
                        label_R_L_dent_resist.config(bg=FSFailColor)

                    if constant.R.panhard:
                        if outputs.R.P_FS_Yield > inputs.V.Desired_FS_Yield:
                            label_R_P_FS_yield.config(bg=FSPassColor)
                        else:
                            label_R_P_FS_yield.config(bg=FSFailColor)
                        if outputs.R.P_FS_buckling > inputs.V.Desired_FS_Buckling:
                            label_R_P_FS_buckling.config(bg=FSPassColor)
                        else:
                            label_R_P_FS_buckling.config(bg=FSFailColor)
                        if outputs.R.P_FS_bending > inputs.V.Desired_FS_Bending:
                            label_R_P_FS_bending.config(bg=FSPassColor)
                        else:
                            label_R_P_FS_bending.config(bg=FSFailColor)
                        if outputs.R.P_FS_RE > inputs.V.Desired_FS_RE:
                            label_R_P_FS_RE.config(bg=FSPassColor)
                        else:
                            label_R_P_FS_RE.config(bg=FSFailColor)
                        if outputs.R.P_Dent_Resistance > inputs.V.Desired_FS_Dent:
                            label_R_P_dent_resist.config(bg=FSPassColor)
                        else:
                            label_R_P_dent_resist.config(bg=FSFailColor)

        if True:  # Detect out of input click
            self.bind("<1>", lambda event: update_outputs())
            calc_front.bind("<1>", lambda event: update_outputs())
            front_upper.bind("<1>", lambda event: update_outputs())
            front_lower.bind("<1>", lambda event: update_outputs())
            front_panhard.bind("<1>", lambda event: update_outputs())
            calc_rear.bind("<1>", lambda event: update_outputs())
            rear_upper.bind("<1>", lambda event: update_outputs())
            rear_lower.bind("<1>", lambda event: update_outputs())
            rear_panhard.bind("<1>", lambda event: update_outputs())

        if True:  # Update with option menu change
            F_U_solid.trace_add("write", update_outputs)
            F_L_solid.trace_add("write", update_outputs)
            F_P_solid.trace_add("write", update_outputs)
            F_U_material.trace_add("write", update_outputs)
            F_L_material.trace_add("write", update_outputs)
            F_P_material.trace_add("write", update_outputs)
            F_U_RE.trace_add("write", update_outputs)
            F_L_RE.trace_add("write", update_outputs)
            F_P_RE.trace_add("write", update_outputs)
            R_U_solid.trace_add("write", update_outputs)
            R_L_solid.trace_add("write", update_outputs)
            R_P_solid.trace_add("write", update_outputs)
            R_U_material.trace_add("write", update_outputs)
            R_L_material.trace_add("write", update_outputs)
            R_P_material.trace_add("write", update_outputs)
            R_U_RE.trace_add("write", update_outputs)
            R_L_RE.trace_add("write", update_outputs)
            R_P_RE.trace_add("write", update_outputs)

        update_outputs()

        def load_from_file():
            load_susp()
            master.switch_frame("linkSizing")
