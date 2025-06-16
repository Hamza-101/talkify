import sys
import os
from googletrans import Translator, LANGUAGES
from TTS.api import TTS

def detect_language(text):
    translator = Translator()
    detected = translator.detect(text)
    print(f"🕵️ Detected language: {LANGUAGES.get(detected.lang, detected.lang)} ({detected.lang})")
    return detected.lang

def translate_text(text, target_lang='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    print(f"🌐 Translated to {LANGUAGES[target_lang]}: {translation.text}")
    return translation.text

def speak(text, model_name="tts_models/en/ljspeech/tacotron2-DDC"):
    print(f"🗣 Speaking: {text}")
    tts = TTS(model_name)
    tts.tts_to_file(text=text, file_path="output.wav")
    os.system("start output.wav" if os.name == "nt" else "aplay output.wav")

def main():
    if len(sys.argv) < 3:
        print("Usage:\n python tts_modes.py <mode: speak|translate> \"<text>\" [target_language_code]")
        return

    mode = sys.argv[1].lower()
    input_text = sys.argv[2]
    target_lang = sys.argv[3] if len(sys.argv) > 3 else "en"

    if mode not in ["speak", "translate"]:
        print("❌ Invalid mode. Use 'speak' or 'translate'")
        return

    detected_lang = detect_language(input_text)

    if mode == "translate":
        if target_lang not in LANGUAGES:
            print(f"❌ Target language '{target_lang}' not supported.")
            return
        if detected_lang == target_lang:
            print("ℹ️ Source and target language are the same. Speaking without translation.")
            speak(input_text)
        else:
            translated_text = translate_text(input_text, target_lang)
            speak(translated_text)
    else:  # speak mode
        speak(input_text)

if __name__ == "__main__":
    main()
