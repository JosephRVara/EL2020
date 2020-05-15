#This script creates a Flask server, and serves the index.html out of the templates folder.
#It also creates an app route to be called via ajax from javascript in the index.html to query
#the database that is being written to by each of the .py scripts, and return the data as a json object.

#This was written for Joshua Simons's Embedded Linux Class at SUNY New Paltz 2020
#And is licenses under the MIT Software License

#Import libraries as needed
from flask import Flask, render_template, jsonify, Response
import sqlite3 as sql
import json
import RPi.GPIO as GPIO
import time

#GPIO.setwarnings(False)

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/DHT11_TempData")
def DHT11_TempChartData():
	con = sql.connect('EnvironmentMonitor.db')
	cur = con.cursor()
	con.row_factory = sql.Row
	cur.execute("SELECT Date, RoomTemp FROM DHT11_TempLog WHERE RoomTemp >= 65")
	dataset = cur.fetchall()
	print (dataset)
	chartData1 = []
	for row in dataset:
		chartData1.append({"Date": row[0], "RoomTemp": float(row[1])})
	return Response(json.dumps(chartData1), mimetype='application/json')

@app.route("/DHT11_HumData")
def DHT11_HumChartData():
	con = sql.connect('EnvironmentMonitor.db')
	cur = con.cursor()
	con.row_factory = sql.Row
	cur.execute("SELECT Date, Humidity FROM DHT11_HumidityLog WHERE Humidity >= 35")
	dataset = cur.fetchall()
	print (dataset)
	chartData2 = []
	for row in dataset:
		chartData2.append({"Date": row[0], "Humidity": float(row[1])})
	return Response(json.dumps(chartData2), mimetype='application/json')

@app.route("/DS18B20_Data")
def DS18B20_ChartData():
	con = sql.connect('EnvironmentMonitor.db')
	cur = con.cursor()
	con.row_factory = sql.Row
	cur.execute("SELECT Date, SoilTemp FROM DS18B20_TempLog WHERE SoilTemp >= 65")
	dataset = cur.fetchall()
	print (dataset)
	chartData3 = []
	for row in dataset:
		chartData3.append({"Date": row[0], "SoilTemp": float(row[1])})
	return Response(json.dumps(chartData3), mimetype='application/json')

@app.route("/Photoresistor_Data")
def Light_ChartData():
	con = sql.connect('EnvironmentMonitor.db')
	cur = con.cursor()
	con.row_factory = sql.Row
	cur.execute("SELECT Date, Light FROM LightLog WHERE Light > 0")
	dataset = cur.fetchall()
	print (dataset)
	chartData4 = []
	for row in dataset:
		chartData4.append({"Date": row[0], "Light": float(row[1])})
	return Response(json.dumps(chartData4), mimetype='application/json')

@app.route("/WaterLevelSens_Data")
def WaterLevel_ChartData():
	con = sql.connect('EnvironmentMonitor.db')
	cur = con.cursor()
	con.row_factory = sql.Row
	cur.execute("SELECT Date, WaterLevel FROM WaterLevelLog WHERE WaterLevel > 0")
	dataset = cur.fetchall()
	print (dataset)
	chartData5 = []
	for row in dataset:
		chartData5.append({"Date": row[0], "WaterLevel": float(row[1])})
	return Response(json.dumps(chartData5), mimetype='application/json')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=2020, debug=True, use_reloader=False)
