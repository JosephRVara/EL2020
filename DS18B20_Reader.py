import glob
import time
import sqlite3
import RPi.GPIO as GPIO

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

con = sqlite3.connect('EnvironmentMonitor.db')
cur = con.cursor()

oldTime = 60

currentDate = time.strftime("%Y-%m-%d")
currentTime = time.strftime("%H:%M:%S")
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

try:
	while True:

    		if time.time() - oldTime > 59:
			tempC, tempF = read_temp()
			currentTime = time.strftime("%H:%M:S")
			cur.execute("insert into DS18B20_TempLog values(?,?)", (time.strftime('%Y-%m-%d %H:%M:%S'), tempF))
			con.commit()
			print(tempC)
			print(tempF)
			oldTime = time.time()
			currentTime = time.strftime("%H:%M:%S")

except KeyboardInterrupt:
	con.close()
	print('\nDS18B20 Successfully Shutdown')
	GPIO.cleanup()
