import cv2
from picamera2 import Picamera2

# Initialize the camera
camera = Picamera2()

try:
  # Attempt to capture a frame (basic test)
  raw_capture = camera.capture_raw(format="bgr")
except Exception as e:
  print(f"Error capturing frame: {e}")
  exit()
finally:
  # Close the camera regardless of exceptions 
  camera.close()

# We don't need to decode or process the image data for this test

print("picamera2 and cv2 appear to be compatible. No errors encountered during capture.")
