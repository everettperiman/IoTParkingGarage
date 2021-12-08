"""
This script is used to simulate as many garage floors and nodes as you want too
Set floor count("garage"), spot_count(number of spots/floor), and the status ranges define the raw sensor values (mm)
"""

import paho.mqtt.client as mqtt
import random
import time
import json

# JSON Data setup
floor_count = 4
spot_count = 50
status_range_max = 12*1000 #12M
status_range_min = 0

time_period = 15*60
start_time = 1636347447

# Time delay setup
spot_delay = 0
floor_delay = 0
loop_delay = 10

# MQTT setup
mqtt_ip = "192.168.1.110"
mqtt_topic = "node_red"
mqtt_client_name = "TestNode" #Doesnt matter its the name of the current node

client = mqtt.Client()

while True:
	for floor in range(1,floor_count+1): # Start the floors and spots at 1 so no NULL numbers in the database

		for spot in range(1,spot_count+1):

			client.connect(mqtt_ip)
			
			# Random status values
			status = random.randint(status_range_min,status_range_max)
			#status = 0
			# Get current timestamp I dont think this really matters
			timestamp = int(time.time())

			data_dict = {"node":spot,
						"garage":floor,
						"status":status,
						"timestamp":timestamp
						}

			data_string = json.dumps(data_dict)
			
			print(data_string)

			client.publish(mqtt_topic, data_string, qos=1)

			#Setup all of the delays
			time.sleep(spot_delay)
		time.sleep(floor_delay)
	time.sleep(loop_delay)
	
