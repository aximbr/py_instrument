"""Class definition for Power Meter GUI"""
import tkinter as tk
from tkinter import ttk

#from random import randrange

from collections import deque

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from ladybug import LB5908A

BLACK = "#000000"
RED = "#e7305b"
GREEN = "#55ff33"
FONT_NAME = "Ariel"
#include here the frequecies to work with
FREQS = [50, 954, 1000, 2185, 2200, 4000, 4300]

READ_INTERVAL_MS = 300
MAX_SEC_READINGS = 60
MAX_READINGS = int(MAX_SEC_READINGS / (READ_INTERVAL_MS/1000))

class App(tk.Tk):
    """Class for PM GUI"""
    def __init__(self):
        super().__init__()
        #main window
        self.title("Very Very Simple Power Meter")
        self.geometry('470x240')
        self.config(background="white", padx=1, pady=1)
        #Title
        self.title_label = ttk.Label(text="Power Meter", foreground=BLACK,
                                     background="white", font=("Courrier", 16))
        self.title_label.grid(column=1, row=0)
        #Canvas
        self.canvas = tk.Canvas(width=150, height=40, background=BLACK, highlightthickness=0)
        self.read_text = self.canvas.create_text(80, 20, fill=GREEN, text="", font=(FONT_NAME, 18))
        self.canvas.grid(column=1, row=1,pady=0)
        #List Box with know frequencies
        self.list_freq = tk.Listbox(height=3, width=7, selectmode='single')
        self.list_freq.bind('<<ListboxSelect>>', self.callback_list_freq)
        self.list_freq.grid(column=0, row=1, sticky='W' )
        #Include a yscrollbar besides the listbox
        self.list_scrollbar = tk.Scrollbar(orient='vertical', width=15)
        self.list_scrollbar.grid(column=0, row=1, sticky='N,S,E')
        #Attach srollbar to listbox
        self.list_freq.config(yscrollcommand= self.list_scrollbar.set)
        self.list_scrollbar.config(command = self.list_freq.yview)
        #MHZ Label
        self.label_mhz = ttk.Label(text="MHz", background="white", foreground="black",
                                   font=("Arial",8, "bold"))
        self.label_mhz.grid(column=0, row=0)
        #Info Label
        self.info_label = ttk.Label(text="", wraplength=70, background="white",foreground="black",
                                    font=("Arial",8))
        self.info_label.grid(column=0,row=2, sticky='N', pady=10)
        #Read Button
        self.read_button = ttk.Button(text="", command=self.start_stop_read)
        self.read_button.grid(column=2, row=1)
        #End of UI definition
        #Create PM
        self.pm_frequency = 1.0E09
        self.my_pm = LB5908A()
        self.task_id = ""
        #Create a place to store the last 60*0.3 = 200 readings
        self.pm_reads = deque(maxlen=MAX_READINGS)
        self.x_data = list(range(MAX_READINGS))
        #Figure that will contain the plot
        self.fig = Figure(figsize = (3, 2), dpi = 100)
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.set_facecolor('black')
        self.ax.grid(visible=True, which='both',linestyle='dotted')
        self.ax.set_ylim(-80,20)
        self.ax.tick_params(axis='both',labelsize=6)
        self.ax.set_xlim(60, 0)
        self.ax.yaxis.tick_right()
        self.fig.canvas.draw()
        #Create a canvas to contains the figure
        self.canvas_fig = FigureCanvasTkAgg(self.fig)
        self.canvas_fig.get_tk_widget().configure(width=200,height=70)
        self.canvas_fig.get_tk_widget().grid(column=1, row=2, pady= 0, ipadx=40,
                                             ipady=40, sticky='N')
        #Initial condition
        self.isreading = False
        self.__setup__()

    def __setup__(self):
        #Fill with description of Power Sensor
        self.info_label.config(text=self.my_pm.description)
        #self.info_label.config(text="Ladybug simulation")
        #Prepare start/stop button
        if not self.isreading:
            self.read_button.config(text="Start")
        else:
            self.read_button.config(text="Stop")
        #Fill Freq List
        for freq in FREQS:
            self.list_freq.insert(tk.END, freq)
        #Find index for Freq 1000 Mhz
        try:
            idx = FREQS.index(1000)
        except ValueError:
            idx = 0
        #Select the Freq 1000 MhZ on list box
        self.list_freq.select_set(idx)
        self.list_freq.see(idx)
        #Prepare to fetch values from Power Sensor
        self.my_pm.prepare_to_fetch(self.pm_frequency)
        #Initialize an store for PM Reading
        for _ in range(MAX_READINGS):
            self.pm_reads.append(0)

    def callback_list_freq(self, event):
        """Callback function when a frequency is select"""
        self.pm_frequency = FREQS[self.list_freq.curselection()[0]] *10E06
        #if reading, stop read and setting with new freq
        if self.isreading:
            self.start_stop_read()
        self.my_pm.prepare_to_fetch(self.pm_frequency)

    def start_stop_read(self):
        """Read Button action"""
        if not self.isreading:
            self.read_button.config(text="Stop")
            #self.ax.set_visible(True)
            self.task_id = self.after(READ_INTERVAL_MS, self.read)
        else:
            self.read_button.config(text="Start")
            self.after_cancel(self.task_id)
            self.isreading = False

    def read(self):
        """Read the Power Meter sensor in dBm using Fetch method, use 2 digits for precision"""
        self.isreading = True
        pm_read = self.my_pm.fetch()
        #pm_read = randrange(-60, 10)
        self.canvas.itemconfig(self.read_text,text=f'{pm_read:.2f} dBm')
        #save PM read on storage
        self.pm_reads.appendleft(pm_read)
        #converte deque to a list that can be plot
        y_data = list(self.pm_reads)
        self.plot(y_data)
        self.task_id = self.after(READ_INTERVAL_MS, self.read)

    def plot(self, y_list):
        """Plot the store reading"""
        #clear any previous plot and plot with new data
        self.ax.cla()
        self.ax.grid(visible=True, which='both',linestyle='dotted')
        self.ax.set_ylim(-80,20)
        self.ax.tick_params(axis='both',labelsize=6)
        self.ax.set_xlim(60, 0)
        self.ax.yaxis.tick_right()
        self.ax.plot(self.x_data, y_list, color='orange', linewidth=1.5)
        self.fig.canvas.draw()
        