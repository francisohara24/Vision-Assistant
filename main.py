from ai_reader import ocr
from ai_reader import capture_image
from ai_reader import proximity
from ai_reader import tts
from gpiozero import Button
from PIL import Image
import threading
import time


# define buttons for triggering pipelines
ocr_button = Button(17)
ultrasonic_button = Button(27)


# function for triggering text reading pipeline
def ocr_pipeline():
    """Run the text recognition and speech synthesis pipeline of the project."""
    while True:
        if ocr_button.is_pressed:
            image_path = capture_image.capture()
            image = Image.open(image_path)
            text = ocr.extract_text(image)
            print(text)
            #tts.say(text)
            time.sleep(1)


# function for triggering distance measurement pipeline
def ultrasonic_pipeline():
    """Run the ultrasonic proximity detection pipeline of the project."""
    while True:
        if ultrasonic_button.is_pressed:
            distance = proximity.check_proximity()
            tts.say(f"You are {distance} centimeters away from the nearest object.")
            time.sleep(1)


# schedule pipeline coroutines as tasks in top-level coroutine
if __name__ == "__main__":
    ocr_thread = threading.Thread(target=ocr_pipeline)
    ultrasonic_thread = threading.Thread(target=ultrasonic_pipeline)
    ocr_thread.start()
    ultrasonic_thread.start()
