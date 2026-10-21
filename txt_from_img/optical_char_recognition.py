#!/usr/bin/env python3

"""
See documentation:
    https://tesseract-ocr.github.io/tessdoc/

tesseract
    - https://github.com/tesseract-ocr/tesseract
tessdata
    - https://github.com/tesseract-ocr/tessdata_best (accuracy)
    - https://github.com/tesseract-ocr/tessdata_fast (speed)
    Special data files
        - https://github.com/tesseract-ocr/tessdata/raw/3.04.00/osd.traineddata (Orientation and script)
        - https://github.com/tesseract-ocr/tessdata/raw/3.04.00/equ.traineddata (Math / equation)

Installation
    - install tesseract-ocr binaries
    - install dependencies
        pip install pytesseract
        pip install pillow
    - copy and paste traineddata into 'C:\\Program Files\\Tesseract-OCR\\tessdata'
"""


from PIL import Image
import pytesseract
import os


this_path = os.path.dirname(__file__)
img_path = os.path.join(this_path, 'test_english.png')
image = Image.open(img_path)

text = pytesseract.image_to_string(image)

print(text)

img_path = os.path.join(this_path, "test_portuguese.png")
image = Image.open(img_path)

text = pytesseract.image_to_string(image)

print(text)

img_path = os.path.join(this_path, "test_equation.png")
image = Image.open(img_path)

text = pytesseract.image_to_string(image)

print(text)

