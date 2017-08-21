#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python
checkfile=/home/endaga/alert_statuses/voltage.txt;
touch $checkfile
#checkfile must exist or script won't run. 

echo Running volt alert

#config
alertnumber=700;
arduinoport=/dev/ttyACM0;
arduinoscript=/usr/share/freeswitch/scripts/read_voltage_arduino.py;
alertscript=/usr/share/freeswitch/scripts/alert.py;
alertgroup=$1;

lowvoltage=11;

prev_volt=$(cat $checkfile);
#prev_volt=12;
#echo 10.5 > "$checkfile";
python "$arduinoscript" "$arduinoport" "$checkfile";
PID=$!;
wait $PID;
volt=$(cat $checkfile);
#volt=12;
echo prev volt $prev_volt;
echo volt $volt;

warningmsg="BABALA: MABABANG BOLTAHE. Ang boltahe ng baterya ay $volt V na lang. I-charge ang baterya upang mapigilang mamatay ang buong sistema matapos ang ilang oras."
okmsg="Boltahe OK: $volt Volts."

if [ -z "$prev_volt" ]
then
    if (( $(echo "$volt <= $lowvoltage" | bc -l) ))
    then
        echo No prev voltage. Low voltage alert run;
        python "$alertscript" "$alertnumber" "$alertgroup" "$warningmsg"
    else
        echo No prev voltage. No low voltage alert;
    fi
else
    if (( $(echo "$volt <= $lowvoltage" | bc -l) )) && (( $(echo "$prev_volt > $lowvoltage" | bc -l) ))
    then
        echo Low voltage alert run;
        python "$alertscript" "$alertnumber" "$alertgroup" "$warningmsg"
    elif (( $(echo "$volt >= $lowvoltage" | bc -l) )) && (( $(echo "$prev_volt <= $lowvoltage" | bc -l) ))
    then
        echo Voltage ok alert run;
        python "$alertscript" "$alertnumber" "$alertgroup" "$okmsg";
    else
        echo same state;
    fi
fi

