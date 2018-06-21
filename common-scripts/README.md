Includes Python 2.7 and bash scripts that run when called by a chatplan or dialplan.

The "arduino" directory contains the python scripts that send and receive data to and from the arduino. In the latest version these are run via systemd.

The "sms-utilities" directory contains scripts for sending automated one-off texts to specific recipients or a group of recipients (including all camped subscribers). It also contains other helpful scripts including getting all camped subscribers.

The "filipino-freeswitch-python" directory contains the python scripts called by the freeswitch chatplans which handle requests for sensor readings (such as voltage, backhaul link state, etc.) or enrollment in automated sensor-based alerts. These messages are in Filipino by default. There are English versions in "english-freeswitch-python."
It contains the following files:

VBTS_Check_Temp.py: Python script called by chatplan when a text is sent to the temperature check request number. 
Currently the request number is hardcoded to 400.

VBTS_Check_Backhaul.py: Python script called by a chatplan when a text (containing any content) is sent to the backhaul check request phone number. 
Currently the request number is hardcoded to 500.

VBTS_Check_Mem.py: Python script called by chatplan when a text is sent to the memory check request number.
Currently the request number is hardcoded to 600.

VBTS_Enroll_Alert.py: Python script called by chatplan when a text is sent to the enrollment number for alerts. 
Currently the enrollment number is hardcoded to 900.

The "cronjobs" directory under "old-defunct" contains the old version of the code in which a separate cron job was run for each sensor. It contains the following files:

cron_backhaul_alert.sh: bash script (called as a cron job) to check internet connectivity via a call to the curl command; if curl fails, a text message is sent to the "alert numbers." Default crontab specifies a check every minute.

cron_mem_alert.sh: bash script (called as a cron job) to check the amount of available memory and send a text message warning if it is less than 1 Mb. Default crontab checks every minute.

cron_temp_alert.sh: bash script (called as a cron job) to check cpu temp and send a text message warning if it is over 70C. Default crontab checks every 5 minutes. 
