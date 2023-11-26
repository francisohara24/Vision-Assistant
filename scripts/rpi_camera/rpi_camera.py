"""Autofocus the Raspberry Pi camera and take a picture."""
from picamera2 import Picamera2
from libcamera import controls
from time import sleep

# create a camera instance
camera = Picamera2()

# turn on camera
camera.start()

# configure autofocus
camera.set_controls({"AfMode": 2, "AfTrigger": 0})

# wait 2 seconds for autofocus
sleep(2)

# capture image
image = camera.capture_image()

# save the image
image.save("./scripts/rpi_camera/image1.jpg")