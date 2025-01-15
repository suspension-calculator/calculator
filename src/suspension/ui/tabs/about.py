# src/suspension/ui/tabs/about.py

# IO Imports
from tool_io.initialize_IO import *
from tool_io.save_suspension import save_susp, save_as_susp
from tool_io.load_suspension import load_susp

# UI Imports
from ui.styles import *

# Library Imports
import tkinter as tk
import tkinter.scrolledtext as st
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from math import cos, sin, radians


class aboutPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
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
                fg=buttonColor,
                bg=pressedButtonColor,
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

        if True:  # Frame setup
            infoFrame = tk.Frame(self, bg=bgColor)
            infoFrame.grid(row=2, column=0, sticky="n")
            RevisionHistoryFrame = tk.Frame(self, bg=bgColor)
            RevisionHistoryFrame.grid(row=2, column=2, rowspan=2, sticky="ns")
            coordFrame = tk.Frame(self, bg=bgColor)
            coordFrame.grid(row=1, column=1, sticky="nsew", rowspan=2)

        if True:  # About Section
            label = tk.Label(
                self,
                text="Read Me",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 20),
                anchor="w",
            )
            label.grid(row=1, column=0, pady=1)

            i_row = 0

            label = tk.Label(
                infoFrame,
                text="The unit system can be selected under settings. The options are the Metric system and the Imperial system.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="Other setting include number of travel points, front X inversion, and if tire loading should me simulated",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="The link arrangement, at either end, can be:",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="4 link (2 upper + 2 lower), 3 link (1 upper + 2 lower) plus panhard, or 4 link (2 upper + 2 lower) plus panhard.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="When there are more than 4 links, e.g. 4 link plus panhard (AKA 5 link) the suspension is said to be “over-constrained” and rigid links will prevent articulation.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="Vehicles with factory fitted 4 link plus panhard suspension overcome the binding to some extent by making the upper and lower links close to parallel and using flexible bushes in the link joints.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="Another problem with over-constrained suspension, e.g. radius arms, or 4 link plus panhard, is that some properties such as roll axis inclination can't easily be calculated with certainty.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="The calculator doesn't care nor check for binding during suspension travel or articulation – user beware if you use this to simulate radius arm or 4 link plus panhard suspension.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="The datum (0.00) for all x coordinates is the center of the rear axle, with x coordinates increasing in the direction from rear to front axle, i.e. positive to the right, negative to left of rear axle.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="For convenience with front suspension data entry only, a pseudo X' coordinate has been added, where X' is measured in the x direction from the center of the front axle.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="The user can choose to use the global sign convensions",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="The calculator will automatically calculate the true X coordinates by adding the wheelbase to the X' values.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="The Driveshafts and Shocks also uses the pseudo X' coordinate.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="On Link Calculator, the movement of points due to suspension travel are plotted with respect to the body being held fixed.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="On Vehicle Pitch, links are ploted with respect to level ground.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="Anti-squat for the rear suspension, and anti-lift for the front suspension is calculated for the case of forward acceleration.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="Anti-dive for the front suspension, and anti-lift for the rear suspension is calculated for the case of braking.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="If all of the drive is transmitted through the rear wheels (front drive bias = 0%), i.e. rear two wheel drive, anti-squat will be high and anti-lift at the front suspension will be zero.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="If the drive is split/shared between rear and front wheels, i.e. four wheel drive, the value for anti-squat will reduce and anti-lift (front) will increase. For example, if the drive split is 50%/50%",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="  the anti-squat will be 0.50 times what it would be in two wheel drive, for the same suspension geometry – note earlier versions of the calculator assume front drive bias = 0% (two wheel drive).",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="If the transfer case has a non-biasing open center diff, the drive bias will be 50% to both the rear and front axles. If the center diff is locked, or the transfer case has no center diff the",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="  rear and front drive shafts will be forced to turn at the same speed and the drive bias will be governed by the rear/front traction. For example, if insignificant front traction, front drive bias can be 0%",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="The amount of weight/force transfer during acceleration/braking that induces squat/dive  = [acceleration x sprung mass x height of center of gravity of sprung mass / wheelbase]",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="The spreadsheet calculates sprung mass by subtracting the unsprung mass from the vehicle mass. The height of center of gravity of sprung mass is calculated using",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="  the height of the vehicle center of gravity, the vehicle mass, rear and front unsprung masses. Guessing or disregarding those values will affect the accuracy of some calculations, so use your best estimates.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="For rear suspension links the forces are calculated assuming all of the drive force is transferred through the rear wheels (worse case).",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="For front suspension links the forces are calculated assuming all of the braking force is transferred through the front wheels.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="The forces do not account for the change in force from the coilovers.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="If you are only interested in the suspension at the rear axle (or only at the front axle), you only need to change the link geometry for the axle you are interested in",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="  and leave the link geometry for the other axle “as is”. That won't affect the results for the suspension you are interested in, but you should ignore results for the other axle and vehicle roll axis.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="For simplicity of calculation, the nominated wheel travel, up (bump) or down (droop) is assumed to apply at the axle end of the lower links.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1
            label = tk.Label(
                infoFrame,
                text="The error resulting from this assumption is negligible when thepinion rotation is small.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="The effect of sideways motion from the panhard bar is not accounted for in squat, dive, lift, and spring rate calculations. ",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

            label = tk.Label(
                infoFrame,
                text="Coilover can be used to find installation ratios and mounting location for air shocks and struts. Information related to the springs should be disregarded in such cases.",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=i_row, column=0, sticky="w")
            i_row = i_row + 1

        if True:  # Version History
            label = tk.Label(
                self,
                text="Version History",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=1, column=2, pady=1)

            revisionArea = st.ScrolledText(
                RevisionHistoryFrame,
                width=70,
                height=70,
                font=(fontType, 15),
                bg=bgColor,
                fg=entryTextColor,
                relief="flat",
            )
            revisionArea.grid(row=0, column=0)

            revisionArea.insert(
                tk.INSERT,
                """\
1.5b     2003.12.05
    Corrections to the roll center calculation.
    Additional "unit" descriptors added.
    Added Coordinate System Diagram Sheet.
1.5c     2003.12.07
    Added more materials and properties to pulldown menus
    Added calculation for link weight, based on length and material
    density
    Fixed typo in cell D53
    Deleted comment in C54
    Revised wording in D44 to better explain FS Bending for upper
    link
    Deleted comments in D23 and J23  (Dan's explanation of
    "symmetrical roll center")
    Slight changes to column widths for consistency between "like"
    data columns
    Minor Color changes and cell alignment changes to aid
    readability
1.5d     2003.12.19
    Changed link weight calculations to use values already
    calculated.
    Moved tables that were outside of normal viewing area.
    Fixed typo in D48
    Rearranged order
    Added units to vector components
    Changed the "created by" list to alphabetical order ;)
    Added Comments to Input Values With Coordinates
    Added Coordinate System Diagram Sheet

2.0      2004.01.007
    Added Graphical Display
    Flipped Coordinate System Drawing to Match Graphical
    Display
    Fixed Typos in comments
    Moved Cells and Removed Blank Lines
    Fixed Units in Material Specs
2.1      2004.02.01
Was called ExcelCAD
    Moved graphical charts to main page
    Aligned Top-View to be in same scale and proportion with side
    view
    Restored graphic conventions  (Solid lines = real links,
    Dashed lines = calculated values)
    Added New Input section to accept more "conventional"
    measurements and extrapolate them into the necessary x, y,
    z coordinate system.  (i.e.  Separation values)
    Moved graphical coordinates for tires & other vector data to
    front page (off screen to right)
    Minor changes to allow longer lines for "Actual A.S" and "100%
    Antisquat" beyond the stated wheelbase
    Moved all "User Definable" data into a single column for easier
    online collaboration and sharing of values
    Changed color scheme for consistency and to aid readability
    (Blue = Upper links, Red= Lower Links)

3.0      2004.12.04
    Added Bump/Droop travel calculation sheet w/ macro
    Rearranged to make it less cluttered and more user friendly
    Added Calculation of Sprung Mass CG & Anti-Squat CG
    (CG - rear axle)
    Changed all calculations that used CG to Anti-Squat CG
    Fixed Errors When Bars are Parallel
    Added Automatic Display of Roll Understeer/Oversteer
    Saved as Excel 5.0/97 File
3.0c     2005.04.01
    Added driveshaft angle and plunge calculations, not complete!
    Fixed Anti-Squat CG Height Calculation
3.1     2007.05.08
Revision by Chris Manock (Vetteboy79)
    Changed travel calculations to not require solver add-in
    Added travel chart to front page
    Added travel specs to front page

4.0      2016.09.03
Revision by Bush65
    Added Front Suspension
    Added Front Axle Bias options for 4WD Acceleration and
    Braking to Main page
    Added anti-lift calculations for front suspension during
    acceleration in 4WD
    Added anti-dive calculations for front suspension during
    braking
    Added anti-lift calculations for rear suspension during
    braking
    Added options to allow suspension to be 4-link, 3-link +
    panhard, or 4-link + panhard
    Macros no longer used, travel calculations now only up,
    half-up, half-down and down
    General, but not thorough clean-up
4.1      2020.06.13
Revision by Treefrog
    Added Front Links to Material Page
    Added rod ends and Factor of Safety check to Material page
    Fixed full droop of upper links not plotting correctly
    Changed Material page forces to max forces on link
    Changed pinion angle calculation, added effect, added image
    to Coordinate page
    Added panhard bars to Material Page
    Added link separation angles
    General formatting clean up and unification
    Changed rear variable names to be more consistent with front
    variable names
    Added F/R weight bias and sprung CG to roll axis distance
4.1.1    2020.06.18
Revision by Treefrog
    Fixed error in pinion angle calculation
    Added roll over angle calculations

5.0      2020.07.08
Revision by Treefrog
    Added Coilovers
    Renamed Materials to Link Sizing
    Renamed Main To Link Calculator
    Added closet spring rates
    Added chosen spring rates
    Added install ratio calculations and plots
    Added wheel rate and wheel force calculations and plots
    Added rate selection approach
    Reordering of sheets
5.1      2020.07.27
Revision by Treefrog
    Added total link weight to Link Sizing
    Changed Link Sizing material and rod end list lookups to no
    longer require sorting
    Added Minimum FS to Link Sizing
    Fixed rod end FS force
    Fixed link forces cell links in FS calculations
    More cleanup, spelling fixes, and clarified value labels
    Added recommendations to Link Sizing
    Fixed initial wheel rate calculations
5.2      2020.08.09
Revision by Treefrog
    More cleanup and fixes regarding correct displaying of values
    Fixed preload calculations
    Fixed initial wheel rate calculation not accounting for preload
    Fixed some front coilover values using rear mounting style
    Added bypass calculations
    Added bypasses to plots and bypass ratio plots
    Added ability to toggle bypasses on plots
    Renamed Coilover sheet to Shocks
    Fixed front link install ratio using rear link mounting points
    Rearranged info presentation on Shocks
5.3      2020.12.09
Revision by Treefrog
    Wording Change
    Dent Resistance Comparison
    Travel results now account for the movement of the tire ground
    contact point
    Change from lowest FoS to target FoS on sizing
    Account for wheelbase change and travel change in anti calcs
    Added target shock lengths
5.4      2020.12.23
Revision by Treefrog
    Plots now use the correct track width
    Fix to bypass result white outing
    Added portal height to plots
    Added Driveshaft Length and U-joint angle calculations
5.5      2020.12.28
Revision by Treefrog
    Link sizing lookups now links to tables instead of cells
    Link Sizing Selection menus link to tables instead of cells

6.0      2021.02.18
Revision by Treefrog
    Sheet title added to version display
    Calculations separated to Calculations and Plots
    Moved calculations from Link Sizing to Calculations
    Added solid link option to Link Sizing
    Added shank diameter vs link diameter and wall thickness
    checks to Link Sizing
    Added selectable dual rate stops to Shocks
    Moved Chosen Spring Rates on Shocks
    Simplified closest spring selection formula
    Added show on plot toggles
    Added wheel center path on side view plot
    Added body roll axis on side view plot
    Simplified link force output
    Rearraigned vehicle data outputs
    Changed front pinion angle change to follow rear sign
    convention
    Changed data presentation on Link Calculator
    Increased resolution of travel data
    Portal height offset now used for unspung mass CG height
    calculation
    Added highlight travel position
    Plots now hide convergence lines if parallel
    Changed how not used fields on Shocks are hidden
    Added minimum distance between bypasses and coilovers
    Added minimum distance from bypasses and coilovers to body
    roll axis
    Added support for metric
    Changed coil slider stop from 50% up to user input
    Added Vehicle Pitch sheet
    Added plots to shot side view of vehicle undergoing
    acceleration
    Added calculations to predict steady state travel amounts for
    various accelerations
    Added values of interest to Vehicle Pitch
    Updated and fixed Read Me
    Changed bias inputs from decimal to percent
    Changed input method for pinion yoke location
    Added data input validation where possible
    Moved majority of cell input prompts from notes to input
    messages
6.1      2021.03.07
Revision by Treefrog
    Fixed wrong cell link on Vehicle Pitch
    Put limits on coilover stop location
    Filled in early development history
    Readded gridlines on Link Calculator
    Fixed 100% antidive equation
    Readded axis numbers on Link Calculator
    Fixed front lower roll point equation
    Fixed anti equations dealing with brake bias
6.2      2021.04.12
Revision by Treefrog
    Fixed vehicle pitch front roll center equation
6.3      2021.04.30
Revision by Treefrog
    Fixed anti graphs in metric mode
    Gradient added to panhard bars
    Added full bump and full droop plots to Vehicle Pitch
    Added combined acceleration and slope to Vehicle Pitch
    predictions
    Fixed front axle location in Vehicle Pitch
    Added bias prediction to Vehicle Pitch
    Vehicle Pitch now has its own drive and brake biases instead
    of using the ones on Link Calculator
6.4      2021.04.30
Revision by Treefrog
    Fixed units on Driveshafts
    Replaced multiple functions to improve support of older
    versions of excel
6.5      2021.05.05
Revision by Treefrog
    Fixed dropdown lists on Link Sizing
    Changed sheet titling to use max revision value
    Fixed weights on Link Sizing
    Fixed rod end threads on Link Sizing
    Fixed plot sizing on Vehicle Pitch
    Fixed front anti lift for 100% up on Vehicle Pitch
    Fixed front drivshaft calculations
6.6      2021.05.06
Revision by Treefrog
    Fixed front driveshaft angles
6.7      2021.5.11
Revision by Treefrog and 93blackxj
    Fixed front driveshaft angles
    Fixed rear driveshaft angles
6.8      2022.01.30
Revision by Treefrog
    Fixed coilover and shock rotation value for rear lower links
    Fixed data  validation on percent of coilover shaft showing
    Fixed units and added input validation to pitch drive bias and
    brake bias
    Updated spring vendors
    Fixed front panhard tranverse movement plot
    Fixed roll over prediction calculations
6.9      2022.04.13
Revision by Treefrog
    Fixed rear panhard axle Z input
6.10     2022.04.13
Revision by Treefrog
    Fix to change in front driveshaft length
    Change to how version number is inputted referenced.

7.alpha  2023.08.20
Revision by Treefrog
    Switch from Excel based to Python
    Switched sample points from 10 up/down to variable
    Seperated save data from program
    Added tire loading modeling
    Added support for different size tires front and rear
    Updated plot colors for uniformity
    Added link end angles to Link Sizing
    Added Desire Ratio for dent resistance
    Changed pinion angle on Driveshafts from change to actual
    Added length and hypoid pinion location method option
    Shock and pitch pages not started (alpha version)
    Consolidated Read Me, Coordinates, and Reversion to About
                                    """,
            )

        if True:  # Coordinate System Images
            label = tk.Label(
                self,
                text="Coordinate System",
                background=bgColor,
                foreground=entryTextColor,
                font=(fontType, 15),
                anchor="w",
            )
            label.grid(row=1, column=1, pady=1)

            circleX = np.zeros(361)
            circleY = np.zeros(361)
            for theta in range(0, 361):
                circleX[theta] = cos(radians(theta))
                circleY[theta] = sin(radians(theta))

            if True:  # Top view coordinate system
                figTopCoord, axTopCoord = plt.subplots(1, 1)
                figTopCoord.set_facecolor(bgColor)

                topCoord = FigureCanvasTkAgg(figTopCoord, coordFrame)
                topCoord.get_tk_widget().grid(row=0, column=0, sticky="nesw")

                axTopCoord.grid(False)
                axTopCoord.set_facecolor(textEntryColor)
                axTopCoord.set_xticks([])
                axTopCoord.set_yticks([])

                axTopCoord.plot(circleX * 0.4, circleY * 0.4, color=entryTextColor)
                axTopCoord.plot(
                    circleX * 0.4 + 5, circleY * 0.4 + 0.5, color=entryTextColor
                )
                axTopCoord.plot(
                    [1, 1, -1, -1, 1], [2, 1.2, 1.2, 2, 2], color=entryTextColor
                )
                axTopCoord.plot(
                    [1, 1, -1, -1, 1], [-2, -1.2, -1.2, -2, -2], color=entryTextColor
                )
                axTopCoord.plot(
                    [6, 6, 4, 4, 6], [2, 1.2, 1.2, 2, 2], color=entryTextColor
                )
                axTopCoord.plot(
                    [6, 6, 4, 4, 6], [-2, -1.2, -1.2, -2, -2], color=entryTextColor
                )
                axTopCoord.plot([-0.1, -0.1], [-1.2, 1.2], color=entryTextColor)
                axTopCoord.plot([0.1, 0.1], [-1.2, 1.2], color=entryTextColor)
                axTopCoord.plot([4.9, 4.9], [-1.2, 1.2], color=entryTextColor)
                axTopCoord.plot([5.1, 5.1], [-1.2, 1.2], color=entryTextColor)

                axTopCoord.plot([0.05, 1], [0, 0], color="#CF0000", linewidth=2)
                axTopCoord.plot([0.93, 1], [-0.07, 0], color="#CF0000", linewidth=3)
                axTopCoord.plot([0.93, 1], [0.07, 0], color="#CF0000", linewidth=3)
                axTopCoord.text(1.1, 0, "X", color="#CF0000")
                axTopCoord.plot([0, 0], [0.05, 1], color="#00FF00", linewidth=2)
                axTopCoord.plot([0.07, 0], [0.93, 1], color="#00FF00", linewidth=2)
                axTopCoord.plot([-0.07, 0], [0.93, 1], color="#00FF00", linewidth=2)
                axTopCoord.text(0.15, 0.9, "Y", color="#00FF00")

                axTopCoord.axis("equal")

            if True:  # Side View coordinate system
                figSideCoord, axSideCoord = plt.subplots(1, 1)
                figSideCoord.set_facecolor(bgColor)

                sideCoord = FigureCanvasTkAgg(figSideCoord, coordFrame)
                sideCoord.get_tk_widget().grid(row=1, column=0, sticky="nesw")

                axSideCoord.grid(False)
                axSideCoord.set_facecolor(textEntryColor)
                axSideCoord.set_xticks([])
                axSideCoord.set_yticks([])

                axSideCoord.plot(circleX, circleY + 1, color=entryTextColor)
                axSideCoord.plot(circleX + 5, circleY + 1, color=entryTextColor)
                axSideCoord.plot([6.1, 6.2], [1, 1], color=entryTextColor)
                axSideCoord.plot([6.2, 6.2], [1, 2.1], color=entryTextColor)
                axSideCoord.plot([6.2, 5], [2.1, 2.3], color=entryTextColor)
                axSideCoord.plot([5, 3.8], [2.3, 2.3], color=entryTextColor)
                axSideCoord.plot([3.8, 3.2], [2.3, 3.3], color=entryTextColor)
                axSideCoord.plot([3.2, 3.2], [3.3, 2.3], color=entryTextColor)
                axSideCoord.plot([3.2, -1.5], [2.3, 2.3], color=entryTextColor)
                axSideCoord.plot([-1.5, -1.6], [2.3, 1], color=entryTextColor)
                axSideCoord.plot([-1.6, -1.1], [1, 1], color=entryTextColor)
                axSideCoord.plot(
                    1.1 * circleX[0:179], 1.1 * circleY[0:179] + 1, color=entryTextColor
                )
                axSideCoord.plot([1.1, 3.9], [1, 1], color=entryTextColor)
                axSideCoord.plot(
                    1.1 * circleX[0:179] + 5,
                    1.1 * circleY[0:179] + 1,
                    color=entryTextColor,
                )

                axSideCoord.plot([0.05, 1], [0, 0], color="#CF0000", linewidth=2)
                axSideCoord.plot([0.93, 1], [-0.07, 0], color="#CF0000", linewidth=3)
                axSideCoord.plot([0.93, 1], [0.07, 0], color="#CF0000", linewidth=3)
                axSideCoord.text(1.1, 0, "X", color="#CF0000")
                axSideCoord.plot([0, 0], [0.05, 1], color="#0000FF", linewidth=2)
                axSideCoord.plot([0.07, 0], [0.93, 1], color="#0000FF", linewidth=2)
                axSideCoord.plot([-0.07, 0], [0.93, 1], color="#0000FF", linewidth=2)
                axSideCoord.text(0, 1.1, "Z", color="#0000FF")

                axSideCoord.axis("equal")

        def load_from_file():
            load_susp()
            master.switch_frame("About")
