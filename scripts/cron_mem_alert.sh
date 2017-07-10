#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python

mem_loc="/proc/meminfo"
mem_free=$(cat $mem_loc | grep "MemAvailable" | awk '{print $2}')
warning=$[$mem_free<=1000]
if (($warning))
then
	python /usr/share/freeswitch/scripts/alert.py 600
fi
