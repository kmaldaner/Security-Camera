import os
import RPi.GPIO as GPIO
from take_photo import take_photo
from send_email import send_email

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
