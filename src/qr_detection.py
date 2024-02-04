import cv2
from pyzbar.pyzbar import decode
import speech_recognition as sr

cap = cv2.VideoCapture(0)
cap. set (3,640)
cap.set(4,480)

def qr():
    while True:
        success, img = cap.read()
        for barcode in decode(img):
            print(barcode. data)
            myData = barcode.data.decode('utf-8')
            print(myData)
        cv2. imshow('Result',img)
        cv2.waitKey(1)

if __name__ == "__name__":
    qr()
