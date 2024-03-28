import pyvisa as visa

#VISA_LIB_PATH = '/usr/lib/librsvisa.so'
#VISA_LIB_PATH = '/usr/lib/x86_64-linux-gnu/libvisa.so.24.0.0'
VISA_LIB_PATH = '@py'



rm = visa.ResourceManager(VISA_LIB_PATH)
print(rm)
address = rm.list_resources('USB?*::INSTR')
try:
    pm = rm.open_resource(address[0])
    print(pm.query('*IDN?'))
except:
    print("não deu!")
    