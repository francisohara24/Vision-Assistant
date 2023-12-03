"""Function for recognizing and extracting text from a Pillow Image using the current OCR model.
Current model: Tesseract-OCR (https://github.com/tesseract-ocr/tesseract)
TODO: Implement Online mode vs Offline mode
"""
import pytesseract
from PIL import Image
import requests


def extract_text(image):
    """Check if device is online or offline and call the appropriate extract_text function"""
    request = requests.get("http://clients3.google.com/generate_204")
    if request.status_code == 204:
        extract_online(image)
    else:
        extract_offline(image)


def extract_offline(image: Image.Image) -> str:
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
    text = pytesseract.image_to_string(image)

    if len(text) > 0:
        return text

    return "No text was detected!"


def extract_online(image: Image.Image) -> str:
    """Extract and return any text contained within `image` using the cloud-based text recognition model."""
    return "You are online!"


if __name__ == "__main__":
    image = Image.open("../data/rpi_images/image_26.jpg")
    result = extract_text(image)
    print(result)