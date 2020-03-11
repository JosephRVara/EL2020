#Import Libraries we will be using
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import sqlite3
import smtplib

#Create a Connection object
conn = sqlite3.connect('tempLog.db')

#Cursor object to perform SQL commands
csr = conn.cursor()

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
GPIO.setup(GreenPin,GPIO.OUT)
GPIO.setup(RedPin,GPIO.OUT)

#Number of times to Blink the LED
blinkDur = .1
blinkTime = 7

#SMTP eMail Variables
eFROM = "JosephRoccoVara@gmail.com"
eTO = "8452745839@vtext.com"
Subject = "Alert!"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

eChk = 0

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT11

def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin,False)
	time.sleep(blinkDur)

def alert(tempF):
	global eChk
	if eChk == 0:
		Text = "The monitor now indicates that the temperature is now "+str(tempF)
		eMessage = 'Subject: {}\n\n{}'.format(Subject, Text)
		server.login("JosephRoccoVara@gmail.com", "nalkmrskwwjuvrxr")
		server.sendmail(eFROM, eTO, eMessage)
		server.quit
		eChk = 1 

def readDHT(tempPin):
        humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
        temperature = temperature * 9/5.0 +32
        if humidity is not None and temperature is not None:
                tempFahr = '{0:0.1f}'.format(temperature)
                humPercent = '{0:0.1f}'.format(humidity)
        else:
                print('Failed to get reading.')
        return tempFahr, humPercent

#Dummy time for first iteration of the loop
oldTime = 60

#Read Temperature right off the bat
tempF, hum = readDHT(tempPin)

try:
                while True:
                       #Send text message alert if temperature is out of range
			if 68 <= float(tempF) <= 78:
				eChk = 0
				GPIO.output(RedPin,False)
				GPIO.output(GreenPin,True)
			else:
				GPIO.output(GreenPin,False)
				alert(tempF)
				oneBlink(redPin)

			#if loop set for ever 60 sec
			if time.time() - oldTime >59:
				tempF, humid = readDHT(tempPin)
				#Defines and executes the SQL query (tempLog is the table name is the .db)
				csr.execute("insert into tempLogLEDs values(?,?,?)",(time.strftime('%Y-%m%d %H:%M:%S'),tempF,humid))
				conn.commit()

				#Create local variable 'table', execute 
				table = conn.execute("select * from tempLogLEDs limit 5")
				os.system('clear')
				for row in table:
					print "%-30s %-20s %-20s" %(row[0], row[1], row[2])
				oldTime = time.time()
except KeyboardInterrupt:
	os.system('clear')
 	conn.close()
        print('\nTemperature Logger and Web App Exited Cleanly')
	exit(0)
        GPIO.cleanup()
