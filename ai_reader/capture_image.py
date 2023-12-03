"""Script for capturing image using raspberry Pi camera"""
from picamera2 import Picamera2
from libcamera import controls
from PIL.Image import Image

# instantiate camera object
camera = Picamera2()

# turn on camera
camera.start()

# enable camera autofocus for clearer images
camera.set_controls({"AfMode": 2, "AfTrigger": 0})


def capture() -> Image:
    """Capture an image with the camera and return it as a Pillow Image."""
    camera.capture_file("image.jpg")  # test code
    return camera.capture_image()
