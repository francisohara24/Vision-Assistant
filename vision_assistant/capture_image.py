"""Module for capturing image using raspberry Pi camera"""
# import required libraries
from picamera2 import Picamera2
from libcamera import controls
from PIL.Image import Image

# instantiate camera object
camera = Picamera2()

# turn on camera
camera.start()

# enable camera autofocus features for clearer images
camera.set_controls({"AfMode": 2, "AfTrigger": 0})


def capture() -> str:
    """Capture an image with the camera, save the image, and return the path to the captured image."""
    # capture the image
    image = camera.capture_image()

    # define path for saving image
    image_path = "./Projects/Vision-Assistant/data/temp/input.jpg"

    # save the image
    image.save(image_path)

    # return path to saved image
    return image_path
