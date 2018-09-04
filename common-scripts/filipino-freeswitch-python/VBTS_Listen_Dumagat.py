# Copyright (c) 2016-present, Facebook, Inc.
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant 
# of patent rights can be found in the PATENTS file in the same directory.

from freeswitch import consoleLog
import os.path
import callback

# shortcode for recording is 998, listening is 999
LISTEN = "999"
RECORD = "998"
# recordings will be saved in /home/endaga/recordings/
RECORDING_DIR = "/home/endaga/recordings/"
# recording that plays on a failed lookup will be in /home/endaga/recordings/lookup_fail.wav
FAIL_FN = RECORDING_DIR + "lookup_fail.wav"
# on the chatplan side, the keyword texted to 998/999 is "YOUR_CODE" (case insensitive)
# recorded files are saved in /home/endaga/recordings/YOUR_CODE.wav

def recording_lookup(code):
    fn = RECORDING_DIR + str(code) + ".wav"
    if os.path.isfile(fn):
        return fn
    else:
        return FAIL_FN

def chat(message, args):
    recipient = args[0]
    code = args[1]
    fn = recording_lookup(code) 
    #send the filename to play back
    callback.python_callback(LISTEN, recipient, fn)
    consoleLog('info', "Recording lookup: " fn + "\n")
    message.chat_execute('set', 'play_fn=%s' % fn)

def fsapi(session, stream, env, args):
    recipient = args[0]
    code = args[1]
    res = recording_lookup(code) 
    if isinstance(session, str):
        # we're in the FS CLI, so no session object
        consoleLog('info', "No session; otherwise would set _localstr=%s" % res)
    else:
        session.execute("set", "_localstr=%s" % res)

def handler(session, args):
    recipient = args[0]
    code = args[1]
    res = recording_lookup(code) 
    session.execute("set", "_localstr=%s" % res)
    
