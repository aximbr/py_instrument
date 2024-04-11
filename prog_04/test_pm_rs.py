"""This is a test suite for LadyBug Power Sensor with RsInstrument module"""
from RsInstrument import RsInstrument

# A good practice is to assure that you have a certain minimum version installed
RsInstrument.assert_minimum_version('1.50.0')

#List of Resources
instr_list = RsInstrument.list_resources('USB?*::INSTR')
#instr_list = RsInstrument.list_resources('?*')
print(instr_list)
# # Initializing the session
instr = RsInstrument(instr_list[0], False, True)

# Switch ON logging to the console.
instr.logger.log_to_console = True
instr.logger.start()
instr.reset()

idn = instr.query('*IDN?')
print(f"\nHello, I am: '{idn}'")