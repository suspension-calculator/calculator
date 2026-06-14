# src/suspension/main.py

#pyinstaller --noconsole --add-data "resources;Resources" --hidden-import=ui --hidden-import=core --hidden-import=tool_io "main.py"
#pyinstaller --noconsole --add-data "resources;Resources" "main.py"

# UI Imports
from ui.app import Window
from ui.styles import *

# Tab Imports
from ui.tabs.link import linkPage
from ui.tabs.sizing import sizingPage
from ui.tabs.driveshaft import driveshaftPage
from ui.tabs.shock import shockPage
from ui.tabs.pitch import pitchPage
from ui.tabs.settings import settingsPage
from ui.tabs.about import aboutPage
from ui.tabs.rod_end import rodEndsPage
from ui.tabs.materials import materialsPage

# Calculation Imports
from core.calculations.link_calc import run_link_calc
from core.calculations.link_sizing import run_link_sizing
from core.calculations.driveshaft import run_driveshaft
from core.calculations.shocks import run_shocks
from core.calculations.vehicle_pitch import run_vehicle_pitch

# IO Imports
from tool_io.materials import load_materials
from tool_io.rod_ends import load_rod_ends
from tool_io.springs import load_spring_rates
from tool_io.save_suspension import save_susp

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
    app.tk.call("tk",
        "scaling",
        min(
            app.winfo_screenwidth() / 2560, 
            app.winfo_screenheight() / 1440,
        ),
    )

    def closing_cbk():
        # Shutdown procedure
        app.quit()
        app.destroy()
    app.protocol("WM_DELETE_WINDOW", closing_cbk)

    app.bind("<Control-s>", lambda event: save_susp())
    app.mainloop()


if __name__ == "__main__":
    main()
