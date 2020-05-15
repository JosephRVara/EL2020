<img src="https://www.newpaltz.edu/media/identity/logos/newpaltzlogo.jpg" width="50%">

# **Final Project for CPS342 Embedded Linux 2020**
This repository contains all files, code and updates for the Final Project.

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
for water level. Other electronic components in this project which are considered to be analog devices include the Photosensitive Light module.

Additionally, a few modules will be used in the Python code using the import function. These modules include json, sqlite3, smtplib 
and flask. The JSON module will enable the python script to be read as a string into another file. Specifically, the .html file which 
will be used as the formatting of the web server. The sqlite3 module will allow for SQL statements to be executed within the Python code. 
Email communication will be made available using the smtplib module. Information and updates regarding the state of the plant environment
will alert the admin. The flask module is imported for implementing flask templates and commands.

<img src="/images/GPIO.png" alt="GPIO" width="250"/> **Fig. 1** GPIO Extension Board

<img src="/images/MCP3008_ADC.png" alt="ADC" width="250"/> **Fig. 2** MCP3008 Analog-to-Digital Converter

<img src="/images/DS18B20.png" alt="DS18B20" width="100"/> **Fig. 3** DS18B20 Temperature Sensor Module

<img src="/images/DHT11.png" alt="DHT11" width="100"/> **Fig. 4** DHT11 Temperature & Humidity Sensor Module

<img src="/images/PhotoResistorSens.png" alt="PhotoResistorSens" width="250"/> **Fig. 5** Photosensitive Light Module

<img src="/images/WaterLevelSens.png" alt="WaterLevelSens" width="100"/> **Fig. 6** Water Level Sensor Module

## **Materials**
* *Succulent* - Price varies	
* *Plant Holder/Pot* - Price varies
* *CanaKit Raspberry Pi 4 4GB Starter Kit* - $99.99
* *KOOKYE 16 in 1 Smart Home Sensor Modules Kit* - $22.97
* *SunFounder Raspberry Pi RAB Holder Breadboard Kit* - $13.59

## **Project Diagram**
<img src="/images/ProjectDiagram.png" alt="Diagram"/> 

**Fig. 7** Final Project Diagram made in Google Drawing

## **Wiring Instructions**

1. GPIO Extension board to Raspberry Pi 4.

2. Fan attached to Raspberry Pi 4 to avoid overheating. Connect to ground and 3.3V.

3. From the 3.3V pin and any GND pin on the GPIO Extension Board, link up both power rails to 3.3V and GND.

4. Connect the MCP3008 analog-to-digital converter to the breadboard.

5. Following the description of each pin from Figure 1, proceed to ground all CH2-CH7. This will avoid any 
   interference with CH1 and CH0. We only need two channels for this project because the only data being sent back  
   from the ADC to the GPIO is from two analog devices.

6. Connect Raspberry Pi 3.3V to MCP3008 VDD

7. Connect Raspberry Pi 3.3V to MCP3008 VREF

8. Connect Raspberry Pi GND to MCP3008 AGND

9. Connect Raspberry Pi GND to MCP3008 DGND

10. Connect Raspberry Pi pin 18 to MCP3008 CLK

11. Connect Raspberry Pi pin 23 to MCP3008 DOUT

12. Connect Raspberry Pi pin 24 to MCP3008 DIN

13. Connect Raspberry Pi pin 25 to MCP3008 CS/SHDN

14. Connect the Water Level Sensor to ground, 3.3V and signal to CH0.

15. Connect the Photosensitive Light Sensor Module to ground, 3.3V and signal to CH1.

16. The DHT11 will be connected to ground, 3.3V and signal to pin 26.

17. The DS18B20 Module will be connected to ground, 3.3V and signal to pin 4.

<img src="https://cdn-learn.adafruit.com/assets/assets/000/030/456/medium800/sensors_raspberry_pi_mcp3008pin.gif?1455010861" alt="MCP3008"/> 

**Fig. 8** MCP3008 Pin Detail

