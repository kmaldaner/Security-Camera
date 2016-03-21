def take_photo():
	import picamera
	import datetime

	camera = picamera.PiCamera()
	
	camera.hflip = True
	camera.vflip = True

	name = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + ".jpg"
	camera.capture(name)
	
	return name

