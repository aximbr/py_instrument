import matplotlib.pyplot as plt
from random import randint
import time

x_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def new_data(origin):
    return [randint(1,10) for _ in origin]

#y_data = new_data(x_data)


#Do not show the toolbar
plt.rcParams['toolbar']= 'None'
#set the Dark Theme
plt.style.use('dark_background')

#make interactive on
plt.ion()
#Create the figure and the lines
my_fig = plt.figure()
ax = my_fig.add_subplot(111)
#Create the graphic for x and y values, set the line color as orange
for _ in range(50):
    y_data = new_data(x_data)
    ax.plot(x_data, y_data, color='orange')
    #Show the grid
    #ax.grid(visible=True)
    #Invert the x axis values
    ax.invert_xaxis()
    #exibit the graphic
    my_fig.canvas.draw()
    #wait 3 seconds
    time.sleep(0.2)
    my_fig.canvas.flush_events()
    ax.cla()

