#Import libraries
import RPi.GPIO as GPIO
import time
import signal
import os

#sensor pin define
touch = 26
LED = 17

#Initialize the GPIO ports
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(touch,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#read digital touch sensor
def read_touchsensor():
	if(GPIO.input(touch)==True):
		GPIO.output(LED,True)
	else:
		GPIO.output(LED,False)
	pass

try:
	while True:
		read_touchsensor()

except KeyboardInterrupt:
	os.system('clear')
	print('Thanks for Blinking and Thinking!')
#Cleanup the GPIO when done
	GPIO.cleanup()
