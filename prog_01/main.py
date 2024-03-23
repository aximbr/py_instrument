#This is my first program to test using a Ladybug Power Sensor Model LB5908A with Python on Linux

import time
import pyvisa as visa


rm = visa.ResourceManager('/usr/lib/librsvisa.so')
#print(rm.list_resources('USB?*::INSTR'))
ladybug = rm.open_resource('USB0::6669::5592::210118::1::INSTR')

print(ladybug.query('*IDN?'))
#print(rm)

#place the power sensor to know state
ladybug.write('*RST')
time.sleep(0.2)

#request the state for auto average
auto_average = int(ladybug.query('AVER:COUN:AUTO?'))
print(auto_average)

#set auto average to off
if auto_average == 1:
    ladybug.write('AVER:COUN:AUTO 0')

#check if changes
auto_average = int(ladybug.query('AVER:COUN:AUTO?'))
print(auto_average)

#check the average count
average_count = int(ladybug.query('AVER:COUN?'))
print(average_count)

#set the average count to 10
if average_count != 10:
    ladybug.write('AVER:COUN 10')

#now read 10 times the input
for _ in range(10):
    print(ladybug.query('READ?'))
    time.sleep(0.1)


