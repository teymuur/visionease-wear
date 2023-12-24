import pyttsx3
import cv2
import os,sys
                                               
text_speech = pyttsx3.init()
def speak(answer):
    text_speech.say(answer)
    text_speech.runAndWait()

#This is for opening web cam and detecting your face and emotion



