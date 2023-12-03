"""Function for recognizing and extracting text from a Pillow Image using the current OCR model.
Current model: Tesseract-OCR (https://github.com/tesseract-ocr/tesseract)
"""
import pytesseract
from PIL import Image


def extract_text(image: Image.Image) -> str:
    """Extract any text contained within `image`.

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
    text = pytesseract.image_to_string(image, timeout=10)

    if len(text) > 0:
        return text

    return "No text was detected!"

if __name__ == "__main__":
    image = Image.open("../data/rpi_images/image_11.jpg")
    result = extract_text(image)
    print(result)