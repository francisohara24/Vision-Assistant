"""Blink an LED connected to pin GPIO14."""
from gpiozero import LED
from time import sleep

# initialize pin 14 as LED pin
led = LED(14)

# Method 1: blink the LED at 1 second intervals using LED.on, LED.off, and sleep
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

# Method 2: blink the LED using LED.blink()
while True:
    led.blink()