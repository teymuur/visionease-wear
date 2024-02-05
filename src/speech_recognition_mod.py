##Speech recognition model
import speech_recognition
import pyttsx3

import requests

# Text to speech
text_speech = pyttsx3.init()
text_speech.setProperty("rate",180)


def speak(answer):
    text_speech.say(answer)
    try:
        text_speech.runAndWait()
    except Exception as e:
        print(f"Error in speak function: {e}")

text = None
# Speech recognition
recognizer = speech_recognition.Recognizer()
loop_flag= True
def __listen__():
    while True:
        try:
            with speech_recognition.Microphone () as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()   
                print(text)  
                if "000" in text:
                    return -2
                return text                             

        except Exception :
            recognizer = speech_recognition.Recognizer()
            continue
def getweather():
    api_key = open('weather_api_key.txt', 'r').read()
    while loop_flag:
        
        location = "Baku"

        result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')
        if result.json()['cod'] == '404':
            print("Invalid location!")
            continue
        break
    
    description = result.json()['weather'][0]['description']
    temperature = round(result.json()['main']['temp'])
    feels_like = round(result.json()['main']['feels_like'])
    high = round(result.json()['main']['temp_max'])
    low = round(result.json()['main']['temp_min'])

    speak(f"The weather in {location[0].upper()}{location[1:]} is {temperature}° C with {description}.It feels like {feels_like}° C. Today's high is {high}° C and today's low is {low}° C.")

def listen():
    global loop_flag
    while loop_flag:
        t  = __listen__()
        if t ==-2:
            speak("I aint gonna shut up. Just Kidding, Bye")
            loop_flag = False
        elif "zenith"in t :
            if "for all my" in t and "know me" in t:
                speak("I feel like me and Taylor might still have sex")
                speak("Why .. I made that bitch famous... Goddamn")
                speak("For all the girls that got dick from Kanye West.. they just mad they aint famous.. Goddamn")
            elif "w men's" in t:
                speak("Hell yeah brother")
                continue
            elif "weather" in t: 
                getweather()
                continue
            elif "help" in t:
                speak("There a multiple stuff i can help you with please be more specific")
            elif "direct me" in t:
                # soon to be added
                continue
            elif "i love you" in t:
                speak("i love you too bro")
            elif "fuck you" in t:
                speak("Fuck you too T. you wanna start a robot fight huh?")
            elif "kill myself" in t:
                speak('''Hey Bro,

    I've noticed you might be going through a tough time, and I want you to know I'm here for you. Your feelings are valid, and it's okay to ask for help. If you're comfortable, I'm here to listen. Remember, seeking support is a sign of strength, not weakness. Reach out to someone you trust or consider talking to a professional. You're not alone, and I care about you.

    Take care,''') 
            elif "thank you T" in t:
                speak("No problem")

if __name__ == "__main__":
    print(listen())