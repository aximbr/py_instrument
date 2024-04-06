"""Class definition for Power Meter GUI"""
import tkinter as tk
from tkinter import ttk

import random

BLACK = "#000000"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reads = [0, 1, 3, 6, 2, 6, 8, 9]


class App(tk.Tk):
    """Class for PM GUI"""
    def __init__(self):
        super().__init__()
        #main window
        self.title("Very Very Simple Power Meter")
        self.config(background=YELLOW, padx=10, pady=10)
        #Title
        self.title_label = ttk.Label(text="Power Meter", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 40))
        self.title_label.grid(column=1, row=0)
        #Canvas
        self.canvas = tk.Canvas(width=100, height=50, background=BLACK, highlightthickness=0)
        self.read_text = self.canvas.create_text(50, 35, fill=GREEN, text="", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)
        #Info Button
        self.info_button = ttk.Button(text="info", command=self.show_info)
        self.info_button.grid(column=0, row=2)
        #Read Button
        self.read_button = ttk.Button(text="Read", command=self.read)
        self.read_button.grid(column=2, row=2)

    def read(self):
        """Read Button action"""
        pm_read = reads[random.randint(0, len(reads)-1)]
        self.canvas.itemconfig(self.read_text,text=pm_read)

    def show_info(self):
        """Info Button action"""
        pass

    