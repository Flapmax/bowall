#MaxPi 1
import board, vlc
from digitalio import DigitalInOut, Direction
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#restart als variable
restart = 1

#importing Sounds
location = vlc.MediaPlayer("Localisation.wav")
Error = vlc.MediaPlayer("Error.wav")
Celebration = vlc.MediaPlayer("Wishful_Thinking.mp3")
Success = vlc.MediaPlayer("Success.wav")

def main():
    global pull_up_down

    while True:

        if GPIO.input(10) == GPIO.HIGH:
            print("Button was pushed!")
            Celebration.play()



main()