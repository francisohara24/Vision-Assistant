"""Capture images of the pages of physical books to create a dataset for testing OCR models."""
from picamera2 import Picamera2
from libcamera import controls
from gpiozero import Button
from time import sleep

# Instantiate camera object and start the hardware
camera = Picamera2()
camera.start(show_preview=True)

# set camera to continuous autofocus mode
camera.set_controls({"AfMode": 2, "AfTrigger":0})

# initialize button at GPIO14
button = Button(14)

# counter for no. of images captured
n_captures = 0

# run the program indefinitely
while True:
    # capture image when button pressed
    if button.is_pressed:
        print(f"Captured image_{n_captures}")
        camera.capture_file(f"/home/francisohara24/Projects/AI-Reader/data/rpi_images/image_{n_captures}.jpg")
        n_captures += 1

    # delay 0.25 seconds to avoid overcapturing images
    sleep(0.25)
