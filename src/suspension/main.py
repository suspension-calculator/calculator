# src/suspension/main.py
from suspension.ui.app import Window
from VariableIO.visual_scheme import *  # Keep old import for now

from tab_frames.linkTab import linkPage
from tab_frames.sizingTab import sizingPage
from tab_frames.driveshaftTab import driveshaftPage
from tab_frames.shockTab import shockPage
from tab_frames.pitchTab import pitchPage
from tab_frames.settingsTab import settingsPage
from tab_frames.aboutTab import aboutPage
from tab_frames.rodEndTab import rodEndsPage
from tab_frames.materialsTab import materialsPage

from calculations.link_calc import run_link_calc
from calculations.link_sizing import run_link_sizing
from calculations.driveshaft import run_driveshaft
from calculations.shocks import run_shocks
from calculations.vehicle_pitch import run_vehicle_pitch

from VariableIO.materials import load_materials
from VariableIO.rod_ends import load_rod_ends
from VariableIO.springs import load_spring_rates
from VariableIO.save_suspension import save_susp

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
    "rodEnds":rodEndsPage,
    "materials":materialsPage
}

def main():
    app = Window()
    app.tk.call('tk','scaling',app.winfo_screenwidth()/2560)
    app.bind("<Control-s>", lambda event: save_susp())
    app.mainloop()

if __name__ == "__main__":
    main()