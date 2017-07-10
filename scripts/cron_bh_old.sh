#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python

curl ccm.cs.washington.edu > /dev/null 2>&1
disconnected=$?
echo Disconnected is $disconnected
if ((~$disconnected))
then
	python /usr/share/freeswitch/scripts/alert.py 700
fi
