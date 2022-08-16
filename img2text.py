from PIL import Image
from pytesseract import pytesseract
path_to_tesseract = 'tesseract'


def get_text(img_loc):
    pytesseract.tesseract_cmd = path_to_tesseract
    img = Image.open(img_loc)
    text = pytesseract.image_to_string(img)
    return text

