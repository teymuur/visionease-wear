import pyzbar.pyzbar as decode
import cv2
import time
import requests
from bs4 import BeautifulSoup

import speech_recognition_mod as sr

from picamera2 import Picamera2

camera = Picamera2()
scanned_qr_codes = {}


def read_website(url):
    if url.startswith('http'):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        sr.speak(text)


def main():
    # Configure a preview stream for continuous image capture
    camera.configure(PreviewRequest(640, 480))  # Set resolution

    def capture_callback(image):
        # Convert the image data to OpenCV format (optional for QR decoding)
        frame = image.planes[0].array.copy()

        # Decode QR codes from the frame
        for barcode in decode(frame):
            data = barcode.data.decode('utf-8')
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))

            # Draw bounding box and text on the frame
            cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
            pts2 = barcode.rect
            cv2.putText(frame, data, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

            if data not in scanned_qr_codes or (time.time() - scanned_qr_codes[data]) > 300:
                sr.speak(f"QR Code Decoded: {data}")
                print(f"QR Code Decoded: {data}")

                # Update scanned QR codes list and handle website reading
                scanned_qr_codes[data] = time.time()
                if data.startswith('http'):
                    read_website(data)

        # Display the frame (can be removed for efficiency)
        cv2.imshow('QR Code Detector', frame)

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
