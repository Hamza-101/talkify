import sys
from googletrans import Translator, LANGUAGES

def TextToText():
    if len(sys.argv) < 3:
        print("Usage: python translate_file.py <input_file> <target_language_code>")
        sys.exit(1)

    input_file = sys.argv[1]
    target_lang = sys.argv[2]

    if target_lang not in LANGUAGES:
        print(f"❌ Error: Target language '{target_lang}' is not supported.")
        print("👉 Use one of the following language codes:")
        print(", ".join(sorted(LANGUAGES.keys())))
        sys.exit(1)

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"❌ Error: File not found: {input_file}")
        sys.exit(1)

    translator = Translator()
    try:
        detected = translator.detect(text)
    except Exception as e:
        print(f"❌ Error during language detection: {e}")
        sys.exit(1)

    source_lang = detected.lang

    if source_lang not in LANGUAGES:
        print(f"❌ Error: Detected language '{source_lang}' is not supported for translation.")
        sys.exit(1)

    print(f"✅ Detected language: {LANGUAGES[source_lang]} ({source_lang})")

    if source_lang == target_lang:
        print("⚠️  Source and target languages are the same. No translation performed.")
        sys.exit(0)

    try:
        translation = translator.translate(text, src=source_lang, dest=target_lang)
    except Exception as e:
        print(f"❌ Error during translation: {e}")
        sys.exit(1)

    print(f"\n--- 📝 Translated Text ({LANGUAGES[target_lang]}): ---\n")
    print(translation.text)

if __name__ == "__main__":
    TextToText()
