import speech_recognition
import pyttsx3

# Text to speech
text_speech = pyttsx3.init()
def speak(answer):
    text_speech.say(answer)
    text_speech.runAndWait()

# Speech recognition
recognizer = speech_recognition.Recognizer()
def __listen__():
    while True:
        try:
            with speech_recognition.Microphone () as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()   
                print(text)                               
                return text
        except Exception :
            recognizer = speech_recognition.Recognizer()
            continue
def listen():
    while True:
        __listen__()