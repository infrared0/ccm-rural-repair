#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python

#config
alertnumber=400;
alertscript=/usr/share/freeswitch/scripts/alert.py;
alertgroup=639360101920;
hightemp=70;

temp=$(</sys/class/thermal/thermal_zone0/temp);
ctemp=$(echo "$temp/1000" | bc)
warning=$[$ctemp>=$hightemp];

warningmsg="BABALA: Mataas ang temperatura ng sistema. Maaari itong mamatay ano mang oras. Ang temperatura ng BTS computer ay $ctemp degrees C.";

if (($warning))
then
    python "$alertscript" "$alertnumber" "$alertgroup" "$warningmsg";
fi
