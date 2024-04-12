"""Class definition for Power Meter GUI"""
import tkinter as tk
from tkinter import ttk
from ladybug import LB5908A

BLACK = "#000000"
RED = "#e7305b"
GREEN = "#55ff33"
FONT_NAME = "Ariel"
#include here the frequecies to work with
FREQS = [50, 954, 1000, 2185, 2200, 4000, 4300]

class App(tk.Tk):
    """Class for PM GUI"""
    def __init__(self):
        super().__init__()
        #main window 
        self.title("Very Very Simple Power Meter")
        self.geometry('470x240')
        self.config(background="white", padx=5, pady=5)
        #Title
        self.title_label = ttk.Label(text="Power Meter", foreground=BLACK, background="white", font=("Courrier", 26))
        self.title_label.grid(column=1, row=0)
        #Canvas
        self.canvas = tk.Canvas(width=150, height=60, background=BLACK, highlightthickness=0)
        self.read_text = self.canvas.create_text(80, 30, fill=GREEN, text="", font=(FONT_NAME, 18))
        self.canvas.grid(column=1, row=1)
        #List Box with know frequencies
        self.list_freq = tk.Listbox(height=3, width=5, selectmode='single')
        self.list_freq.bind('<<ListboxSelect>>', self.callback_list_freq)
        self.list_freq.grid(column=0, row=1, rowspan=1 )
        #MHZ Label
        self.label_mhz = ttk.Label(text="MHz", background="white", foreground="black", font=("Arial",8, "bold"))
        self.label_mhz.grid(column=0, row=2)
        #Info Label
        self.info_label = ttk.Label(text="", background="white",foreground="black", font=("Arial",8))
        self.info_label.grid(column=1,row=3)
        #Read Button
        self.read_button = ttk.Button(text="", command=self.start_stop_read)
        self.read_button.grid(column=2, row=1)
        #End of UI definition
        #Create PM
        self.pm_frequency = 1.0E09
        self.my_pm = LB5908A()
        self.task_id = ""
        #Initial condition
        self.isreading = False
        self.__setup__()

    def __setup__(self):
        #Fill with description of Power Sensor
        self.info_label.config(text=self.my_pm.description)
        #Prepare start/stop button
        if not self.isreading:
            self.read_button.config(text="Start")
        else:
            self.read_button.config(text="Stop")
        #Fill Freq List
        for freq in FREQS:
            self.list_freq.insert(tk.END, freq)
        #Prepare to fetch values from Power Sensor
        self.my_pm.prepare_to_fetch(self.pm_frequency)

    def callback_list_freq(self, event):
        """Callback function when a frequency is select"""
        self.pm_frequency = FREQS[self.list_freq.curselection()[0]] *10E06
        #print(self.pm_frequency)
        #if reading, stop read and setting with new freq
        if self.isreading:
            self.start_stop_read()
        self.my_pm.prepare_to_fetch(self.pm_frequency)

    def start_stop_read(self):
        """Read Button action"""
        if not self.isreading:
            self.read_button.config(text="Stop")
            self.task_id = self.after(300, self.read)
        else:
            self.read_button.config(text="Start")
            self.after_cancel(self.task_id)
            self.isreading = False

    def read(self):
        """Read the Power Meter sensor in dBm using Fetch method, use 2 digits for precision"""
        self.isreading = True
        pm_read = f'{self.my_pm.fetch():.2f} dBm'
        self.canvas.itemconfig(self.read_text,text=pm_read)
        self.task_id = self.after(300, self.read)
 