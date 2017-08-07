## python script to make call

from ESL import *
from core.subscriber import subscriber
from core.subscriber.base import SubscriberNotFound
import subprocess

def python_originate(alert_recipient, alert_dial_number):
    result = subprocess.check_output(['endaga_db_get', 'bts.type'])
    # openbts requires IMSI to originate
    if result == 'openbts\n':
    	try:
    	    username = str(subscriber.get_imsi_from_number(str(alert_recipient), False))
    	except SubscriberNotFound:
    	    username = ''
    # else assumed to be osmocom, which works with phone number
    else:
        username = alert_recipient
    con = ESLconnection("127.0.0.1", "8021", "ClueCon")
    if con.connected():
        con.api(str("originate {origination_call_id_name=%s,origination"
            "_caller_id_number=%s}sofia/internal/%s@127.0.0.1:"
            "5060 &echo" % (username, username, alert_dial_number)))
    else: 
        Exception("ESL Connection Failed")
