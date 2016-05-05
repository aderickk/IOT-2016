import spidev
import time
import RPi.GPIO as GPIO
import sevenSegmentLED as SSL

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0,0)

SSL.InitializeSevenSegment()

while True:
        fromMCP = spi.xfer2([1, 8 << 4, 0])
        ADCvalue = ((fromMCP[1] & 3) << 8) + fromMCP[2]
        #print "ADC value = %d" % ADCvalue
        #str("ADC value = %d", ADCvalue)
        
        per=(ADCvalue/1023.00)*100
        print "per = %d" % per


        if(per > 75):
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(8,GPIO.LOW)
        elif(per > 0 and per < 75):
                GPIO.output(8,GPIO.HIGH)
                GPIO.output(7,GPIO.LOW)
        if(per == 0):
                GPIO.output(7, GPIO.LOW)
                GPIO.output(8, GPIO.LOW)
        SSL.ShowNumber(per)
                
        time.sleep(1)
			





