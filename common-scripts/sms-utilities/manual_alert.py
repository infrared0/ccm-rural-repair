from alert import python_alert
from os import system
import sys
import json

MESSAGES = 'messages.json' 

def manual_alert(alert_num, number, arg=None): 
    '''
    Usage: python manual_alert.py alert_number (or group) recipient_number arg=filepath_to_custom_message (or # hours for '001', or custom string for '000')
    There is also a messages dictionary in a json file.
    '''
    if alert_num == '400':
        cmd = "./cron_temp_alert.sh %s" % alert_num 
        system(cmd)
    elif alert_num == '500':
        cmd = "./cron_backhaul_alert.sh %s" % alert_num
        system(cmd)
    elif alert_num == '600':
        cmd = "./cron_mem_alert.sh %s" % alert_num
        system(cmd)
    elif alert_num == '700':
        cmd = "./cron_volt_alert.sh %s" % alert_num
        system(cmd)
    elif alert_num == '000':
        print arg
        python_alert(alert_num, number, arg) 
    else:
        with open(MESSAGES, 'r+') as m:
            message_dict = json.load(m)
        # read filepath
        if alert_num in message_dict:
            if alert_num == '001':
                downtime_msg = message_dict[alert_num] % arg
                print downtime_msg
                python_alert(alert_num, number, downtime_msg)
            else:
                msg = message_dict[alert_num]
                print msg
                python_alert(alert_num, number, msg)
        else:
            with open(arg, 'r+') as f:
                CUSTOM_MSG = f.read().strip()
            print CUSTOM_MSG
            python_alert(alert_num, number, CUSTOM_MSG) 
            print "custom alert run"

#MAIN

if __name__ == '__main__':

    args = sys.argv
    alert_num = args[1]
    recipient_num = args[2]
    if len(args) > 3:
        manual_alert(alert_num, recipient_num, arg=args[3])
    else:
        manual_alert(alert_num, recipient_num)
        
