"""Capture images of the pages of physical books to create a dataset for testing OCR models."""
from picamera2 import Picamera2
from libcamera import controls
from gpiozero import Button
from time import sleep

# Instantiate camera object and start the hardware
camera = Picamera2()
camera.start(show_preview=True)

# set to continuous autofocus mode
camera.set_controls({"AfMode": 2, "AfTrigger":0})

# counter for no. of images captured
n_captures = 0

# define function for capturing image w/ camera
def capture():
    global n_captures
    camera.capture_file(f"./scripts/rpi_camera/images/image_{n_captures}.jpg")
    n_captures += 1    
    

# Initialize button at GPIO14
button = Button(14)

# Assign button callback to capture function
button.when_pressed = capture() 

# run the program indefinitely
while True:
    sleep(1)