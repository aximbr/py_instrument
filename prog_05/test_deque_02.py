from collections import deque
from random import randrange
import sys, time

pm_reads = deque(maxlen=10)
pm_reads.append(0)

def new_reading():
    new_read = randrange(0, 11)
    pm_reads.appendleft(new_read)

#main
for _ in range(100):
    sys.stdout.write(f"Our reading set is: {list(pm_reads)}   \r")
    sys.stdout.flush()
    new_reading()
    time.sleep(0.1)
