#! /usr/bin/python3

'''
This file contains code to receive data on serial port
This test code is to test Serial Expansion HAT
'''

import RPi.GPIO as GPIO
import serial
import time

UART = 0 #use ttySC0  => UART = 0, use ttySC1 => UART = 1
if UART == 0:
    # ttySC0
    ser = serial.Serial("/dev/ttySC0",115200,timeout=1)
else:
    # ttySC1
    ser = serial.Serial("/dev/ttySC1",115200,timeout=1)
    
time.sleep(1)
ser.flushInput()

recv_data = ''
while True: 
    while ser.inWaiting() > 0:
        recv_data = ser.read(ser.inWaiting())
    if recv_data != "":
            print("Receive data: ",recv_data.decode())
    recv_data = ''
        
