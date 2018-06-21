from os import system
from datetime import datetime
import subprocess
import json

SOURCE_USERS = "/home/endaga/alert_recipients/all.json"
OUT_USERS = "/home/endaga/alert_recipients/camped.json"

with open(SOURCE_USERS, 'r+') as f:
    users = json.load(f)

#print "Checking who's camped at %s" % datetime.now().strftime("%m/%d/%y %I:%M%p")

camped = {}

for num in users:
    #print num
    if num[0] == '0':
        num_local = num
    else:
        num_local = '0'+num[2:]

    cmd = "fs_cli -x 'python endaga_camped %s'" % num_local
    is_camped = subprocess.check_output(cmd, shell=True).strip()

    if is_camped=='TRUE':
        camped[num]=0 
print camped

with open(OUT_USERS, 'r+') as outfile:
    json.dump(camped, outfile)
    outfile.truncate()
