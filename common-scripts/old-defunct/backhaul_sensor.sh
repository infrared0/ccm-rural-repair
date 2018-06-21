#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python

# config moved to systemd environment file
python "$backhaul_alert_script" "$serial_port" "$backhaul_state_file" 

