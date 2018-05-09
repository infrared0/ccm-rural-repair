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

    backhaul_file = sys.argv[2]
    SERIAL_PORT = sys.argv[1]
    serial_open = False

    while True:
        if not serial_open:
            try:
                ardSerial = serial.Serial(SERIAL_PORT, 9600)
                serial_open = True
                print "Serial opened"
            except serial.serialutil.SerialException:
                print "Serial failed to open"
                time.sleep(30)
        else:
            try:
                state = get_backhaul_status()

                print state
                with open(backhaul_file, "r+") as f:
                    f.write(state + "\n") 

                write_state_arduino(ardSerial, state)
                time.sleep(10)
            except serial.serialutil.SerialException:
                ardSerial.close()
                serial_open = False
                print "Serial closed"
                time.sleep(30)

