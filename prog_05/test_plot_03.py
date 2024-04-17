import matplotlib.pyplot as plt
from random import randrange
from collections import deque
import time
#1 read per sec, 60 sec of data
MAX_READINGS=60

pm_reads = deque(maxlen=MAX_READINGS)
x_data = [n for n in range(MAX_READINGS)]

for _ in range(MAX_READINGS):
    pm_reads.append(0)

def new_reading():
    new_read = randrange(0, 11)
    pm_reads.appendleft(new_read)


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
for _ in range(500):
    new_reading()
    y_data = list(pm_reads)
    ax.plot(x_data, y_data, color='orange')
    #Show the grid
    ax.grid(visible=True, which='major',linestyle='dotted')
    ax.set_ylim(-80,20)
    ax.set_xlim(60,0)
    ax.yaxis.tick_right()
    #exibit the graphic
    my_fig.canvas.draw()
    #wait 3 seconds
    time.sleep(0.1)
    my_fig.canvas.flush_events()
    ax.cla()

