# Copyright (c) 2016-present, Facebook, Inc.
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant 
# of patent rights can be found in the PATENTS file in the same directory.

#from freeswitch import consoleLog
import os.path
import sys
import json

# recordings will be saved in /home/endaga/recordings/
RECORDING_DIR = "/home/endaga/recordings/"
RECORD_DICT = "/home/endaga/recordings/recording_dict.json"
# recorded files are saved in /home/endaga/recordings/${rec_num}.wav

def recording_lookup():
    with open(RECORD_DICT, 'r') as f:
        record = json.load(f)
        if len(record) > 0:
            new = max(record.values()) + 1
        else:
            new = 1
        record[str(new)] = new

    with open(RECORD_DICT, 'w') as f:
        json.dump(record, f)

    return new

def chat(message):
    new = recording_lookup() 
    message.chat_execute('set', 'rec_number=%s' % new)
    rec_message = "Your recording is number %s. You can enter this number to listen to the recording." % new
    message.chat_execute('set', 'rec_message=%s' % )
    consoleLog('info', "Recording will be made at " + RECORDING_DIR + str(new) + ".wav \n")

def fsapi(session, stream, env):
    res = recording_lookup() 
    if isinstance(session, str):
        # we're in the FS CLI, so no session object
        consoleLog('info', "No session; otherwise would set _localstr=%s" % res)
    else:
        session.execute("set", "_localstr=%s" % res)

def handler(session):
    res = recording_lookup() 
    session.execute("set", "_localstr=%s" % res)
    

##################
#if __name__=="__main__":
#    #arguments: recipient, code
#    print "lookup 1", recording_lookup()
#    print "lookup 2", recording_lookup()
#    print "lookup 3", recording_lookup()
