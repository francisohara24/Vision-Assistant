"""Test Tesseract-OCR on Raspberry Pi."""
import pytesseract

# extrect text from image_2
text = pytesseract.image_to_string("data/image_1.png")
print(text)