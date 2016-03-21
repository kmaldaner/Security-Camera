# Security-Camera
Security camera for my apartment. I will be using a Raspberry Pi 1 Model B computer and the Raspberry Pi NoIR camera module. 
I am using IR LEDs as the flash and a magnetic door trigger to activate the camera.

## Raspberry Pi Setup

I am using the Raspbian Jessie Lite on a 4GB SD card. Ensure you have the camera module enabled and all apropriate 'updates' and 'upgrades'.

On the GPIO  board I am using pin 18 for control the LEDs and pin 23 to detect the door switch.

## Python Setup
The packages I installed are:

- python-picamera
