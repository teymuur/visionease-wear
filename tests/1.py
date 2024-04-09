import speech_recognition as sr 
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening...")
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")
    except Exception as e:
        print(f"{e} ")
    return query

print(takeCommand())

