#Import Libraries we will be using
import RPi.GPIO as GPIO
import Adafruit_DHT

#Assign GPIO pins
tempPin = 26

#Initialize GPIO
GPIO.setwarnings(False);
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

except KeyboardInterrupt:
	print('\nSensational Sensing!')
	GPIO.cleanup()
