# Copyright (c) 2016-present, Facebook, Inc.
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant 
# of patent rights can be found in the PATENTS file in the same directory.

from freeswitch import consoleLog

import subprocess

def python_curl():
    #if test_url == "":
    url = "https://www.ccm.cs.washington.edu"
    result = subprocess.call(["curl", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result == 0:
        return "Internet connected."
    else:
        return "Check internet connection- may be down."

def chat(message, url):
    res = python_curl() 
    url = "https://www.ccm.cs.washington.edu"
    consoleLog('info', "Checking result of curl to %s: %s" % (url, res))
    message.chat_execute('set', '_localstr=%s' % res)

def fsapi(session, stream, env, url):
    res = python_curl()
    if isinstance(session, str):
        # we're in the FS CLI, so no session object
        consoleLog('info', "No session; otherwise would set _localstr=%s" % res)
    else:
        session.execute("set", "_localstr=%s" % res)

def handler(session, url):
    res = python_curl()
    session.execute("set", "_localstr=%s" % res)
# not sure if there should be a separate handler
# not sure if I should just write to stream for fsapi
