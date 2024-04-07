"""Class definition for Power Meter GUI"""
import tkinter as tk
from tkinter import ttk
from ladybug import LB5908A
import random

BLACK = "#000000"
RED = "#e7305b"
GREEN = "#55ff33"
YELLOW = "#f7f5dd"
#FONT_NAME = "RADIOLAND"
FONT_NAME = "Ariel"
reads = [0, 1, 3, 6, 2, 6, 8, 9]


class App(tk.Tk):
    """Class for PM GUI"""
    def __init__(self):
        super().__init__()
        #main window
        self.title("Very Very Simple Power Meter")
        self.config(background="white", padx=10, pady=5)
        #Title
        self.title_label = ttk.Label(text="Power Meter", foreground=BLACK, background="white", font=("Courrier", 30))
        self.title_label.grid(column=1, row=0)
        #Canvas
        self.canvas = tk.Canvas(width=150, height=60, background=BLACK, highlightthickness=0)
        self.read_text = self.canvas.create_text(80, 30, fill=GREEN, text="", font=(FONT_NAME, 18))
        self.canvas.grid(column=1, row=1)
        #Info Button
        self.info_button = ttk.Button(text="info", command=self.show_info)
        self.info_button.grid(column=0, row=2)
        #Info Label
        self.info_label = ttk.Label(text="", anchor='n', background="white", foreground="black", font=("Arial",8))
        self.info_label.grid(column=1,row=3)
        #Read Button
        self.read_button = ttk.Button(text="", command=self.start_stop_read)
        self.read_button.grid(column=2, row=2)
        #Create PM
        self.pm_frequency = 1.0E09
        self.my_pm = LB5908A()
        #Initial condition
        self.isreading = False
        self.__setup__()
        
        

    def __setup__(self):
        self.info_label.config(text=self.my_pm.description)
        self.my_pm.prepare_to_fetch(self.pm_frequency)
        if not self.isreading:
            self.read_button.config(text="Start")
        else:
            self.read_button.config(text="Stop")

        

    def start_stop_read(self):
        """Read Button action"""
        #pm_read = reads[random.randint(0, len(reads)-1)]
        if not self.isreading:
            self.read_button.config(text="Stop")
            self.task_id = self.after(300, self.read)
        else:
            self.read_button.config(text="Start")
            self.after_cancel(self.task_id)
            self.isreading = False

    def read(self):
        self.isreading = True
        pm_read = f'{self.my_pm.fetch():.2f} dBm'
        self.canvas.itemconfig(self.read_text,text=pm_read)
        self.task_id = self.after(300, self.read)
        
    def show_info(self):
        """Info Button action"""
        pass

    