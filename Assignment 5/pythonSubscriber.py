import paho.mqtt.client as mqtt
import os, urlparse, sys

brokerUrl = "test.mosquitto.org"
topicName = "test/mqtt"
client = mqtt.Client()

def on_subscribe(mosq, userdata, message, qos):
	print("Subscribed to:" + str(message))

def on_message(client, userdata, msg):
	if ("shutdown" in msg.payload):
		client.unsubscribe(topicName)
	else:
		print(msg.topic + " " + str(msg.payload))

client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(brokerUrl, 1883, 60)

client.subscribe(topicName, 0)

while True:
	client.loop_start()

