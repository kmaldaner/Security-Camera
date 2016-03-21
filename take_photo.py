def take_photo():
	import picamera
	import datetime
	import RPi.GPIO as GPIO

	camera = picamera.PiCamera()
	
	camera.hflip = True
	camera.vflip = True

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(18,GPIO.OUT)

	name = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + ".jpg"
	camera.capture(name)
 
	GPIO.output(18,GPIO.LOW)
	
	return name

