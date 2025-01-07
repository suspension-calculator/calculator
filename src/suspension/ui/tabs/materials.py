# src/suspension/ui/tabs/materials.py

import tkinter as tk
from suspension.ui.styles import *
from suspension.io.material_add import add_material


class materialsPage(tk.Frame):
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
            text="Material:",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="e",
        )
        label.grid(row=0, column=0, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="Elastic Modulus:",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="e",
        )
        label.grid(row=1, column=0, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="Yield Strength:",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="e",
        )
        label.grid(row=2, column=0, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="Density:",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="e",
        )
        label.grid(row=3, column=0, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="Notes",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="e",
        )
        label.grid(row=4, column=0, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        text = tk.StringVar()
        text.set("")
        name_input = tk.Entry(
            input_frame,
            font=(fontType, 17),
            justify=tk.CENTER,
            width=20,
            textvariable=text,
            insertbackground=entryTextColor,
        )
        name_input.grid(row=0, column=1, sticky="e")
        name_input.config(bg=textEntryColor)
        name_input.config(fg=entryTextColor)
        name_input.bind("<Return>", lambda event: update_outputs())

        text = tk.StringVar()
        text.set("")
        modulus_input = tk.Entry(
            input_frame,
            font=(fontType, 17),
            justify=tk.CENTER,
            width=13,
            textvariable=text,
            insertbackground=entryTextColor,
        )
        modulus_input.grid(row=1, column=1, sticky="e")
        modulus_input.config(bg=textEntryColor)
        modulus_input.config(fg=entryTextColor)
        modulus_input.bind("<Return>", lambda event: update_outputs())

        text = tk.StringVar()
        text.set("")
        yield_input = tk.Entry(
            input_frame,
            font=(fontType, 17),
            justify=tk.CENTER,
            width=12,
            textvariable=text,
            insertbackground=entryTextColor,
        )
        yield_input.grid(row=2, column=1, sticky="e")
        yield_input.config(bg=textEntryColor)
        yield_input.config(fg=entryTextColor)
        yield_input.bind("<Return>", lambda event: update_outputs())

        text = tk.StringVar()
        text.set("")
        density_input = tk.Entry(
            input_frame,
            font=(fontType, 17),
            justify=tk.CENTER,
            width=11,
            textvariable=text,
            insertbackground=entryTextColor,
        )
        density_input.grid(row=3, column=1, sticky="e")
        density_input.config(bg=textEntryColor)
        density_input.config(fg=entryTextColor)
        density_input.bind("<Return>", lambda event: update_outputs())

        text = tk.StringVar()
        text.set("")
        notes_input = tk.Entry(
            input_frame,
            font=(fontType, 17),
            justify=tk.CENTER,
            width=50,
            textvariable=text,
            insertbackground=entryTextColor,
        )
        notes_input.grid(row=4, column=1, columnspan=3, sticky="w")
        notes_input.config(bg=textEntryColor)
        notes_input.config(fg=entryTextColor)
        notes_input.bind("<Return>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="psi",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="w",
        )
        label.grid(row=1, column=2, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="psi",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="w",
        )
        label.grid(row=2, column=2, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        label = tk.Label(
            input_frame,
            text="lbs/in\u00B3",
            background=bgColor,
            foreground=entryTextColor,
            font=(fontType, 17),
            anchor="w",
            width=40,
        )
        label.grid(row=3, column=2, sticky="nesw", pady=5)
        label.bind("<1>", lambda event: update_outputs())

        add_button = tk.Button(
            input_frame,
            text="Add Material",
            fg=pressedButtonColor,
            bg=buttonColor,
            command=lambda: add_button_press(),
            height=1,
            width=11,
            font=(fontType, 13),
        )
        add_button.grid(row=5, column=1, padx=2)

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
        cancel_button.grid(row=5, column=0, padx=2)

        def update_outputs(*args):
            self.focus_set()

        def add_button_press(*args):
            if (
                len(name_input.get()) > 0
                and len(modulus_input.get()) > 0
                and len(yield_input.get()) > 0
                and len(density_input.get()) > 0
                and len(notes_input.get()) > 0
            ):
                try:
                    add_material(
                        name_input.get(),
                        modulus_input.get(),
                        yield_input.get(),
                        density_input.get(),
                        notes_input.get(),
                    )
                except:
                    a = 1
            master.switch_frame("linkSizing")
