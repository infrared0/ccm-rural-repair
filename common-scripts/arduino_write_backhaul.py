import serial
import sys
import subprocess
import time

def write_state_arduino(serialport, status):
    tosend = status + ";"
    serialport.write(tosend)

def get_backhaul_status():
    cmd = "curl ccm.cs.washington.edu > /dev/null 2>&1"
    result = subprocess.call(cmd, shell=True)

    if result == 0:
        #print "light off"
        backhaul_status = "0"
    else:
        #print "light on"
        backhaul_status = "1"

    return backhaul_status

if __name__ == '__main__':
    SERIAL_PORT = sys.argv[1]
    ardSerial = serial.Serial(SERIAL_PORT, 9600)
    while True:
        state = get_backhaul_status()
        #print state
        write_state_arduino(ardSerial, state)
        time.sleep(10)
    ardSerial.close()


