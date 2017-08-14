# Copyright (c) 2016-present, Facebook, Inc.
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant 
# of patent rights can be found in the PATENTS file in the same directory.

from freeswitch import consoleLog

import subprocess
import json

ENROLL_FILE_PATH = "/home/endaga/alert_recipients/alert_recipients.json"

def python_enroll(enroll_number):
    # NOTE: this function requires a file of the form alert_recipients/alert_recipients.json with a dictionary in it to run correctly
    with open(ENROLL_FILE_PATH, 'r+') as f:
        recipients = json.load(f)    # recipients is a dictionary for fast checking
         
    if enroll_number not in recipients:
        recipients[enroll_number] = 0
        with open(ENROLL_FILE_PATH, 'w') as f:
            json.dump(recipients, f)
        return "Mabuhay! Ito ang cell tower alert service. I-text ang CHECK at ipadala sa 400 upang malaman ang temperatura ng sistema, sa 500 upang malaman kung konektado ito sa internet, sa 600 upang malaman ang computer memory, o sa 700 upang malaman ang boltahe ng baterya. Kayo rin ay makatatanggap ng mensaheng pang- abiso sa inyong cellphone."
    else:
        return "Number %s enrolled." % enroll_number

def chat(message, number):
    res = python_enroll(number) 
    consoleLog('info', "Enrolling number to receive alerts, sending text: %s" % res)
    message.chat_execute('set', '_localstr=%s' % res)

def fsapi(session, stream, env, number):
    res = python_enroll(number)
    if isinstance(session, str):
        # we're in the FS CLI, so no session object
        consoleLog('info', "No session; otherwise would set _localstr=%s" % res)
    else:
        session.execute("set", "_localstr=%s" % res)

def handler(session, number):
    res = python_enroll(number)
    session.execute("set", "_localstr=%s" % res)
