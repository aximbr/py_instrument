"""Another program for test Ladybug Power sensor"""
import time
import pyvisa as visa

VISA_LIB_PATH = '/usr/lib/librsvisa.so'

def get_info(instrument):
    return(instrument.query('*IDN?'))

def reset(instrument):
    instrument.write('*RST')
    time.sleep(0.2)

def get_auto_average(instrument):
    return int(instrument.query('AVER:COUN:AUTO?'))

def clear_auto_average(instrument):
    instrument.write('AVER:COUN:AUTO 0')
    
def set_auto_average(instrument):
    instrument.write('AVER:COUN:AUTO 1')

def set_average_count(instrument, num):
    instrument.write(f"AVER:COUN {num}")

def read_many_times(instrument, num):
    for _ in range(num):
        print(instrument.query('READ?'))
        time.sleep(0.1)

def get_unit_power(instrument):
    return instrument.query('UNIT:POW?')

def set_unit_power_dbm(instrument):
    instrument.write('UNIT:POW DBM')

def set_unit_power_watt(instrument):
    instrument.write('UNIT:POW W')


def teste(instrument):
    clear_auto_average(instrument)
    set_average_count(instrument, 10)
    read_many_times(instrument, 10)


#main()
rm = visa.ResourceManager(VISA_LIB_PATH)
address = rm.list_resources('USB?*::INSTR')
print(address[0])
my_pm = rm.open_resource(address[0])

print(f"My Power Meter is {get_info(my_pm)}\n")

reset(my_pm)
set_unit_power_dbm(my_pm)
teste(my_pm)

set_unit_power_watt(my_pm)
teste(my_pm)


rm.close()


