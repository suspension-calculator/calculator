# src/suspension/ui/tabs/rod_end.py

import tkinter as tk
from suspension.ui.styles import *
from suspension.io.rod_end_add import add_rod_end


class rodEndsPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.bind("<1>", lambda event: update_outputs())
        self.grid_configure(sticky="nesw")
        input_frame = tk.Frame(self, background=bgColor)
        input_frame.grid(row=1, column=1, sticky="nesw")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        label = tk.Label(
            self, text="a", background=bgColor, foreground=bgColor, font=(fontType, 17)
        )
        label.grid(row=1, column=0, sticky="nesw")
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            self, text="a", background=bgColor, foreground=bgColor, font=(fontType, 17)
        )
        label.grid(row=1, column=2, sticky="nesw")
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            self, text="a", background=bgColor, foreground=bgColor, font=(fontType, 17)
        )
        label.grid(row=0, column=1, sticky="nesw")
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            self, text="a", background=bgColor, foreground=bgColor, font=(fontType, 17)
        )
        label.grid(row=2, column=1, sticky="nesw")
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="Rod End:",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="e",
        )
        label.grid(row=0, column=0, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="Radial Load:",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="e",
        )
        label.grid(row=1, column=0, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="Weight:",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="e",
        )
        label.grid(row=2, column=0, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="Through Hole Diameter:",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="e",
        )
        label.grid(row=3, column=0, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="Shank Diameter",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="e",
        )
        label.grid(row=4, column=0, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="Shank Thread:",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="e",
        )
        label.grid(row=5, column=0, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        text = tk.StringVar()
        text.set("")
        name_input = tk.Entry(
            input_frame,
            font=(fontType, 17),
            justify=tk.CENTER,
            width=15,
            textvariable=text,
            insertbackground=entryTextColor,
        )
        name_input.grid(row=0, column=1, sticky="e")
        name_input.config(bg=textEntryColor)
        name_input.config(fg=entryTextColor)
        name_input.bind("<Return>", lambda event: update_outputs())

        text = tk.StringVar()
        text.set("")
        radial_load_input = tk.Entry(
            input_frame,
            font=(fontType, 17),
            justify=tk.CENTER,
            width=10,
            textvariable=text,
            insertbackground=entryTextColor,
        )
        radial_load_input.grid(row=1, column=1, sticky="e")
        radial_load_input.config(bg=textEntryColor)
        radial_load_input.config(fg=entryTextColor)
        radial_load_input.bind("<Return>", lambda event: update_outputs())

        text = tk.StringVar()
        text.set("")
        weight_input = tk.Entry(
            input_frame,
            font=(fontType, 17),
            justify=tk.CENTER,
            width=7,
            textvariable=text,
            insertbackground=entryTextColor,
        )
        weight_input.grid(row=2, column=1, sticky="e")
        weight_input.config(bg=textEntryColor)
        weight_input.config(fg=entryTextColor)
        weight_input.bind("<Return>", lambda event: update_outputs())

        text = tk.StringVar()
        text.set("")
        hole_input = tk.Entry(
            input_frame,
            font=(fontType, 17),
            justify=tk.CENTER,
            width=11,
            textvariable=text,
            insertbackground=entryTextColor,
        )
        hole_input.grid(row=3, column=1, sticky="e")
        hole_input.config(bg=textEntryColor)
        hole_input.config(fg=entryTextColor)
        hole_input.bind("<Return>", lambda event: update_outputs())

        text = tk.StringVar()
        text.set("")
        shank_input = tk.Entry(
            input_frame,
            font=(fontType, 17),
            justify=tk.CENTER,
            width=8,
            textvariable=text,
            insertbackground=entryTextColor,
        )
        shank_input.grid(row=4, column=1, sticky="e")
        shank_input.config(bg=textEntryColor)
        shank_input.config(fg=entryTextColor)
        shank_input.bind("<Return>", lambda event: update_outputs())

        text = tk.StringVar()
        text.set("")
        thread_input = tk.Entry(
            input_frame,
            font=(fontType, 17),
            justify=tk.CENTER,
            width=10,
            textvariable=text,
            insertbackground=entryTextColor,
        )
        thread_input.grid(row=5, column=1, sticky="e")
        thread_input.config(bg=textEntryColor)
        thread_input.config(fg=entryTextColor)
        thread_input.bind("<Return>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="lbs",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="w",
        )
        label.grid(row=1, column=2, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="lbs",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="w",
        )
        label.grid(row=2, column=2, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="in",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="w",
        )
        label.grid(row=3, column=2, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="in",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="w",
        )
        label.grid(row=4, column=2, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        add_button = tk.Button(
            input_frame,
            text="Add Rod End",
            fg=pressedButtonColor,
            bg=buttonColor,
            command=lambda: add_button_press(),
            height=1,
            width=11,
            font=(fontType, 13),
        )
        add_button.grid(row=6, column=1, padx=2)

        cancel_button = tk.Button(
            input_frame,
            text="Cancel",
            fg=pressedButtonColor,
            bg=buttonColor,
            command=lambda: master.switch_frame("linkSizing"),
            height=1,
            width=11,
            font=(fontType, 13),
        )
        cancel_button.grid(row=6, column=0, padx=2)

        def update_outputs(*args):
            self.focus_set()

        def add_button_press(*args):
            if (
                len(name_input.get()) > 0
                and len(radial_load_input.get()) > 0
                and len(weight_input.get()) > 0
                and len(hole_input.get()) > 0
                and len(shank_input.get()) > 0
                and len(thread_input.get()) > 0
            ):
                try:
                    add_rod_end(
                        name_input.get(),
                        float(radial_load_input.get()),
                        float(weight_input.get()),
                        float(hole_input.get()),
                        float(shank_input.get()),
                        thread_input.get(),
                    )
                except:
                    a = 1
            master.switch_frame("linkSizing")
