"""Script for capturing image using raspberry Pi camera"""
from picamera2 import Picamera2
from libcamera import controls
import time

# instantiate camera object
camera = Picamera2()

# turn on camera
camera.start()

# enable camera autofocus for clearer images
camera.set_controls({"AfMode": 2, "AfTrigger": 0})

def capture():
    """capture an image with the camera and return it as a Pillow Image"""
    return camera.capture_image()
