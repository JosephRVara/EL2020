#Import Libraries we will be using
import RPi.GPIO as GPIO
import Adafruit_DHT
#import time
#import os

#Assign GPIO pins
tempPin = 26
#LEDPin = 27

#Initialize GPIO
GPIO.setmode(GPIO.BCM)

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT11

try:
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
		temperature = temperature * 9/5.0 +32
		if humidity is not None and temperature is not None:
			tempFahr = '{0:0.1f}*F'.format(temperature)
			print('Temperature = {0:0.1f}*F Humidity = {1:0.1f}%'.format(temperature, humidity))
		else:
			print('Failed to get reading. Try again!')
#temp,hum=[DHT.read_retry(DHT.DH11,17)]
except KeyboardInterrupt:
	GPIO.cleanup()
