#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python

#config
alertnumber=600;
alertscript=/usr/share/freeswitch/scripts/alert_nocall.py;
lowmemory=1000;

memloc="/proc/meminfo"
memfree=$(cat $memloc | grep "MemAvailable" | awk '{print $2}')
warning=$[$memfree<=$lowmemory]

if (($warning))
then
    python "$alertscript" "$alertnumber" "BABALA: MABABA NA ANG MEMORY NG SYSTEM. $memfree Mb na lamang ang natitira sa memory ng BTS computer. Magbura ng ilang di mahalagang bagay upang magkaron ng sapat na memory ang system.";
fi
