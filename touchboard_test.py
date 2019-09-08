def main():
    # Test Code
    import board
    from digitalio import DigitalInOut, Direction
    import vlc
    from firebase import firebase

    # calling firebase getting the ID and printing the result
    firebase = firebase.FirebaseApplication('https://bowall.firebaseio.com/')
    result = firebase.get('/checkValue', 'checkID')
    print(result)

    #restart als variable
    restart = 1

    # importing the Sounds
    location = vlc.MediaPlayer("Localistation.wav")
    Error = vlc.MediaPlayer("Error.wav")
    Success = vlc.MediaPlayer("Success.wav")
    Celebration = vlc.MediaPlayer("Celebration.wav")

    # set the GPIO input pins
    pad0_pin = board.D4

    pad0 = DigitalInOut(pad0_pin)

    pad0.direction = Direction.INPUT

    pad0_already_pressed = True

    if result == 1:
        location.play()

        while True:

            if pad0.value and not pad0_already_pressed:
                # playing the sound on touch
                Success.play()
                print("Pad 0 Pressed")
                # Changing the ID to 1
                post = firebase.patch('/checkValue', {'checkID': 2})
            pad0_already_pressed = pad0.value

    if restart == 1:
        print("looping")
        main()

main()


