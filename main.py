import os
from playsound import playsound
from lib import recognize_voice, translate, saveAudio


original_lang = "en-US"
target_lang = "de"

audio_file = os.path.join(os.getcwd(), f'audio_{original_lang}_{target_lang}.mp3')

if __name__ == '__main__':
    original_text = recognize_voice(original_lang)
    print(f"original text in {original_lang}: {original_text}")
    translated_text = translate(original_text, target_lang)
    print(f"translated_text in {target_lang}: {translated_text}")

    saveAudio(audio_file, translated_text, target_lang)
    playsound(audio_file)
