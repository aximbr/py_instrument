"""Another program for test Ladybug Power sensor"""
#import time
from ladybug import LB5908A

def teste(pm):
    """Small test program"""
    pm.clear_auto_average()
    pm.set_average_count(10)
    pm.read_many_times(10)

#main()
my_pm = LB5908A()
print(f"My Power Meter is {my_pm.show_info()}\n")

my_pm.reset()
print("Show reading in dBm")
my_pm.set_unit_power_dbm()
teste(my_pm)

print("Show reading in Watts")
my_pm.set_unit_power_watt()
teste(my_pm)
