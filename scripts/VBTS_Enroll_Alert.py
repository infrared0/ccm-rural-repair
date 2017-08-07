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
        recipients = json.load(f)    # recipients is a dictionary
         
    if enroll_number not in recipients:
        recipients[enroll_number] = 0
        with open(ENROLL_FILE_PATH, 'w') as f:
            json.dump(recipients, f)
        return "Number %s enrolled." % enroll_number
    else:
        return "Number %s already enrolled to receive alerts." % enroll_number

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
