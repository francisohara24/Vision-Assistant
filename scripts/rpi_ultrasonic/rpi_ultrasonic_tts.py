# import required libraries
import time
import board
import adafruit_hcsr04
import pyttsx3

# instantiate ultrasonic sensor object
ultrasonic  = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

# wait 0.1 second and measure distance
time.sleep(0.5)
distance = f"{ultrasonic.distance:0.2f}"

# instantiate tts engine
engine = pyttsx3.init()

# construct sentence and pass as input to tts engine
sentence = f"You are {distance} centimeters away from the nearest object."
engine.say(sentence)

# read the distance aloud
engine.runAndWait()
