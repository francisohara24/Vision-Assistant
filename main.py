# import required libraries
from ai_reader import ocr
from ai_reader import capture_image
from ai_reader import proximity
from ai_reader import tts
from gpiozero import Button
import threading
import time


# define GPIO buttons for triggering each pipeline
ocr_button = Button(17)
ultrasonic_button = Button(27)


# function for triggering text reading pipeline
def ocr_pipeline():
    """Run the text recognition and speech synthesis pipeline of the project."""
    while True:
        if ocr_button.is_pressed:
            # capture an image with the camera
            image_path = capture_image.capture()

            # extract text from the captured image
            text = ocr.extract_text(image_path)

            # print the extracted text for remote debugging purposes with SSH
            print(text)

            # read aloud the extracted text
            tts.say(text)
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
    tts.say("Power On!")
    ocr_thread = threading.Thread(target=ocr_pipeline)
    ultrasonic_thread = threading.Thread(target=ultrasonic_pipeline)
    ocr_thread.start()
    ultrasonic_thread.start()
