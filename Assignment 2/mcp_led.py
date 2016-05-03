import spidev
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)


spi = spidev.SpiDev()
spi.open(0,0)

while True:
        fromMCP = spi.xfer2([1, 8 << 4, 0])
        ADCvalue = ((fromMCP[1] & 3) << 8) + fromMCP[2]
        print "ADC value = %d" % ADCvalue

        per=(ADCvalue/1023.00)*100
        print "per = %d" % per
        if(per > 75):
                GPIO.output(38,GPIO.HIGH)
                GPIO.output(40,GPIO.LOW)
        elif(per > 0 and per < 75):
                GPIO.output(40,GPIO.HIGH)
                GPIO.output(38,GPIO.LOW)
        elif(per == 0):
                GPIO.output(38, GPIO.LOW)
                GPIO.output(40, GPIO.LOW)
        time.sleep(1)
