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


def capture() -> str:
    """Capture an image with the camera and return the path to the captured image."""
    # test
    image = camera.capture_image()
    image_path = "./data/temp/input.jpg"
    image.save(image_path)
    return image_path
    #test
    #return camera.capture_image()
