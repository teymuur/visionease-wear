##Qr detection model
from pyzbar.pyzbar import decode
import cv2

import numpy as np
import time
import requests
from bs4 import BeautifulSoup

import speech_recognition_mod as sr

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)


scanned_qr_codes = {}

while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255,0,255),2)
        

        if myData not in scanned_qr_codes or (time.time() - scanned_qr_codes[myData]) > 300:

            sr.speak(f"QR Code Decoded: {myData}")
            print(f"QR Code Decoded: {myData}")

            # Update the scanned QR codes list with the current time
            scanned_qr_codes[myData] = time.time()

            # Check if the data is a URL
            if myData.startswith('http'):
                response = requests.get(myData)
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text()
                sr.speak(text)