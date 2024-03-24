import pyvisa as visa


rm = visa.ResourceManager('/usr/lib/librsvisa.so')
#rm = visa.ResourceManager('@py')
#rm = visa.ResourceManager('/usr/lib/x86_64-linux-gnu/libiovisa.so')
print(rm)
print(rm.list_resources('USB?*::INSTR'))
ladybug = rm.open_resource('USB0::6669::5592::210118::1::INSTR')

print(ladybug.query('*IDN?'))
