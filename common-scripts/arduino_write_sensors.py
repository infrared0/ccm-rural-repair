import serial
import sys
import subprocess
import time

def write_state_arduino(serialport, status):
    #tosend = status + ";"
    tosend = status
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

def get_memory_status():
    mem_limit = 2000
    mem_loc="/proc/meminfo"

    memfree_cmd = "echo $(cat " + mem_loc + " | grep \"MemAvailable\" | awk '{print $2}')"
    result = subprocess.check_output(memfree_cmd, shell=True)

    mem_kb = int(result)

    if mem_kb > mem_limit:
        #print "light off"
        mem_full = "0"
    else:
        #print "light on"
        mem_full = "1"

    return mem_full

def get_temp_status():
    temp_threshold = 70

    temp_cmd = "cat /sys/class/thermal/thermal_zone0/temp" 
    result = subprocess.check_output(temp_cmd, shell=True)

    temp_c = float(result)/1000

    if temp_c > temp_threshold:
        #print "light off"
        temp_high = "1"
    else:
        #print "light on"
        temp_high = "0"

    return temp_high


if __name__ == '__main__':

    SERIAL_PORT = sys.argv[1]
    serial_open = False

    backhaul_code = "b"
    backhaul_file = sys.argv[2]
    memory_code = "m"
    temperature_code = "t"

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
                backhaul_state = get_backhaul_status() + backhaul_code
                #backhaul_state = "1" + backhaul_code
                print backhaul_state
                memory_state = get_memory_status() + memory_code
                #memory_state = "1" + memory_code
                print memory_state
                temperature_state = get_temp_status() + temperature_code
                #temperature_state = "1" + temperature_code
                print temperature_state

                with open(backhaul_file, "r+") as f:
                    f.write(backhaul_state[0] + "\n") 

                write_state_arduino(ardSerial, backhaul_state)
                write_state_arduino(ardSerial, memory_state)
                write_state_arduino(ardSerial, temperature_state)

                time.sleep(10)

            except serial.serialutil.SerialException:
                ardSerial.close()
                serial_open = False
                print "Serial closed"
                time.sleep(30)

