"""Another program for test Ladybug Power sensor"""
#import time
from os import system, name
import sys
from ladybug import LB5908A



def teste_dbm(pm):
    """Small test program"""
    pm.clear_auto_average()
    pm.set_average_count(10)
    print(f"{pm.read_power_dbm(2)} dBm")

def teste_watt(pm):
    """Small test program"""
    pm.clear_auto_average()
    pm.set_average_count(10)
    print(f"{pm.read_power_watt(2)} Watts")

# define our clear function
def clear():
    """Clear screen"""
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#main()
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

my_pm = LB5908A()

#clear()
print(f"My Power Meter is {my_pm.show_info()}\n")

print("Show reading in dBm")
teste_dbm(my_pm)

print("Show reading in Watts")
teste_watt(my_pm)