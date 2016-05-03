import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

while 1:
	GPIO.output(40, GPIO.LOW)
	time.sleep(1)
	GPIO.output(40, GPIO.HIGH)
	time.sleep(1)

try:
	main()
except KeyboardInterrupt:
	GPIO.cleanup()
	exit()
