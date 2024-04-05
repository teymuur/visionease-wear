import speech_recognition_mod as sr
from gtts import gTTS
import os
from playsound import playsound
from googletrans import Translator

def translate(text, target_language='ar'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def speak(text, language='ar'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("src/output.mp3")
    playsound("./src/output.mp3")  # Added "./" to specify the full path to the file
    os.remove("src/output.mp3")

if __name__ == "__main__":
    
    while True:
        original_text = sr.__listen__()
        translated_text = translate(original_text)
        print("Translated:", translated_text)
        speak(translated_text)