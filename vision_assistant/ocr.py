"""Function for recognizing and extracting text from a Pillow Image using the current OCR model.
Offline model: Tesseract-OCR (https://github.com/tesseract-ocr/tesseract)
Online model: Google Vision API (https://cloud.google.com/vision?hl=en)
"""
# import required libraries
import pytesseract
import requests
from google.cloud import vision


def extract_text(image_path: str) -> str:
    """Check if device is online or offline and call the appropriate extract_text function

    Parameters
    ----------
    image_path : str
        The path to an image file containing text.

    Returns
    -------
    str
        The text extracted from the image using either the offline or online ocr function.
    """
    # check if connected to internet
    request = requests.get("http://clients3.google.com/generate_204")
    if request.status_code == 204:
        return extract_online(image_path)  # when online
    else:
        return extract_offline(image_path)  # when offline


def extract_offline(image_path: str) -> str:
    """Extract and return any text contained within image located at `image_path` using the offline text recognition model.

    Parameters
    ----------
    image_path : str
        The path to the image containing text to be extracted using the OCR model.

    Returns
    -------
    str
        The extracted text if any text was recognized.
        If not, the string "No text was detected" is returned instead.
    """
    # extract text from image using Tesseract-OCR
    text = pytesseract.image_to_string(image_path)

    # return extracted text or prompt user if no text could be found
    if len(text) > 0:
        return text
    return "No text was detected!"


def extract_online(image_path: str) -> str:
    """Extract and return any text contained within image located at `image_path` using the cloud-based text recognition
     model.

     Parameters
    ----------
    image_path : str
        The path to the image containing text to be extracted using the OCR model.

    Returns
    -------
    str
        The extracted text if any text was recognized.
        If not, the string "No text was detected" is returned instead.
        If there was an error with the API request, the string "Sorry. Please try again." is returned instead.

    """

    # instantiate google vision client for text recognition
    client = vision.ImageAnnotatorClient()

    # open image file to be read and extract file content
    with open(image_path, "rb") as image_file:
        content = image_file.read()

    # convert image to google vision image format
    image = vision.Image(content=content)

    # send request for text recognition using the client
    response = client.text_detection(image=image)

    # check if request was unsuccessful due to API errors.
    if response.error.message:
        return "Sorry. Please try again."

    try:
        # if request successful, extract actual text from response if any
        text = response.text_annotations[0].description
        return text

    except IndexError:
        return "No text was detected."


# main script for testing the module
if __name__ == "__main__":
    image_path = "./Projects/Vision-Assistant/data/rpi_images/image_26.jpg"
    result = extract_text(image_path)
    print(result)
