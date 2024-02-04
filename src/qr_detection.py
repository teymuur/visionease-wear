import cv2
from pyzbar.pyzbar import decode
import numpy as np
import speech_recognition_mod as sr
import time

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

    cv2.imshow('Result',img)
    cv2.waitKey(1)