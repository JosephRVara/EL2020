#Import libraries
import RPi.GPIO as GPIO
import time
import os

#Initialize the GPIO
GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

#This function will make the light blink once
def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(1)
	GPIO.output(pin,False)
	time.sleep(1)
try:

	while True:
		for i in range(10):
			blinkOnce(17)

except KeyboardInterrupt:
	os.system('clear')
	print('Thanks for Blinking and Thinking!')

#Cleanup the GPIO when done
GPIO.cleanup()
