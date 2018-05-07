import serial
import sys
import subprocess

def write_state_arduino(SERIAL_PORT, status):
    ardSerial = serial.Serial(SERIAL_PORT, 9600)
    ardSerial.write(status + ";")
    ardSerial.close()

def get_backhaul_status():
    cmd = "curl ccm.cs.washington.edu"
    result = subprocess.call(cmd, shell=True)
    print result 

    # DEBUG
    #backhaul_status = "1"
    #print "light on"

    if result == 0:
        print "light off"
        backhaul_status = "0"
    else:
        print "light on"
        backhaul_status = "1"

    return backhaul_status

if __name__ == '__main__':
    SERIAL_PORT = sys.argv[1]
    state = sys.argv[2]
    #result = get_backhaul_status()
    write_state_arduino(SERIAL_PORT, state)
    #print result

