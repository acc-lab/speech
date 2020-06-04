import speech
import time

from microbit import *

last_gesture = accelerometer.current_gesture()

while True:
    gesture = accelerometer.current_gesture()
    if last_gesture != gesture:
        if gesture == "left":
            speech.pronounce("CHUXAH",speed=150,mouth=70)
        elif gesture=="right":
            speech.pronounce("IHAA",speed=150,mouth=90)
        elif gesture == "up":
            speech.pronounce("/HOW4",speed=150)
        elif gesture=="down":
            speech.pronounce("CHEY4",speed=150)
        last_gesture=gesture