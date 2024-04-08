from tkinter import *
import random

BLACK = "#000000"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reads = [0, 1, 3, 6, 2, 6, 8, 9]

#---- Define local function
def show_info():
    pass

def read():
    pm_read = reads[random.randint(0, len(reads)-1)]
    canvas.itemconfig(read_text,text=pm_read)

#---- User interface
root = Tk()
root.title("Very Very Simple Power Meter")
root.config(background=YELLOW, padx=10, pady=10)

title_label = Label(text="Power Meter", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

canvas = Canvas(width=100, height=50, bg=BLACK, highlightthickness=0)

read_text = canvas.create_text(50, 35, fill=GREEN, text="", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

info_button = Button(text="info", highlightthickness=0, command=show_info)
info_button.grid(column=0, row=2)

read_button = Button(text="Read", highlightthickness=0, command=read)
read_button.grid(column=2, row=2)

root.mainloop()