# -*- coding: utf-8 -*-  
# import GPIO library
import RPi.GPIO as GPIO  
# import time library. allow us to use 'sleep'
import time  

# use BCM pin numbering
GPIO.setmode(GPIO.BCM)  
# setup GPIO Pin 23 to OUT mode
GPIO.setup(23, GPIO.OUT)  

# define Blink function
def Blink(nTimes, speed):
	for nIndex in range(0, nTimes):
		print "Iteration " + str(nIndex+1)
		GPIO.output(23, True)
		time.sleep(speed)
		GPIO.output(23, False)
		time.sleep(speed)
	print "Done"
	GPIO.cleanup()

# Ask user for total number of blinks and length of each blink
iterations = raw_input( "Enter total number of times to blink:")
speed = raw_input("Enter length of each blink(seconds):")

# start blink() funciton.
Blink(int(iterations), float(speed))
			
