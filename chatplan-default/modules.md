**cardboard with polaroid photos with problem codes?? display in tree format?

001 text "info" to 777
(text a component number or word to a number to get the list of predicted problems per component and how to diagnose, each has a code)

Please text the following numbers to find out more about each component of the system.
Batteries, inverter, power strip- 100 text "pow"
BTS- 200 text "bts"
Antennas and their cables- 300 ant
Router and ethernet cables- 400 rou
Vsat modem and dish- 500 sat
Computer- 600 com
Solar panels and solar charge controller- 700 sol

002 text "help" to 777

Please text the following numbers for a how-to guide for the following.
--one or more components are powered off. --> go to debugging for the power strip and/or the particular component. 013 1
--not able to reach numbers outside diotorin 011 2
--there is signal but not able to connect calls 012 3
--there is no signal 4
--other specific problem 5
--how to use a multimeter- 020 6

Batteries, inverter, power strip- 100
--how to check for correct functionality (normal state appearance) 10
--list of how to guides 110 text 11
---how to assemble/disassemble 112 13
--list of possible problems and what to do 120 12
---too much current draw (serious)- timer burning, inverter beeping, power strip burning/not able to turn on (fuse blown) 121 14
---battery died 122 15
---power strip malfunctioning 123 16

BTS- 200
--how to check for correct functionality (normal state appearance) 201 text 20
--list of how to guides 210 21
---how to reboot 211 23
---how to disconnect/reconnect 212 24
--list of possible problems and how to check for them 220 "prob" 22
---antenna loose or damaged 221 (high vswr) 25
---high temperature --> either shade it, or possible hardware malfunction and either power brick or nuranneeds replacement. 222 26
---fails to power on --> if not power cable failure, either power brick or nuran needs replacement. 223 27
---other blink codes for nuran box? 224 28

Antennas and their cables- 300
--how to check for correct functionality (normal state appearance) 30
--list of how to guides 310 31
---how to assemble/disassemble 311 33
--list of possible problems and how to check for them 320 32
---antenna turned (decreased signal, looks turned) 321 34
---antenna cable detached (no signal, nuran error codes) 322 35
---antenna damaged (no signal, nuran error codes) 323 36

Router and ethernet cables- 400
--how to check for correct functionality (normal state appearance) 401 40
--list of how to guides 410 41
---how to reboot 411 43
---how to hook up and detach cables 412 44
--list of possible problems and how to check for them 420 42
---router software error, needs reboot 421 45

Vsat modem and dish- 500
--how to check for correct functionality (normal state appearance) 501 50
--list of how to guides 510 51
---how to reboot 511 53
---how to hook up and detach cables 512 54
--list of possible problems and how to check for them 520 52
---vsat firmware/software error, needs reboot 521 55
---satellite connection not available due to bad weather 522 56
---dish misaligned 523 57

Computer- 600
--how to check for correct functionality (normal state appearance) 601 60
--list of how to guides 610 61
---how to reboot 611 63
---how to hook up and detach cables 612 64
--list of possible problems and how to check for them 620 62
---software error, needs reboot 621 65

Solar panels and solar charge controller- 700
--how to check for correct functionality (normal state appearance) 70
--list of how to guides 710 71
---how to hook up and detach cables 711 73
---how to turn on solar charge controller 712 74
--list of possible problems and how to check for them 720 72
---solar charge controller malfunction 721 75
---solar panels shaded 722 76




-------------------------------
Brainstorm:
the problem is that a picture is worth a thousand words.
text an image code to rcv a link to a video or a picture.
there should be a series of pictures in order of importance (or usefulness?)

maybe have a screen available that will display these pictures in response to the messages?

text a problem code to enter troubleshooting for that problem. these should be "detectable problems" including the blink codes
