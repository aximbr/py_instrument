"""Ladybug Power Sensor Class"""
import time
import pyvisa as visa

VISA_LIB_PATH = '/usr/lib/librsvisa.so'
#VISA_LIB_PATH = '@py'

class LB5908A():
    """Ladybug Power Sensor LB5908A class"""
    def __init__(self):
        rm = visa.ResourceManager(VISA_LIB_PATH)
        address = rm.list_resources('USB?*::INSTR')
        print(address)
        self.pm = rm.open_resource(address[0])
        self.description = self.pm.query('*IDN?')
        self.reset()

    def show_info(self):
        return self.description

    def reset(self):
        self.pm.write('*RST')
        time.sleep(0.2)

    def read_power(self):
        return self.pm.query('READ?')
    
    def get_auto_average(self):
        return int(self.pm.query('AVER:COUN:AUTO?'))

    def clear_auto_average(self):
        self.pm.write('AVER:COUN:AUTO 0')

    def set_auto_average(self):
        self.pm.write('AVER:COUN:AUTO 1')

    def set_average_count(self, num):
        self.pm.write(f"AVER:COUN {num}")

    def get_unit_power(self):
        return self.pm.query('UNIT:POW?') 

    def set_unit_power_dbm(self):
        self.pm.write('UNIT:POW DBM')

    def set_unit_power_watt(self):
        self.pm.write('UNIT:POW W')

    def read_power_dbm(self, num_dig):
        self.set_unit_power_dbm()
        num = float(self.read_power())
        return f"{num:.{num_dig}f}"

    def read_power_watt(self, num_dig):
        self.set_unit_power_watt()
        num = float(self.read_power())
        return f"{num:.{num_dig}e}"

