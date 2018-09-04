# python script to trigger calling a dialplan

import sys
from ESL import *


def python_callback(dial_number, recipient, play_fn):
    con = ESLconnection("127.0.0.1", "8021", "ClueCon")
    if con.connected():
        con.api(str("originate {origination_call_id_name=%s,origination"
            "_caller_id_number=%s}sofia/internal/%s@127.0.0.1:"
            "5060 &echo" % (recipient, play_fn, dial_number)))
    else: 
        Exception("ESL Connection Failed")


