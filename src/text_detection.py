import pytesseract
import cv2
import picamera2

from picamera2.picamera2 import PreviewRequest, CaptureRequest

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

previous_text = set()


def process_image(image):
    # Convert the image to grayscale for better OCR accuracy
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to enhance text visibility
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Use Tesseract OCR to extract text from the thresholded image
    text = pytesseract.image_to_string(thresholded, config='--psm 6')
    return text


def main():
    # Initialize the camera with a preview stream
    camera = picamera2.Picamera2()
    camera.configure(PreviewRequest(640, 480))  # Set resolution

    # Create a capture callback to process incoming frames
    def capture_callback(image):
        text = process_image(image.planes[0].array)  # Access image data directly

        # Display the original frame (can be removed for efficiency)
        cv2.imshow('Original Frame', image.planes[0].array)

        if text.strip() not in previous_text:
            # Text-to-speech using your preferred library (replace with sr.speak())
            print(f"Reading text: {text}")
            previous_text.add(text.strip())

    camera.start_preview(capture_callback=capture_callback)

    # Wait for user input to quit
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up resources
    camera.stop_preview()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
