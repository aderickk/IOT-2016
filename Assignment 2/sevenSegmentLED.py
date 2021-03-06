import RPi.GPIO as GPIO
import time
        
SevenSegmentPin = [31,32,33,35,36,37,38]

def InitializeSevenSegment():
        GPIO.setmode(GPIO.BOARD)
        for x in range(0,7):
                GPIO.setup(SevenSegmentPin[x], GPIO.OUT)
        str("All lamp configured")
	
def PrintLED(lampStatus):
        InitializeSevenSegment()
	for x in range(0, 7):
		GPIO.output(SevenSegmentPin[x], lampStatus[x])

LEDMapping = { '0': PrintLED([1,1,1,1,1,1,0]),
		'1': PrintLED([0,1,1,0,0,0,0]),
		'2': PrintLED([1,1,0,1,1,0,1]),
		'3': PrintLED([1,1,1,1,0,0,1]),
		'4': PrintLED([0,1,1,0,0,1,1]),
		'5': PrintLED([1,0,1,1,0,1,1]),
		'6': PrintLED([1,0,1,1,1,1,1]),
		'7': PrintLED([1,1,1,0,0,0,0]),
		'8': PrintLED([1,1,1,1,1,1,1]),
		'9': PrintLED([1,1,1,1,0,1,1])}	
			
def ShowNumber(perNumber):
        if(perNumber < 10.00):
                LEDMapping['0']
        else:
                perString = str(perNumber)
                requestedNumber = perString[:1]
                LEDMapping[requestedNumber]
				
		

