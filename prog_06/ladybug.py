"""Ladybug Power Sensor Class"""
import time
import pyvisa as visa

#Select one of VISA lib implementation, make sure it is installed
#VISA_LIB_PATH = '/usr/lib/librsvisa.so'
#VISA_LIB_PATH = '/usr/lib/x86_64-linux-gnu/libvisa.so.24.0.0'
VISA_LIB_PATH = '@py'

#Min and Max Freq (MHz) for this model
MIN_FREQ = 1.0E06
MAX_FREQ = 8.0E09

class LB5908A():
    """Ladybug Power Sensor LB5908A class"""
    def __init__(self):
        rm = visa.ResourceManager(VISA_LIB_PATH)
        #print(rm)
        address = rm.list_resources('USB?*::INSTR')
        self.pm = rm.open_resource(address[0])
        self.description = self.pm.query('*IDN?')
        self.power_mode = ""
        self.reset()
        #visa.log_to_screen()

    def close(self):
        """Close the session"""
        self.pm.close()

    def show_info(self):
        """Returns description for instrument"""
        return self.description

    def reset(self):
        """Set the instrument to a know state"""
        self.pm.write('*RST')
        self.power_mode = self.get_unit_power()
        time.sleep(0.1)

    def clear(self):
        """Device Clear Command"""
        self.pm.write('DCL')
        
    def set_default_state(self):
        """Set to default settings"""
        self.pm.write('SYST:PRES DEF')

    def clear_auto_average(self):
        """Disable the Auto Average"""
        self.pm.write('AVER:COUN:AUTO 0')

    def turn_off_step_detection(self):
        """Turn off step detection"""
        self.pm.write('SENS:AVER:SDET OFF')

    def turn_off_continuos_triggering(self):
        """Turn off continuous triggering"""
        self.pm.write('INIT:CONT OFF')

    def turn_on_continuos_triggering(self):
        """Turn on continuous triggering"""
        self.pm.write('INIT:CONT ON')

    def prepare_to_read(self, freq):
        """Send commands to prepare to read"""
        self.clear()
        self.set_default_state()
        self.clear_auto_average()
        self.turn_off_step_detection()
        self.turn_off_continuos_triggering()
        self.set_average_count(10)
        self.set_freq(freq)

    def read_power(self):
        """Return one power reading"""
        return self.pm.query('READ?')
    
    def prepare_to_fetch(self, freq):
        """Send commands to prepare to fetch"""
        self.clear()
        self.set_default_state()
        self.clear_auto_average()
        self.turn_off_step_detection()
        self.turn_on_continuos_triggering()
        self.set_average_count(10)
        self.set_freq(freq)

    def fetch(self):
        """Return one power using Fetch"""
        return float(self.pm.query('FETCH?'))

    def prepare_to_measure(self, freq):
        """Send commands to prepare to measure"""
        self.pm.timeout = 50000
        self.clear()
        self.set_default_state()
        self.set_freq(freq)

    def measure(self):
        """Perform a measure"""
        return float(self.pm.query('MEAS?'))

    def get_auto_average(self):
        """Return the state of Auto Average"""
        return self.pm.query('AVER:COUN:AUTO?')

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
        self.power_mode = 'DBM'

    def set_unit_power_watt(self):
        """Set the power unit to Watt"""
        self.pm.write('UNIT:POW W')
        self.power_mode = 'W'

    def read_power_dbm(self, num_dig):
        """Set the power unit to dBm and make a read, retun the reading with 'num_dig' 
        of decimals"""
        if self.power_mode != 'DBM':
            self.set_unit_power_dbm()
        num = float(self.read_power())
        return f"{num:.{num_dig}f}"

    def read_power_watt(self, num_dig):
        """Set the power unit to Watt and make a read, retun the reading with 'num_dig'
        of decimals"""
        if self.power_mode != 'W':
            self.set_unit_power_watt()
        num = float(self.read_power())
        return f"{num:.{num_dig}e}"

    def get_freq(self):
        """Read the current frequency set"""
        return float(self.pm.query('FREQ?'))

    
    def set_freq(self, new_freq):
        """Set new frequency on Power Sensor"""
        if MIN_FREQ < new_freq < MAX_FREQ:
            self.pm.write(f'FREQ {new_freq} HZ')
