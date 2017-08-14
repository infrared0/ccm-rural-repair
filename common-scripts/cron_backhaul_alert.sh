#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python
checkfile="/home/endaga/alert_statuses/internet_status.txt"
touch $checkfile
#checkfile must exist or script won't run. If it doesn't exist, will run next time.

alertnumber=500;

curl ccm.cs.washington.edu > /dev/null 2>&1;
disconnected=$?;
prev_disconnected=$(cat $checkfile);

#DEBUG
#echo Disconnected is $disconnected;
#echo Prev_disconnected is $prev_disconnected;

if [ -z "$prev_disconnected" ]
then
	echo checkfile created
	echo 0 > $checkfile
elif [ $disconnected -gt 0 ] && [ "$prev_disconnected" -eq 0 ] 
then
#        echo Disconnected alert run;
	python /usr/share/freeswitch/scripts/alert.py "$alertnumber";
	echo 1 > $checkfile
#        echo checkfile 1 written
elif [ $disconnected -eq 0 ] && [ "$prev_disconnected" -eq 1 ]
then
#        echo Reconnected alert run;
	python /usr/share/freeswitch/scripts/alert.py "$alertnumber";
	echo 0 > $checkfile
#        echo checkfile 0 written
else
	echo same state;
#	echo 0 > $checkfile
fi
