# python script to trigger warning text by calling a dialplan

import sys
import call_esl
import json
from os import system

ALERT_NUMBER = sys.argv[1]
MSG = sys.argv[2]

def python_alert(ALERT_NUMBER, MSG):
    with open("/home/endaga/alert_recipients/alert_recipients.json", 'r+') as f:
        alert_recipients = json.load(f)
        for recipient in alert_recipients:
            cmd = 'fs_cli -x "python VBTS_Send_SMS %s|%s|%s"' % (recipient, ALERT_NUMBER, MSG)
            system(cmd) 
    return "alerts run"

python_alert(ALERT_NUMBER, MSG)
