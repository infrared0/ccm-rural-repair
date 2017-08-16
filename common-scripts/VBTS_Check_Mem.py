# Copyright (c) 2016-present, Facebook, Inc.
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant 
# of patent rights can be found in the PATENTS file in the same directory.

from freeswitch import consoleLog

import subprocess
import os

def python_get_mem():
    memory_loc = "/proc/meminfo"
    low_memory_kb = 1000 #1000 kb of memory left
    raw_out = subprocess.check_output(["cat", memory_loc]).split()
    memory_available_kb = raw_out[7]
    integer_memory_kb = int(memory_available_kb)
    integer_memory_kb = 923
    memory_available_mb = integer_memory_kb/1000.0

    if integer_memory_kb <= low_memory_kb:
        warning_status = "BABALA: MABABA MEMORY NG BTS COMPUTER. Magbura ng ilang di mahalagang bagay upang magkaron ng sapat na memory."
    else:
        warning_status = "BTS computer memory OK."
    return "%s %s Mb memory." % (warning_status, memory_available_mb)

def chat(message, placeholder):
    res = python_get_mem() 
    memory_loc = "/proc/meminfo"
    consoleLog('info', "Checking available mem: %s" % res)
    message.chat_execute('set', '_localstr=%s' % res)

def fsapi(session, stream, env, placeholder):
    res = python_get_mem()
    if isinstance(session, str):
        # we're in the FS CLI, so no session object
        consoleLog('info', "No session; otherwise would set _localstr=%s" % res)
    else:
        session.execute("set", "_localstr=%s" % res)

def handler(session, placeholder):
    res = python_get_mem()
    session.execute("set", "_localstr=%s" % res)
