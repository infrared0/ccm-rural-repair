import serial
import sys

SERIAL_PORT = sys.argv[1]

ardSerial = serial.Serial(SERIAL_PORT, 9600)
low_voltage = 11

prevVoltage = 0
steadyCount = 0
totalCount = 0

while True:
    totalCount += 1
    readVoltage = ardSerial.readline() 
    voltage = float(readVoltage)
    if voltage == prevVoltage:
        steadyCount += 1
    if steadyCount >= 4:
        finalVoltage = voltage
        break
    elif totalCount >= 50:
        finalVoltage = voltage
        break
    else:
        prevVoltage = voltage
         
if finalVoltage <= 11:
    print finalVoltage 
