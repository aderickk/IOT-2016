import paho.mqtt.client as mqtt
import os, urlparse, sys

brokerUrl = "192.76.241.164"
topicTemp = "groupD/temperature"
# topicVolt = "groupD/voltage"
topicShut = "groupD/shutdown"
client = mqtt.Client()

def on_subscribe(mosq, userdata, message, qos):
	print("Subscribed to:" + str(message))

def on_message(client, userdata, msg):
	if (msg.topic == topicShut): #and "shutdown" in msg.payload):
		print("Shut down system")
		client.unsubscribe(topicTemp)
		# client.unsubscribe(topicVolt)
		client.unsubscribe(topicShut)
	elif (msg.topic == topicTemp):
		print("CPU Temperature is: " + str(msg.payload))
	# elif (msg.topic == topicVolt):
	# 	print("CPU Voltage: " + str(msg.payload))

client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(brokerUrl, 1883, 60)

client.subscribe(topicTemp, 0)
# client.subscribe(topicVolt, 1)
client.subscribe(topicShut, 1)

while True:
	client.loop_start()
