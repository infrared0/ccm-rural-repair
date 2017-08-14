#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python
checkfile="/home/endaga/alert_statuses/voltage.txt"
touch $checkfile
#checkfile must exist or script won't run. If it doesn't exist, will run next time.

alertnumber=700;
arduinoport=/dev/ttyACM0;
lowvoltage=11;
#prev_volt=$(cat $checkfile);
prev_volt=12;
echo prev volt $prev_volt;
python read_voltage_arduino.py "$arduinoport" > "$checkfile";
volt=$(cat $checkfile);
echo volt $volt;

if [ -z "$prev_volt" ]
then
    if (( $(echo "$volt <= $lowvoltage" | bc -l) ))
    then
        echo No prev voltage. Low voltage alert run;
        python /usr/share/freeswitch/scripts/alert.py "$alertnumber";
    else
        echo No prev voltage. No low voltage alert;
    fi
else
    if (( $(echo "$volt <= $lowvoltage" | bc -l) )) && (( $(echo "$prev_volt > $lowvoltage" | bc -l) ))
    then
        echo Low voltage alert run;
        python /usr/share/freeswitch/scripts/alert.py "$alertnumber";
    elif (( $(echo "$volt >= $lowvoltage" | bc -l) )) && (( $(echo "$prev_volt <= $lowvoltage" | bc -l) ))
    then
        echo Voltage ok alert run;
        python /usr/share/freeswitch/scripts/alert.py "$alertnumber";
    else
        echo same state;
    fi
fi

