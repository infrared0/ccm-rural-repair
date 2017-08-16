#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python

#config
alertnumber=600;
alertscript=/usr/share/freeswitch/scripts/alert.py;
alertgroup=639360101920;
lowmemory=2000; # in kb

memloc="/proc/meminfo"
memfree=$(cat $memloc | grep "MemAvailable" | awk '{print $2}')
memfree=1500
memmb=$(echo "$memfree/1000" | bc)

warningmsg="BABALA: MABABA MEMORY NG SYSTEM. $memmb Mb na lamang ang natitira sa memory ng BTS computer. Magbura ng ilang di mahalagang bagay upang magkaron ng sapat na memory."

warning=$[$memfree<=$lowmemory]

if (($warning))
then
    python "$alertscript" "$alertnumber" "$alertgroup" "$warningmsg";
fi
