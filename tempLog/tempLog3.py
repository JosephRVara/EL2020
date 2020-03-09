#Import Libraries we will be using
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
#import sqlite3

#Create a Connection object
#conn = sqlite3.connect('tempLog.db')

#Cursor object to perform SQL commands
#csr = conn.cursor()

#Assign GPIO pins
tempPin = 26
RedPin = 17
GreenPin = 13

#Time Variables
currentDate = time.strftime("%Y-%m-%d")
currentTime = time.strftime("%H:%M:%S")

#Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GreenPin,RedPin, GPIO.OUT)

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
                while True:
                        temp, hum =readF(tempPin)
                        print(temp)
                        print(hum)
                        print(currentDate)
                        print(currentTime)
                       # csr.execute('insert into tempLog (date, time, temp, hum) values(?,?,?,?)', (currentDate, currentTime, temp, hum))
                       # conn.commit()
			time.sleep(2)
			if temp >=70 and temp <=80:
				GPIO.output(GreenPin,True)
				GPIO.output(RedPin,False)
			elif temp <70 or temp >80:
				GPIO.output(GreenPin,False)
				GPIO.output(RedPin,True)

except KeyboardInterrupt:
 #       conn.close()
        print('\nSensational Sensing!')
        GPIO.cleanup()
