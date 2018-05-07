#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python

#config

#alertscript=/usr/share/freeswitch/scripts/write_state_arduino.py;

alertscript=/home/infrared/Research/ccm-rural-repair/common-scripts/write_state_arduino.py;
serialport=/dev/ttyACM0;
prev_disconnected=0;
disconnected=0;

while true 
do 
	# test backhaul
	curl ccm.cs.washington.edu > /dev/null 2>&1
	disconnected=$?;
	echo Current State "$disconnected";

	if [ -z "$prev_disconnected" ]
	then
	    echo prev_disconnected not initialized;
	elif [ $disconnected -gt 0 ] && [ "$prev_disconnected" -eq 0 ] 
	then
	    echo Newly disconnected;
	    python "$alertscript" "$serialport" "$disconnected";
	elif [ $disconnected -eq 0 ] && [ "$prev_disconnected" -gt 0 ]
	then
	    echo Newly reconnected;
	    python "$alertscript" "$serialport" "$disconnected";
	else
	    echo same state;
	fi
	prev_disconnected="$disconnected";

	sleep 10
done
