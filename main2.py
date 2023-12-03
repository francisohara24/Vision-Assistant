from ai_reader import ocr
from ai_reader import capture_image
from ai_reader import proximity
from ai_reader import tts
from gpiozero import Button
import time
import pytesseract # for testing
from PIL import Image


def ocr_pipeline():
    """Run the text recognition and speech synthesis pipeline of the project."""
    while True:
        if ocr_button.is_pressed:
            # test code
            capture_image.capture()
            image = Image.open("test.jpg")
            # test code
            #image = capture_image.capture()
            text = ocr.extract_text(image)
            tts.say(text)
            time.sleep(0.25)


def ultrasonic_pipeline():
    """Run the ultrasonic proximity detection pipeline of the project."""
    while True:
        if ultrasonic_button.is_pressed:
            distance = proximity.check_proximity()
            tts.say(f"You are {distance} centimeters away from the nearest object.")


# schedule pipeline coroutines as tasks in top-level coroutine
if __name__ == "__main__":
    # indicate to user that device is working
    tts.say("Power On!")

    # define buttons for triggering pipelines
    ocr_button = Button(17)
    ultrasonic_button = Button(27)

    # assign button callbacks to pipeline functions
    ocr_button.when_pressed = ocr_pipeline
    ultrasonic_button.when_pressed = ultrasonic_pipeline

    while True:
        pass
