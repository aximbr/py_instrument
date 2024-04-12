# from tkinter import *
# import os, sys

# if not sys.warnoptions:
#     import warnings
#     warnings.simplefilter("ignore")

# if os.getenv('DISPLAY') == None:
#     os.environ['DISPLAY'] = ":0.0"

########################################
# gui = Tk(className='Python Examples - Window Size')

# # Set window size
# gui.geometry("470x240")

# gui.mainloop()
########################################

# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	


from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import random
 
# initial data
x = [1]
y = [random.randint(1,10)]
 
# creating the first plot and frame
fig, ax = plt.subplots()
graph = ax.plot(x,y,color = 'g')[0]
plt.ylim(0,10)
 
 
# updates the data and graph
def update(frame):
    global graph
 
    # updating the data
    x.append(x[-1] + 1)
    y.append(random.randint(1,10))
 
    # creating a new graph or updating the graph
    graph.set_xdata(x)
    graph.set_ydata(y)
    plt.xlim(x[0], x[-1])
 
anim = FuncAnimation(fig, update, frames = None)
plt.show()
