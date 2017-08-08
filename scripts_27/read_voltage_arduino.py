import serial
import sys

SERIAL_PORT = sys.argv[1]

ardSerial = serial.Serial(SERIAL_PORT, 9600)

prevVoltage = 0
steadyCount = 0
totalCount = 0

while True:
    totalCount += 1
    rawVoltage = ardSerial.readline() 
    readVoltage = rawVoltage.strip()
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

ardSerial.close()
print finalVoltage
