#MaxPi 2
import time
import board
from digitalio import DigitalInOut, Direction
import vlc
from firebase import firebase

#calling firebase getting the ID and printing the result
firebase = firebase.FirebaseApplication('https://bowall.firebaseio.com/')
result = firebase.get('/checkValue','checkID')
print(result)

#importing the Sounds
location = vlc.MediaPlayer("bowall/Localistation.wav")
Error = vlc.MediaPlayer("bowall/Error.wav")
Success = vlc.MediaPlayer("bowall/Success.wav")
Celebration = vlc.MediaPlayer("bowall/Celebration.wav")

# set the GPIO input pins
pad0_pin = board.D22

pad0 = DigitalInOut(pad0_pin)

pad0.direction = Direction.INPUT

pad0_already_pressed = True


while True:


    if pad0.value and not pad0_already_pressed:
        #playing the sound on touch
        Success.play()
        print("Pad 0 Pressed")
        #Changing the ID to 1
        post = firebase.patch('/checkValue',{'checkID': 1})
    pad0_already_pressed = pad0.value

    time.sleep(0.1)
    
    result = firebase.get('/checkValue','checkID') 
    
    if result == 1:
        exit()
