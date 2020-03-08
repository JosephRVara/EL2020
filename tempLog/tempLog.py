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
		humPercent = '{0:0.1f}%'.format(humidity)
	else:
		print('Failed to get reading.')
	return tempFahr, humPercent
try:
	with open("../tempLog/tempLog.csv", "a") as log:

		while True:
			data1, data2 =readF(tempPin)
			print(data1)
			print(data2)
			log.write("{0}      {1}              {2}\n".format(time.strftime("%Y - %m - %d  %H:%M:%S"),str(data1),str(data2)))
			time.sleep(60)

except KeyboardInterrupt:
	print('\nSensational Sensing!')
	GPIO.cleanup()
