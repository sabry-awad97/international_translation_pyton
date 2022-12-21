from deep_translator import GoogleTranslator
import speech_recognition as sr
import gtts


def translate(text: str, target_lang):
    translator = GoogleTranslator(source='auto', target=target_lang)
    return translator.translate(text)


def recognize_voice(lang: str) -> str:
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Speak Now 🎙️")
            voice = recognizer.listen(source)
            text = recognizer.recognize_google(voice, language=lang)
            return text
    except:
        pass


def saveAudio(filename, text, target_lang):
    google_audio = gtts.gTTS(text, lang=target_lang)
    google_audio.save(filename)
