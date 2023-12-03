"""Function for measuring the proximity of the user to the nearest object pointed to using the ultrasonic sensors."""
import adafruit_hcsr04
import board
import time

ultrasonic_sensor = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)


def check_proximity() -> str:
    """Check proximity to the nearest object using the device's ultrasonic sensors.

    Returns
    -------
    str
        a string containing a float representing the proximity reading from the ultrasonic sensors in centimeters rounded
        to two decimal places.
    """
    distance = ultrasonic_sensor.distance
    return f"{distance:0.2f}"

    #TODO: add error handling code


if __name__ == "__main__":
    distance = check_proximity()
    print(f"Current proximity: {distance} centimeters.")