import speech_recognition

recognizer = speech_recognition.Recognizer()
while True:
    try:
        with speech_recognition.Microphone () as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
                                                                
            print(text)
    except speech_recognition.UnknownValueError():
        recognizer = speech_recognition.Recognizer()
        continue
