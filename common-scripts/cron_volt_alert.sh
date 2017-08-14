#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python
checkfile="/home/endaga/alert_statuses/voltage.txt"
touch $checkfile
#checkfile must exist or script won't run. 

#config
alertnumber=700;
arduinoport=/dev/ttyACM0;
alertscript=/usr/share/freeswitch/scripts/alert_nocall.py;
lowvoltage=9;

prev_volt=$(cat $checkfile);
#prev_volt=12;
#echo 10.5 > "$checkfile";
#python read_voltage_arduino.py "$arduinoport" >> "$checkfile";
python read_voltage_arduino.py "$arduinoport" "$checkfile";
volt=$(cat $checkfile);
echo prev volt $prev_volt;
echo volt $volt;

if [ -z "$prev_volt" ]
then
    if (( $(echo "$volt <= $lowvoltage" | bc -l) ))
    then
        echo No prev voltage. Low voltage alert run;
        python "$alertscript" "$alertnumber" "BABALA: MABABA ANG BOLTAHE NG BATERYA. Ito ay $volt volts na lamang. I-charge ang baterya upang mapigilang mamatay ang buong sistema matapos ang ilang oras."
    else
        echo No prev voltage. No low voltage alert;
    fi
else
    if (( $(echo "$volt <= $lowvoltage" | bc -l) )) && (( $(echo "$prev_volt > $lowvoltage" | bc -l) ))
    then
        echo Low voltage alert run;
        python "$alertscript" "$alertnumber" "BABALA: MABABA ANG BOLTAHE NG BATERYA. Ito ay $volt volts na lamang. I-charge ang baterya upang mapigilang mamatay ang buong sistema matapos ang ilang oras."
    elif (( $(echo "$volt >= $lowvoltage" | bc -l) )) && (( $(echo "$prev_volt <= $lowvoltage" | bc -l) ))
    then
        echo Voltage ok alert run;
        python "$alertscript" "$alertnumber" "Boltahe OK: $volt Volts.";
    else
        echo same state;
    fi
fi

