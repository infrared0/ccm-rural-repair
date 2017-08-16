# python script to trigger warning text by calling a dialplan

import sys
import json
from os import system

ALERT_NUMBER = sys.argv[1]
ALERT_GROUP = sys.argv[2]
MSG = sys.argv[3]

def python_alert(ALERT_NUMBER, ALERT_GROUP, MSG):
    '''
    Usage: python alert.py ALERT_NUMBER ALERT_GROUP "MESSAGE"
    Alert number is the number you're sending from
    Alert group is "camped", "all", "samahan", or "pamana"
    Message to send must be in quotes
    '''
    if ALERT_GROUP=='samahan':
        recipients_file = "/home/endaga/alert_recipients/samahan.json"
    elif ALERT_GROUP=='pamana':
        recipients_file = "/home/endaga/alert_recipients/pamana.json"
    elif ALERT_GROUP=='all':
        recipients_file = "/home/endaga/alert_recipients/all.json"
    elif ALERT_GROUP=='camped':
        recipients_file = "/home/endaga/alert_recipients/camped.json"
    else:
        recipient = ALERT_GROUP        # assume is a number
        cmd = 'fs_cli -x "python VBTS_Send_SMS %s|%s|%s"' % (recipient, ALERT_NUMBER, MSG)
        system(cmd) 
        return "alert run"

    with open(recipients_file, 'r+') as f:
        alert_recipients = json.load(f)
        for recipient in alert_recipients:
            cmd = 'fs_cli -x "python VBTS_Send_SMS %s|%s|%s"' % (recipient, ALERT_NUMBER, MSG)
            system(cmd) 

    return "alerts run"

python_alert(ALERT_NUMBER, ALERT_GROUP, MSG)
