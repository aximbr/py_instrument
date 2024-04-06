"""Another program for test Ladybug Power sensor"""
import time
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
    print("[4] - Make a reading in dBm for 10 sec")
    print("[5] - Make a reading in Watt for 10 sec")
    print("[6] - Make a measure in dBm - take a long time!")
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
        my_pm.prepare_to_read(1.0E09)
        start_time = time.perf_counter()
        stop_time = start_time
        while stop_time - start_time < 10.0:
            n = my_pm.read_power_dbm(2)
            sys.stdout.write(f"Current read is: {n} dBm   \r")
            time.sleep(0.1)
            sys.stdout.flush()
            stop_time = time.perf_counter()
    elif option == 5:
        my_pm.prepare_to_read(1.0E09)
        start_time = time.perf_counter()
        stop_time = start_time
        while stop_time - start_time < 10.0:
            n = my_pm.read_power_watt(2)
            sys.stdout.write(f"Current read is: {n} Watt   \r")
            time.sleep(0.1)
            sys.stdout.flush()
            stop_time = time.perf_counter()
    elif option == 6:
        my_pm.prepare_to_measure(1.0E09)
        start_time = time.perf_counter()
        n = my_pm.measure()
        sys.stdout.write(f"Current measure is: {n:.2f} dBm   \n")
        sys.stdout.write(f"Time ellapsed {(time.perf_counter() - start_time):.2f} sec\n")
        sys.stdout.flush()
    
    input("\nPress ENTER to continue")
    return False


#main()

isFinished = False

while not isFinished:
    show_menu()
    option = int(input("Please choose one option: "))
    isFinished = exec_test(option)
sys.exit()

