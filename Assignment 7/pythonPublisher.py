import paho.mqtt.client as mqtt
import os, sys, urlparse, time
import paho.mqtt.publish as publish
from random import randint
import Adafruit_DHT
#import pydht

brokerUrl = "test.mosquitto.org"
topicTemp = "groupD/temperature"
# topicVolt = "groupD/voltage"
topicShut = "groupD/shutdown"

# def getCPUVolt():
# 	res = os.popen('/opt/vc/bin/vcgencmd measure_volts core').readline()
#     resFormat = res.replace("volt=","").replace("'C\n","")
#     return (resFormat)

# def getCPUTemperature():
# 	res = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline()
#     resFormat = res.replace("temp=","").replace("'C\n","")
# 	return(resFormat)

def getDHTTemperature():
	#return pydht.get(board_mode='BOARD', pin=4)
	return Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)

for i in range (1, 5):
	# publish.single(topicVolt, str(getCPUVolt()), hostname = brokerUrl)
	publish.single(topicTemp, str(getDHTTemperature()), hostname=brokerUrl)
	time.sleep(1)

# publish.single(topicShut, "shutdown", hostname = brokerUrl)
