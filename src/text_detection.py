import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import speech_recognition_mod as sr

def extract_text_from_image(image):
    # Use pytesseract to extract text from the image
    while sr.loop_flag:
        return pytesseract.image_to_string(image, config='--psm 1')

def process_frame_with_ocr():
    global frame
    text_from_ocr = extract_text_from_image(frame)
     # Print or use the OCR result as needed
    print(f"OCR Result from Entire Image: {text_from_ocr}")
    sr.speak(f"Reading text: {text_from_ocr}")
