import serial
import sys


def read_voltage_arduino(SERIAL_PORT):
    ardSerial = serial.Serial(SERIAL_PORT, 9600)
    
    prevVoltage = 0
    steadyCount = 0
    totalCount = 0
    readSuccess = False
    
    while True:
        totalCount += 1
        while readSuccess == False:
            rawVoltage = ardSerial.readline() 
            readVoltage = rawVoltage.strip()
            readSuccess = True
            try:
                voltage = float(readVoltage)
            except:
                readSuccess = False
    
        readSuccess = False
    
        if voltage == prevVoltage:
            steadyCount += 1
        else:
            steadyCount = 0
        if steadyCount >= 4:
            finalVoltage = voltage
            break
        elif totalCount >= 50:
            finalVoltage = voltage
            break
        else:
            prevVoltage = voltage
    
    ardSerial.close()
    
    return finalVoltage


if __name__ == '__main__':
    SERIAL_PORT = sys.argv[1]
    WRITE_FILE = sys.argv[2]
    result = read_voltage_arduino(SERIAL_PORT)

    with open(WRITE_FILE, 'r+') as f:
        f.write(str(result))
        f.truncate()

