#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python
checkfile="/home/endaga/alert_statuses/voltage.txt"
touch $checkfile
#checkfile must exist or script won't run. If it doesn't exist, will run next time.

alertnumber=700;
arduinoport=/dev/ttyACM0;

prev_volt=$(cat $checkfile);

python read_voltage_arduino.py "$arduinoport" > "$checkfile";
volt=$(cat $checkfile);

if [ -z "$prev_volt" ]
then
	echo checkfile created;
	echo 12 > $checkfile;
elif (( $(echo "$volt <= 11" | bc -l) )) && (( $(echo "$prev_volt > 11" | bc -l) ))
then
    echo Low voltage alert run;
	python /usr/share/freeswitch/scripts/alert.py "$alertnumber";
	echo $volt > $checkfile;
elif (( $(echo "$volt >= 11" | bc -l) )) && (( $(echo "$prev_volt <= 11" | bc -l) ))
then
    echo Voltage ok alert run;
	python /usr/share/freeswitch/scripts/alert.py "$alertnumber";
	echo $volt > $checkfile;
else
	echo same state;
fi
