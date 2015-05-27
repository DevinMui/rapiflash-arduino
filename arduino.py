import requests
import json
import serial
import rapiflash
# get serials/pins
ser = serial.Serial(4,115200)
while True:
    line = ser.readline() # sends current_level
    if line == True:
        # sends data to api
        # current_level, normal_level, flooded, location, upstream
        print rapiflash.create_data(5,4,False,'Dublin,CA',1234)
