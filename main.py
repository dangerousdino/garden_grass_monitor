#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import requests
 
#GPIO SETUP
sensor_pin = 20
relay_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(relay_pin, GPIO.OUT)

# test the sensor to find out if the soil is moist
def get_sensor(sensor_pin):
	# see if sensor has detected moisture
    if GPIO.input(sensor_pin):
        r = False
    else:
        r = True
    # returns true or false
    return r

def turn_on(relay_pin):

	GPIO.output(relay_pin, GPIO.LOW) # out
	GPIO.output(relay_pin, GPIO.HIGH) # on

def turn_off(relay_pin):
	GPIO.output(relay_pin, GPIO.LOW) # out
	GPIO.output(relay_pin, GPIO.LOW) # off

# a stupid way to do a loop
def main():
    while True:
    	# checks the sensor if moisture level is over the specific limit
        result = get_sensor(sensor_pin)
        if result == True:
        	# if water is detected then it will make sure the relay is off
    	    print("Water Detected")
    	    turn_off(relay_pin)
    	    # time to wait in seconds
    	    time.sleep(10)
        else:
        	# if no moisture is detected it will turn the relay on
    	    print("No Water Detected")
    	    turn_on(relay_pin)
    	    # how long the relay is on for till it reaccesses the situation
    	    time.sleep(10)
main()