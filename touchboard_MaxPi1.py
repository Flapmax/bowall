#MaxPi 1
import board, vlc
from digitalio import DigitalInOut, Direction

#restart als variable
restart = 1

#importing Sounds
location = vlc.MediaPlayer("Localisation.wav")
Error = vlc.MediaPlayer("Error.wav")
Celebration = vlc.MediaPlayer("Wishful_Thinking.mp3")
Success = vlc.MediaPlayer("Success.wav")

def main():
    global restart

    #set GPIO input pins
    pad0_pin = board.D4
    pad0 = DigitalInOut(pad0_pin)
    pad0.direction = Direction.INPUT
    pad0_already_pressed = True

    while True:
        from firebase import firebase
        #calling firebase getting the ID and printing the result
        firebase = firebase.FirebaseApplication('https://bowall.firebaseio.com/')
        result = firebase.get('/checkValue','checkID')
        print(result)

        if resutl == 1:
            Celebration.play()

        if pad0.value and not pad0_already_pressed
            #playing the sound on touch
            Celebration.stop()
            Success.play()
            print("Pad 0 Pressed")
            #changing the ID to 2
            post = firebase.patch('/checkValue', {'checkID': 2})
            Success.stop()
        pad0_already_pressed = pad0.value

main()




