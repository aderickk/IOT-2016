import spidev
import time
import sys

spi = spidev.SpiDev()
spi.open(0,0)

while True:
        fromMCP = spi.xfer2([1, 8 << 4, 0])
        ADCvalue = ((fromMCP[1] & 3) << 8) + fromMCP[2]
        # print "ADC value = %d" % ADCvalue

        per=(ADCvalue/1023.00)*100
	#print "per = %d" % per	
	sys.stdout.write("{adcvalue: \"%s\" }\n" %per)			
        sys.stdout.flush()
        time.sleep(1)

