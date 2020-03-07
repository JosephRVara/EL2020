#Import Libraries we will be using
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
#Assign GPIO pins
LEDPin = 17
tempPin = 26
#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT11
#LED Variables--------------------------------------------------------
#Duration of each Blink
blinkDur = .1
#Number of times to Blink the LED
blinkTime = 7
#---------------------------------------------------------------------
#Initialize the GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPin,GPIO.OUT)

def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin,False)
	time.sleep(blinkDur)

def readF(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor,tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		if temperature <78.0:
			print('______________')
			print('LED OFF')
			print('TEMP SENS OFF')
			print('______________')
		if temperature >=78.0:
			for i in range (blinkTime):
				print('Temperature: {0:0.1f}*F || Humidity: {1:0.1f}%'.format(temperature, humidity))
				oneBlink(LEDPin)
				time.sleep(.2)
	else:
		print('Error Reading Sensor')

try:
	while True:
		readF(tempPin)
except KeyboardInterrupt:
	os.system('clear')
	print('Thanks for Blinking and Thinking!')
	GPIO.cleanup()
