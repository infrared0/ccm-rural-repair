# Copyright (c) 2016-present, Facebook, Inc.
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant 
# of patent rights can be found in the PATENTS file in the same directory.

from freeswitch import consoleLog

import subprocess
import os
import json

MANUAL = 'sms-manual.json'

def man_lookup(code):
    with open(MANUAL, 'r+') as man:
        man_dict = json.load(man)
        return man_dict[code]

def chat(message, code):
    res = man_lookup(code) 
    consoleLog('info', "Getting manual entry for %s" % (code, res))
    message.chat_execute('set', '_localstr=%s' % res)

def fsapi(session, stream, env, code):
    res = man_lookup(code)
    if isinstance(session, str):
        # we're in the FS CLI, so no session object
        consoleLog('info', "No session; otherwise would set _localstr=%s" % res)
    else:
        session.execute("set", "_localstr=%s" % res)

def handler(session, code):
    res = man_lookup(code)
    session.execute("set", "_localstr=%s" % res)
