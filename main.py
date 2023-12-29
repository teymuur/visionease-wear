import cv2
import threading
import numpy as np
import speech_recognition_mod as sr
import pytesseract

def get_output_layers(net):
    layer_names = net.getUnconnectedOutLayersNames()
    return [layer_names[i[0] - 1] for i in enumerate(net.getLayerNames()) if i[0] - 1 in layer_names]


announced_objects = {}
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def extract_text_from_image(image):
    # Use pytesseract to extract text from the image
    return pytesseract.image_to_string(image, config='--psm 6')


def process_frame_with_ocr(frame):
    # Perform OCR on the entire frame
    text_from_ocr = extract_text_from_image(frame)

    # Print or use the OCR result as needed
    print(f"OCR Result from Entire Image: {text_from_ocr}")
    sr.speak(f"Reading text: {text_from_ocr}")
# Modify the draw_prediction function
def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    confidence_percentage = round(confidence * 100, 2)
    distance = round((2 * 3.14 * 180) / (w + h * 360.0), 2)

    key = (label, distance)  # Use a tuple as the key
    if key not in announced_objects:
        announced_objects[key] = True  # Mark the object as announced
        print(f"Object: {label}, Confidence: {confidence_percentage}%, Distance: {distance} units")
        sr.speak(f"{label} is {distance} units away")

    color = COLORS[class_id]
    cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 2)
    cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = get_output_layers(net)

# Generate random colors for different classes
np.random.seed(42)
COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

# Open webcam
cap = cv2.VideoCapture(1)
def object_detection_mode():
    global w,h
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        
        # Get the frame dimensions
        height, width, channels = frame.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing information on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])



        # Apply non-max suppression to avoid duplicate detections
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        # Display the results
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                draw_prediction(frame, class_ids[i], confidences[i], x, y, x + w, y + h)

        # Display the frame
        cv2.imshow("VisionEase Wear by Teymur and Sanam SABIS(R) STARS 2024", frame)
        # process_frame_with_ocr(frame)
        # Break the loop when 'q' key is pressed
        if  cv2.waitKey(1) == ord('q'):
            break

# Create two threads
thread_1 = threading.Thread(target=object_detection_mode)
thread_2 = threading.Thread(target=sr.listen)

# Start the threads
thread_1.start()
thread_2.start()

# Wait for both threads to finish (although they run indefinitely in this example)
thread_1.join()
thread_2.join()

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
