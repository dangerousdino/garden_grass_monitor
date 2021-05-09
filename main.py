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
    if GPIO.input(sensor_pin):
        r = False
    else:
        r = True

    return r

def turn_on(relay_pin):

	GPIO.output(relay_pin, GPIO.LOW) # out
	GPIO.output(relay_pin, GPIO.HIGH) # on

def turn_off(relay_pin):
	GPIO.output(relay_pin, GPIO.LOW) # out
	GPIO.output(relay_pin, GPIO.LOW) # on

def main():

    while True:
        result = get_sensor(sensor_pin)
        if result == True:
    	    print("Water Detected")
    	    turn_off(relay_pin)
    	    time.sleep(10)
        else:
    	    print("No Water Detected")
    	    turn_on(relay_pin)
    	    time.sleep(10)

main()