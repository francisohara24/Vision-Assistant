"""Output state of button connected to GPIO4"""
from gpiozero import Button

button = Button(4)

while True:
    if button.is_pressed:
        print("Pressed")
    else:
        print("Released")
