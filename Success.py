#MaxPi 1
import vlc
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)



#importing Sounds
Success = vlc.MediaPlayer("Success.wav")

while True:
    input_state = GPIO.input(26)
    if input_state == False:
        print("Button was pushed!")
        Success.play()
        time.sleep(1)
        Success.stop()
