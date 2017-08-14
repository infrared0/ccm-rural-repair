# python script to trigger warning text by calling a dialplan

import sys
import call_esl
import json


ALERT_DIAL_NUMBER = sys.argv[1]

def python_alert(ALERT_DIAL_NUMBER):
    with open("/home/endaga/alert_recipients/alert_recipients.json", 'r+') as f:
        alert_recipients = json.load(f)
        for recipient in alert_recipients:
            call_esl.python_originate(recipient, ALERT_DIAL_NUMBER)
    return "alerts run"

python_alert(ALERT_DIAL_NUMBER)
