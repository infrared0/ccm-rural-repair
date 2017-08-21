#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/python

phonenumber=639360101920;
alertnumber=900;

#fs_cli -x "python VBTS_Send_SMS '$phonenumber'|'$alertnumber'|'4:56PM: Ang maintenance ay maaaring isagawa mula 8AM hanggang 6PM. Salamat po!'";

fs_cli -x "python VBTS_Send_SMS '$phonenumber'|'$alertnumber'|'5:30PM: Paumanhin sa abala. Magkakaroon ng system maintenance. Pansamantalang mapuputol ang VBTS network sa loob ng 0.5 oras.'";

#fs_cli -x "python VBTS_Send_SMS '$phonenumber'|'$alertnumber'|'4:56PM: Ang maintenance ay maaaring isagawa mula 8AM hanggang 6PM. Salamat po!'";
