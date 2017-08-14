# Copyright (c) 2016-present, Facebook, Inc.
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant 
# of patent rights can be found in the PATENTS file in the same directory.

from freeswitch import consoleLog

import subprocess
import serial

ardSerial = serial.Serial("/dev/ttyACM0", 9600)
low_voltage = 11

def python_get_volt():
    prevVoltage = 0
    steadyCount = 0
    totalCount = 0 

    while True:
        totalCount += 1
        rawVoltage = ardSerial.readline()
        readVoltage = rawVoltage.strip()
        voltage = float(readVoltage)
        if voltage == prevVoltage:
            steadyCount += 1
        if steadyCount >= 4:
            finalVoltage = voltage
            break
        elif totalCount >= 30:
            finalVoltage = voltage
            break
        else:
            prevVoltage = voltage

    if finalVoltage <= low_voltage:
        warning_status = "BABALA: MABABA ANG BOLTAHE. Ang boltahe ng baterya ay mababa. Ito ay %s volts na lamang. I-charge ang baterya upang mapigilang mamatay ang buong sistema matapos ang ilang oras." % finalVoltage
    else:
        warning_status = "Boltahe OK: %s V." % finalVoltage
    return warning_status

def chat(message, placeholder):
    res = python_get_volt() 
    consoleLog('info', "Checking battery voltage: %s" % res)
    message.chat_execute('set', '_localstr=%s' % res)

def fsapi(session, stream, env, placeholder):
    res = python_get_volt()
    if isinstance(session, str):
        # we're in the FS CLI, so no session object
        consoleLog('info', "No session; otherwise would set _localstr=%s" % res)
    else:
        session.execute("set", "_localstr=%s" % res)

def handler(session, placeholder):
    res = python_get_volt()
    session.execute("set", "_localstr=%s" % res)
