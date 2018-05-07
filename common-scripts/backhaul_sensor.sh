#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python

###Config

#alertscript=/usr/share/freeswitch/scripts/arduino_write_backhaul.py;
alertscript=/home/infrared/Research/ccm-rural-repair/common-scripts/arduino_write_backhaul.py;
serialport=/dev/ttyACM0;

python "$alertscript" "$serialport" &

