#Import Libraries we will be using
import RPi.GPIO as GPIO
import time
import sqlite3
import os
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#Create a Connection object 
con = sqlite3.connect('EnvironmentMonitor.db')

#Cursor object to perform SQL commands
cur = con.cursor()

#Dummy time for first iteration of the loop
oldTime = 60

#Time Variables
currentDate = time.strftime("%Y-%m-%d")
currentTime = time.strftime("%H:%M:%S")

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

print('Reading MCP3008 values, press Ctrl-C to quit...')

# Main program loop.
try:
	while True:

		if time.time() - oldTime > 59:
			waterLev = mcp.read_adc(0)
			photoSens = mcp.read_adc(1)
			waterPercentage = round(((waterLev/float(500))*100),1)
			lightPercentage = 100-round(((photoSens/float(950))*100),1)
			currentTime=time.strftime("%H:%M:%S")
                	cur.execute("insert into WaterLevelLog values(?,?)", (time.strftime('%Y-%m-%d %H:%M:%S'), waterPercentage))
                	cur.execute("insert into LightLog values(?,?)", (time.strftime('%Y-%m-%d %H:%M:%S'), lightPercentage))
			con.commit()
			print("_______________")
			print("DATE / TIME")
			print(currentDate)
			print(currentTime)
			print("____________________")
			print("WATER LEVEL / LIGHT LEVEL")
			print(str(waterPercentage) + "% Water")
			print(str(lightPercentage) + "% Light")
			print("_______________")
			print("\n")
			oldTime = time.time()
			currentTime=time.strftime("%H:%M:%S")

except KeyboardInterrupt:
	con.close()
	print('\nAnalog Devices: SUCCESS!')
        GPIO.cleanup()    
