"""
Copyright (c) 2010 Sense Tecnic Systems Inc.

@author:        Jake Lin, Vincent Tsao

Description:    This module defines all the configuration constants
"""


# the latitude and longitude where these phidgets are located
LAT = 49.26058617071484
LNG = -123.24791193008423


# Client Id #
CLIENT_ID = "phidgets"

# Set Phidget configuration service name
SERV_NAME = "SetPhidgetConfig"
# Topic to use for registering service
SERV_CHAN = "device.phidget.in"
# Service description
SERV_DESC = "Service to modify the phidget module configurations."
# Service authentication
SERV_AUTH = "basic"

#TODO: add your username/password or key/secret
# Service authentication user
SERV_USER = ""
# Service authentication pasword
SERV_PASS = ""

# File directory to save phidget configurations
CONFIG_FILE = "config.txt"

# Dictionary of all port available on interface kit
port = {

# RFID Configuration {Enabled, Name, Topic}

"RFID": {"enabled": False,
		 "name": "RFID",
		 "topic": "phidgets.rfid",
		 "sensor": "rfid"
		 },

# Digital Input Configuration {Enabled, Name, Topic}

"INPUT_0": {"enabled": False,
			"name": "Simple Input",
			"topic": "phidgets.simpleinput",
			"sensor": "simpleinput"
			},

"INPUT_1": {"enabled": False,
			"name": None,
			"topic": None,
			"sensor": None
			},

"INPUT_2": {"enabled": False,
			"name": None,
			"topic": None,
			"processors": None},

"INPUT_3": {"enabled": False,
			"name": None,
			"topic": None},

"INPUT_4": {"enabled": False,
			"name": None,
			"topic": None},

"INPUT_5": {"enabled": False,
			"name": None,
			"topic": None},

"INPUT_6": {"enabled": False,
			"name": None,
			"topic": None},

"INPUT_7": {"enabled": False,
			"name": None,
			"topic": None},

# Analog Input Configuration 
# {Enabled, Name, Topic, Timeout, Processors}
# -Timeout is the amount of time in seconds to wait before sending an
#  aggregate event.
# -Processors takes a list of strings that calls a processor in the
#  order that the processors are to be called. 
#  (e.g. ["enough_difference(limit=20)", "average_window(period=1)"]

"SENSOR_0": {"enabled": True,
			 "sensor": "sensetecnic.demo-phidgets-light",
			 "timeout": 0,
			 "processors": ["pause(period=30)"]},

"SENSOR_1": {"enabled": True,
			 "sensor": "sensetecnic.demo-phidgets-temp",
			 "timeout": 0,
			 "processors": ["temperature(scale='c')"]},

"SENSOR_2": {"enabled": True,
			 "data": "Rotation",
			 "sensor": "sensetecnic.demo-phidgets-rotation",
			 "timeout": 0,
			 "processors": ["pause(period=1)"]},

"SENSOR_3": {"enabled": False,
			 "data": "Touch",
			 "timeout": 0,
			 "sensor":"sensetecnic.demo-phidgets-touch",
			 "processors": None},

"SENSOR_4": {"enabled": True,
			 "data": "Slider",
			 "sensor": "sensetecnic.demo-phidgets-slider",
			 "timeout": 0,
			 "processors": ["pause(period=1)",
			 				"enough_difference(limit=2)"]},

"SENSOR_5": {"enabled": True,
			 "data": "Force",
			 "sensor": "sensetecnic.demo-phidgets-force",
			 "timeout": 0,
			 "processors": ["pause(period=1)"]},

"SENSOR_6": {"enabled": False,
			 "data": None,
			 "timeout": 0,
			 "sensor":None,
			 "processors": None},

"SENSOR_7": {"enabled": False,
			 "data": None,
			 "timeout": 0,
			 "sensor":None,
			 "processors": None}
}
