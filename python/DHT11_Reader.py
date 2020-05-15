#Import Libraries we will be using
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import sqlite3

#Create a Connection object 
con = sqlite3.connect('../EnvironmentMonitor.db')

#Cursor object to perform SQL commands
cur = con.cursor()

#Assign GPIO pins
tempPin = 26

#Dummy time for first iteration of the loop
oldTime = 60

#Time Variables
currentDate = time.strftime("%Y-%m-%d")
currentTime = time.strftime("%H:%M:%S")

#Initialize GPIO
GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM)

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT11
def readF(tempPin):
        humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
        temperature = temperature * 9/5.0 +32
        if humidity is not None and temperature is not None:
                tempFahr = '{0:0.1f}'.format(temperature)
		humPercent = '{0:0.1f}'.format(humidity)
        else:
                print('Failed to get reading.')
        return tempFahr, humPercent
try:
                while True:

			if time.time() - oldTime > 59:
                        	temp, hum =readF(tempPin)
				currentTime=time.strftime("%H:%M:%S")
                        	cur.execute("insert into DHT11_TempLog values(?,?)", (time.strftime('%Y-%m-%d %H:%M:%S'), temp))
                        	cur.execute("insert into DHT11_HumidityLog values(?,?)", (time.strftime('%Y-%m-%d %H:%M:%S'), hum))
				con.commit()
				print("_______________")
				print("DATE / TIME")
				print(currentDate)
				print(currentTime)
				print("_______________")
				print("TEMP / HUM (outside plant holder)")
				print(temp + ' *F')
				print(hum + '% Humidity')
				print("_______________")
				print("\n")
				oldTime = time.time()
				currentTime=time.strftime("%H:%M:%S")

except KeyboardInterrupt:
	con.close()
	print('\nDHT11 Testing: SUCCESS!')
        GPIO.cleanup()

