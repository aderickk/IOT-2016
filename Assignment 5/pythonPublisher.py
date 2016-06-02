import paho.mqtt.client as mqtt
import os, sys, urlparse
import paho.mqtt.publish as publish
from random import randint

brokerUrl = "test.mosquitto.org"
topicName = "test/mqtt"

def getCPUVolt():
	res = os.popen('vcgencmd measure_volts core').readline()
	return (res)

def getCPUTemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	resFormat = res.replace("temp=","").replace("'C\n","")
	#sys.stdout.write("Temp = "+ resFormat);
	return(resFormat)

def getRandom():
	return randint(1, 128)

publish.single(topicName, str(getRandom()), hostname=brokerUrl)

messages = [{'topic': topicName, 'payload':str(getRandom())},
	(topicName, str(getRandom()), 0, False)]

publish.multiple(messages, hostname = brokerUrl)

publish.single(topicName, "shutdown", hostname=brokerUrl)


