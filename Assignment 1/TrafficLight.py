import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#Red light
GPIO.setup(40, GPIO.OUT)
#Yellow light
GPIO.setup(38, GPIO.OUT)
#Green light
GPIO.setup(36, GPIO.OUT)

while 1:
	#Red on, all off
	GPIO.output(40, GPIO.HIGH)
	GPIO.output(38, GPIO.LOW)
	GPIO.output(36, GPIO.LOW)
	time.sleep(3)

	#Yellow on, all off
	GPIO.output(40, GPIO.LOW)
	GPIO.output(38, GPIO.HIGH)
	GPIO.output(36, GPIO.LOW)
	time.sleep(1)

	#Green on, all off
	GPIO.output(40, GPIO.LOW)
	GPIO.output(38, GPIO.LOW)
	GPIO.output(36, GPIO.HIGH)
	time.sleep(5)

def alloff():
	GPIO.output(40, GPIO.LOW)
	GPIO.output(38, GPIO.LOW)
	GPIO.output(36, GPIO.LOW)
	
try:
	main()
except KeyboardInterrupt:
	alloff()
	GPIO.cleanup()
	exit()
