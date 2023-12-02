# import required libraries
import time
import board
import adafruit_hcsr04

# create ultrasonic sensor instance
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        # read distance from sensor and print
        print(f"Distance: {sonar.distance:0.2f} cm")
    # handle reading error
    except RuntimeError:
        print("Failed. Retrying...")
    # wait 0.1 seconds before next reading
    time.sleep(0.1)