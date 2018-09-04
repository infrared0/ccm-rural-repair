# python script to trigger calling a dialplan

import sys
from ESL import *


def python_originate(dial_number, recipient):
    con = ESLconnection("127.0.0.1", "8021", "ClueCon")
    if con.connected():
        con.api(str("originate {origination_call_id_name=%s,origination"
            "_caller_id_number=%s}sofia/internal/%s@127.0.0.1:"
            "5060 &echo" % (recipient, recipient, dial_number)))
    else: 
        Exception("ESL Connection Failed")


#DIAL_NUMBER = sys.argv[1]
#RECIPIENT = sys.argv[2]
#python_originate(DIAL_NUMBER, RECIPIENT)
