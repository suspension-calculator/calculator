#pyinstaller --add-data "Lists;Lists" Calculator.py
import tkinter as tk
import matplotlib.pyplot as plt
from VariableIO.visual_scheme import *

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
#from VariableIO.initialize_IO import inputs, outputs
#from VariableIO.variables import constant, travel, S
from VariableIO.materials import load_materials
from VariableIO.rod_ends import load_rod_ends
from VariableIO.springs import load_spring_rates
#from VariableIO.rod_end_add import add_rod_end
#from VariableIO.material_add import add_material
from VariableIO.save_suspension import save_susp,save_as_susp,save_susp_string
#from VariableIO.load_suspension import load_susp

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

class window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame("linkCalc")

        self.configure(bg=buttonColor)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.title(calcVersion)
        self.geometry("%dx%d" % (self.winfo_screenwidth(),self.winfo_screenheight()))
        self.state('zoomed')

    def switch_frame(self, page_name):
        #"""Destroys current frame and replaces it with a new one."""
        cls = tabs[page_name]
        plt.close('all')
        new_frame = cls(master = self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row = 0, column=0,sticky='nsew')
        self._frame.config(bg=bgColor)


app = window()
#width= app.winfo_screenwidth()
#app.winfo_screenmmwidth()
#height= app.winfo_screenheight()
#app.geometry("%dx%d" % (width, height))

#ORIGINAL_DPI = 96.01758241758242
#
#def get_dpi():
#    screen = tk.Tk()
#    current_dpi = screen.winfo_fpixels('1i')
#    screen.destroy()
#    return current_dpi
#
#def get_width():
#    screen = tk.Tk()
#    current_width = screen.winfo_screenwidth()
#    screen.destroy()
#    return current_width
#
#screen_scale = get_width()/2560

app.tk.call('tk','scaling',app.winfo_screenwidth()/2560)

def run_save_susp(event):
    save_susp()
app.bind("<Control-s>",run_save_susp)
app.mainloop()