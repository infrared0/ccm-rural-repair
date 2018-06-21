## python script to make call

from ESL import *

def python_originate(alert_recipient, alert_dial_number):
    con = ESLconnection("127.0.0.1", "8021", "ClueCon")
    if con.connected():
        con.api(str("originate {origination_call_id_name=%s,origination"
            "_caller_id_number=%s}sofia/internal/%s@127.0.0.1:"
            "5060 &echo" % (alert_recipient, alert_recipient, alert_dial_number)))
    else: 
        Exception("ESL Connection Failed")

