import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os
import time

# Initialize translator and recognizer
translator = Translator()
recognizer = sr.Recognizer()

def translate_speech(source_lang='en', target_lang='te'):
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)

        try:
            # Step 1: Recognize Speech
            text = recognizer.recognize_google(audio, language=source_lang)
            print(f"🗣️ You said: {text}")

            # Step 2: Translate
            translated = translator.translate(text, src=source_lang, dest=target_lang)
            print(f"🌍 Translated: {translated.text}")

            # Step 3: Convert to speech and play
            tts = gTTS(text=translated.text, lang=target_lang)
            filename = "temp_audio.mp3"
            tts.save(filename)
            playsound.playsound(filename)
            os.remove(filename)

        except Exception as e:
            print("❌ Error:", e)

# Run continuously
while True:
    translate_speech('en', 'te')  # English to Telugu
    time.sleep(1)
