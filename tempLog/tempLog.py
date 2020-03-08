#Import Libraries we will be using
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os

#Assign GPIO pins
tempPin = 26

#Initialize GPIO
GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM)

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT11
def readF(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}*F'.format(temperature)
	else:
		print('Failed to get reading.')
	return tempFahr

try:
	with open("../tempLog/tempLog.csv", "a") as log:

		while True:
			data = readF(tempPin)
			print (data)
			log.write("{0}      {1}\n".format(time.strftime("%Y - %m - %d  %H:%M:%S"),str(data)))

except KeyboardInterrupt:
	print('\nSensational Sensing!')
	GPIO.cleanup()
