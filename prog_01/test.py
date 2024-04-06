import pyvisa as visa

visa.log_to_screen()
#rm = visa.ResourceManager('/usr/lib/librsvisa.so')
rm = visa.ResourceManager('@py')
#rm = visa.ResourceManager('/usr/lib/x86_64-linux-gnu/libivivisa.so.7.0.0')
#rm = visa.ResourceManager()
print(rm)
print(rm.list_resources('USB?*::INSTR'))
ladybug = rm.open_resource('USB0::6669::5592::210118::1::INSTR')

print(ladybug.query('*IDN?'))
