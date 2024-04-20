##Speech recognition model
import speech_recognition as sr
import pyttsx3
import qr_detection as qr
import requests
import time
# Text to speech
engine = pyttsx3.init()
engine.setProperty("rate",180)

sample = '''Artificial intelligence (AI) stands at the forefront of innovation in today's rapidly advancing technological landscape. With its ability to analyze vast amounts of data and make intelligent decisions, AI has revolutionized numerous industries, from healthcare to finance, manufacturing to transportation. This sample text serves to illustrate the transformative power of AI and technology.

AI algorithms are continuously evolving, becoming more adept at understanding complex patterns and making predictions with remarkable accuracy. Whether it's optimizing supply chains, personalizing user experiences, or detecting fraudulent activities, AI-powered solutions are reshaping the way businesses operate. Moreover, AI-driven automation is streamlining processes, reducing costs, and increasing efficiency across various sectors.

Furthermore, the integration of AI into everyday devices is making our lives more convenient and interconnected. From smart assistants that anticipate our needs to autonomous vehicles that navigate the streets safely, AI is enabling a future where technology seamlessly enhances human capabilities.

As AI continues to advance, it's crucial to consider the ethical implications and ensure that its development remains aligned with societal values. From data privacy concerns to potential job displacement, addressing these challenges is essential to harnessing the full potential of AI for the benefit of humanity.

This sample text serves as a glimpse into the transformative power of AI and technology, illustrating its potential to reshape industries and improve lives. As we navigate this technological revolution, embracing innovation while prioritizing ethical considerations will be key to unlocking a future where AI enhances our world in meaningful ways.
'''

def speak(answer):
    engine.say(answer)
    try:
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speak function: {e}")

text = None
# Speech recognition
recognizer = sr.Recognizer()
loop_flag= True
def __listen__():
    while True:
        try:
            with sr.Microphone () as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()   
                print(text)  
                if "000" in text:
                    return -2
                return text                             

        except Exception :
            recognizer = sr.Recognizer()
            continue
def getweather():
    api_key = open('src/weather_api_key.txt', 'r').read()
    while loop_flag:
        print("ok")
        location = "Muscat"

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
            break
        elif "vision" in t :
            if "w men's" in t:
                speak("Hell yeah brother")
                continue
            elif "weather" in t: 
                getweather()
                continue
            elif "text" in t:
                time.wait(4)
                speak(sample)
            elif "help" in t:
                speak("There a multiple stuff i can help you with please be more specific")
            elif "open website" in t:
                url_start_index = text.find("open website") + len("open website")
                website_url = text[url_start_index:].strip()
                qr.read_website(website_url)
                continue
            elif "i love you" in t:
                speak("i love you too bro")
            # elif "fuck you" in t:
            #     speak("Fuck you too T. you wanna start a robot fight huh?")
            elif "kill myself" in t:
                speak('''Hey Bro,

    I've noticed you might be going through a tough time, and I want you to know I'm here for you. Your feelings are valid, and it's okay to ask for help. If you're comfortable, I'm here to listen. Remember, seeking support is a sign of strength, not weakness. Reach out to someone you trust or consider talking to a professional. You're not alone, and I care about you.

    Take care,''') 
            elif "thank you T" in t:
                speak("No problem")
            
            else:
                speak("Sorry I didnt get that")

if __name__ == "__main__":
    # speak("hello world")
    
    print(listen())