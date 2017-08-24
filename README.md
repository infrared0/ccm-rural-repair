# ccm-rural-repair
Additions to the Community Cellular Manager (CCM) stack that facilitate community management and maintenance.

Install instructions (temporary):

Python scripts under folder scripts go in /usr/share/freeswitch/scripts
Chatplan xml files under folder chatplan-default go in /etc/freeswitch/chatplan/default/
Dialplan xml files under folder dialplan-default go in /etc/freeswitch/dialplan/default/
Folders under the folder state-files should go as-is in the home directory (i.e. /home/endaga)
Write permissions on files that were copied from state-files to home directory should be modified via chmod 666 FILENAME
File crontab.bak should be copy pasted into the root crontab file (via sudo crontab -e)
test
