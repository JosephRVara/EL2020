<img src="https://www.newpaltz.edu/media/identity/logos/newpaltzlogo.jpg" width="50%">

# **Final Project for CPS342 Embedded Linux 2020**
This repository contains all files, code and class work for the Final Project.

## **Goal**
Create an environment monitor for one of my succulents. An elecronic system will monitor water level, soil temperature, humidity, and
light. This will be achieved by having all of the electronic components submerged in the soil or placed around the perimeter of the 
plant pot. All sensor readings will be logged into SQL databases and transferred into representative charts using Google Charts API. 
A web server will display all information relating to this project using the Flask web application framework.


## **Technologies**
Electronic components used in the project can be seen in the figures below. Scripting languages to be used include Python, HTML, CSS, 
Git, and bash. A couple of imported Python libraries are required to interface the sensors with the Raspberry Pi 4. 
These libraries are “Adafruit_DHT”, for the DHT11 digital humidity and temperature sensor, and “Adafruit_Python_MCP3008”, for the MCP3008 
ADC IC.

The Raspberry Pi 4 can only host digital devices unless an analog to digital converter is implemented. For example, the water level 
sensor is an analog device which outputs a signal voltage that corresponds to water level. In order to measure water level using this 
sensor, the MCP3008 is required. The MCP3008 is a 10 bit ADC which represents the value on a channel from 0 to 1023 (total possible 
values of 1024) where 1023 is the maximum voltage of the GPIO output pin. This value can then be converted to a representative value
for water level. Other electronic components in this project which are considered to be analog devices include the temperature sensor and
photoresistive sensor.

Additionally, a few modules will be used in the Python code using the import function. These modules include json, sqlite3, smtplib 
and flask. The JSON module will enable the python script to be read as a string into another file. Specifically, the .html file which 
will be used as the formatting of the web server. The sqlite3 module will allow for SQL statements to be executed within the Python code. 
Email communication will be made available using the smtplib module. Information and updates regarding the state of the plant environment
will alert the admin. The flask module is imported for implementing flask templates and commands.

![GPIOExtensionBoard](/images/GPIO.png =50x)
![MCP3008_ADC](/images/MCP3008_ADC.png =50x)
![DHT11](/images/DHT11.png =50x)
![TemperatureSensor](/images/TempSens.png =50x)
![PhotoResistor](/images/PhotoResistor.png =50x)
![WaterLevelSensor](/images/WaterLevelSens.png =50x)

