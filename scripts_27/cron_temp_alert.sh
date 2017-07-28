#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python

alertnumber=400

temp=$(</sys/class/thermal/thermal_zone0/temp)
warning=$[$temp>=70000]
if (($warning))
then
	python /usr/share/freeswitch/scripts/alert.py "$alertnumber"
fi
