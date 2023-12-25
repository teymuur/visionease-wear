import pyttsx3
import cv2
import threading
import numpy as np
import speech_recognition_mod as sr




def get_output_layers(net):
    layer_names = net.getUnconnectedOutLayersNames()
    return [layer_names[i[0] - 1] for i in enumerate(net.getLayerNames()) if i[0] - 1 in layer_names]


announced_objects = {}

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

    # Break the loop when 'q' key is pressed
    if  cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
