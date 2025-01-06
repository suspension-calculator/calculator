# src/suspension/ui/tabs/link.py

import tkinter as tk
from suspension.io.variables import (constant, S, PS, x,y,z)

from suspension.core.calculations.link_calc import run_link_calc
from suspension.io.initialize_IO import *
from suspension.ui.styles import *
from suspension.io.save_suspension import save_susp,save_as_susp
from suspension.io.load_suspension import load_susp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import pi,floor

class linkPage(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.grid_columnconfigure(1,weight=1)
        #self.grid_columnconfigure([0,2],weight=1)
        
        self.rowconfigure([3,4],weight=1)
        #self.bind('<Control-s>',save_susp())

        self.opening = True

        #def get_width():
        #    screen = tk.Tk()
        #    current_width = screen.winfo_screenwidth()
        #    screen.destroy()
        #    return current_width
        #
        #screen_scale = get_width()
        self.tk.call('tk','scaling',self.winfo_screenwidth()/2560)

        plt.rcParams['axes.titlesize'] = 15
        plt.rcParams['axes.labelsize'] = 15
        plt.rcParams['font.size'] = 11
        plt.rcParams['figure.subplot.bottom'] = .1
        plt.rcParams['figure.subplot.hspace'] = .11
        plt.rcParams['figure.subplot.left'] = 0.03
        plt.rcParams['figure.subplot.right'] = .97
        plt.rcParams['figure.subplot.top'] = .97
        plt.rcParams['figure.subplot.wspace'] = .1

        if True: # Page Selection
            calc_page_sel = tk.Frame(self,background=bgColor)
            calc_page_sel.grid(row = 0, column=0,columnspan=3,sticky='w', padx=10)
    
            label = tk.Label(calc_page_sel, text=calcVersion,font=(fontType,20),background=bgColor,foreground=entryTextColor)
            label.grid(row=0, column = 0, padx=5)
            label.bind("<1>", lambda event: update_outputs())

            button1 = tk.Button(calc_page_sel, text ="Save As", fg=pressedButtonColor, bg=buttonColor, command = lambda : save_as_susp(),height= 1, width=7,font=(fontType,13))
            button1.grid(row = 0, column = 1, padx = 5)

            button1 = tk.Button(calc_page_sel, text ="Save", fg=pressedButtonColor, bg=buttonColor, command = lambda : save_susp(),height= 1, width=4,font=(fontType,13))
            button1.grid(row = 0, column = 2, padx = 5)

            button1 = tk.Button(calc_page_sel, text ="Load", fg=pressedButtonColor, bg=buttonColor, command = lambda : load_from_file(),height= 1, width=4,font=(fontType,13))
            button1.grid(row = 0, column = 3, padx = 5)

            button2 = tk.Button(calc_page_sel, text ="Settings", fg=pressedButtonColor, bg=buttonColor, command = lambda : master.switch_frame("settings"),height= 1, width=8,font=(fontType,13))
            button2.grid(row = 0, column = 4, padx = 5)

            button2 = tk.Button(calc_page_sel, text ="About", fg=pressedButtonColor, bg=buttonColor, command = lambda : master.switch_frame("about"),height= 1, width=8,font=(fontType,13))
            button2.grid(row = 0, column = 5, padx = 5)

            button1 = tk.Button(calc_page_sel, text ="Link Calculator", fg=buttonColor, bg=pressedButtonColor, command = lambda : master.switch_frame("linkCalc"),height= 1, width=12,font=(fontType,13))
            button1.grid(row = 0, column = 6, padx = 5)
    
            button2 = tk.Button(calc_page_sel, text ="Link Sizing", fg=pressedButtonColor, bg=buttonColor, command = lambda : master.switch_frame("linkSizing"),height= 1, width=12,font=(fontType,13))
            button2.grid(row = 0, column = 7, padx = 5)
    
            button3 = tk.Button(calc_page_sel, text ="Driveshafts", fg=pressedButtonColor, bg=buttonColor, command = lambda : master.switch_frame("driveshaft"),height= 1, width=12,font=(fontType,13))
            button3.grid(row = 0, column = 8, padx = 5)
    
            button4 = tk.Button(calc_page_sel, text ="Shocks", fg=pressedButtonColor, bg=buttonColor, command = lambda : master.switch_frame("shocks"),height= 1, width=12,font=(fontType,13))
            button4.grid(row = 0, column = 9, padx = 5)
    
            button5 = tk.Button(calc_page_sel, text ="Vehicle Pitch", fg=pressedButtonColor, bg=buttonColor, command = lambda : master.switch_frame("pitch"),height= 1, width=12,font=(fontType,13))
            button5.grid(row = 0, column = 10, padx = 5)
        
        if True: # Front Inputs
            calc_front = tk.Frame(self,background=bgColor)
            calc_front.grid(row=1,column=2,sticky='n')
    
            i_column = 0
            i_row = 0
    
            label = tk.Label(calc_front, text="Front",background=bgColor,foreground=entryTextColor,font=(fontType,20), justify=tk.CENTER)
            label.grid(row=i_row, column = i_column, pady=1)
            label.bind("<1>", lambda event: update_outputs())

            # Front inputs
            front_inputs_1 = tk.Frame(calc_front,background=bgColor)
            front_inputs_1.grid(row = 1,column=0)
    
            i_row = 0
    
            label = tk.Label(front_inputs_1, text="One or Two Upper Links?",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row, column = i_column+0,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
    
            label = tk.Label(front_inputs_1, text="Panhard Bar?",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row, column = i_column+4,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
    
            F_UL_Count = tk.StringVar()
            if inputs.F.U_count == 1:
                default = "1"
            else:
                default = "2"
            F_UL_Count.set(default)
            F_UL_Count_menu = tk.OptionMenu(front_inputs_1,F_UL_Count,"1","2")
            F_UL_Count_menu.grid(row = i_row, column=i_column+1)
            F_UL_Count_menu.config(bg=textEntryColor)
            F_UL_Count_menu.config(fg=entryTextColor)
            F_UL_Count_menu.config(highlightthickness=0)
            F_UL_Count_menu.config(font=(fontType,17))
            F_UL_Count_menu.nametowidget(F_UL_Count_menu.menuname).config(font=(fontType,17))
    
            F_P_exist = tk.StringVar()
            if inputs.F.panhard:
                default = "Yes"
            else:
                default = "No"
            F_P_exist.set(default)
            F_P_exist_menu = tk.OptionMenu(front_inputs_1,F_P_exist,"No","Yes")
            F_P_exist_menu.grid(row = i_row, column=i_column+5)
            F_P_exist_menu.config(bg=textEntryColor)
            F_P_exist_menu.config(fg=entryTextColor)
            F_P_exist_menu.config(highlightthickness=0)
            F_P_exist_menu.config(width=3)
            F_P_exist_menu.config(font=(fontType,17))
            F_P_exist_menu.nametowidget(F_P_exist_menu.menuname).config(font=(fontType,17))
    
            label = tk.Label(front_inputs_1, text="Up Travel:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+1, column = i_column+0,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
    
            label = tk.Label(front_inputs_1, text="Down Travel:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+2, column = i_column+0,sticky='e')
            label.bind("<1>", lambda event: update_outputs())

            label = tk.Label(front_inputs_1, text="Unsprung mass:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+3, column = i_column+0,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
    
            label = tk.Label(front_inputs_1, text="Tire Rolling Radius:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+4, column = i_column+0,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
    
            text = tk.StringVar()
            text.set(inputs.F.bump)
            F_Bump = tk.Entry(front_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            F_Bump.grid(row = i_row+1, column=i_column+1)
            F_Bump.config(bg=textEntryColor)
            F_Bump.config(fg=entryTextColor)
            F_Bump.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.droop)
            F_Droop = tk.Entry(front_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            F_Droop.grid(row = i_row+2, column=i_column+1)
            F_Droop.config(bg=textEntryColor)
            F_Droop.config(fg=entryTextColor)
            F_Droop.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.unsprung_mass)
            F_mass = tk.Entry(front_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            F_mass.grid(row = i_row+3, column=i_column+1)
            F_mass.config(bg=textEntryColor)
            F_mass.config(fg=entryTextColor)
            F_mass.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.tire_radius)
            F_tire_radius = tk.Entry(front_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            F_tire_radius.grid(row = i_row+4, column=i_column+1)
            F_tire_radius.config(bg=textEntryColor)
            F_tire_radius.config(fg=entryTextColor)
            F_tire_radius.bind("<Return>", lambda event: update_outputs())

            for i in range(1,5):
                if i == 3:
                    label = tk.Label(front_inputs_1, text=" {}".format(S.mass_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                else:
                    label = tk.Label(front_inputs_1, text=" {}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+2,sticky='w')
                label.bind("<1>", lambda event: update_outputs())

            label = tk.Label(front_inputs_1, text=" ",background=bgColor,foreground=bgColor,font=(fontType,1))
            label.grid(row=i_row+1, column = 3,padx=20)
            label.bind("<1>", lambda event: update_outputs())
    
            label = tk.Label(front_inputs_1, text="Track Width:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+1, column = i_column+4,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
    
            label = tk.Label(front_inputs_1, text="Portal Height:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+2, column = i_column+4,sticky='e')
            label.bind("<1>", lambda event: update_outputs())

            label = tk.Label(front_inputs_1, text="Axle Tube Diameter:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+3, column = i_column+4,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
    
            label = tk.Label(front_inputs_1, text="Tire Diameter:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+4, column = i_column+4,sticky='e')
            label.bind("<1>", lambda event: update_outputs())

            label = tk.Label(front_inputs_1, text="Tire Width:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+5, column = i_column+4,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
    
            text = tk.StringVar()
            text.set(inputs.F.track_width)
            F_Track = tk.Entry(front_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            F_Track.grid(row = i_row+1, column=i_column+5)
            F_Track.config(bg=textEntryColor)
            F_Track.config(fg=entryTextColor)
            F_Track.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.portal_height)
            F_Portal = tk.Entry(front_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            F_Portal.grid(row = i_row+2, column=i_column+5)
            F_Portal.config(bg=textEntryColor)
            F_Portal.config(fg=entryTextColor)
            F_Portal.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.axle_tube)
            F_axle_tube = tk.Entry(front_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            F_axle_tube.grid(row = i_row+3, column=i_column+5)
            F_axle_tube.config(bg=textEntryColor)
            F_axle_tube.config(fg=entryTextColor)
            F_axle_tube.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.tire_diameter)
            F_tire_diameter = tk.Entry(front_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            F_tire_diameter.grid(row = i_row+4, column=i_column+5)
            F_tire_diameter.config(bg=textEntryColor)
            F_tire_diameter.config(fg=entryTextColor)
            F_tire_diameter.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.tire_width)
            F_tire_width = tk.Entry(front_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            F_tire_width.grid(row = i_row+5, column=i_column+5)
            F_tire_width.config(bg=textEntryColor)
            F_tire_width.config(fg=entryTextColor)
            F_tire_width.bind("<Return>", lambda event: update_outputs())

            for i in range(1,6):
                label = tk.Label(front_inputs_1, text=" {}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+6,sticky='w')
                label.bind("<1>", lambda event: update_outputs())
    
            label = tk.Label(front_inputs_1, text=" ",background=bgColor,foreground=bgColor,font=(fontType,1))
            label.grid(row=i_row+6, column = 0)
            label.bind("<1>", lambda event: update_outputs())
    
            # Front upper inputs
            front_inputs_2 = tk.Frame(calc_front,background=bgColor)
            front_inputs_2.grid(row = 2,column=0)
            i_row = 0
    
            label = tk.Label(front_inputs_2, text="Upper Link",background=upperColor,foreground=entryTextColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+0,sticky='sewn')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(front_inputs_2, text="X'",background=upperColor,foreground=entryTextColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+1,columnspan=2,sticky="sewn")
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(front_inputs_2, text="Y",background=upperColor,foreground=entryTextColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+3,columnspan=2,sticky="sewn")
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(front_inputs_2, text="Z",background=upperColor,foreground=entryTextColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+5,columnspan=2,sticky="sewn")
            label.bind("<1>", lambda event: update_outputs())
            
            label = tk.Label(front_inputs_2, text="Upper Axle",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+1, column = i_column+0,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(front_inputs_2, text="Upper Frame",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+2, column = i_column+0,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
    
            text = tk.StringVar()
            text.set(inputs.F.UA[x])
            FUAX = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FUAX.grid(row = i_row+1, column=i_column+1)
            FUAX.config(bg=textEntryColor)
            FUAX.config(fg=entryTextColor)
            FUAX.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.UA[y])
            FUAY = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FUAY.grid(row = i_row+1, column=i_column+3)
            FUAY.config(bg=textEntryColor)
            FUAY.config(fg=entryTextColor)
            FUAY.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.UA[z])
            FUAZ = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FUAZ.grid(row = i_row+1, column=i_column+5)
            FUAZ.config(bg=textEntryColor)
            FUAZ.config(fg=entryTextColor)
            FUAZ.bind("<Return>", lambda event: update_outputs())
    
            text = tk.StringVar()
            text.set(inputs.F.UF[x])
            FUFX = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FUFX.grid(row = i_row+2, column=i_column+1)
            FUFX.config(bg=textEntryColor)
            FUFX.config(fg=entryTextColor)
            FUFX.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.UF[y])
            FUFY = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FUFY.grid(row = i_row+2, column=i_column+3)
            FUFY.config(bg=textEntryColor)
            FUFY.config(fg=entryTextColor)
            FUFY.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.UF[z])
            FUFZ = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FUFZ.grid(row = i_row+2, column=i_column+5)
            FUFZ.config(bg=textEntryColor)
            FUFZ.config(fg=entryTextColor)
            FUFZ.bind("<Return>", lambda event: update_outputs())

            for i in range(1,3):
                label = tk.Label(front_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+2,sticky='w',padx=2)
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(front_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+4,sticky='w',padx=2)
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(front_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+6,sticky='w',padx=2)
                label.bind("<1>", lambda event: update_outputs())
    
            label = tk.Label(front_inputs_2, text=" ",background=bgColor,foreground=bgColor,font=(fontType,1))
            label.grid(row=i_row+3, column = 0)
            label.bind("<1>", lambda event: update_outputs())
    
    
            # Front lower input
            i_row = 4
    
            label = tk.Label(front_inputs_2, text="Lower Link",background=lowerColor,foreground=textEntryColor,font=((fontType,17),20))
            label.grid(row=i_row, column = i_column+0,sticky='sewn')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(front_inputs_2, text="X'",background=lowerColor,foreground=textEntryColor,font=((fontType,17),20))
            label.grid(row=i_row, column = i_column+1,columnspan=2,sticky="sewn")
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(front_inputs_2, text="Y",background=lowerColor,foreground=textEntryColor,font=((fontType,17),20))
            label.grid(row=i_row, column = i_column+3,columnspan=2,sticky="sewn")
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(front_inputs_2, text="Z",background=lowerColor,foreground=textEntryColor,font=((fontType,17),20))
            label.grid(row=i_row, column = i_column+5,columnspan=2,sticky="sewn")
            label.bind("<1>", lambda event: update_outputs())
            
            label = tk.Label(front_inputs_2, text="Lower Axle",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+1, column = i_column+0,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(front_inputs_2, text="Lower Frame",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+2, column = i_column+0,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
    
            text = tk.StringVar()
            text.set(inputs.F.LA[x])
            FLAX = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FLAX.grid(row = i_row+1, column=i_column+1)
            FLAX.config(bg=textEntryColor)
            FLAX.config(fg=entryTextColor)
            FLAX.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.LA[y])
            FLAY = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FLAY.grid(row = i_row+1, column=i_column+3)
            FLAY.config(bg=textEntryColor)
            FLAY.config(fg=entryTextColor)
            FLAY.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.LA[z])
            FLAZ = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FLAZ.grid(row = i_row+1, column=i_column+5)
            FLAZ.config(bg=textEntryColor)
            FLAZ.config(fg=entryTextColor)
            FLAZ.bind("<Return>", lambda event: update_outputs())
    
            text = tk.StringVar()
            text.set(inputs.F.LF[x])
            FLFX = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FLFX.grid(row = i_row+2, column=i_column+1)
            FLFX.config(bg=textEntryColor)
            FLFX.config(fg=entryTextColor)
            FLFX.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.LF[y])
            FLFY = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FLFY.grid(row = i_row+2, column=i_column+3)
            FLFY.config(bg=textEntryColor)
            FLFY.config(fg=entryTextColor)
            FLFY.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.LF[z])
            FLFZ = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FLFZ.grid(row = i_row+2, column=i_column+5)
            FLFZ.config(bg=textEntryColor)
            FLFZ.config(fg=entryTextColor)
            FLFZ.bind("<Return>", lambda event: update_outputs())

            for i in range(1,3):
                label = tk.Label(front_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+2,sticky='w',padx=2)
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(front_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+4,sticky='w',padx=2)
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(front_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+6,sticky='w',padx=2)
                label.bind("<1>", lambda event: update_outputs())
    
            label = tk.Label(front_inputs_2, text=" ",background=bgColor,foreground=bgColor,font=(fontType,1))
            label.grid(row=i_row+3, column = 0)
            label.bind("<1>", lambda event: update_outputs())
    
            # Front panhard input
    
            i_row = 8
            
            label = tk.Label(front_inputs_2, text="Panhard",background=panhardColor,foreground=textEntryColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+0,sticky='sewn')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(front_inputs_2, text="X'",background=panhardColor,foreground=textEntryColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+1,columnspan=2,sticky="sewn")
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(front_inputs_2, text="Y",background=panhardColor,foreground=textEntryColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+3,columnspan=2,sticky="sewn")
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(front_inputs_2, text="Z",background=panhardColor,foreground=textEntryColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+5,columnspan=2,sticky="sewn")
            label.bind("<1>", lambda event: update_outputs())

            label = tk.Label(front_inputs_2, text="Panhard Axle",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+1, column = i_column+0,sticky='e')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(front_inputs_2, text="Panhard Frame",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+2, column = i_column+0,sticky='e')
            label.bind("<1>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.PA[x])
            FPAX = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FPAX.grid(row = i_row+1, column=i_column+1)
            FPAX.config(bg=textEntryColor)
            FPAX.config(fg=entryTextColor)
            FPAX.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.PA[y])
            FPAY = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FPAY.grid(row = i_row+1, column=i_column+3)
            FPAY.config(bg=textEntryColor)
            FPAY.config(fg=entryTextColor)
            FPAY.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.PA[z])
            FPAZ = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FPAZ.grid(row = i_row+1, column=i_column+5)
            FPAZ.config(bg=textEntryColor)
            FPAZ.config(fg=entryTextColor)
            FPAZ.bind("<Return>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.F.PF[x])
            FPFX = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FPFX.grid(row = i_row+2, column=i_column+1)
            FPFX.config(bg=textEntryColor)
            FPFX.config(fg=entryTextColor)
            FPFX.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.PF[y])
            FPFY = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FPFY.grid(row = i_row+2, column=i_column+3)
            FPFY.config(bg=textEntryColor)
            FPFY.config(fg=entryTextColor)
            FPFY.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.F.PF[z])
            FPFZ = tk.Entry(front_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            FPFZ.grid(row = i_row+2, column=i_column+5)
            FPFZ.config(bg=textEntryColor)
            FPFZ.config(fg=entryTextColor)
            FPFZ.bind("<Return>", lambda event: update_outputs())

            for i in range(1,3):
                label = tk.Label(front_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+2,sticky='w',padx=2)
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(front_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+4,sticky='w',padx=2)
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(front_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+6,sticky='w',padx=2)
                label.bind("<1>", lambda event: update_outputs())

        if True: # Rear Inputs
            calc_rear = tk.Frame(self,background=bgColor)
            calc_rear.grid(row=1,column=0,sticky='n')
    
            i_column = 0
            i_row = 0
    
            label = tk.Label(calc_rear, text="Rear",background=bgColor,foreground=entryTextColor,font=(fontType,20), justify=tk.CENTER)
            label.grid(row=i_row, column = i_column, pady=1)

            # Rear inputs
            rear_inputs_1 = tk.Frame(calc_rear,background=bgColor)
            rear_inputs_1.grid(row = 1,column=0)
    
            i_row = 0
    
            label = tk.Label(rear_inputs_1, text="One or Two Upper Links?",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row, column = i_column+0,sticky='e')
    
            label = tk.Label(rear_inputs_1, text="Panhard Bar?",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row, column = i_column+4,sticky='e')
    
            R_UL_Count = tk.StringVar()
            if inputs.R.U_count == 1:
                default = "1"
            else:
                default = "2"
            R_UL_Count.set(default)
            R_UL_Count_menu = tk.OptionMenu(rear_inputs_1,R_UL_Count,"1","2")
            R_UL_Count_menu.grid(row = i_row, column=i_column+1)
            R_UL_Count_menu.config(bg=textEntryColor)
            R_UL_Count_menu.config(fg=entryTextColor)
            R_UL_Count_menu.config(highlightthickness=0)
            R_UL_Count_menu.config(font=(fontType,17))
            R_UL_Count_menu.nametowidget(R_UL_Count_menu.menuname).config(font=(fontType,17))
    
            R_P_exist = tk.StringVar()
            if inputs.R.panhard:
                default = "Yes"
            else:
                default = "No"
            R_P_exist.set(default)
            R_P_exist_menu = tk.OptionMenu(rear_inputs_1,R_P_exist,"No","Yes")
            R_P_exist_menu.grid(row = i_row, column=i_column+5)
            R_P_exist_menu.config(bg=textEntryColor)
            R_P_exist_menu.config(fg=entryTextColor)
            R_P_exist_menu.config(highlightthickness=0)
            R_P_exist_menu.config(width=3)
            R_P_exist_menu.config(font=(fontType,17))
            R_P_exist_menu.nametowidget(R_P_exist_menu.menuname).config(font=(fontType,17))
    
            label = tk.Label(rear_inputs_1, text="Up Travel:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+1, column = i_column+0,sticky='e')
    
            label = tk.Label(rear_inputs_1, text="Down Travel:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+2, column = i_column+0,sticky='e')

            label = tk.Label(rear_inputs_1, text="Unsprung:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+3, column = i_column+0,sticky='e')
    
            label = tk.Label(rear_inputs_1, text="Tire Rolling Radius:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+4, column = i_column+0,sticky='e')
    
            text = tk.StringVar()
            text.set(inputs.R.bump)
            R_Bump = tk.Entry(rear_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            R_Bump.grid(row = i_row+1, column=i_column+1)
            R_Bump.config(bg=textEntryColor)
            R_Bump.config(fg=entryTextColor)
            R_Bump.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.droop)
            R_Droop = tk.Entry(rear_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            R_Droop.grid(row = i_row+2, column=i_column+1)
            R_Droop.config(bg=textEntryColor)
            R_Droop.config(fg=entryTextColor)
            R_Droop.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.unsprung_mass)
            R_mass = tk.Entry(rear_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            R_mass.grid(row = i_row+3, column=i_column+1)
            R_mass.config(bg=textEntryColor)
            R_mass.config(fg=entryTextColor)
            R_mass.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.tire_radius)
            R_tire_radius = tk.Entry(rear_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            R_tire_radius.grid(row = i_row+4, column=i_column+1)
            R_tire_radius.config(bg=textEntryColor)
            R_tire_radius.config(fg=entryTextColor)
            R_tire_radius.bind("<Return>", lambda event: update_outputs())

            for i in range(1,5):
                if i == 3:
                    label = tk.Label(rear_inputs_1, text=S.mass_units,background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                else:
                    label = tk.Label(rear_inputs_1, text=S.position_units,background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+2,sticky='w')

            label = tk.Label(rear_inputs_1, text=" ",background=bgColor,foreground=bgColor,font=(fontType,1))
            label.grid(row=i_row+1, column = 3,padx=20)
    
            label = tk.Label(rear_inputs_1, text="Track Width:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+1, column = i_column+4,sticky='e')
    
            label = tk.Label(rear_inputs_1, text="Portal Height:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+2, column = i_column+4,sticky='e')

            label = tk.Label(rear_inputs_1, text="Axle Tube Diameter:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+3, column = i_column+4,sticky='e')
    
            label = tk.Label(rear_inputs_1, text="Tire Diameter:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+4, column = i_column+4,sticky='e')

            label = tk.Label(rear_inputs_1, text="Tire Width:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+5, column = i_column+4,sticky='e')
    
            text = tk.StringVar()
            text.set(inputs.R.track_width)
            R_Track = tk.Entry(rear_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            R_Track.grid(row = i_row+1, column=i_column+5)
            R_Track.config(bg=textEntryColor)
            R_Track.config(fg=entryTextColor)
            R_Track.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.portal_height)
            R_Portal = tk.Entry(rear_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            R_Portal.grid(row = i_row+2, column=i_column+5)
            R_Portal.config(bg=textEntryColor)
            R_Portal.config(fg=entryTextColor)
            R_Portal.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.axle_tube)
            R_axle_tube = tk.Entry(rear_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            R_axle_tube.grid(row = i_row+3, column=i_column+5)
            R_axle_tube.config(bg=textEntryColor)
            R_axle_tube.config(fg=entryTextColor)
            R_axle_tube.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.tire_diameter)
            R_tire_diameter = tk.Entry(rear_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            R_tire_diameter.grid(row = i_row+4, column=i_column+5)
            R_tire_diameter.config(bg=textEntryColor)
            R_tire_diameter.config(fg=entryTextColor)
            R_tire_diameter.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.tire_width)
            R_tire_width = tk.Entry(rear_inputs_1,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            R_tire_width.grid(row = i_row+5, column=i_column+5)
            R_tire_width.config(bg=textEntryColor)
            R_tire_width.config(fg=entryTextColor)
            R_tire_width.bind("<Return>", lambda event: update_outputs())

            for i in range(1,6):
                label = tk.Label(rear_inputs_1, text=S.position_units,background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+6,sticky='w')
    
            label = tk.Label(rear_inputs_1, text=" ",background=bgColor,foreground=bgColor,font=(fontType,1))
            label.grid(row=i_row+6, column = 0)
    
            # Rear upper inputs
            rear_inputs_2 = tk.Frame(calc_rear,background=bgColor)
            rear_inputs_2.grid(row = 2,column=0)
            i_row = 0
    
            label = tk.Label(rear_inputs_2, text="Upper Link",background=upperColor,foreground=entryTextColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+0,sticky='sewn')
            label = tk.Label(rear_inputs_2, text="X",background=upperColor,foreground=entryTextColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+1,columnspan=2,sticky="sewn")
            label = tk.Label(rear_inputs_2, text="Y",background=upperColor,foreground=entryTextColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+3,columnspan=2,sticky="sewn")
            label = tk.Label(rear_inputs_2, text="Z",background=upperColor,foreground=entryTextColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+5,columnspan=2,sticky="sewn")
            
            label = tk.Label(rear_inputs_2, text="Upper Axle",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+1, column = i_column+0,sticky='e')
            label = tk.Label(rear_inputs_2, text="Upper Frame",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+2, column = i_column+0,sticky='e')
    
            text = tk.StringVar()
            text.set(inputs.R.UA[x])
            RUAX = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RUAX.grid(row = i_row+1, column=i_column+1)
            RUAX.config(bg=textEntryColor)
            RUAX.config(fg=entryTextColor)
            RUAX.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.UA[y])
            RUAY = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RUAY.grid(row = i_row+1, column=i_column+3)
            RUAY.config(bg=textEntryColor)
            RUAY.config(fg=entryTextColor)
            RUAY.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.UA[z])
            RUAZ = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RUAZ.grid(row = i_row+1, column=i_column+5)
            RUAZ.config(bg=textEntryColor)
            RUAZ.config(fg=entryTextColor)
            RUAZ.bind("<Return>", lambda event: update_outputs())
    
            text = tk.StringVar()
            text.set(inputs.R.UF[x])
            RUFX = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RUFX.grid(row = i_row+2, column=i_column+1)
            RUFX.config(bg=textEntryColor)
            RUFX.config(fg=entryTextColor)
            RUFX.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.UF[y])
            RUFY = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RUFY.grid(row = i_row+2, column=i_column+3)
            RUFY.config(bg=textEntryColor)
            RUFY.config(fg=entryTextColor)
            RUFY.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.UF[z])
            RUFZ = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RUFZ.grid(row = i_row+2, column=i_column+5)
            RUFZ.config(bg=textEntryColor)
            RUFZ.config(fg=entryTextColor)
            RUFZ.bind("<Return>", lambda event: update_outputs())

            for i in range(1,3):
                label = tk.Label(rear_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+2,sticky='w',padx=2)
                label = tk.Label(rear_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+4,sticky='w',padx=2)
                label = tk.Label(rear_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+6,sticky='w',padx=2)
    
            label = tk.Label(rear_inputs_2, text=" ",background=bgColor,foreground=bgColor,font=(fontType,1))
            label.grid(row=i_row+3, column = 0)
    
    
            # Rear lower input
            i_row = 4
    
            label = tk.Label(rear_inputs_2, text="Lower Link",background=lowerColor,foreground=textEntryColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+0,sticky='sewn')
            label = tk.Label(rear_inputs_2, text="X",background=lowerColor,foreground=textEntryColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+1,columnspan=2,sticky="sewn")
            label = tk.Label(rear_inputs_2, text="Y",background=lowerColor,foreground=textEntryColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+3,columnspan=2,sticky="sewn")
            label = tk.Label(rear_inputs_2, text="Z",background=lowerColor,foreground=textEntryColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+5,columnspan=2,sticky="sewn")
            
            label = tk.Label(rear_inputs_2, text="Lower Axle",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+1, column = i_column+0,sticky='e')
            label = tk.Label(rear_inputs_2, text="Lower Frame",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+2, column = i_column+0,sticky='e')
    
            text = tk.StringVar()
            text.set(inputs.R.LA[x])
            RLAX = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RLAX.grid(row = i_row+1, column=i_column+1)
            RLAX.config(bg=textEntryColor)
            RLAX.config(fg=entryTextColor)
            RLAX.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.LA[y])
            RLAY = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RLAY.grid(row = i_row+1, column=i_column+3)
            RLAY.config(bg=textEntryColor)
            RLAY.config(fg=entryTextColor)
            RLAY.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.LA[z])
            RLAZ = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RLAZ.grid(row = i_row+1, column=i_column+5)
            RLAZ.config(bg=textEntryColor)
            RLAZ.config(fg=entryTextColor)
            RLAZ.bind("<Return>", lambda event: update_outputs())
    
            text = tk.StringVar()
            text.set(inputs.R.LF[x])
            RLFX = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RLFX.grid(row = i_row+2, column=i_column+1)
            RLFX.config(bg=textEntryColor)
            RLFX.config(fg=entryTextColor)
            RLFX.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.LF[y])
            RLFY = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RLFY.grid(row = i_row+2, column=i_column+3)
            RLFY.config(bg=textEntryColor)
            RLFY.config(fg=entryTextColor)
            RLFY.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.LF[z])
            RLFZ = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RLFZ.grid(row = i_row+2, column=i_column+5)
            RLFZ.config(bg=textEntryColor)
            RLFZ.config(fg=entryTextColor)
            RLFZ.bind("<Return>", lambda event: update_outputs())

            for i in range(1,3):
                label = tk.Label(rear_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+2,sticky='w',padx=2)
                label = tk.Label(rear_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+4,sticky='w',padx=2)
                label = tk.Label(rear_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+6,sticky='w',padx=2)
    
            label = tk.Label(rear_inputs_2, text=" ",background=bgColor,foreground=bgColor,font=(fontType,1))
            label.grid(row=i_row+3, column = 0)
    
            # Rear panhard input
    
            i_row = 8
            
            label = tk.Label(rear_inputs_2, text="Panhard",background=panhardColor,foreground=textEntryColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+0,sticky='sewn')
            label = tk.Label(rear_inputs_2, text="X",background=panhardColor,foreground=textEntryColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+1,columnspan=2,sticky="sewn")
            label = tk.Label(rear_inputs_2, text="Y",background=panhardColor,foreground=textEntryColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+3,columnspan=2,sticky="sewn")
            label = tk.Label(rear_inputs_2, text="Z",background=panhardColor,foreground=textEntryColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+5,columnspan=2,sticky="sewn")

            label = tk.Label(rear_inputs_2, text="Panhard Axle",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+1, column = i_column+0,sticky='e')
            label = tk.Label(rear_inputs_2, text="Panhard Frame",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+2, column = i_column+0,sticky='e')

            text = tk.StringVar()
            text.set(inputs.R.PA[x])
            RPAX = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RPAX.grid(row = i_row+1, column=i_column+1)
            RPAX.config(bg=textEntryColor)
            RPAX.config(fg=entryTextColor)
            RPAX.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.PA[y])
            RPAY = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RPAY.grid(row = i_row+1, column=i_column+3)
            RPAY.config(bg=textEntryColor)
            RPAY.config(fg=entryTextColor)
            RPAY.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.PA[z])
            RPAZ = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RPAZ.grid(row = i_row+1, column=i_column+5)
            RPAZ.config(bg=textEntryColor)
            RPAZ.config(fg=entryTextColor)
            RPAZ.bind("<Return>", lambda event: update_outputs())

            text = tk.StringVar()
            text.set(inputs.R.PF[x])
            RPFX = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RPFX.grid(row = i_row+2, column=i_column+1)
            RPFX.config(bg=textEntryColor)
            RPFX.config(fg=entryTextColor)
            RPFX.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.PF[y])
            RPFY = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RPFY.grid(row = i_row+2, column=i_column+3)
            RPFY.config(bg=textEntryColor)
            RPFY.config(fg=entryTextColor)
            RPFY.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.R.PF[z])
            RPFZ = tk.Entry(rear_inputs_2,font=(fontType,17), justify=tk.CENTER,width=10, textvariable=text,insertbackground=entryTextColor)
            RPFZ.grid(row = i_row+2, column=i_column+5)
            RPFZ.config(bg=textEntryColor)
            RPFZ.config(fg=entryTextColor)
            RPFZ.bind("<Return>", lambda event: update_outputs())

            for i in range(1,3):
                label = tk.Label(rear_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+2,sticky='w',padx=2)
                label = tk.Label(rear_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+4,sticky='w',padx=2)
                label = tk.Label(rear_inputs_2, text="{}".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="w")
                label.grid(row=i_row+i, column = i_column+6,sticky='w',padx=2)
    
        if True: # Vehicle Inputs
            calc_vehicle = tk.Frame(self,background=bgColor)
            calc_vehicle.grid(row=1,column=1,sticky='n')
    
            i_column = 0
            i_row = 0

            calc_vehicle_inputs = tk.Frame(calc_vehicle,background=bgColor)
            calc_vehicle_inputs.grid(row=0,column=0,sticky='n')
    
            label = tk.Label(calc_vehicle_inputs, text="Vehicle Specs",background=bgColor,foreground=entryTextColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column, columnspan = 4, pady=1)
            label.bind("<1>", lambda event: update_outputs())
    
            label = tk.Label(calc_vehicle_inputs, text="Wheelbase [{}]:".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+1, column = i_column,sticky='e', pady=2)
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="Front Drive Bias:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+2, column = i_column,sticky='e', pady=2)
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="Front Brake Bias:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+3, column = i_column,sticky='e', pady=2)
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="Weight Distribution:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+4, column = i_column,sticky='e', pady=2)
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="Vehicle Mass [{}]:".format(S.mass_units),background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+1, column = i_column+2,sticky='e', pady=2)
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="Vehicle CG Height [{}]:".format(S.position_units),background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+2, column = i_column+2,sticky='e', pady=2)
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="Acceleration:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+3, column = i_column+2,sticky='e', pady=2)
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="Transverse Acceleration:",background=bgColor,foreground=entryTextColor,font=(fontType,17), justify=tk.RIGHT)
            label.grid(row=i_row+4, column = i_column+2,sticky='e', pady=2)
            label.bind("<1>", lambda event: update_outputs())
    
            text = tk.StringVar()
            text.set(inputs.V.wheelbase)
            wheelbase = tk.Entry(calc_vehicle_inputs,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            wheelbase.grid(row = i_row+1, column=i_column+1)
            wheelbase.config(bg=textEntryColor)
            wheelbase.config(fg=entryTextColor)
            wheelbase.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.V.drive_bias)
            drive_bias = tk.Entry(calc_vehicle_inputs,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            drive_bias.grid(row = i_row+2, column=i_column+1)
            drive_bias.config(bg=textEntryColor)
            drive_bias.config(fg=entryTextColor)
            drive_bias.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.V.brake_bias)
            brake_bias = tk.Entry(calc_vehicle_inputs,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            brake_bias.grid(row = i_row+3, column=i_column+1)
            brake_bias.config(bg=textEntryColor)
            brake_bias.config(fg=entryTextColor)
            brake_bias.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.V.weight_distribution)
            weight_dist = tk.Entry(calc_vehicle_inputs,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            weight_dist.grid(row = i_row+4, column=i_column+1)
            weight_dist.config(bg=textEntryColor)
            weight_dist.config(fg=entryTextColor)
            weight_dist.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.V.mass)
            V_mass = tk.Entry(calc_vehicle_inputs,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            V_mass.grid(row = i_row+1, column=i_column+3)
            V_mass.config(bg=textEntryColor)
            V_mass.config(fg=entryTextColor)
            V_mass.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.V.CG_height)
            V_CG_Height = tk.Entry(calc_vehicle_inputs,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            V_CG_Height.grid(row = i_row+2, column=i_column+3)
            V_CG_Height.config(bg=textEntryColor)
            V_CG_Height.config(fg=entryTextColor)
            V_CG_Height.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.V.acceleration)
            accel = tk.Entry(calc_vehicle_inputs,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            accel.grid(row = i_row+3, column=i_column+3)
            accel.config(bg=textEntryColor)
            accel.config(fg=entryTextColor)
            accel.bind("<Return>", lambda event: update_outputs())
            text = tk.StringVar()
            text.set(inputs.V.transverse_acceleration)
            tran_accel = tk.Entry(calc_vehicle_inputs,font=(fontType,17), justify=tk.CENTER,width=6, textvariable=text,insertbackground=entryTextColor)
            tran_accel.grid(row = i_row+4, column=i_column+3)
            tran_accel.config(bg=textEntryColor)
            tran_accel.config(fg=entryTextColor)
            tran_accel.bind("<Return>", lambda event: update_outputs())
    
            label = tk.Label(calc_vehicle_inputs, text=".....",background=bgColor,foreground=entryTextColor,font=(fontType,5))
            label.grid(row=i_row, column = 4)#, padx=100)
            label.bind("<1>", lambda event: update_outputs())
            
            i_column = 5

            label = tk.Label(calc_vehicle_inputs, text="Plot Settings",background=bgColor,foreground=entryTextColor,font=(fontType,20))
            label.grid(row=i_row, column = i_column+0, columnspan = 4, pady=1)
            label.bind("<1>", lambda event: update_outputs())
    
            label = tk.Label(calc_vehicle_inputs, text="Link Convergence ",background=bgColor,foreground=entryTextColor,font=(fontType,17),anchor="e")
            label.grid(row=i_row+1, column = i_column+0,sticky='nesw')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="IC Movement ",background=ICcolor,foreground=textEntryColor,font=(fontType,17),anchor="e")
            label.grid(row=i_row+2, column = i_column+0,sticky='nesw')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="Ride ICs ",background=ICcolor,foreground=textEntryColor,font=(fontType,17), anchor="e")
            label.grid(row=i_row+3, column = i_column+0,sticky='nesw')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="Axle Roll Axes ",background=rollColor,foreground=textEntryColor,font=(fontType,17),anchor="e")
            label.grid(row=i_row+4, column = i_column+0,sticky='nesw')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="Roll Centers ",background=rollColor,foreground=textEntryColor,font=(fontType,17),anchor="e")
            label.grid(row=i_row+1, column = i_column+2,sticky='nesw')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="Body Roll Axis ",background=bodyRollColor,foreground=textEntryColor,font=(fontType,17),anchor="e")
            label.grid(row=i_row+2, column = i_column+2,sticky='nesw')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="100% Anti Lines ",background=anti100Color,foreground=textEntryColor,font=(fontType,17),anchor="e")
            label.grid(row=i_row+3, column = i_column+2,sticky='nesw')
            label.bind("<1>", lambda event: update_outputs())
            label = tk.Label(calc_vehicle_inputs, text="Ride Anti Lines ",background=rideAntiColor,foreground=textEntryColor,font=(fontType,17),anchor="e")
            label.grid(row=i_row+4, column = i_column+2,sticky='nesw')
            label.bind("<1>", lambda event: update_outputs())
    
            ps_converge = tk.StringVar(calc_vehicle_inputs)
            ps_converge.set("Show")
            ps_converge_menu = tk.OptionMenu(calc_vehicle_inputs,ps_converge,"Show","Hide")
            ps_converge_menu.grid(row = i_row+1, column=i_column+1)
            ps_converge_menu.config(bg=textEntryColor)
            ps_converge_menu.config(fg=entryTextColor)
            ps_converge_menu.config(highlightthickness=0)
            ps_converge_menu.config(font=(fontType,17))
            ps_converge_menu.nametowidget(ps_converge_menu.menuname).config(font=(fontType,17))
            ps_IC_move = tk.StringVar(calc_vehicle)
            ps_IC_move.set("Show")
            ps_IC_move_menu = tk.OptionMenu(calc_vehicle_inputs,ps_IC_move,"Show","Hide")
            ps_IC_move_menu.grid(row = i_row+2, column=i_column+1)
            ps_IC_move_menu.config(bg=textEntryColor)
            ps_IC_move_menu.config(fg=entryTextColor)
            ps_IC_move_menu.config(highlightthickness=0)
            ps_IC_move_menu.config(font=(fontType,17))
            ps_IC_move_menu.nametowidget(ps_IC_move_menu.menuname).config(font=(fontType,17))
            ps_ride_IC = tk.StringVar(calc_vehicle)
            ps_ride_IC.set("Show")
            ps_ride_IC_menu = tk.OptionMenu(calc_vehicle_inputs,ps_ride_IC,"Show","Hide")
            ps_ride_IC_menu.grid(row = i_row+3, column=i_column+1)
            ps_ride_IC_menu.config(bg=textEntryColor)
            ps_ride_IC_menu.config(fg=entryTextColor)
            ps_ride_IC_menu.config(highlightthickness=0)
            ps_ride_IC_menu.config(font=(fontType,17))
            ps_ride_IC_menu.nametowidget(ps_ride_IC_menu.menuname).config(font=(fontType,17))
            ps_axle_roll = tk.StringVar(calc_vehicle)
            ps_axle_roll.set("Show")
            ps_axle_roll_menu = tk.OptionMenu(calc_vehicle_inputs,ps_axle_roll,"Show","Hide")
            ps_axle_roll_menu.grid(row = i_row+4, column=i_column+1)
            ps_axle_roll_menu.config(bg=textEntryColor)
            ps_axle_roll_menu.config(fg=entryTextColor)
            ps_axle_roll_menu.config(highlightthickness=0)
            ps_axle_roll_menu.config(font=(fontType,17))
            ps_axle_roll_menu.nametowidget(ps_axle_roll_menu.menuname).config(font=(fontType,17))
            ps_roll_center = tk.StringVar(calc_vehicle)
            ps_roll_center.set("Show")
            ps_roll_center_menu = tk.OptionMenu(calc_vehicle_inputs,ps_roll_center,"Show","Hide")
            ps_roll_center_menu.grid(row = i_row+1, column=i_column+3)
            ps_roll_center_menu.config(bg=textEntryColor)
            ps_roll_center_menu.config(fg=entryTextColor)
            ps_roll_center_menu.config(highlightthickness=0)
            ps_roll_center_menu.config(font=(fontType,17))
            ps_roll_center_menu.nametowidget(ps_roll_center_menu.menuname).config(font=(fontType,17))
            ps_body_roll = tk.StringVar(calc_vehicle)
            ps_body_roll.set("Show")
            ps_body_roll_menu = tk.OptionMenu(calc_vehicle_inputs,ps_body_roll,"Show","Hide")
            ps_body_roll_menu.grid(row = i_row+2, column=i_column+3)
            ps_body_roll_menu.config(bg=textEntryColor)
            ps_body_roll_menu.config(fg=entryTextColor)
            ps_body_roll_menu.config(highlightthickness=0)
            ps_body_roll_menu.config(font=(fontType,17))
            ps_body_roll_menu.nametowidget(ps_body_roll_menu.menuname).config(font=(fontType,17))
            ps_100_anti = tk.StringVar(calc_vehicle)
            ps_100_anti.set("Show")
            ps_100_anti_menu = tk.OptionMenu(calc_vehicle_inputs,ps_100_anti,"Show","Hide")
            ps_100_anti_menu.grid(row = i_row+3, column=i_column+3)
            ps_100_anti_menu.config(bg=textEntryColor)
            ps_100_anti_menu.config(fg=entryTextColor)
            ps_100_anti_menu.config(highlightthickness=0)
            ps_100_anti_menu.config(font=(fontType,17))
            ps_100_anti_menu.nametowidget(ps_100_anti_menu.menuname).config(font=(fontType,17))
            ps_ride_anti = tk.StringVar(calc_vehicle)
            ps_ride_anti.set("Show")
            ps_ride_anti_menu = tk.OptionMenu(calc_vehicle_inputs,ps_ride_anti,"Show","Hide")
            ps_ride_anti_menu.grid(row = i_row+4, column=i_column+3)
            ps_ride_anti_menu.config(bg=textEntryColor)
            ps_ride_anti_menu.config(fg=entryTextColor)
            ps_ride_anti_menu.config(highlightthickness=0)
            ps_ride_anti_menu.config(font=(fontType,17))
            ps_ride_anti_menu.nametowidget(ps_ride_anti_menu.menuname).config(font=(fontType,17))

        if True: # Vehicle Outputs
            calc_outputs = tk.Frame(calc_vehicle,background=bgColor)
            calc_outputs.grid(row=1,column=0,sticky='nesw')

            if True: # Vehicle Outputs
                label = tk.Label(calc_outputs, text="Sprung Mass Center of Gravity",background=bgColor,foreground=entryTextColor,font=(fontType,20), justify=tk.CENTER)
                label.grid(row=0,column=0,columnspan=6,sticky="sewn")
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="At Static Ride Height:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=1,column=0,sticky='e',columnspan=2)
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="From Roll Axis:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=1,column=3,sticky='e',columnspan=2)
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Above Rear Roll Center:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=2,column=0,sticky='e',columnspan=2)
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Above Front Roll Center:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=2,column=3,sticky='e',columnspan=2)
                label.bind("<1>", lambda event: update_outputs())
                label_CG_ride = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_CG_ride.grid(row=1,column=2,sticky='w')
                label_CG_ride.bind("<1>", lambda event: update_outputs())
                label_CG_body = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_CG_body.grid(row=1,column=5,sticky='w')
                label_CG_body.bind("<1>", lambda event: update_outputs())
                label_CG_rear = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_CG_rear.grid(row=2,column=2,sticky='w')
                label_CG_rear.bind("<1>", lambda event: update_outputs())
                label_CG_front = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_CG_front.grid(row=2,column=5,sticky='w')
                label_CG_front.bind("<1>", lambda event: update_outputs())
                

                label = tk.Label(calc_outputs, text="Roll Information",background=bgColor,foreground=entryTextColor,font=(fontType,20), justify=tk.CENTER)
                label.grid(row=0,column=9,columnspan=6,sticky="sewn")
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Body Roll Axis:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=1,column=11,sticky='e',columnspan=2)
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Side Roll Over:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=1,column=9,sticky='e',columnspan=2)
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Climb Flip Over:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=2,column=9,sticky='e',columnspan=2)
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Descent Flip Over:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=2,column=11,sticky='e',columnspan=2)
                label.bind("<1>", lambda event: update_outputs())
                label_body_roll = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_body_roll.grid(row=1,column=13,sticky='w',columnspan=2)
                label_body_roll.bind("<1>", lambda event: update_outputs())
                label_side_flip = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_side_flip.grid(row=1,column=11,sticky='w')
                label_side_flip.bind("<1>", lambda event: update_outputs())
                label_climb_flip = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_climb_flip.grid(row=2,column=11,sticky='w')
                label_climb_flip.bind("<1>", lambda event: update_outputs())
                label_descent_flip = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_descent_flip.grid(row=2,column=13,sticky='w')
                label_descent_flip.bind("<1>", lambda event: update_outputs())

            label = tk.Label(calc_outputs, text=" ",background=bgColor,foreground=bgColor,font=(fontType,1))
            label.grid(row=3, column = 0)
            label.bind("<1>", lambda event: update_outputs())

            if True: # Rear Text Outputs
                i_column = 0
                i_row = 4

                label = tk.Label(calc_outputs, text="Rear Upper",background=upperColor,foreground=entryTextColor,font=(fontType,20), justify=tk.CENTER)
                label.grid(row=i_row+0,column=i_column+0,columnspan=2,padx=3,sticky="sewn")
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Rear Lower",background=lowerColor,foreground=textEntryColor,font=(fontType,20), justify=tk.CENTER)
                label.grid(row=i_row+0,column=i_column+2,columnspan=2,padx=3,sticky="sewn")
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Rear Panhard",background=panhardColor,foreground=textEntryColor,font=(fontType,20), justify=tk.CENTER)
                label.grid(row=i_row+0,column=i_column+4,columnspan=2,padx=3,sticky="sewn")
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(calc_outputs, text="Max Force:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+1,column=i_column+0,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Max Force:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+1,column=i_column+2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Max Force:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+1,column=i_column+4,sticky='e')
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(calc_outputs, text="Convergence:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+2,column=i_column+0,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="3d Length:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+3,column=i_column+0,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="% of 3d Lower:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+4,column=i_column+0,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Side View Length:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+5,column=i_column+0,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="% Side View Lower:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+6,column=i_column+0,sticky='e')
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(calc_outputs, text="Convergence:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+2,column=i_column+2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="3d Length:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+3,column=i_column+2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="% 3d Upper:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+4,column=i_column+2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Side View Length:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+5,column=i_column+2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="% Side View Upper:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+6,column=i_column+2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(calc_outputs, text="3d Length:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+2,column=i_column+4,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Rear View Length:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+3,column=i_column+4,sticky='e')
                label.bind("<1>", lambda event: update_outputs())

                label_RU_Force = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),width=7,anchor="w")
                label_RU_Force.grid(row=i_row+1,column=i_column+1,sticky='w')
                label_RU_Force.bind("<1>", lambda event: update_outputs())
                label_RL_Force = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),width=7,anchor="w")
                label_RL_Force.grid(row=i_row+1,column=i_column+3,sticky='w')
                label_RL_Force.bind("<1>", lambda event: update_outputs())
                label_RP_Force = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),width=7,anchor="w")
                label_RP_Force.grid(row=i_row+1,column=i_column+5,sticky='w')
                label_RP_Force.bind("<1>", lambda event: update_outputs())

                label_RU_Converge = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_RU_Converge.grid(row=i_row+2,column=i_column+1,sticky='w')
                label_RU_Converge.bind("<1>", lambda event: update_outputs())
                label_RL_Converge = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_RL_Converge.grid(row=i_row+2,column=i_column+3,sticky='w')
                label_RL_Converge.bind("<1>", lambda event: update_outputs())

                label_RU_3d_length = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_RU_3d_length.grid(row=i_row+3,column=i_column+1,sticky='w')
                label_RU_3d_length.bind("<1>", lambda event: update_outputs())
                label_RL_3d_length = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_RL_3d_length.grid(row=i_row+3,column=i_column+3,sticky='w')
                label_RL_3d_length.bind("<1>", lambda event: update_outputs())
                
                label_RP_3d_length = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_RP_3d_length.grid(row=i_row+2,column=i_column+5,sticky='w')
                label_RP_3d_length.bind("<1>", lambda event: update_outputs())

                label_RU_2d_length = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_RU_2d_length.grid(row=i_row+5,column=i_column+1,sticky='w')
                label_RU_2d_length.bind("<1>", lambda event: update_outputs())
                label_RL_2d_length = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_RL_2d_length.grid(row=i_row+5,column=i_column+3,sticky='w')
                label_RL_2d_length.bind("<1>", lambda event: update_outputs())
                label_RP_2d_length = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_RP_2d_length.grid(row=i_row+3,column=i_column+5,sticky='w')
                label_RP_2d_length.bind("<1>", lambda event: update_outputs())

                label_RU_3d_percent = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_RU_3d_percent.grid(row=i_row+4,column=i_column+1,sticky='w')
                label_RU_3d_percent.bind("<1>", lambda event: update_outputs())
                label_RL_3d_percent = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_RL_3d_percent.grid(row=i_row+4,column=i_column+3,sticky='w')
                label_RL_3d_percent.bind("<1>", lambda event: update_outputs())

                label_RU_2d_percent = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_RU_2d_percent.grid(row=i_row+6,column=i_column+1,sticky='w')
                label_RU_2d_percent.bind("<1>", lambda event: update_outputs())
                label_RL_2d_percent = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_RL_2d_percent.grid(row=i_row+6,column=i_column+3,sticky='w')
                label_RL_2d_percent.bind("<1>", lambda event: update_outputs())

                label = tk.Label(calc_outputs, text="Rear Total Convergence:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+7,column=i_column+0,columnspan=2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label_R_converge = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_R_converge.grid(row=i_row+7,column=i_column+2,columnspan=2,sticky='w')
                label_R_converge.bind("<1>", lambda event: update_outputs())

            label = tk.Label(calc_outputs, text=" ",background=bgColor,foreground=bgColor,font=(fontType,15))
            label.grid(row=0,column=8)
            label.bind("<1>", lambda event: update_outputs())

            if True: # Front Text Outputs
                i_column = 9

                label = tk.Label(calc_outputs, text="Front Upper",background=upperColor,foreground=entryTextColor,font=(fontType,20), justify=tk.CENTER)
                label.grid(row=i_row+0,column=i_column+0,columnspan=2,padx=3,sticky="sewn")
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Front Lower",background=lowerColor,foreground=textEntryColor,font=(fontType,20), justify=tk.CENTER)
                label.grid(row=i_row+0,column=i_column+2,columnspan=2,padx=3,sticky="sewn")
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Front Panhard",background=panhardColor,foreground=textEntryColor,font=(fontType,20), justify=tk.CENTER)
                label.grid(row=i_row+0,column=i_column+4,columnspan=2,padx=3,sticky="sewn")
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(calc_outputs, text="Max Force:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+1,column=i_column+0,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Max Force:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+1,column=i_column+2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Max Force:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+1,column=i_column+4,sticky='e')
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(calc_outputs, text="Convergence:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+2,column=i_column+0,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="3d Length:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+3,column=i_column+0,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="% of 3d Lower:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+4,column=i_column+0,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Side View Length:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+5,column=i_column+0,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="% Side View Lower:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+6,column=i_column+0,sticky='e')
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(calc_outputs, text="Convergence:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+2,column=i_column+2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="3d Length:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+3,column=i_column+2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="% of 3d Upper:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+4,column=i_column+2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Side View Length:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+5,column=i_column+2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="% Side View Upper:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+6,column=i_column+2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())

                label = tk.Label(calc_outputs, text="3d Length:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+2,column=i_column+4,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label = tk.Label(calc_outputs, text="Front View Length:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+3,column=i_column+4,sticky='e')
                label.bind("<1>", lambda event: update_outputs())

                label_FU_Force = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),width=7,anchor="w")
                label_FU_Force.grid(row=i_row+1,column=i_column+1,sticky='w')
                label_FU_Force.bind("<1>", lambda event: update_outputs())
                label_FL_Force = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),width=7,anchor="w")
                label_FL_Force.grid(row=i_row+1,column=i_column+3,sticky='w')
                label_FL_Force.bind("<1>", lambda event: update_outputs())
                label_FP_Force = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),width=7,anchor="w")
                label_FP_Force.grid(row=i_row+1,column=i_column+5,sticky='w')
                label_FP_Force.bind("<1>", lambda event: update_outputs())

                label_FU_Converge = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_FU_Converge.grid(row=i_row+2,column=i_column+1,sticky='w')
                label_FU_Converge.bind("<1>", lambda event: update_outputs())
                label_FL_Converge = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_FL_Converge.grid(row=i_row+2,column=i_column+3,sticky='w')
                label_FL_Converge.bind("<1>", lambda event: update_outputs())

                label_FU_3d_length = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_FU_3d_length.grid(row=i_row+3,column=i_column+1,sticky='w')
                label_FU_3d_length.bind("<1>", lambda event: update_outputs())
                label_FL_3d_length = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_FL_3d_length.grid(row=i_row+3,column=i_column+3,sticky='w')
                label_FL_3d_length.bind("<1>", lambda event: update_outputs())
                label_FP_3d_length = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_FP_3d_length.grid(row=i_row+2,column=i_column+5,sticky='w')
                label_FP_3d_length.bind("<1>", lambda event: update_outputs())

                label_FU_2d_length = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_FU_2d_length.grid(row=i_row+5,column=i_column+1,sticky='w')
                label_FU_2d_length.bind("<1>", lambda event: update_outputs())
                label_FL_2d_length = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_FL_2d_length.grid(row=i_row+5,column=i_column+3,sticky='w')
                label_FL_2d_length.bind("<1>", lambda event: update_outputs())
                label_FP_2d_length = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_FP_2d_length.grid(row=i_row+3,column=i_column+5,sticky='w')
                label_FP_2d_length.bind("<1>", lambda event: update_outputs())

                label_FU_3d_percent = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_FU_3d_percent.grid(row=i_row+4,column=i_column+1,sticky='w')
                label_FU_3d_percent.bind("<1>", lambda event: update_outputs())
                label_FL_3d_percent = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_FL_3d_percent.grid(row=i_row+4,column=i_column+3,sticky='w')
                label_FL_3d_percent.bind("<1>", lambda event: update_outputs())

                label_FU_2d_percent = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_FU_2d_percent.grid(row=i_row+6,column=i_column+1,sticky='w')
                label_FU_2d_percent.bind("<1>", lambda event: update_outputs())
                label_FL_2d_percent = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_FL_2d_percent.grid(row=i_row+6,column=i_column+3,sticky='w')
                label_FL_2d_percent.bind("<1>", lambda event: update_outputs())

                label = tk.Label(calc_outputs, text="Front Total Convergence:",background=bgColor,foreground=entryTextColor,font=(fontType,15), justify=tk.RIGHT)
                label.grid(row=i_row+7,column=i_column+0,columnspan=2,sticky='e')
                label.bind("<1>", lambda event: update_outputs())
                label_F_converge = tk.Label(calc_outputs, text="",background=bgColor,foreground=entryTextColor,font=(fontType,15),anchor="w")
                label_F_converge.grid(row=i_row+7,column=i_column+2,columnspan=2,sticky='w')
                label_F_converge.bind("<1>", lambda event: update_outputs())

            

        if True: # Setup Plot Areas
            self.figF, self.axF = plt.subplots(2,2)
            self.figF.subplots_adjust(hspace=.25)
            self.figF.subplots_adjust(wspace=.2)
            self.figF.set_facecolor(bgColor)

            self.figR, self.axR = plt.subplots(2,2)
            self.figF.subplots_adjust(hspace=.25)
            self.figF.subplots_adjust(wspace=.2)
            self.figR.set_facecolor(bgColor)

            self.figF_view,self.axF_view = plt.subplots(1,1)
            self.figF_view.set_facecolor(bgColor)
            self.figF_view.tight_layout()
            self.figR_view,self.axR_view = plt.subplots(1,1)
            self.figR_view.set_facecolor(bgColor)
            self.figR_view.tight_layout()

            self.figV, self.axV = plt.subplots(2,2)
            self.figV.set_facecolor(bgColor)

            self.F_plots = FigureCanvasTkAgg(self.figF,self)
            self.R_plots = FigureCanvasTkAgg(self.figR,self)
            self.F_view = FigureCanvasTkAgg(self.figF_view,self)
            self.R_view = FigureCanvasTkAgg(self.figR_view,self)
            self.V_plots = FigureCanvasTkAgg(self.figV,self)
            self.F_plots.get_tk_widget().grid(row=3,column=2,sticky="nesw")
            self.R_plots.get_tk_widget().grid(row=3,column=0,sticky="nesw")
            self.F_view.get_tk_widget().grid(row=4,column=2,sticky="nesw")
            self.R_view.get_tk_widget().grid(row=4,column=0,sticky="nesw")
            self.V_plots.get_tk_widget().grid(row=2,column=1,rowspan=3,sticky="nesw")

        def update_outputs(*args):
            self.focus_set()
            plots_changed = False
            
            if self.opening:
                plots_changed = True
            else:
                if True: # Get Front Inputs
                    if F_UL_Count.get() == "1" and inputs.F.U_count == 2:
                        inputs.F.U_count = 1
                        plots_changed = True
                    elif F_UL_Count.get() == "2" and inputs.F.U_count == 1:
                        inputs.F.U_count = 2
                        plots_changed = True
                    if F_P_exist.get() == "Yes" and inputs.F.panhard == False:
                        inputs.F.panhard = True
                        plots_changed = True
                    elif F_P_exist.get() == "No" and inputs.F.panhard == True:
                        inputs.F.panhard = False
                        plots_changed = True

                    if inputs.F.bump != float(F_Bump.get()):
                        inputs.F.bump = float(F_Bump.get())
                        plots_changed = True
                    if inputs.F.droop != float(F_Droop.get()):
                        inputs.F.droop = float(F_Droop.get())
                        plots_changed = True
                    if inputs.F.unsprung_mass != float(F_mass.get()):
                        inputs.F.unsprung_mass = float(F_mass.get())
                        plots_changed = True
                    if inputs.F.tire_radius != float(F_tire_radius.get()):
                        inputs.F.tire_radius = float(F_tire_radius.get())
                        plots_changed = True

                    if inputs.F.track_width != float(F_Track.get()):
                        inputs.F.track_width = float(F_Track.get())
                        plots_changed = True
                    if inputs.F.portal_height != float(F_Portal.get()):
                        inputs.F.portal_height = float(F_Portal.get())
                        plots_changed = True
                    if inputs.F.axle_tube != float(F_axle_tube.get()):
                        inputs.F.axle_tube = float(F_axle_tube.get())
                        plots_changed = True
                    if inputs.F.tire_diameter != float(F_tire_diameter.get()):
                        inputs.F.tire_diameter = float(F_tire_diameter.get())
                        plots_changed = True
                    if inputs.F.tire_width != float(F_tire_width.get()):
                        inputs.F.tire_width = float(F_tire_width.get())
                        plots_changed = True

                    if inputs.F.UA[x] != float(FUAX.get()):
                        inputs.F.UA[x] = float(FUAX.get())
                        plots_changed = True
                    if inputs.F.UA[y] != float(FUAY.get()):
                        inputs.F.UA[y] = float(FUAY.get())
                        plots_changed = True
                    if inputs.F.UA[z] != float(FUAZ.get()):
                        inputs.F.UA[z] = float(FUAZ.get())
                        plots_changed = True
                    if inputs.F.UF[x] != float(FUFX.get()):
                        inputs.F.UF[x] = float(FUFX.get())
                        plots_changed = True
                    if inputs.F.UF[y] != float(FUFY.get()):
                        inputs.F.UF[y] = float(FUFY.get())
                        plots_changed = True
                    if inputs.F.UF[z] != float(FUFZ.get()):
                        inputs.F.UF[z] = float(FUFZ.get())
                        plots_changed = True

                    if inputs.F.LA[x] != float(FLAX.get()):
                        inputs.F.LA[x] = float(FLAX.get())
                        plots_changed = True
                    if inputs.F.LA[y] != float(FLAY.get()):
                        inputs.F.LA[y] = float(FLAY.get())
                        plots_changed = True
                    if inputs.F.LA[z] != float(FLAZ.get()):
                        inputs.F.LA[z] = float(FLAZ.get())
                        plots_changed = True
                    if inputs.F.LF[x] != float(FLFX.get()):
                        inputs.F.LF[x] = float(FLFX.get())
                        plots_changed = True
                    if inputs.F.LF[y] != float(FLFY.get()):
                        inputs.F.LF[y] = float(FLFY.get())
                        plots_changed = True
                    if inputs.F.LF[z] != float(FLFZ.get()):
                        inputs.F.LF[z] = float(FLFZ.get())
                        plots_changed = True

                    if inputs.F.panhard:
                        if inputs.F.PA[x] != float(FPAX.get()):
                            inputs.F.PA[x] = float(FPAX.get())
                            plots_changed = True
                        if inputs.F.PA[y] != float(FPAY.get()):
                            inputs.F.PA[y] = float(FPAY.get())
                            plots_changed = True
                        if inputs.F.PA[z] != float(FPAZ.get()):
                            inputs.F.PA[z] = float(FPAZ.get())
                            plots_changed = True
                        if inputs.F.PF[x] != float(FPFX.get()):
                            inputs.F.PF[x] = float(FPFX.get())
                            plots_changed = True
                        if inputs.F.PF[y] != float(FPFY.get()):
                            inputs.F.PF[y] = float(FPFY.get())
                            plots_changed = True
                        if inputs.F.PF[z] != float(FPFZ.get()):
                            inputs.F.PF[z] = float(FPFZ.get())
                            plots_changed = True

                if True: # Get Rear Inputs
                    if R_UL_Count.get() == "1" and inputs.R.U_count == 2:
                        inputs.R.U_count = 1
                        plots_changed = True
                    elif R_UL_Count.get() == "2" and inputs.R.U_count == 1:
                        inputs.R.U_count = 2
                        plots_changed = True
                    if R_P_exist.get() == "Yes" and inputs.R.panhard == False:
                        inputs.R.panhard = True
                        plots_changed = True
                    elif R_P_exist.get() == "No" and inputs.R.panhard == True:
                        inputs.R.panhard = False
                        plots_changed = True

                    if inputs.R.bump != float(R_Bump.get()):
                        inputs.R.bump = float(R_Bump.get())
                        plots_changed = True
                    if inputs.R.droop != float(R_Droop.get()):
                        inputs.R.droop = float(R_Droop.get())
                        plots_changed = True
                    if inputs.R.unsprung_mass != float(R_mass.get()):
                        inputs.R.unsprung_mass = float(R_mass.get())
                        plots_changed = True
                    if inputs.R.tire_radius != float(R_tire_radius.get()):
                        inputs.R.tire_radius = float(R_tire_radius.get())
                        plots_changed = True

                    if inputs.R.track_width != float(R_Track.get()):
                        inputs.R.track_width = float(R_Track.get())
                        plots_changed = True
                    if inputs.R.portal_height != float(R_Portal.get()):
                        inputs.R.portal_height = float(R_Portal.get())
                        plots_changed = True
                    if inputs.R.axle_tube != float(R_axle_tube.get()):
                        inputs.R.axle_tube = float(R_axle_tube.get())
                        plots_changed = True
                    if inputs.R.tire_diameter != float(R_tire_diameter.get()):
                        inputs.R.tire_diameter = float(R_tire_diameter.get())
                        plots_changed = True
                    if inputs.R.tire_width != float(R_tire_width.get()):
                        inputs.R.tire_width = float(R_tire_width.get())
                        plots_changed = True

                    if inputs.R.UA[x] != float(RUAX.get()):
                        inputs.R.UA[x] = float(RUAX.get())
                        plots_changed = True
                    if inputs.R.UA[y] != float(RUAY.get()):
                        inputs.R.UA[y] = float(RUAY.get())
                        plots_changed = True
                    if inputs.R.UA[z] != float(RUAZ.get()):
                        inputs.R.UA[z] = float(RUAZ.get())
                        plots_changed = True
                    if inputs.R.UF[x] != float(RUFX.get()):
                        inputs.R.UF[x] = float(RUFX.get())
                        plots_changed = True
                    if inputs.R.UF[y] != float(RUFY.get()):
                        inputs.R.UF[y] = float(RUFY.get())
                        plots_changed = True
                    if inputs.R.UF[z] != float(RUFZ.get()):
                        inputs.R.UF[z] = float(RUFZ.get())
                        plots_changed = True

                    if inputs.R.LA[x] != float(RLAX.get()):
                        inputs.R.LA[x] = float(RLAX.get())
                        plots_changed = True
                    if inputs.R.LA[y] != float(RLAY.get()):
                        inputs.R.LA[y] = float(RLAY.get())
                        plots_changed = True
                    if inputs.R.LA[z] != float(RLAZ.get()):
                        inputs.R.LA[z] = float(RLAZ.get())
                        plots_changed = True
                    if inputs.R.LF[x] != float(RLFX.get()):
                        inputs.R.LF[x] = float(RLFX.get())
                        plots_changed = True
                    if inputs.R.LF[y] != float(RLFY.get()):
                        inputs.R.LF[y] = float(RLFY.get())
                        plots_changed = True
                    if inputs.R.LF[z] != float(RLFZ.get()):
                        inputs.R.LF[z] = float(RLFZ.get())
                        plots_changed = True

                    if inputs.R.panhard:
                        if inputs.R.PA[x] != float(RPAX.get()):
                            inputs.R.PA[x] = float(RPAX.get())
                            plots_changed = True
                        if inputs.R.PA[y] != float(RPAY.get()):
                            inputs.R.PA[y] = float(RPAY.get())
                            plots_changed = True
                        if inputs.R.PA[z] != float(RPAZ.get()):
                            inputs.R.PA[z] = float(RPAZ.get())
                            plots_changed = True
                        if inputs.R.PF[x] != float(RPFX.get()):
                            inputs.R.PF[x] = float(RPFX.get())
                            plots_changed = True
                        if inputs.R.PF[y] != float(RPFY.get()):
                            inputs.R.PF[y] = float(RPFY.get())
                            plots_changed = True
                        if inputs.R.PF[z] != float(RPFZ.get()):
                            inputs.R.PF[z] = float(RPFZ.get())
                            plots_changed = True

                if True: # Get Vehicle Inputs
                    if inputs.V.wheelbase != float(wheelbase.get()):
                        inputs.V.wheelbase = float(wheelbase.get())
                        plots_changed = True
                    if inputs.V.drive_bias != float(drive_bias.get()):
                        inputs.V.drive_bias = float(drive_bias.get())
                        plots_changed = True
                    if inputs.V.brake_bias != float(brake_bias.get()):
                        inputs.V.brake_bias = float(brake_bias.get())
                        plots_changed = True
                    if inputs.V.weight_distribution != float(weight_dist.get()):
                        inputs.V.weight_distribution = float(weight_dist.get())
                        plots_changed = True
                    if inputs.V.mass != float(V_mass.get()):
                        inputs.V.mass = float(V_mass.get())
                        plots_changed = True
                    if inputs.V.CG_height != float(V_CG_Height.get()):
                        inputs.V.CG_height = float(V_CG_Height.get())
                        plots_changed = True
                    if inputs.V.acceleration != float(accel.get()):
                        inputs.V.acceleration = float(accel.get())
                        plots_changed = True
                    if inputs.V.transverse_acceleration != float(tran_accel.get()):
                        inputs.V.transverse_acceleration = float(tran_accel.get())
                        plots_changed = True

                if True: # Get Plot Settings
                    if PS.converge != ps_converge.get():
                        PS.converge = ps_converge.get()
                        plots_changed = True
                    if PS.IC_move != ps_IC_move.get():
                        PS.IC_move = ps_IC_move.get()
                        plots_changed = True
                    if PS.axle_roll != ps_axle_roll.get():
                        PS.axle_roll = ps_axle_roll.get()
                        plots_changed = True
                    if PS.body_roll != ps_body_roll.get():
                        PS.body_roll = ps_body_roll.get()
                        plots_changed = True
                    if PS.anti_100 != ps_100_anti.get():
                        PS.anti_100 = ps_100_anti.get()
                        plots_changed = True
                    if PS.ride_anti != ps_ride_anti.get():
                        PS.ride_anti = ps_ride_anti.get()
                        plots_changed = True
                    if PS.roll_center != ps_roll_center.get():
                        PS.roll_center = ps_roll_center.get()
                        plots_changed = True
                    if PS.ride_IC != ps_ride_IC.get():
                        PS.ride_IC = ps_ride_IC.get()
                        plots_changed = True

            run_link_calc()

            if plots_changed:
                if self.opening: # Clear Plots
                    self.opening = False
                else:
                    self.axF[0,0].clear()
                    self.axF[1,0].clear()
                    self.axF[0,1].clear()
                    self.axF[1,1].clear()
                    self.axF_view.clear()
                    self.axR[0,0].clear()
                    self.axR[1,0].clear()
                    self.axR[0,1].clear()
                    self.axR[1,1].clear()
                    self.axR_view.clear()
                    self.axV[0,0].clear()
                    self.axV[1,0].clear()
                    self.axV[0,1].clear()
                    self.axV[1,1].clear()

                linkLine = 3.5
                dottedLine = 2.5
                travelLine = 2.5
                markerSize = 7

                if True: # Plot Front
                    if True: # Antis
                        self.axF[0,0].plot(outputs.F.Anti_Dive,outputs.F.Travel,color=rideAntiColor)
                        self.axF[0,0].plot(outputs.F.Anti_Lift,outputs.F.Travel,color=plotSecondaryColor)
                        if inputs.V.brake_bias > inputs.V.drive_bias:
                            temp1 = 'left'
                            temp2 = 'right'
                        else:
                            temp1 = 'right'
                            temp2 = 'left'
                        self.axF[0,0].text(outputs.F.Anti_Dive[0],outputs.F.Travel[0],"{:.1f}%".format(outputs.F.Anti_Dive[0]),color=rideAntiColor,horizontalalignment=temp1)
                        self.axF[0,0].text(outputs.F.Anti_Lift[0],outputs.F.Travel[0],"{:.1f}%".format(outputs.F.Anti_Lift[0]),color=plotSecondaryColor,horizontalalignment=temp2)
                        self.axF[0,0].text(outputs.F.Anti_Dive[S.sample_points],outputs.F.Travel[S.sample_points],"{:.1f}%\nAntidive".format(outputs.F.Anti_Dive[S.sample_points]),color=rideAntiColor,horizontalalignment=temp1)
                        self.axF[0,0].text(outputs.F.Anti_Lift[S.sample_points],outputs.F.Travel[S.sample_points],"{:.1f}%\nAntilift".format(outputs.F.Anti_Lift[S.sample_points]),color=plotSecondaryColor,horizontalalignment=temp2)
                        self.axF[0,0].text(outputs.F.Anti_Dive[S.sample_points*2],outputs.F.Travel[S.sample_points*2],"{:.1f}%".format(outputs.F.Anti_Dive[S.sample_points*2]),color=rideAntiColor,horizontalalignment=temp1,va='top')
                        self.axF[0,0].text(outputs.F.Anti_Lift[S.sample_points*2],outputs.F.Travel[S.sample_points*2],"{:.1f}%".format(outputs.F.Anti_Lift[S.sample_points*2]),color=plotSecondaryColor,horizontalalignment=temp2,va='top')
                        self.axF[0,0].set_xlim([min(min(outputs.F.Anti_Lift),min(outputs.F.Anti_Dive))-5,max(max(outputs.F.Anti_Lift),max(outputs.F.Anti_Dive))+5])
                        self.axF[0,0].set_ylim([inputs.F.droop,inputs.F.bump])
                        self.axF[0,0].set_xlabel('Antis')
                        self.axF[0,0].set_ylabel('Travel [{}]'.format(S.position_units))
                        self.axF[0,0].grid(linewidth = 0.5,color=bgColor)

                    if True: # Roll slope
                        self.axF[0,1].plot(-outputs.F.Roll_Slope,outputs.F.Travel,color=rollColor)
                        self.axF[0,1].text(-outputs.F.Roll_Slope[0],outputs.F.Travel[0],"{:.1f}".format(-outputs.F.Roll_Slope[0]),color=rollColor)
                        self.axF[0,1].text(-outputs.F.Roll_Slope[S.sample_points],outputs.F.Travel[S.sample_points],"{:.1f}".format(-outputs.F.Roll_Slope[S.sample_points]),color=rollColor)
                        self.axF[0,1].text(-outputs.F.Roll_Slope[S.sample_points*2],outputs.F.Travel[S.sample_points*2],"{:.1f}".format(-outputs.F.Roll_Slope[S.sample_points*2]),color=rollColor,va='top')
                        self.axF[0,1].set_xlim([min(-outputs.F.Roll_Slope)-1,max(-outputs.F.Roll_Slope)+1])
                        self.axF[0,1].set_ylim([inputs.F.droop,inputs.F.bump])
                        self.axF[0,1].set_xlabel('Roll Slope [deg]')
                        self.axF[0,1].set_ylabel('Travel [{}]'.format(S.position_units))
                        self.axF[0,1].grid(linewidth = 0.5,color=bgColor)

                    if True: # Roll Center
                        self.axF[1,1].plot(outputs.F.Roll_Center,outputs.F.Travel,color=rollColor)
                        self.axF[1,1].text(outputs.F.Roll_Center[0],outputs.F.Travel[0],"{:.1f}".format(outputs.F.Roll_Center[0]),color=rollColor)
                        self.axF[1,1].text(outputs.F.Roll_Center[S.sample_points],outputs.F.Travel[S.sample_points],"{:.1f}".format(outputs.F.Roll_Center[S.sample_points]),color=rollColor)
                        self.axF[1,1].text(outputs.F.Roll_Center[S.sample_points*2],outputs.F.Travel[S.sample_points*2],"{:.1f}".format(outputs.F.Roll_Center[S.sample_points*2]),color=rollColor,va='top')
                        self.axF[1,1].set_xlim([min(outputs.F.Roll_Center)-1,max(outputs.F.Roll_Center)+1])
                        self.axF[1,1].set_ylim([inputs.F.droop,inputs.F.bump])
                        self.axF[1,1].set_xlabel('Roll Center [{}]'.format(S.position_units))
                        self.axF[1,1].set_ylabel('Travel [{}]'.format(S.position_units))
                        self.axF[1,1].grid(linewidth = 0.5,color=bgColor)

                    if True: # Pinion Change
                        self.axF[1,0].plot(-outputs.F.Pinion_Change,outputs.F.Travel,color=plotMainColor)
                        self.axF[1,0].text(-outputs.F.Pinion_Change[0],outputs.F.Travel[0],"{:.1f}".format(-outputs.F.Pinion_Change[0]),color=plotMainColor)
                        self.axF[1,0].text(-outputs.F.Pinion_Change[S.sample_points],outputs.F.Travel[S.sample_points],"0",color=plotMainColor)
                        self.axF[1,0].text(-outputs.F.Pinion_Change[S.sample_points*2],outputs.F.Travel[S.sample_points*2],"{:.1f}".format(-outputs.F.Pinion_Change[S.sample_points*2]),color=plotMainColor,va='top')
                        self.axF[1,0].set_xlim([min(-outputs.F.Pinion_Change)-1,max(-outputs.F.Pinion_Change)+1])
                        self.axF[1,0].set_ylim([inputs.F.droop,inputs.F.bump])
                        self.axF[1,0].set_xlabel('Pinion Change [deg]')
                        self.axF[1,0].set_ylabel('Travel [{}]'.format(S.position_units))
                        self.axF[1,0].grid(linewidth = 0.5,color=bgColor)

                    for i_x in range(2):
                        for i_y in range(2):
                            self.axF[i_x,i_y].set_facecolor(textEntryColor)
                            self.axF[i_x,i_y].xaxis.label.set_color(entryTextColor)
                            self.axF[i_x,i_y].yaxis.label.set_color(entryTextColor)
                            self.axF[i_x,i_y].spines[['top','bottom','left','right']].set_color(entryTextColor)
                            self.axF[i_x,i_y].tick_params(axis='x', colors=entryTextColor) 
                            self.axF[i_x,i_y].tick_params(axis='y', colors=entryTextColor)

                    c1x = inputs.F.track_width/2+inputs.F.tire_width/2
                    c1y = inputs.F.tire_radius+.5*inputs.F.tire_diameter
                    c2x = inputs.F.track_width/2+inputs.F.tire_width/2
                    c2y = 0
                    c3x = inputs.F.track_width/2-inputs.F.tire_width/2
                    c3y = 0
                    c4x = inputs.F.track_width/2-inputs.F.tire_width/2
                    c4y = inputs.F.tire_radius+.5*inputs.F.tire_diameter
                    self.axF_view.plot([c1x,c4x],[c1y,c4y],color=vehicleColor) # Pos y tire top line
                    self.axF_view.plot([c2x,c3x],[c2y,c3y],color=vehicleColor) # Pos y tire bottom line
                    self.axF_view.plot([c1x,c2x],[c1y,c2y],color=vehicleColor) # Pos y tire pos y line
                    self.axF_view.plot([c3x,c4x],[c3y,c4y],color=vehicleColor) # Pos y tire neg y line

                    c1x = -inputs.F.track_width/2+inputs.F.tire_width/2
                    c1y = inputs.F.tire_radius+.5*inputs.F.tire_diameter
                    c2x = -inputs.F.track_width/2+inputs.F.tire_width/2
                    c2y = 0
                    c3x = -inputs.F.track_width/2-inputs.F.tire_width/2
                    c3y = 0
                    c4x = -inputs.F.track_width/2-inputs.F.tire_width/2
                    c4y = inputs.F.tire_radius+.5*inputs.F.tire_diameter
                    self.axF_view.plot([c1x,c4x],[c1y,c4y],color=vehicleColor) # Neg y tire top line
                    self.axF_view.plot([c2x,c3x],[c2y,c3y],color=vehicleColor) # Neg y tire bottom line
                    self.axF_view.plot([c1x,c2x],[c1y,c2y],color=vehicleColor) # Neg y tire pos y line
                    self.axF_view.plot([c3x,c4x],[c3y,c4y],color=vehicleColor) # Neg y tire neg y line

                    x1 = inputs.F.track_width/2-inputs.F.tire_width/2
                    x2 = -inputs.F.track_width/2+inputs.F.tire_width/2
                    y1 = inputs.F.tire_radius+inputs.F.axle_tube/2
                    y2 = inputs.F.tire_radius+inputs.F.axle_tube/2
                    self.axF_view.plot([x1,x2],[y1,y2],color=vehicleColor) # Upper axle tube
                    x1 = inputs.F.track_width/2-inputs.F.tire_width/2
                    x2 = -inputs.F.track_width/2+inputs.F.tire_width/2
                    y1 = inputs.F.tire_radius-inputs.F.axle_tube/2
                    y2 = inputs.F.tire_radius-inputs.F.axle_tube/2
                    self.axF_view.plot([x1,x2],[y1,y2],color=vehicleColor) # Lower axle tube

                    if inputs.F.panhard:
                        x1 = outputs.F.PF[y]
                        x2 = outputs.F.PA[S.sample_points,y]
                        y1 = outputs.F.PF[z]
                        y2 = outputs.F.PA[S.sample_points,z]
                        self.axF_view.plot([x1,x2],[y1,y2],linewidth=linkLine,color=panhardColor) # Panhard ride
                        x1 = outputs.F.PF[y]
                        x2 = outputs.F.PA[2*S.sample_points,y]
                        y1 = outputs.F.PF[z]
                        y2 = outputs.F.PA[2*S.sample_points,z]
                        self.axF_view.plot([x1,x2],[y1,y2],linewidth=travelLine,color=panhardColor) # Panhard bump
                        x1 = outputs.F.PF[y]
                        x2 = outputs.F.PA[0,y]
                        y1 = outputs.F.PF[z]
                        y2 = outputs.F.PA[0,z]
                        self.axF_view.plot([x1,x2],[y1,y2],linewidth=travelLine,color=panhardColor) # Panhard droop
                        self.axF_view.plot(outputs.F.PA[:,y],outputs.F.PA[:,z],linestyle="dotted",linewidth=dottedLine,color=panhardColor) # Panhard arc

                    self.axF_view.axis('equal')
                    self.axF_view.set_xlim([-1.1*inputs.F.track_width/2-inputs.F.tire_width,1.1*inputs.F.track_width/2+inputs.F.tire_width])
                    self.axF_view.set_ylim([0,1.1*inputs.F.tire_diameter])

                    self.axF_view.set_facecolor(textEntryColor)
                    self.axF_view.xaxis.label.set_color(entryTextColor)
                    self.axF_view.yaxis.label.set_color(entryTextColor)
                    self.axF_view.spines[['top','bottom','left','right']].set_color(entryTextColor)
                    self.axF_view.tick_params(axis='x', colors=entryTextColor)
                    self.axF_view.tick_params(axis='y', colors=entryTextColor)

                    self.axF_view.set_title('View From Front',color=entryTextColor, y=1.0, pad=-23)


                if True: # Plot Rear
                    if True: # Antis
                        self.axR[0,0].plot(outputs.R.Anti_Squat,outputs.R.Travel,color=rideAntiColor)
                        self.axR[0,0].plot(outputs.R.Anti_Lift,outputs.R.Travel,color=plotSecondaryColor)
                        if inputs.V.brake_bias > inputs.V.drive_bias:
                            temp1 = 'left'
                            temp2 = 'right'
                        else:
                            temp1 = 'right'
                            temp2 = 'left'
                        self.axR[0,0].text(outputs.R.Anti_Squat[0],outputs.R.Travel[0],"{:.1f}%".format(outputs.R.Anti_Squat[0]),color=rideAntiColor,horizontalalignment=temp1)
                        self.axR[0,0].text(outputs.R.Anti_Lift[0],outputs.R.Travel[0],"{:.1f}%".format(outputs.R.Anti_Lift[0]),color=plotSecondaryColor,horizontalalignment=temp2)
                        self.axR[0,0].text(outputs.R.Anti_Squat[S.sample_points],outputs.R.Travel[S.sample_points],"{:.1f}%\nAntisquat".format(outputs.R.Anti_Squat[S.sample_points]),color=rideAntiColor,horizontalalignment=temp1)
                        self.axR[0,0].text(outputs.R.Anti_Lift[S.sample_points],outputs.R.Travel[S.sample_points],"{:.1f}%\nAntilift".format(outputs.R.Anti_Lift[S.sample_points]),color=plotSecondaryColor,horizontalalignment=temp2)
                        self.axR[0,0].text(outputs.R.Anti_Squat[S.sample_points*2],outputs.R.Travel[S.sample_points*2],"{:.1f}%".format(outputs.R.Anti_Squat[S.sample_points*2]),color=rideAntiColor,horizontalalignment=temp1,va='top')
                        self.axR[0,0].text(outputs.R.Anti_Lift[S.sample_points*2],outputs.R.Travel[S.sample_points*2],"{:.1f}%".format(outputs.R.Anti_Lift[S.sample_points*2]),color=plotSecondaryColor,horizontalalignment=temp2,va='top')
                        self.axR[0,0].set_xlim([min(min(outputs.R.Anti_Lift),min(outputs.R.Anti_Squat))-5,max(max(outputs.R.Anti_Lift),max(outputs.R.Anti_Squat))+5])
                        self.axR[0,0].set_ylim([inputs.R.droop,inputs.R.bump])
                        self.axR[0,0].set_xlabel('Antis')
                        self.axR[0,0].set_ylabel('Travel [{}]'.format(S.position_units))
                        self.axR[0,0].grid(linewidth = 0.5,color=bgColor)

                    if True: # Roll slope
                        self.axR[0,1].plot(outputs.R.Roll_Slope,outputs.R.Travel,color=rollColor)
                        self.axR[0,1].text(outputs.R.Roll_Slope[0],outputs.R.Travel[0],"{:.1f}".format(outputs.R.Roll_Slope[0]),color=rollColor)
                        self.axR[0,1].text(outputs.R.Roll_Slope[S.sample_points],outputs.R.Travel[S.sample_points],"{:.1f}".format(outputs.R.Roll_Slope[S.sample_points]),color=rollColor)
                        self.axR[0,1].text(outputs.R.Roll_Slope[S.sample_points*2],outputs.R.Travel[S.sample_points*2],"{:.1f}".format(outputs.R.Roll_Slope[S.sample_points*2]),color=rollColor,va='top')
                        self.axR[0,1].set_xlim([min(outputs.R.Roll_Slope)-1,max(outputs.R.Roll_Slope)+1])
                        self.axR[0,1].set_ylim([inputs.R.droop,inputs.R.bump])
                        self.axR[0,1].set_xlabel('Roll Slope [deg]')
                        self.axR[0,1].set_ylabel('Travel [{}]'.format(S.position_units))
                        self.axR[0,1].grid(linewidth = 0.5,color=bgColor)

                    if True: # Roll Center
                        self.axR[1,1].plot(outputs.R.Roll_Center,outputs.R.Travel,color=rollColor)
                        self.axR[1,1].text(outputs.R.Roll_Center[0],outputs.R.Travel[0],"{:.1f}".format(-outputs.R.Roll_Center[0]),color=rollColor)
                        self.axR[1,1].text(outputs.R.Roll_Center[S.sample_points],outputs.R.Travel[S.sample_points],"{:.1f}".format(outputs.R.Roll_Center[S.sample_points]),color=rollColor)
                        self.axR[1,1].text(outputs.R.Roll_Center[S.sample_points*2],outputs.R.Travel[S.sample_points*2],"{:.1f}".format(outputs.R.Roll_Center[S.sample_points*2]),color=rollColor,va='top')
                        self.axR[1,1].set_xlim([min(outputs.R.Roll_Center)-1,max(outputs.R.Roll_Center)+1])
                        self.axR[1,1].set_ylim([inputs.R.droop,inputs.R.bump])
                        self.axR[1,1].set_xlabel('Roll Center [{}]'.format(S.position_units))
                        self.axR[1,1].set_ylabel('Travel [{}]'.format(S.position_units))
                        self.axR[1,1].grid(linewidth = 0.5,color=bgColor)

                    if True: # Pinion Change
                        self.axR[1,0].plot(outputs.R.Pinion_Change,outputs.R.Travel,color=plotMainColor)
                        self.axR[1,0].text(outputs.R.Pinion_Change[0],outputs.R.Travel[0],"{:.1f}".format(outputs.R.Pinion_Change[0]),color=plotMainColor)
                        self.axR[1,0].text(outputs.R.Pinion_Change[S.sample_points],outputs.R.Travel[S.sample_points],"0",color=plotMainColor)
                        self.axR[1,0].text(outputs.R.Pinion_Change[S.sample_points*2],outputs.R.Travel[S.sample_points*2],"{:.1f}".format(outputs.R.Pinion_Change[S.sample_points*2]),color=plotMainColor,va='top')
                        self.axR[1,0].set_xlim([min(outputs.R.Pinion_Change)-1,max(outputs.R.Pinion_Change)+1])
                        self.axR[1,0].set_ylim([inputs.R.droop,inputs.R.bump])
                        self.axR[1,0].set_xlabel('Pinion Change [deg]')
                        self.axR[1,0].set_ylabel('Travel [{}]'.format(S.position_units))
                        self.axR[1,0].grid(linewidth = 0.5,color=bgColor)

                    for i_x in range(2):
                        for i_y in range(2):
                            self.axR[i_x,i_y].set_facecolor(textEntryColor)
                            self.axR[i_x,i_y].xaxis.label.set_color(entryTextColor)
                            self.axR[i_x,i_y].yaxis.label.set_color(entryTextColor)
                            self.axR[i_x,i_y].spines[['top','bottom','left','right']].set_color(entryTextColor)
                            self.axR[i_x,i_y].tick_params(axis='x', colors=entryTextColor) 
                            self.axR[i_x,i_y].tick_params(axis='y', colors=entryTextColor)

                    c1x = inputs.R.track_width/2+inputs.R.tire_width/2
                    c1y = inputs.R.tire_radius+.5*inputs.R.tire_diameter
                    c2x = inputs.R.track_width/2+inputs.R.tire_width/2
                    c2y = 0
                    c3x = inputs.R.track_width/2-inputs.R.tire_width/2
                    c3y = 0
                    c4x = inputs.R.track_width/2-inputs.R.tire_width/2
                    c4y = inputs.R.tire_radius+.5*inputs.R.tire_diameter
                    self.axR_view.plot([c1x,c4x],[c1y,c4y],color=vehicleColor) # Pos y tire top line
                    self.axR_view.plot([c2x,c3x],[c2y,c3y],color=vehicleColor) # Pos y tire bottom line
                    self.axR_view.plot([c1x,c2x],[c1y,c2y],color=vehicleColor) # Pos y tire pos y line
                    self.axR_view.plot([c3x,c4x],[c3y,c4y],color=vehicleColor) # Pos y tire neg y line

                    c1x = -inputs.R.track_width/2+inputs.R.tire_width/2
                    c1y = inputs.R.tire_radius+.5*inputs.R.tire_diameter
                    c2x = -inputs.R.track_width/2+inputs.R.tire_width/2
                    c2y = 0
                    c3x = -inputs.R.track_width/2-inputs.R.tire_width/2
                    c3y = 0
                    c4x = -inputs.R.track_width/2-inputs.R.tire_width/2
                    c4y = inputs.R.tire_radius+.5*inputs.R.tire_diameter
                    self.axR_view.plot([c1x,c4x],[c1y,c4y],color=vehicleColor) # Neg y tire top line
                    self.axR_view.plot([c2x,c3x],[c2y,c3y],color=vehicleColor) # Neg y tire bottom line
                    self.axR_view.plot([c1x,c2x],[c1y,c2y],color=vehicleColor) # Neg y tire pos y line
                    self.axR_view.plot([c3x,c4x],[c3y,c4y],color=vehicleColor) # Neg y tire neg y line

                    x1 = inputs.R.track_width/2-inputs.R.tire_width/2
                    x2 = -inputs.R.track_width/2+inputs.R.tire_width/2
                    y1 = inputs.R.tire_radius+inputs.R.axle_tube/2
                    y2 = inputs.R.tire_radius+inputs.R.axle_tube/2
                    self.axR_view.plot([x1,x2],[y1,y2],color=vehicleColor) # Upper axle tube
                    x1 = inputs.R.track_width/2-inputs.R.tire_width/2
                    x2 = -inputs.R.track_width/2+inputs.R.tire_width/2
                    y1 = inputs.R.tire_radius-inputs.R.axle_tube/2
                    y2 = inputs.R.tire_radius-inputs.R.axle_tube/2
                    self.axR_view.plot([x1,x2],[y1,y2],color=vehicleColor) # Lower axle tube

                    if inputs.R.panhard:
                        x1 = -outputs.R.PF[y]
                        x2 = -outputs.R.PA[S.sample_points,y]
                        y1 = outputs.R.PF[z]
                        y2 = outputs.R.PA[S.sample_points,z]
                        self.axR_view.plot([x1,x2],[y1,y2],linewidth=linkLine,color=panhardColor) # Panhard ride
                        x1 = -outputs.R.PF[y]
                        x2 = -outputs.R.PA[2*S.sample_points,y]
                        y1 = outputs.R.PF[z]
                        y2 = outputs.R.PA[2*S.sample_points,z]
                        self.axR_view.plot([x1,x2],[y1,y2],linewidth=travelLine,color=panhardColor) # Panhard bump
                        x1 = -outputs.R.PF[y]
                        x2 = -outputs.R.PA[0,y]
                        y1 = outputs.R.PF[z]
                        y2 = outputs.R.PA[0,z]
                        self.axR_view.plot([x1,x2],[y1,y2],linewidth=travelLine,color=panhardColor) # Panhard droop
                        self.axR_view.plot(-outputs.R.PA[:,y],outputs.R.PA[:,z],linestyle="dotted",linewidth=dottedLine,color=panhardColor) # Panhard arc

                    self.axR_view.axis('equal')
                    self.axR_view.set_xlim([-1.1*inputs.R.track_width/2-inputs.R.tire_width,1.1*inputs.R.track_width/2+inputs.R.tire_width])
                    self.axR_view.set_ylim([0,1.1*inputs.R.tire_diameter])

                    self.axR_view.set_facecolor(textEntryColor)
                    self.axR_view.xaxis.label.set_color(entryTextColor)
                    self.axR_view.yaxis.label.set_color(entryTextColor)
                    self.axR_view.spines[['top','bottom','left','right']].set_color(entryTextColor)
                    self.axR_view.tick_params(axis='x', colors=entryTextColor)
                    self.axR_view.tick_params(axis='y', colors=entryTextColor)

                    self.axR_view.set_title('View From Rear',color=entryTextColor, y=1.0, pad=-23)

                if True: # Plot Vehicle
                    if True: # Top View
                        x1 = inputs.V.wheelbase-inputs.F.axle_tube/2
                        x2 = inputs.V.wheelbase-inputs.F.axle_tube/2
                        y1 = inputs.F.track_width/2-inputs.F.tire_width/2
                        y2 = -inputs.F.track_width/2+inputs.F.tire_width/2
                        self.axV[0,0].plot([x1,x2],[y1,y2],color=vehicleColor) # Front axletube rear line
                        x1 = inputs.V.wheelbase+inputs.F.axle_tube/2
                        x2 = inputs.V.wheelbase+inputs.F.axle_tube/2
                        y1 = inputs.F.track_width/2-inputs.F.tire_width/2
                        y2 = -inputs.F.track_width/2+inputs.F.tire_width/2
                        self.axV[0,0].plot([x1,x2],[y1,y2],color=vehicleColor) # Front axletube front line
                        x1 = -inputs.F.axle_tube/2
                        x2 = -inputs.F.axle_tube/2
                        y1 = inputs.R.track_width/2-inputs.R.tire_width/2
                        y2 = -inputs.R.track_width/2+inputs.R.tire_width/2
                        self.axV[0,0].plot([x1,x2],[y1,y2],color=vehicleColor) # Rear axletube rear line
                        x1 = inputs.F.axle_tube/2
                        x2 = inputs.F.axle_tube/2
                        y1 = inputs.R.track_width/2-inputs.R.tire_width/2
                        y2 = -inputs.R.track_width/2+inputs.R.tire_width/2
                        self.axV[0,0].plot([x1,x2],[y1,y2],color=vehicleColor) # Rear axletube front line

                        c1x = inputs.V.wheelbase+inputs.F.tire_diameter/2
                        c1y = inputs.F.track_width/2-inputs.F.tire_width/2
                        c2x = inputs.V.wheelbase+inputs.F.tire_diameter/2
                        c2y = inputs.F.track_width/2+inputs.F.tire_width/2
                        c3x = inputs.V.wheelbase-inputs.F.tire_diameter/2
                        c3y = inputs.F.track_width/2+inputs.F.tire_width/2
                        c4x = inputs.V.wheelbase-inputs.F.tire_diameter/2
                        c4y = inputs.F.track_width/2-inputs.F.tire_width/2
                        self.axV[0,0].plot([c2x,c3x],[c2y,c3y],color=vehicleColor) # Front pos y tire pos y line
                        self.axV[0,0].plot([c1x,c4x],[c1y,c4y],color=vehicleColor) # Front pos y tire neg y line
                        self.axV[0,0].plot([c1x,c2x],[c1y,c2y],color=vehicleColor) # Front pos y tire front line 
                        self.axV[0,0].plot([c3x,c4x],[c3y,c4y],color=vehicleColor) # Front pos y tire rear line

                        c1x = inputs.V.wheelbase+inputs.F.tire_diameter/2
                        c1y = -inputs.F.track_width/2-inputs.F.tire_width/2
                        c2x = inputs.V.wheelbase+inputs.F.tire_diameter/2
                        c2y = -inputs.F.track_width/2+inputs.F.tire_width/2
                        c3x = inputs.V.wheelbase-inputs.F.tire_diameter/2
                        c3y = -inputs.F.track_width/2+inputs.F.tire_width/2
                        c4x = inputs.V.wheelbase-inputs.F.tire_diameter/2
                        c4y = -inputs.F.track_width/2-inputs.F.tire_width/2
                        self.axV[0,0].plot([c2x,c3x],[c2y,c3y],color=vehicleColor) # Front neg y tire pos y line
                        self.axV[0,0].plot([c1x,c4x],[c1y,c4y],color=vehicleColor) # Front neg y tire neg y line
                        self.axV[0,0].plot([c1x,c2x],[c1y,c2y],color=vehicleColor) # Front neg y tire front line
                        self.axV[0,0].plot([c3x,c4x],[c3y,c4y],color=vehicleColor) # Front neg y tire rear line

                        c1x = inputs.R.tire_diameter/2
                        c1y = inputs.R.track_width/2-inputs.R.tire_width/2
                        c2x = inputs.R.tire_diameter/2
                        c2y = inputs.R.track_width/2+inputs.R.tire_width/2
                        c3x = -inputs.R.tire_diameter/2
                        c3y = inputs.R.track_width/2+inputs.R.tire_width/2
                        c4x = -inputs.R.tire_diameter/2
                        c4y = inputs.R.track_width/2-inputs.R.tire_width/2
                        self.axV[0,0].plot([c2x,c3x],[c2y,c3y],color=vehicleColor) # Rear pos y tire pos y line
                        self.axV[0,0].plot([c1x,c4x],[c1y,c4y],color=vehicleColor) # Rear pos y tire neg y line
                        self.axV[0,0].plot([c1x,c2x],[c1y,c2y],color=vehicleColor) # Rear pos y tire front line
                        self.axV[0,0].plot([c3x,c4x],[c3y,c4y],color=vehicleColor) # Rear pos y tire rear line

                        c1x = inputs.R.tire_diameter/2
                        c1y = -inputs.R.track_width/2-inputs.R.tire_width/2
                        c2x = inputs.R.tire_diameter/2
                        c2y = -inputs.R.track_width/2+inputs.R.tire_width/2
                        c3x = -inputs.R.tire_diameter/2
                        c3y = -inputs.R.track_width/2+inputs.R.tire_width/2
                        c4x = -inputs.R.tire_diameter/2
                        c4y = -inputs.R.track_width/2-inputs.R.tire_width/2
                        self.axV[0,0].plot([c2x,c3x],[c2y,c3y],color=vehicleColor) # Rear neg y tire pos y line
                        self.axV[0,0].plot([c1x,c4x],[c1y,c4y],color=vehicleColor) # Rear neg y tire neg y line
                        self.axV[0,0].plot([c1x,c2x],[c1y,c2y],color=vehicleColor) # Rear neg y tire front line
                        self.axV[0,0].plot([c3x,c4x],[c3y,c4y],color=vehicleColor) # Rear neg y tire rear line

                        x1 = outputs.F.LA[S.sample_points][x]
                        x2 = outputs.F.LF[x]
                        y1 = outputs.F.LA[S.sample_points][y]
                        y2 = outputs.F.LF[y]
                        self.axV[0,0].plot([x1,x2],[y1,y2],color=lowerColor,linewidth=linkLine) # Front poy y lower link
                        x1 = outputs.F.LA[S.sample_points][x]
                        x2 = outputs.F.LF[x]
                        y1 = -outputs.F.LA[S.sample_points][y]
                        y2 = -outputs.F.LF[y]
                        self.axV[0,0].plot([x1,x2],[y1,y2],color=lowerColor,linewidth=linkLine) # Front neg y lower link
                        x1 = outputs.F.UA[S.sample_points][x]
                        x2 = outputs.F.UF[x]
                        y1 = outputs.F.UA[S.sample_points][y]
                        y2 = outputs.F.UF[y]
                        self.axV[0,0].plot([x1,x2],[y1,y2],color=upperColor,linewidth=linkLine) # Front pos y upper link
                        if inputs.F.U_count == 2:
                            x1 = outputs.F.UA[S.sample_points][x]
                            x2 = outputs.F.UF[x]
                            y1 = -outputs.F.UA[S.sample_points][y]
                            y2 = -outputs.F.UF[y]
                            self.axV[0,0].plot([x1,x2],[y1,y2],color=upperColor,linewidth=linkLine) # Rear neg y upper link
                        x1 = outputs.R.LA[S.sample_points][x]
                        x2 = outputs.R.LF[x]
                        y1 = outputs.R.LA[S.sample_points][y]
                        y2 = outputs.R.LF[y]
                        self.axV[0,0].plot([x1,x2],[y1,y2],color=lowerColor,linewidth=linkLine) # Rear poy y lower link
                        x1 = outputs.R.LA[S.sample_points][x]
                        x2 = outputs.R.LF[x]
                        y1 = -outputs.R.LA[S.sample_points][y]
                        y2 = -outputs.R.LF[y]
                        self.axV[0,0].plot([x1,x2],[y1,y2],color=lowerColor,linewidth=linkLine) # Rear neg y lower link
                        x1 = outputs.R.UA[S.sample_points][x]
                        x2 = outputs.R.UF[x]
                        y1 = outputs.R.UA[S.sample_points][y]
                        y2 = outputs.R.UF[y]
                        self.axV[0,0].plot([x1,x2],[y1,y2],color=upperColor,linewidth=linkLine) # Rear pos y upper link
                        if inputs.R.U_count == 2:
                            x1 = outputs.R.UA[S.sample_points][x]
                            x2 = outputs.R.UF[x]
                            y1 = -outputs.R.UA[S.sample_points][y]
                            y2 = -outputs.R.UF[y]
                            self.axV[0,0].plot([x1,x2],[y1,y2],color=upperColor,linewidth=linkLine) # Rear neg y upper link
                        
                        if inputs.F.panhard:
                            x1 = outputs.F.PA[S.sample_points][x]
                            x2 = outputs.F.PF[x]
                            y1 = outputs.F.PA[S.sample_points][y]
                            y2 = outputs.F.PF[y]
                            self.axV[0,0].plot([x1,x2],[y1,y2],color=panhardColor,linewidth=linkLine) # Front panhard
                        if inputs.R.panhard:
                            x1 = outputs.R.PA[S.sample_points][x]
                            x2 = outputs.R.PF[x]
                            y1 = outputs.R.PA[S.sample_points][y]
                            y2 = outputs.R.PF[y]
                            self.axV[0,0].plot([x1,x2],[y1,y2],color=panhardColor,linewidth=linkLine) # Rear panhard

                        if PS.converge == "Show":
                            x1 = outputs.F.LF[x]
                            x2 = outputs.F.L_converge_point[x]
                            y1 = outputs.F.LF[y]
                            y2 = 0
                            self.axV[0,0].plot([x1,x2],[y1,y2],color=lowerColor,linestyle="dotted",linewidth=dottedLine) # Front pos y lower link extended
                            x1 = outputs.F.LF[x]
                            x2 = outputs.F.L_converge_point[x]
                            y1 = -outputs.F.LF[y]
                            y2 = 0
                            self.axV[0,0].plot([x1,x2],[y1,y2],color=lowerColor,linestyle="dotted",linewidth=dottedLine) # Front neg y lower link extended
                            x1 = outputs.R.LF[x]
                            x2 = outputs.R.L_converge_point[x]
                            y1 = outputs.R.LF[y]
                            y2 = 0
                            self.axV[0,0].plot([x1,x2],[y1,y2],color=lowerColor,linestyle="dotted",linewidth=dottedLine) # Rear pos y lower link extended
                            x1 = outputs.R.LF[x]
                            x2 = outputs.R.L_converge_point[x]
                            y1 = -outputs.R.LF[y]
                            y2 = 0
                            self.axV[0,0].plot([x1,x2],[y1,y2],color=lowerColor,linestyle="dotted",linewidth=dottedLine) # Rear neg y lower link extended
                            if inputs.F.U_count == 2 and not inputs.F.panhard:
                                x1 = outputs.F.UF[x]
                                x2 = outputs.F.U_converge_point[x]
                                y1 = outputs.F.UF[y]
                                y2 = 0
                                self.axV[0,0].plot([x1,x2],[y1,y2],color=upperColor,linestyle="dotted",linewidth=dottedLine) # Front pos y upper link extended
                                x1 = outputs.F.UF[x]
                                x2 = outputs.F.U_converge_point[x]
                                y1 = -outputs.F.UF[y]
                                y2 = 0
                                self.axV[0,0].plot([x1,x2],[y1,y2],color=upperColor,linestyle="dotted",linewidth=dottedLine) # Front neg y upper link extended
                            if inputs.R.U_count == 2 and not inputs.R.panhard:
                                x1 = outputs.R.UF[x]
                                x2 = outputs.R.U_converge_point[x]
                                y1 = outputs.R.UF[y]
                                y2 = 0
                                self.axV[0,0].plot([x1,x2],[y1,y2],color=upperColor,linestyle="dotted",linewidth=dottedLine) # Front pos y upper link extended
                                x1 = outputs.R.UF[x]
                                x2 = outputs.R.U_converge_point[x]
                                y1 = -outputs.R.UF[y]
                                y2 = 0
                                self.axV[0,0].plot([x1,x2],[y1,y2],color=upperColor,linestyle="dotted",linewidth=dottedLine) # Front neg y upper link extended

                        self.axV[0,0].axis('equal')
                        self.axV[0,0].set_xlim([-1.1*inputs.R.tire_diameter/2,1.1*inputs.F.tire_diameter/2+inputs.V.wheelbase])
                        self.axV[0,0].set_ylim([-1.1*(max(inputs.F.track_width,inputs.R.track_width)/2+max(inputs.F.tire_width,inputs.R.tire_width)/2),1.1*(max(inputs.F.track_width,inputs.R.track_width)/2+max(inputs.F.tire_width,inputs.R.tire_width)/2)])

                    if True: # Ride Height side view
                        x1 = outputs.F.UF[x]
                        x2 = outputs.F.UA[S.sample_points][x]
                        y1 = outputs.F.UF[z]
                        y2 = outputs.F.UA[S.sample_points][z]
                        self.axV[1,0].plot([x1,x2],[y1,y2],color=upperColor,linewidth=linkLine) # Front upper
                        x1 = outputs.F.LF[x]
                        x2 = outputs.F.LA[S.sample_points][x]
                        y1 = outputs.F.LF[z]
                        y2 = outputs.F.LA[S.sample_points][z]
                        self.axV[1,0].plot([x1,x2],[y1,y2],color=lowerColor,linewidth=linkLine) # Front lower
                        x1 = outputs.R.UF[x]
                        x2 = outputs.R.UA[S.sample_points][x]
                        y1 = outputs.R.UF[z]
                        y2 = outputs.R.UA[S.sample_points][z]
                        self.axV[1,0].plot([x1,x2],[y1,y2],color=upperColor,linewidth=linkLine) # Rear upper
                        x1 = outputs.R.LF[x]
                        x2 = outputs.R.LA[S.sample_points][x]
                        y1 = outputs.R.LF[z]
                        y2 = outputs.R.LA[S.sample_points][z]
                        self.axV[1,0].plot([x1,x2],[y1,y2],color=lowerColor,linewidth=linkLine) # Rear lower

                        if PS.converge == "Show":
                            x1 = outputs.F.UF[x]
                            x2 = outputs.F.IC[S.sample_points][x]
                            y1 = outputs.F.UF[z]
                            y2 = outputs.F.IC[S.sample_points][z]
                            self.axV[1,0].plot([x1,x2],[y1,y2],color=upperColor,linestyle="dotted",linewidth=dottedLine) # Front upper converge
                            x1 = outputs.F.LF[x]
                            x2 = outputs.F.IC[S.sample_points][x]
                            y1 = outputs.F.LF[z]
                            y2 = outputs.F.IC[S.sample_points][z]
                            self.axV[1,0].plot([x1,x2],[y1,y2],color=lowerColor,linestyle="dotted",linewidth=dottedLine) # Front lower converge
                            x1 = outputs.R.UF[x]
                            x2 = outputs.R.IC[S.sample_points][x]
                            y1 = outputs.R.UF[z]
                            y2 = outputs.R.IC[S.sample_points][z]
                            self.axV[1,0].plot([x1,x2],[y1,y2],color=upperColor,linestyle="dotted",linewidth=dottedLine) # Rear upper converge
                            x1 = outputs.R.LF[x]
                            x2 = outputs.R.IC[S.sample_points][x]
                            y1 = outputs.R.LF[z]
                            y2 = outputs.R.IC[S.sample_points][z]
                            self.axV[1,0].plot([x1,x2],[y1,y2],color=lowerColor,linestyle="dotted",linewidth=dottedLine) # Rear lower converge

                        circle_angle = np.zeros(361)
                        for i in range(0,360):
                            circle_angle[i] = 2*pi*i/360
                        circle_x = inputs.F.axle_tube/2*np.cos(circle_angle)+inputs.V.wheelbase
                        circle_y = inputs.F.axle_tube/2*np.sin(circle_angle)+inputs.F.tire_radius
                        self.axV[1,0].plot(circle_x,circle_y,color=vehicleColor) # Front axle tube
                        circle_x = inputs.F.tire_diameter/2*np.cos(circle_angle)+inputs.V.wheelbase
                        circle_y = inputs.F.tire_diameter/2*np.sin(circle_angle)+inputs.F.tire_radius
                        circle_y[circle_y<0] = 0
                        self.axV[1,0].plot(circle_x,circle_y,color=vehicleColor) # Front tire
                        circle_x = inputs.R.axle_tube/2*np.cos(circle_angle)
                        circle_y = inputs.R.axle_tube/2*np.sin(circle_angle)+inputs.R.tire_radius
                        self.axV[1,0].plot(circle_x,circle_y,color=vehicleColor) # Rear axle tube
                        circle_x = inputs.R.tire_diameter/2*np.cos(circle_angle)
                        circle_y = inputs.R.tire_diameter/2*np.sin(circle_angle)+inputs.R.tire_radius
                        circle_y[circle_y<0] = 0
                        self.axV[1,0].plot(circle_x,circle_y,color=vehicleColor) # Rear tire

                        if PS.axle_roll == "Show":
                            x1 = outputs.F.U_converge_point[x]
                            x2 = outputs.F.L_converge_point[x]
                            y1 = outputs.F.U_converge_point[z]
                            y2 = outputs.F.L_converge_point[z]
                            self.axV[1,0].plot([x1,x2],[y1,y2],color=rollColor) # Front axle roll axis
                            x1 = outputs.R.U_converge_point[x]
                            x2 = outputs.R.L_converge_point[x]
                            y1 = outputs.R.U_converge_point[z]
                            y2 = outputs.R.L_converge_point[z]
                            self.axV[1,0].plot([x1,x2],[y1,y2],color=rollColor) # Rear axle roll axis

                        if PS.body_roll == "Show":
                            x1 = 0
                            x2 = inputs.V.wheelbase
                            y1 = outputs.R.Roll_Center[S.sample_points]
                            y2 = outputs.F.Roll_Center[S.sample_points]
                            self.axV[1,0].plot([x1,x2],[y1,y2],color=bodyRollColor) # Body roll axis

                        if PS.anti_100 == "Show":
                            x1 = inputs.V.wheelbase
                            x2 = inputs.V.wheelbase*(1-inputs.V.brake_bias)
                            y1 = 0
                            y2 = outputs.F.Anti_CG
                            self.axV[1,0].plot([x1,x2],[y1,y2],color=anti100Color) # Front 100% anti line
                            x1 = 0
                            x2 = inputs.V.wheelbase*(1-inputs.V.drive_bias)
                            y1 = 0
                            y2 = outputs.R.Anti_CG
                            self.axV[1,0].plot([x1,x2],[y1,y2],color=anti100Color) # Rear 100% anti line

                        if PS.ride_anti == "Show":
                            x1 = inputs.V.wheelbase
                            x2 = outputs.F.IC[S.sample_points,x]
                            y1 = 0
                            y2 = outputs.F.IC[S.sample_points,z]
                            self.axV[1,0].plot([x1,x2],[y1,y2],color=rideAntiColor) # Front ride anti line
                            x1 = 0
                            x2 = outputs.R.IC[S.sample_points,x]
                            y1 = 0
                            y2 = outputs.R.IC[S.sample_points,z]
                            self.axV[1,0].plot([x1,x2],[y1,y2],color=rideAntiColor) # Rear ride anti line

                        if PS.roll_center == "Show":
                            self.axV[1,0].plot(inputs.V.wheelbase,outputs.F.Roll_Center[S.sample_points],marker='x',markersize= markerSize,color=rollColor) # Front ride roll center
                            self.axV[1,0].plot(0,outputs.R.Roll_Center[S.sample_points],marker='x',markersize= markerSize,color=rollColor) # Rear ride roll center

                        if PS.ride_IC == "Show":
                            self.axV[1,0].plot(outputs.F.IC[S.sample_points,x],outputs.F.IC[S.sample_points,z],marker='x',color=ICcolor,markersize= markerSize) # Front ride IC
                            self.axV[1,0].plot(outputs.R.IC[S.sample_points,x],outputs.R.IC[S.sample_points,z],marker='x',color=ICcolor,markersize= markerSize) # Rear ride IC

                        self.axV[1,0].axis('equal')
                        self.axV[1,0].set_xlim([-1.1*inputs.R.tire_diameter/2,1.1*inputs.F.tire_diameter/2+inputs.V.wheelbase])
                        self.axV[1,0].set_ylim([0,1.1*max(inputs.F.tire_diameter,inputs.R.tire_diameter)])

                    if True: # Side View Travel
                        if True: # Ghost car
                            carX = [
                                inputs.V.wheelbase+inputs.F.tire_diameter/2,
                                inputs.V.wheelbase+inputs.F.tire_diameter/2+inputs.F.tire_diameter*.1,
                                inputs.V.wheelbase+inputs.F.tire_diameter/2+inputs.F.tire_diameter*.1,
                                inputs.V.wheelbase-inputs.F.tire_diameter/2,
                                .9*inputs.V.wheelbase-inputs.F.tire_diameter/2,
                                -inputs.R.tire_diameter/2-inputs.R.tire_diameter*.1,
                                -inputs.R.tire_diameter/2-inputs.R.tire_diameter*.1,
                                -inputs.R.tire_diameter/2,
                                -inputs.R.tire_diameter/4,
                                inputs.R.tire_diameter/4,
                                inputs.R.tire_diameter/2,
                                inputs.V.wheelbase-inputs.F.tire_diameter/2,
                                inputs.V.wheelbase-inputs.F.tire_diameter/4,
                                inputs.V.wheelbase+inputs.F.tire_diameter/4,
                                inputs.V.wheelbase+inputs.F.tire_diameter/2
                            ]
                        
                            carY = [
                                inputs.F.tire_radius+inputs.F.tire_diameter/4,
                                inputs.F.tire_radius+inputs.F.tire_diameter/4,
                                inputs.F.tire_radius+inputs.F.tire_diameter/1.5,
                                inputs.F.tire_radius+inputs.F.tire_diameter/1.4,
                                inputs.F.tire_radius+inputs.F.tire_diameter/1.4+inputs.F.tire_diameter/2,
                                inputs.F.tire_radius+inputs.F.tire_diameter/1.4+inputs.F.tire_diameter/2,
                                inputs.R.tire_radius+inputs.R.tire_diameter/4,
                                inputs.R.tire_radius+inputs.R.tire_diameter/4,
                                inputs.R.tire_radius+1.1*inputs.R.tire_diameter/2,
                                inputs.R.tire_radius+1.1*inputs.R.tire_diameter/2,
                                inputs.F.tire_radius+inputs.F.tire_diameter/4,
                                inputs.F.tire_radius+inputs.F.tire_diameter/4,
                                inputs.F.tire_radius+1.1*inputs.F.tire_diameter/2,
                                inputs.F.tire_radius+1.1*inputs.F.tire_diameter/2,
                                inputs.F.tire_radius+inputs.F.tire_diameter/4
                            ]
                            self.axV[1,1].plot(carX,carY,color=bgColor) # Car

                        x1 = outputs.F.UF[x]
                        x2 = outputs.F.UA[S.sample_points][x]
                        y1 = outputs.F.UF[z]
                        y2 = outputs.F.UA[S.sample_points][z]
                        self.axV[1,1].plot([x1,x2],[y1,y2],color=upperColor,linewidth=linkLine) # Front upper
                        x1 = outputs.F.LF[x]
                        x2 = outputs.F.LA[S.sample_points][x]
                        y1 = outputs.F.LF[z]
                        y2 = outputs.F.LA[S.sample_points][z]
                        self.axV[1,1].plot([x1,x2],[y1,y2],color=lowerColor,linewidth=linkLine) # Front lower
                        x1 = outputs.R.UF[x]
                        x2 = outputs.R.UA[S.sample_points][x]
                        y1 = outputs.R.UF[z]
                        y2 = outputs.R.UA[S.sample_points][z]
                        self.axV[1,1].plot([x1,x2],[y1,y2],color=upperColor,linewidth=linkLine) # Rear upper
                        x1 = outputs.R.LF[x]
                        x2 = outputs.R.LA[S.sample_points][x]
                        y1 = outputs.R.LF[z]
                        y2 = outputs.R.LA[S.sample_points][z]
                        self.axV[1,1].plot([x1,x2],[y1,y2],color=lowerColor,linewidth=linkLine) # Rear lower

                        x1 = outputs.F.UF[x]
                        x2 = outputs.F.UA[S.sample_points*2][x]
                        y1 = outputs.F.UF[z]
                        y2 = outputs.F.UA[S.sample_points*2][z]
                        self.axV[1,1].plot([x1,x2],[y1,y2],color=upperColor,linewidth=travelLine) # Front upper bump
                        x1 = outputs.F.UF[x]
                        x2 = outputs.F.UA[0][x]
                        y1 = outputs.F.UF[z]
                        y2 = outputs.F.UA[0][z]
                        self.axV[1,1].plot([x1,x2],[y1,y2],color=upperColor,linewidth=travelLine) # Front upper droop
                        self.axV[1,1].plot(outputs.F.UA[:,x],outputs.F.UA[:,z],color=upperColor,linestyle="dotted",linewidth=dottedLine) # Front upper arc
                        x1 = outputs.F.LF[x]
                        x2 = outputs.F.LA[S.sample_points*2][x]
                        y1 = outputs.F.LF[z]
                        y2 = outputs.F.LA[S.sample_points*2][z]
                        self.axV[1,1].plot([x1,x2],[y1,y2],color=lowerColor,linewidth=travelLine) # Front lower bump
                        x1 = outputs.F.LF[x]
                        x2 = outputs.F.LA[0][x]
                        y1 = outputs.F.LF[z]
                        y2 = outputs.F.LA[0][z]
                        self.axV[1,1].plot([x1,x2],[y1,y2],color=lowerColor,linewidth=travelLine) # Front lower droop
                        self.axV[1,1].plot(outputs.F.LA[:,x],outputs.F.LA[:,z],color=lowerColor,linestyle="dotted",linewidth=dottedLine) # Front lower arc

                        x1 = outputs.R.UF[x]
                        x2 = outputs.R.UA[S.sample_points*2][x]
                        y1 = outputs.R.UF[z]
                        y2 = outputs.R.UA[S.sample_points*2][z]
                        self.axV[1,1].plot([x1,x2],[y1,y2],color=upperColor,linewidth=travelLine) # Rear upper bump
                        x1 = outputs.R.UF[x]
                        x2 = outputs.R.UA[0][x]
                        y1 = outputs.R.UF[z]
                        y2 = outputs.R.UA[0][z]
                        self.axV[1,1].plot([x1,x2],[y1,y2],color=upperColor,linewidth=travelLine) # Rear upper droop
                        self.axV[1,1].plot(outputs.R.UA[:,x],outputs.R.UA[:,z],color=upperColor,linestyle="dotted",linewidth=dottedLine) # Rear upper arc
                        x1 = outputs.R.LF[x]
                        x2 = outputs.R.LA[S.sample_points*2][x]
                        y1 = outputs.R.LF[z]
                        y2 = outputs.R.LA[S.sample_points*2][z]
                        self.axV[1,1].plot([x1,x2],[y1,y2],color=lowerColor,linewidth=travelLine) # Rear lower bump
                        x1 = outputs.R.LF[x]
                        x2 = outputs.R.LA[0][x]
                        y1 = outputs.R.LF[z]
                        y2 = outputs.R.LA[0][z]
                        self.axV[1,1].plot([x1,x2],[y1,y2],color=lowerColor,linewidth=travelLine) # Rear lower droop
                        self.axV[1,1].plot(outputs.R.LA[:,x],outputs.R.LA[:,z],color=lowerColor,linestyle="dotted",linewidth=dottedLine) # Rear lower arc

                        circle_angle = np.zeros(361)
                        for i in range(0,360):
                            circle_angle[i] = 2*pi*i/360
                        circle_x = inputs.F.axle_tube/2*np.cos(circle_angle)+inputs.V.wheelbase
                        circle_y = inputs.F.axle_tube/2*np.sin(circle_angle)+inputs.F.tire_radius
                        self.axV[1,1].plot(circle_x,circle_y,color=vehicleColor) # Front axle tube
                        circle_x = inputs.F.tire_diameter/2*np.cos(circle_angle)+inputs.V.wheelbase
                        circle_y = inputs.F.tire_diameter/2*np.sin(circle_angle)+inputs.F.tire_radius
                        circle_y[circle_y<0] = 0
                        self.axV[1,1].plot(circle_x,circle_y,color=vehicleColor) # Front tire
                        circle_x = inputs.R.axle_tube/2*np.cos(circle_angle)
                        circle_y = inputs.R.axle_tube/2*np.sin(circle_angle)+inputs.R.tire_radius
                        self.axV[1,1].plot(circle_x,circle_y,color=vehicleColor) # Rear axle tube
                        circle_x = inputs.R.tire_diameter/2*np.cos(circle_angle)
                        circle_y = inputs.R.tire_diameter/2*np.sin(circle_angle)+inputs.R.tire_radius
                        circle_y[circle_y<0] = 0
                        self.axV[1,1].plot(circle_x,circle_y,color=vehicleColor) # Rear tire

                        self.axV[1,1].plot(outputs.F.Hub[:,x],outputs.F.Hub[:,z],color=vehicleColor,linestyle="dotted",linewidth=dottedLine) # Front wheel movement
                        self.axV[1,1].plot(outputs.R.Hub[:,x],outputs.R.Hub[:,z],color=vehicleColor,linestyle="dotted",linewidth=dottedLine) # Rear wheel movement

                        if PS.IC_move == "Show":
                            self.axV[1,1].plot(outputs.F.IC[:,x],outputs.F.IC[:,z],color=ICcolor,linewidth=.5) # Front IC Movement
                            self.axV[1,1].plot(outputs.R.IC[:,x],outputs.R.IC[:,z],color=ICcolor,linewidth=.5) # Rear IC Movement

                        if PS.ride_IC == "Show":
                            self.axV[1,1].plot(outputs.F.IC[S.sample_points,x],outputs.F.IC[S.sample_points,z],marker='x',color=ICcolor,markersize= markerSize) # Front ride IC
                            self.axV[1,1].plot(outputs.R.IC[S.sample_points,x],outputs.R.IC[S.sample_points,z],marker='x',color=ICcolor,markersize= markerSize) # Rear ride IC

                        self.axV[1,1].axis('equal')
                        self.axV[1,1].set_xlim([-1.35*inputs.R.tire_diameter/2,1.35*inputs.F.tire_diameter/2+inputs.V.wheelbase])
                        self.axV[1,1].set_ylim([0,1.1*inputs.F.tire_radius+inputs.F.tire_diameter/1.4+inputs.F.tire_diameter/2])

                    if True: # Both Roll Axis
                        self.axV[0,1].plot(outputs.F.Roll_Center,100*(outputs.F.Travel-inputs.F.droop)/(inputs.F.bump-inputs.F.droop),color=plotMainColor) # Front roll center
                        self.axV[0,1].plot(outputs.R.Roll_Center,100*(outputs.R.Travel-inputs.R.droop)/(inputs.R.bump-inputs.R.droop),color=plotSecondaryColor) # Rear roll center
                        self.axV[0,1].plot(outputs.F.Roll_Center[S.sample_points],-100*inputs.F.droop/(inputs.F.bump-inputs.F.droop),marker = '_',markersize=20, color=plotMainColor) # Front ride %
                        self.axV[0,1].plot(outputs.R.Roll_Center[S.sample_points],-100*inputs.R.droop/(inputs.R.bump-inputs.R.droop),marker = '_',markersize=20, color=plotSecondaryColor) # Rear ride %
                        if outputs.F.Roll_Center[S.sample_points] > outputs.R.Roll_Center[S.sample_points]:
                            temp1 = 'left'
                            temp2 = 'right'
                        else:
                            temp1 = 'right'
                            temp2 = 'left'
                        self.axV[0,1].text(outputs.F.Roll_Center[S.sample_points],-100*inputs.F.droop/(inputs.F.bump-inputs.F.droop),"Front Ride", color=plotMainColor,horizontalalignment=temp1) # Front ride %
                        self.axV[0,1].text(outputs.R.Roll_Center[S.sample_points],-100*inputs.R.droop/(inputs.R.bump-inputs.R.droop),"Rear Ride", color=plotSecondaryColor,horizontalalignment=temp2) # Rear ride %

                        self.axV[0,1].set_xlim([min(min(outputs.F.Roll_Center),min(outputs.R.Roll_Center))-1,max(max(outputs.F.Roll_Center),max(outputs.R.Roll_Center))+1])
                        self.axV[0,1].set_ylim([0,100])

                        self.axV[0,1].set_xlabel('Roll Center Height [{}]'.format(S.position_units))
                        self.axV[0,1].set_ylabel('% Travel')
                        self.axV[0,1].grid(linewidth = 0.5,color=bgColor)

                    for i_x in range(2):
                        for i_y in range(2):
                            self.axV[i_x,i_y].set_facecolor(textEntryColor)
                            self.axV[i_x,i_y].xaxis.label.set_color(entryTextColor)
                            self.axV[i_x,i_y].yaxis.label.set_color(entryTextColor)
                            self.axV[i_x,i_y].spines[['top','bottom','left','right']].set_color(entryTextColor)
                            self.axV[i_x,i_y].tick_params(axis='x', colors=entryTextColor) 
                            self.axV[i_x,i_y].tick_params(axis='y', colors=entryTextColor) 
                
                if True: # Draw Plots
                    self.F_plots.draw()
                    self.R_plots.draw()
                    self.F_view.draw()
                    self.R_view.draw()
                    self.V_plots.draw()

                if True: # Update Text Outputs
                    label_FU_Force.config(text="{:.0f} {}".format(outputs.F.U_Max_Force,S.force_units))
                    label_FL_Force.config(text="{:.0f} {}".format(outputs.F.L_Max_Force,S.force_units))
                    if inputs.F.panhard:
                        label_FP_Force.config(text="{:.0f} {}".format(outputs.F.P_Max_Force,S.force_units))
                    else:
                        label_FP_Force.config(text="N/A")
                    if inputs.F.U_count == 1:
                        label_FU_Converge.config(text="N/A")
                    else:
                        label_FU_Converge.config(text="{:.0f}\u00b0".format(outputs.F.Upper_Convergence))
                    label_FL_Converge.config(text="{:.0f}\u00b0".format(outputs.F.Lower_Convergence))
                    label_FU_3d_length.config(text="{:.1f} {}".format(outputs.F.U_Length_3D,S.position_units))
                    label_FL_3d_length.config(text="{:.1f} {}".format(outputs.F.L_Length_3D,S.position_units))
                    if inputs.F.panhard:
                        label_FP_3d_length.config(text="{:.1f} {}".format(outputs.F.P_Length_3D,S.position_units))
                    else:
                        label_FP_3d_length.config(text="N/A")
                    label_FU_2d_length.config(text="{:.1f} {}".format(outputs.F.U_Length_2D,S.position_units))
                    label_FL_2d_length.config(text="{:.1f} {}".format(outputs.F.L_Length_2D,S.position_units))
                    if inputs.F.panhard:
                        label_FP_2d_length.config(text="{:.1f} {}".format(outputs.F.P_Length_2D,S.position_units))
                    else:
                        label_FP_2d_length.config(text="N/A")
                    label_FU_3d_percent.config(text="{:.1f} %".format(100*outputs.F.U_Length_3D/outputs.F.L_Length_3D))
                    label_FL_3d_percent.config(text="{:.1f} %".format(100*outputs.F.L_Length_3D/outputs.F.U_Length_3D))
                    label_FU_2d_percent.config(text="{:.1f} %".format(100*outputs.F.U_Length_2D/outputs.F.L_Length_2D))
                    label_FL_2d_percent.config(text="{:.1f} %".format(100*outputs.F.L_Length_2D/outputs.F.U_Length_2D))
                    if inputs.F.U_count == 1:
                        label_F_converge.config(text="N/A")
                    else:
                        label_F_converge.config(text="{:.1f}\u00b0".format(outputs.F.Total_Convergence))

                    label_RU_Force.config(text="{:.0f} {}".format(outputs.R.U_Max_Force,S.force_units))
                    label_RL_Force.config(text="{:.0f} {}".format(outputs.R.L_Max_Force,S.force_units))
                    if inputs.R.panhard:
                        label_RP_Force.config(text="{:.0f} {}".format(outputs.R.P_Max_Force,S.force_units))
                    else:
                        label_RP_Force.config(text="N/A")
                    if inputs.R.U_count == 1:
                        label_RU_Converge.config(text="N/A")
                    else:
                        label_RU_Converge.config(text="{:.0f}\u00b0".format(outputs.R.Upper_Convergence))
                    label_RL_Converge.config(text="{:.0f}\u00b0".format(outputs.R.Lower_Convergence))
                    label_RU_3d_length.config(text="{:.1f} {}".format(outputs.R.U_Length_3D,S.position_units))
                    label_RL_3d_length.config(text="{:.1f} {}".format(outputs.R.L_Length_3D,S.position_units))
                    if inputs.R.panhard:
                        label_RP_3d_length.config(text="{:.1f} {}".format(outputs.R.P_Length_3D,S.position_units))
                    else:
                        label_RP_3d_length.config(text="N/A")
                    label_RU_2d_length.config(text="{:.1f} {}".format(outputs.R.U_Length_2D,S.position_units))
                    label_RL_2d_length.config(text="{:.1f} {}".format(outputs.R.L_Length_2D,S.position_units))
                    if inputs.R.panhard:
                        label_RP_2d_length.config(text="{:.1f} {}".format(outputs.R.P_Length_2D,S.position_units))
                    else:
                        label_RP_2d_length.config(text="N/A")
                    label_RU_3d_percent.config(text="{:.1f} %".format(100*outputs.R.U_Length_3D/outputs.R.L_Length_3D))
                    label_RL_3d_percent.config(text="{:.1f} %".format(100*outputs.R.L_Length_3D/outputs.R.U_Length_3D))
                    label_RU_2d_percent.config(text="{:.1f} %".format(100*outputs.R.U_Length_2D/outputs.R.L_Length_2D))
                    label_RL_2d_percent.config(text="{:.1f} %".format(100*outputs.R.L_Length_2D/outputs.R.U_Length_2D))
                    if inputs.R.U_count == 1:
                        label_R_converge.config(text="N/A")
                    else:
                        label_R_converge.config(text="{:.1f}\u00b0".format(outputs.R.Total_Convergence))

                    label_CG_ride.config(text="{:.1f} {}".format(outputs.V.Sprung_CG_height[z],S.position_units))
                    label_CG_body.config(text="{:.1f} {}".format(outputs.V.Sprung_CG_height_Above_Roll_Axis,S.position_units))
                    label_CG_rear.config(text="{:.1f} {}".format(outputs.R.Sprung_CG_height_Above_Roll_Center,S.position_units))
                    label_CG_front.config(text="{:.1f} {}".format(outputs.F.Sprung_CG_height_Above_Roll_Center,S.position_units))
                    if outputs.V.Roll_Axis > 0:
                        temp_text = "Understeer"
                    elif outputs.V.Roll_Axis < 0:
                        temp_text = "Oversteer"
                    else:
                        temp_text = ""
                    label_body_roll.config(text="{:.1f}\u00b0 - {}".format(outputs.V.Roll_Axis,temp_text))
                    label_side_flip.config(text="{:.1f}\u00b0".format(outputs.V.Side_Roll_Angle))
                    label_climb_flip.config(text="{:.1f}\u00b0".format(outputs.V.Climb_Angle))
                    label_descent_flip.config(text="{:.1f}\u00b0".format(outputs.V.Descent_Angle))

                if True: # Panhard input grey out
                    if inputs.F.panhard:
                        FPAX.config(fg=entryTextColor)
                        FPAY.config(fg=entryTextColor)
                        FPAZ.config(fg=entryTextColor)
                        FPFX.config(fg=entryTextColor)
                        FPFY.config(fg=entryTextColor)
                        FPFZ.config(fg=entryTextColor)
                    else:
                        FPAX.config(fg=bgColor)
                        FPAY.config(fg=bgColor)
                        FPAZ.config(fg=bgColor)
                        FPFX.config(fg=bgColor)
                        FPFY.config(fg=bgColor)
                        FPFZ.config(fg=bgColor)

                    if inputs.R.panhard:
                        RPAX.config(fg=entryTextColor)
                        RPAY.config(fg=entryTextColor)
                        RPAZ.config(fg=entryTextColor)
                        RPFX.config(fg=entryTextColor)
                        RPFY.config(fg=entryTextColor)
                        RPFZ.config(fg=entryTextColor)
                    else:
                        RPAX.config(fg=bgColor)
                        RPAY.config(fg=bgColor)
                        RPAZ.config(fg=bgColor)
                        RPFX.config(fg=bgColor)
                        RPFY.config(fg=bgColor)
                        RPFZ.config(fg=bgColor)

        if True: # Detect out of input click
            self.bind("<1>", lambda event: update_outputs())
            calc_front.bind("<1>", lambda event: update_outputs())
            front_inputs_1.bind("<1>", lambda event: update_outputs())
            front_inputs_2.bind("<1>", lambda event: update_outputs())
            calc_rear.bind("<1>", lambda event: update_outputs())
            rear_inputs_1.bind("<1>", lambda event: update_outputs())
            rear_inputs_2.bind("<1>", lambda event: update_outputs())
            calc_vehicle.bind("<1>", lambda event: update_outputs())
            calc_vehicle_inputs.bind("<1>", lambda event: update_outputs())
            calc_outputs.bind("<1>", lambda event: update_outputs())
            calc_page_sel.bind("<1>", lambda event: update_outputs())
            self.F_plots.get_tk_widget().bind("<1>", lambda event: update_outputs())
            self.R_plots.get_tk_widget().bind("<1>", lambda event: update_outputs())
            self.F_view.get_tk_widget().bind("<1>", lambda event: update_outputs())
            self.R_view.get_tk_widget().bind("<1>", lambda event: update_outputs())
            self.V_plots.get_tk_widget().bind("<1>", lambda event: update_outputs())

        if True: # Update with option menu change
            F_UL_Count.trace_add("write", update_outputs)
            F_P_exist.trace_add("write", update_outputs)
            R_UL_Count.trace_add("write", update_outputs)
            R_P_exist.trace_add("write", update_outputs)
            ps_converge.trace_add("write", update_outputs)
            ps_IC_move.trace_add("write", update_outputs)
            ps_axle_roll.trace_add("write", update_outputs)
            ps_body_roll.trace_add("write", update_outputs)
            ps_100_anti.trace_add("write", update_outputs)
            ps_ride_anti.trace_add("write", update_outputs)
            ps_roll_center.trace_add("write", update_outputs)
            ps_ride_IC.trace_add("write", update_outputs)

        update_outputs()

        def load_from_file():
            load_susp()
            master.switch_frame("linkCalc")