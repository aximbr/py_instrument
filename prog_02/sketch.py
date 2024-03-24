import sys
import pyvisa as visa


VISA_LIB_PATH = '/usr/lib/librsvisa.so'
#VISA_LIB_PATH = '@py'

#main()
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

rm = visa.ResourceManager(VISA_LIB_PATH)
address = rm.list_resources('USB?*::INSTR')
print(address)
print(type(address))
print(len(address))
print("tentando abrir o recurso")

try:
    pm = rm.open_resource('USB0::6669::5592::210118::1::INSTR')
except:
    print("deu não!")

