import os
import pytesseract
from pathlib import Path
from PIL import Image, ImageFilter

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

folder = 'input'
for file in os.listdir(folder):
    path = os.path.join(folder, file)
    image = Image.open(path)
    width, height = image.size
    image.resize((width * 10, height * 10))
    image.filter(ImageFilter.SHARPEN)
    text = pytesseract.image_to_string(image, lang='chi_sim')
    with open(f'output/{Path(path).stem}.txt', 'wb+') as output_file:
        output_file.write(text.encode('utf8'))
