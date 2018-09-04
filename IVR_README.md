Current attempt is to implement an IVR system that allows you to make and retrieve recordings.
The IVR system can be reached at the short code 990. (It is triggered by the dialplan that matches 990.)
If you select the record option from the IVR, it hopefully transfers you to the recording dialplan that matches the shortcode 991.
I think the config for the IVR (ivr.conf.xml) should be placed in /etc/freeswitch/ivr_menus.

The sounds for the IVR menu are stored at /home/endaga/menu_sounds/.

Recordings are stored at /home/endaga/recordings/.
Each recording is assigned a number which is its filename (e.g. 1.wav 2.wav etc.)
Also in /home/endaga/recordings is a required file called recording_dict.json which is a dictionary storing these recording numbers as its values, and a reference string as its keys (which might later be useful for sms-based retrieval or something). 
The reference string is the same as the number by default.
