import pyttsx3
import cv2
import os,sys
import numpy as np
                                               
text_speech = pyttsx3.init()
def speak(answer):
    text_speech.say(answer)
    text_speech.runAndWait()

#This is for opening web cam and detecting your face and emotion


def get_output_layers(net):
    layer_names = net.getUnconnectedOutLayersNames()
    return [net.getLayerNames()[i[0] - 1] for i in layer_names]

def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    confidence_percentage = round(confidence * 100, 2)
    distance = round((2 * 3.14 * 180) / (w + h * 360.0), 2)
    
    print(f"Object: {label}, Confidence: {confidence_percentage}%, Distance: {distance} units")

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
cap = cv2.VideoCapture(0)

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
<<<<<<< HEAD

=======
>>>>>>> 8873993b0d4ec4804b74b66bbbef53756e981e57
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
    cv2.imshow("Object Detection", frame)

<<<<<<< HEAD

=======
>>>>>>> 8873993b0d4ec4804b74b66bbbef53756e981e57
    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()


