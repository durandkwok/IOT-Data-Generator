#!/usr/bin/env python

# imports
import time
import random
import base64
import os
import sys
import math
import json
import uuid
import collections
from collections import OrderedDict


outputpath = "file.log"

print outputpath

outputfile = open(outputpath, 'w+')

start = time.time()
start_value = 0

baseTemp = 32.0
basePresure = 1000
baseLevel = 10
baseVoltage = 220

jmsg = {}
x = 0
sensrec = collections.OrderedDict()


# create dictionary
def create_jmsg(timestamp, timezone, millis, sensor, senstype, metric):
	msg = {}
	if(timestamp != ""):
		msg["timestamp"] = timestamp
	if(timezone != ""):
		msg["timezone"] = timezone
	if(millis != ""):
		msg["millis"] = millis
	if(sensor != ""):
		msg["sensor"] = sensor
	if(senstype != ""):
		msg["senstype"] = senstype
	if(metric != ""):
		msg["metric"] = metric
	#print(json.dumps(msg))
	return msg

# main loop
#while (x<40):
while (x>=0):
	x += 1
#	print (x);
#	outputfile.write("x is %d\r\n" %x)

	t = time.strftime('%Y-%m-%dT%H:%M:%S')
	timezone = time.strftime('%z')
	millis = "%.3d" % (time.time() % 1 * 1000)

	sin_value = math.sin(start_value)
	start_value += 1

	metric = random.sample(['currentTemp', 'currentPresure', 'currentLevel', 'currentVoltage'], 1) [0]

	# case --
	if metric == 'currentTemp':
		baseTemp = baseTemp + sin_value
		if baseTemp <= 0:
			baseTemp = 32.0 #reset if sin is negative

		if baseTemp > 65:
			print("Current baseTemp",baseTemp)
#			start_value = 1
#			baseTemp = 32.0 #reset if temp is greater 65
#			print("Over 65-reset to 32",x)

		# create message dictionary
		jmsg = create_jmsg(t,timezone,millis, "sensor101", metric, baseTemp)

	if metric == 'currentPresure':
		basePresure = basePresure + sin_value*10
		if basePresure <= 0:
			basePresure = 1000
		jmsg = create_jmsg(t,timezone,millis, "sensor102", metric, basePresure)

	if metric == 'currentLevel':
		baseLevel = baseLevel + sin_value*.10
		if baseLevel <= 0:
			baseLevel = 10
		jmsg = create_jmsg(t,timezone,millis, "sensor103", metric, baseLevel)

	if metric == 'currentVoltage':
		baseVoltage = baseVoltage + sin_value*1.5
		if baseVoltage <= 0:
			baseVoltage = 220
		if baseVoltage >= 225:
			baseVoltage = 220
		jmsg = create_jmsg(t,timezone,millis, "sensor104", metric, baseVoltage)


	sensrec['sendatetime'] = jmsg.get("timestamp")+jmsg.get("millis")
	sensrec['timezone'] = jmsg.get("timezone")
	sensrec['sensor'] = jmsg.get("sensor")
	sensrec['type'] = jmsg.get("senstype")
	sensrec['metric'] = jmsg.get("metric")

#	outputfile.write(json.dumps(sensrec))
#	outputfile.write("\r\n")

	#if (jmsg.get("senstype") == "currentTemp" and jmsg.get("metric")>65):
	if (metric == "currentTemp" and jmsg.get("metric")>65):
		print("sensordatetime", jmsg.get("timestamp")+jmsg.get("millis"))
		print("timezone", jmsg.get("timezone"))
		print("sensor", jmsg.get("sensor"))
		print("type", jmsg.get("senstype"))
		print("metric",str(jmsg.get("metric")))


	outputfile.write(json.dumps(sensrec))
	outputfile.write("\r\n")


	# sleep to slow down generation
	time.sleep(.7750/1000.0)


	jmsg = {}

#close outputfile
outputfile.close()
