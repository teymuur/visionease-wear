import pytesseract
import speech_recognition_mod as sr
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

cap = cv2.VideoCapture(1)

def extract_text_from_image(image):
    # Use pytesseract to extract text from the image
    while sr.loop_flag:
        return pytesseract.image_to_string(image, config='--psm 1')

def process_frame_with_ocr(image):
    while True:
        image = cap.read()
        text_from_ocr = extract_text_from_image(image)
        # Print or use the OCR result as needed
        print(f"OCR Result from Entire Image: {text_from_ocr}")
        sr.speak(f"Reading text: {text_from_ocr}")


if __name__ == "__main__":
    process_frame_with_ocr(cap)