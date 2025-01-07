# src/suspension/main.py

# UI Imports
from suspension.ui.app import Window
from suspension.ui.styles import *

# Tab Imports
from suspension.ui.tabs.link import linkPage
from suspension.ui.tabs.sizing import sizingPage
from suspension.ui.tabs.driveshaft import driveshaftPage
from suspension.ui.tabs.shock import shockPage
from suspension.ui.tabs.pitch import pitchPage
from suspension.ui.tabs.settings import settingsPage
from suspension.ui.tabs.about import aboutPage
from suspension.ui.tabs.rod_end import rodEndsPage
from suspension.ui.tabs.materials import materialsPage

# Calculation Imports
from suspension.core.calculations.link_calc import run_link_calc
from suspension.core.calculations.link_sizing import run_link_sizing
from suspension.core.calculations.driveshaft import run_driveshaft
from suspension.core.calculations.shocks import run_shocks
from suspension.core.calculations.vehicle_pitch import run_vehicle_pitch

# IO Imports
from suspension.io.materials import load_materials
from suspension.io.rod_ends import load_rod_ends
from suspension.io.springs import load_spring_rates
from suspension.io.save_suspension import save_susp

# Initialize data
load_materials()
load_rod_ends()
load_spring_rates()
run_link_calc()
run_link_sizing()
run_driveshaft()
run_shocks()
run_vehicle_pitch()

tabs = {
    "linkCalc": linkPage,
    "linkSizing": sizingPage,
    "driveshaft": driveshaftPage,
    "shocks": shockPage,
    "pitch": pitchPage,
    "settings": settingsPage,
    "about": aboutPage,
    "rodEnds": rodEndsPage,
    "materials": materialsPage,
}


def main():
    app = Window()
    app.tk.call("tk", "scaling", app.winfo_screenwidth() / 2560)
    app.bind("<Control-s>", lambda event: save_susp())
    app.mainloop()


if __name__ == "__main__":
    main()
