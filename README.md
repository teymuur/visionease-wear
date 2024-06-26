# VisionEase Wear- public name SoundSight
Technology for a better future
## What is this
VisionEase Wear is the concept of pair of glasses that detects obstacles around and assists visually impaired people with audio feedback. This will ease their life and will not only be informed about obstacles but also help them quickly recognize documents and qr codes by directly reading the text or the content of the qr code, for example, a qr menu. People who has access to this device wont need to learn complicated reading and writing systems like Braille. 
## How we will do it
We will take regular pair of glasses for people with low vision or sunglasses for people with no vision at all and attach a small camera and integrate it to the arduino UNO R3 microcontrollers or raspberry pi that would be the processor of our device. Both of these chips can easily be connected to earphones with 3.55 mm AUX of USB. Image recognition wont be that hard as I am already experienced with both text-to-speech and image recognition software in Python(https://teymuur.github.io/mood-detector-py-by-ty.zip). The whole setup will be affordable and if project expands, people from all background will be able to use it as it would be cheaper than most of assistive technology.
Certainly! Below is the documentation for the provided Python script that utilizes YOLO (You Only Look Once) for object detection and integrates speech recognition and text-to-speech functionalities. This script runs on a Raspberry Pi. The documentation includes instructions on how to set it up.

---

## Requirements

- Raspberry Pi (Tested on Raspberry Pi 4 Model B)
- Webcam
- Python 3.7 or later
- OpenCV
- NumPy
- SpeechRecognition
- pyttsx3
- Tesseract
- Pyzbar
- PyGame
- Spotipy


## Installation

1. **Install OpenCV:**
   ```bash
   pip install opencv-python
   ```

2. **Install NumPy:**
   ```bash
   pip install numpy
   ```

3. **Install SpeechRecognition:**
   ```bash
   pip install SpeechRecognition
   pip install pyaudio
   ```
   If pyaudio module doesnt install properly make sure to install it manually via wheel as it is a very glitchy module.

4. **Install pyttsx3:**
   ```bash
   pip install pyttsx3
   ```

5. **Install tesseract:**
   ```bash
   pip install pytesseract
   ```
> [!IMPORTANT]
> If you are on windows make sure install it properly via executable.
More info about installation [tessdoc](https://tesseract-ocr.github.io/tessdoc/Installation.html)
6. **Install pyzbar**
   ```bash
   pip install pyzbar
   ```
7. **Install Spotipy**
      ```bash
   pip install spotipy
   pip install pygame
   ```
## Setup

1. **Download YOLO Weights and Config File:**
   - Download the YOLOv3 weights file (`yolov3.weights`) and the configuration file (`yolov3.cfg`) from the official YOLO website.

2. **Download COCO Names File:**
   - Download the COCO class names file (`coco.names`) from the official YOLO website.

3. **Connect Webcam:**
   - Connect the webcam to the Raspberry Pi.

4. **Run the Script:**
   - Place the script files (`main.py`, `speech_recognition_mod.py` and `qr_detection.py`) in the same directory as the YOLO files.
   - Run the script using the following command:
     ```bash
     python main.py
     ```
   
5. **Interaction:**
   - The script will start the webcam and display the real-time video feed with detected objects.
   - Detected objects will be announced using text-to-speech.
   - Press 'q' to exit the script.

## Troubleshooting

- If the script fails to recognize the microphone, ensure that the microphone is properly connected to the Raspberry Pi.

- If you encounter issues with YOLO weights or configurations, double-check the file paths in the `main.py` script.

## Customization

- You can customize the YOLO configuration and weights files for different detection tasks.

- Adjust the confidence threshold (`0.5`) in the `main.py` script to control the object detection sensitivity.

- Modify the `draw_prediction` function in `main.py` to change how detected objects are displayed on the video feed.

## Conclusion

VisionEase Wear provides a simple yet effective solution for real-time object detection and announcement using YOLO, speech recognition, and text-to-speech on a Raspberry Pi.

## About Us
Even tho it would take a lot of effort to build a prototype of VisionEase Wear, we believe that it could be the winner of SABIS® STARS and help thousands of people  have a better future and easier lives. We are planning to make the code of this device open source so a lot of people can just download it and can make their own glasses by connecting a camera to a microcontroller. 
## Resources used
- [yelov3.weights](https://pjreddie.com/media/files/yolov3.weights)
- [yelov3.cfg](https://pjreddie.com/media/files/yolov3.cfg)
- [coco.names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)
- [tesseract](https://github.com/tesseract-ocr/tesseract)
# More than a SABIS(R) STARS Science fair project✨

Copyright Teymur Babayev (C) 2023-2024

[BSD 3 clause license](LICENSE)


[my website](https://teymuur.github.io)

[my other work](https://github.com/teymuur)

[instagram](https://instagram.com/teyymuurr)
