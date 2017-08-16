from os import system
from datetime import datetime
import subprocess


list=[
    '09360101897',
    '09360101902',
    '09360101903',
    '09360101904',
    '09360101906',
    '09360101907',
    '09360101908',
    '09360101909',
    '09360101910',
    '09360101914',
    '09360101915',
    '09360101916',
    '09360101917',
    '09360101918',
    '09360101919',
    '09360101920',
    '09360101921',
    '09360101922',
    '09360101927',
    '09360101926',
    '09360101929',
    '09360101930',
    '09360101931',
    '09360101932',
    '09360101933'
]

print "Checking who's camped at %s" % datetime.now().strftime("%m/%d/%y %I:%M%p")

for num in list:
    cmd = "fs_cli -x 'python endaga_camped %s'" % num
    is_Camped = subprocess.check_output(cmd, shell=True)
    print "%s, %s" % (num, is_Camped)
