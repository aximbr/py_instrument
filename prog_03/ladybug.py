"""Ladybug Power Sensor Class"""
import time
import pyvisa as visa

#VISA_LIB_PATH = '/usr/lib/librsvisa.so'
#VISA_LIB_PATH = '/usr/lib/x86_64-linux-gnu/libvisa.so.24.0.0'
VISA_LIB_PATH = '@py'


class LB5908A():
    """Ladybug Power Sensor LB5908A class"""
    def __init__(self):
        rm = visa.ResourceManager(VISA_LIB_PATH)
        print(rm)
        address = rm.list_resources('USB?*::INSTR')
        self.pm = rm.open_resource(address[0])
        self.description = self.pm.query('*IDN?')
        self.reset()

    def show_info(self):
        """Returns description for instrument"""
        return self.description

    def reset(self):
        """Set the instrument to a know state"""
        self.pm.write('*RST')
        time.sleep(0.2)

    def read_power(self):
        """Return one power reading"""
        return self.pm.query('READ?')

    def get_auto_average(self):
        """Return the state of Auto Average"""
        return self.pm.query('AVER:COUN:AUTO?')

    def clear_auto_average(self):
        """Disable the Auto Average"""
        self.pm.write('AVER:COUN:AUTO 0')

    def set_auto_average(self):
        """Set the Auto Average"""
        self.pm.write('AVER:COUN:AUTO 1')

    def get_average_count(self):
        """Return the value for average count"""
        return self.pm.query('AVER:COUN ?')

    def set_average_count(self, num):
        """Set the average count to 'num' """
        self.pm.write(f"AVER:COUN {num}")

    def get_unit_power(self):
        """Returns the power unit (DBM or W)"""
        return self.pm.query('UNIT:POW?')

    def set_unit_power_dbm(self):
        """Set the power unit to dBm"""
        self.pm.write('UNIT:POW DBM')

    def set_unit_power_watt(self):
        """Set the power unit to Watt"""
        self.pm.write('UNIT:POW W')

    def read_power_dbm(self, num_dig):
        """Set the power unit to dBm and make a read, retun the reading with 'num_dig' 
        of decimals"""
        self.set_unit_power_dbm()
        num = float(self.read_power())
        return f"{num:.{num_dig}f}"

    def read_power_watt(self, num_dig):
        """Set the power unit to Watt and make a read, retun the reading with 'num_dig'
        of decimals"""
        self.set_unit_power_watt()
        num = float(self.read_power())
        return f"{num:.{num_dig}e}"
