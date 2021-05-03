import os 
import sys
import requests
import random
import time

api_key = 1234

def get_sensor():
    num = random.randint(1,100)
    print(num)
    return num


def turn_on():
	print("Turning Hose Pipe On")

def turn_off():
    print("Turning Hose Pipe Off")

def main():
  
    while True:
    	sensor_info = get_sensor()
    	if sensor_info < 80:
    		print("doing this")
    		turn_on()
    		time.sleep(10)
    	else: 
    		print("not doing this")
    		turn_off()
    		time.sleep(10)

main()

