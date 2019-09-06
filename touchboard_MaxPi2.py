#MaxPi 1
import time
import board
from digitalio import DigitalInOut, Direction
import RPi.GPIO as GPIO
import os
from firebase import firebase

firebase = firebase.FirebaseApplication('https://bowall.firebaseio.com/')
result = firebase.get('/checkValue','checkID')
print(result)

# set the GPIO input pins
pad0_pin = board.D22

pad0 = DigitalInOut(pad0_pin)

pad0.direction = Direction.INPUT

pad0_already_pressed = True


while True:


    if pad0.value and not pad0_already_pressed:
        os.system('omxplayer geschafft.wav &')
        print("Pad 1 pressed and LED ON")
        GPIO.output(26,GPIO.HIGH)
        post = firebase.patch('/checkValue',{'checkID': 1})
    pad0_already_pressed = pad0.value

    time.sleep(0.1)
    
    result = firebase.get('/checkValue','checkID') 
    
    if result == 1:
        exit()
