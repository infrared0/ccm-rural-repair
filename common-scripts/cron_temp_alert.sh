#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python

#config
alertnumber=400;
alertscript=/usr/share/freeswitch/scripts/alert_nocall.py;
hightemp=70000;

temp=$(</sys/class/thermal/thermal_zone0/temp)
warning=$[$temp>=$hightemp]
if (($warning))
then
    python "$alertscript" "$alertnumber" "BABALA: Mataas ang temperatura ng sistema. Maaari itong mamatay ano mang oras. Ang temperatura ng BTS computer ay $temp degrees C."
fi
