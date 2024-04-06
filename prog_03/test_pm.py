"""Another program for test Ladybug Power sensor"""
#import time
from os import system, name
import sys
from ladybug import LB5908A

# define our clear function
def clear():
    """Clear screen"""
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def show_menu():
    """Menu options"""
    clear()
    print("This program will run tests on Lady Bug Power Sensor")
    print("[1] - Show Power Sensor Info")
    print("[2] - Show the current Frequency Set")
    print("[3] - Set the frequency to 1 GHz")
    print("[4] - Make a reading in dBm")
    print("[5] - Make a reading in Watt")
    print("[0] - Exit the program")
    print("\n")

def exec_test(option):
    """Test functions"""
    my_pm = LB5908A()
    clear()
    if option == 0:
        return True
    elif option == 1:
        print(my_pm.description)
    elif option == 2:
        print(f"The current frequency is {my_pm.get_freq()/1000000} MHz")
    elif option == 3:
        my_pm.set_freq(1.0E09)
        print(f"The new frequency is {my_pm.get_freq()/1000000} MHz")
    elif option == 4:
        my_pm.clear_auto_average()
        my_pm.set_average_count(10)
        print(f"Current read is {my_pm.read_power_dbm(2)} dBm")
    elif option == 5:
        my_pm.clear_auto_average()
        my_pm.set_average_count(10)
        print(f"Current read is {my_pm.read_power_watt(2)} Watt")
    input("\nPress ENTER to continue")
    return False
    
    


#main()


finished = False

while not finished:
    show_menu()
    option = int(input("Please choose one option: "))
    finished = exec_test(option)

