#!/usr/bin/env python

"""main.py: detects the door switch and triggers both the take_photo and send_email scripts """


import os
import RPi.GPIO as GPIO
from take_photo import take_photo
from send_email import send_email

__author__= "Kyla Maldaner"
__copyright__= "Copyright 2016"
__credits__="Kyla Maldaner"

__licence__= "MIT"
__version__= "0.1"
__maintainer__= "Kyla Maldaner"
__email__= "kmaldaner@gmail.com"
__status__= "Production"

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
#	GPIO.wait_for_edge(23, GPIO.FALLING)
	name = take_photo()
	send_email(name)
	os.remove(name)
except KeyboardInterupt:
	GPIO.cleanup()
GPIO.cleanup()
