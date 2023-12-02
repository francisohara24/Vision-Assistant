"""Turn the LED(GPIO14) on or off when the push button(GPIO) is pressed."""
from gpiozero import LED, Button

led = LED(14)
button = Button(4)

# "Method" 1: using Button.is_pressed property
while True:
    if button.is_pressed:
        led.on()
    
    else:
        led.off()

# "Method" 2: Using Button.wait_for_press() and Button.wait_for_release() methods
while True:
    button.wait_for_press()
    led.on()
    button.wait_for_release()
    led.off()

# "Method" 3: Using the button.when_pressed and button.when_released callbacks
while True:
    button.when_pressed = led.on
    button.when_released = led.off