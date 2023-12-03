from ai_reader import ocr
from ai_reader import capture_image
from ai_reader import proximity
from ai_reader import tts
from gpiozero import Button
import asyncio
import time
import pytesseract # for testing


# define buttons for triggering pipelines
ocr_button = Button(17)
ultrasonic_button = Button(27)


# coroutine function for indefinite OCR sequence
async def ocr_pipeline():
    """Run the text recognition and speech synthesis pipeline of the project."""
    while True:
        if ocr_button.is_pressed:

            image = capture_image.capture()
            # text = ocr.extract_text(image)
            # for testing
            print("OCR function called")
            text = pytesseract.image_to_string(image, timeout=10)
            print("tesseract finished running")
            # for testing
            tts.say(text)
            await asyncio.sleep(0.25)


# coroutine function for indefinite Ultrasonic distance sequence
async def ultrasonic_pipeline():
    """Run the ultrasonic proximity detection pipeline of the project."""
    while True:
        if ultrasonic_button.is_pressed:
            distance = proximity.check_proximity()
            tts.say(f"You are {distance} centimeters away from the nearest object.")


# schedule pipeline coroutines as tasks in top-level coroutine
async def main():
    """Top-level coroutine for all pipelines"""
    await asyncio.gather(ocr_pipeline(), ultrasonic_pipeline())

# run top level coroutine
asyncio.run(main())

#TODO: use button callbacks to implement asynchronous features.