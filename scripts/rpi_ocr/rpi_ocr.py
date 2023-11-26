"""Test Tesseract-OCR on Raspberry Pi."""
import pytesseract


print(pytesseract.image_to_string("data/image_2.png"))