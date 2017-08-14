# python script to trigger warning text by calling a dialplan

import sys
import call_esl
import json
from os import system

ALERT_DIAL_NUMBER = sys.argv[1]

def python_alert(ALERT_DIAL_NUMBER):
    with open("/home/endaga/alert_recipients/alert_recipients.json", 'r+') as f:
        alert_recipients = json.load(f)
        message = "12:28 PM Maedup! Ang ating network ay kasalukuyang umaandar. Kung kayo ay makatatanggap ng alert o mensahe, mangyaring ituring ito na tunay na situwasyon. Maraming Salamat."
        for recipient in alert_recipients:
            cmd = 'fs_cli -x "python VBTS_Send_SMS %s|%s|%s"' % (recipient, ALERT_DIAL_NUMBER, message)
            system(cmd) 
    return "alerts run"

python_alert(ALERT_DIAL_NUMBER)
