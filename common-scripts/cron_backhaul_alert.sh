#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python
checkfile="/home/endaga/alert_statuses/internet_status.txt"
touch $checkfile
#checkfile must exist or script won't run. If it doesn't exist, will run next time.

echo Running backhaul alert

#config
alertnumber=500;
alertscript=/usr/share/freeswitch/scripts/alert.py;
alertgroup=$1;

curl ccm.cs.washington.edu > /dev/null 2>&1;
disconnected=$?;
prev_disconnected=$(cat $checkfile);

alertmsg="BABALA: HINDI KONEKTADO SA INTERNET. Hindi makatatawag o makapagpadala ng text sa ibang networks sa labas ng komunidad. Tignan ang koneksyong ng BTS.";
okmsg="Konektado sa internet.";

if [ -z "$prev_disconnected" ]
then
    echo checkfile created;
    echo 0 > $checkfile;
elif [ $disconnected -gt 0 ] && [ "$prev_disconnected" -eq 0 ] 
then
    echo Disconnected alert run;
    python "$alertscript" "$alertnumber" "$alertgroup" "$alertmsg";
    echo 1 > $checkfile;
#    echo checkfile 1 written
elif [ $disconnected -eq 0 ] && [ "$prev_disconnected" -eq 1 ]
then
    echo Reconnected alert run;
    python "$alertscript" "$alertnumber" "$alertgroup" "$okmsg";
    echo 0 > $checkfile;
#    echo checkfile 0 written
else
    echo same state;
#    echo 0 > $checkfile
fi
