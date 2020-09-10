#! /usr/bin/python3

'''
This file contains code to send data on serial port
This test code is to test Serial Expansion HAT
'''

import RPi.GPIO as GPIO
import serial
import time

ser1 = serial.Serial("/dev/ttySC0",115200,timeout=1)
ser2 = serial.Serial("/dev/ttySC1",115200,timeout=1)

send_data = "Hello"
while True:
    length = ser2.write(send_data.encode())
    print("Send data: ",send_data)
    ser1.flush()
    time.sleep(1)
    
