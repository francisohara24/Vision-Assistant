"""Function for recognizing and extracting text from a Pillow Image using the current OCR model.
Current model: Tesseract-OCR (https://github.com/tesseract-ocr/tesseract)
"""
import pytesseract
from PIL import Image
import requests
from google.cloud import vision


def extract_text(image):
    """Check if device is online or offline and call the appropriate extract_text function"""
    request = requests.get("http://clients3.google.com/generate_204")
    if request.status_code == 204:
        return extract_online(image)
    else:
        return extract_offline(image)


def extract_offline(image_path: str) -> str:
    """Extract and return any text contained within `image` using the offline text recognition model.

    Parameters
    ----------
    image : PIL.Image.Image
        The image containing text to be extracted using the OCR model.

    Returns
    -------
    str
        The extracted text if any text was recognized.
        If not, the string "No text was detected" is returned instead.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)

    if len(text) > 0:
        return text

    return "No text was detected!"


def extract_online(image_path: str) -> str:
    """Extract and return any text contained within image located at `image_path` using the cloud-based text recognition model."""

    # instantiate google vision client for text recognition
    client = vision.ImageAnnotatorClient()

    # open image file to be read as binary and extract content
    with open(image_path, "rb") as image_file:
        content = image_file.read()

    # convert image to google vision image format
    image = vision.Image(content=content)

    # send a request for text recognition on the image to the google vision API
    response = client.text_detection(image=image)

    # extract actual text from API response
    texts = [text.description for text in response.text_annotations]

    # join the extracted texts into a single text and return
    return texts[0]


if __name__ == "__main__":
    image = Image.open("../data/rpi_images/image_26.jpg")
    result = extract_text(image)
    print(result)