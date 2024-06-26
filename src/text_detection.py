##Text detection module
import pytesseract
import cv2

import speech_recognition_mod as sr

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

previous_text = set()

def process_frame(frame):
    # Convert the frame to grayscale for better OCR accuracy
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to enhance text visibility
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Use Tesseract OCR to extract text from the thresholded image
    text = pytesseract.image_to_string(thresholded,config='--psm 6')
    return text

def main():
    # Open a connection to the camera (0 represents the default camera)
    cap = cv2.VideoCapture(1)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame. Exiting...")
            break

        # Process the frame to extract text
        text = process_frame(frame)

        # Display the original frame and the extracted text
        cv2.imshow('Original Frame', frame)
        if text.strip() not in previous_text:
        # Print the extracted text
    
            sr.speak(f"{text}")
        # Add the detected text to the set of previous text
            previous_text.add(text.strip())

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()