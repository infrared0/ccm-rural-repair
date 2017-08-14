## python script to make call

from ESL import *

osmo_sip_connector_remote_ip = "192.168.1.101"

def python_originate(alert_recipient, alert_dial_number):
    con = ESLconnection("127.0.0.1", "8021", "ClueCon")
    if con.connected():
        con.api(str("originate {origination_call_id_name=%s,origination"
            "_caller_id_number=%s}sofia/internal/%s@%s:"
            "5060 &echo" % (alert_recipient, alert_recipient, alert_dial_number, osmo_sip_connector_remote_ip)))
         
#        con.api(str("originate {origination_call_id_name=639991110005,origination"
#            "_caller_id_number=639991110005}sofia/internal/500@192.168.1.101:"
#            "5060 &echo")) #% (alert_recipient, alert_recipient, alert_dial_number)))
    else: 
        Exception("ESL Connection Failed")

