"""Just a space for tests"""
import sys
import pyvisa as visa


#VISA_LIB_PATH = '/usr/lib/librsvisa.so'
VISA_LIB_PATH = '/usr/lib/x86_64-linux-gnu/libvisa.so.24.0.0'
#VISA_LIB_PATH = '@py'

#main()
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

rm = visa.ResourceManager(VISA_LIB_PATH)
print(rm)
address = rm.list_resources('USB?*::INSTR')
print(address)
print(type(address))
print(len(address))
print("tentando abrir o recurso")


try:
    print(rm.resource_info(address[0], extended=True))
    pm = rm.open_resource('USB0::6669::5592::210118::1::INSTR')
    print("Sucesso")
except:
    print("deu não!")

