import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os

# Pobranie kluczy Azure Speech
load_dotenv()
SPEECH_KEY = os.getenv('AZURE_SPEECH_KEY', 'twoj-klucz-tutaj')
SPEECH_REGION = os.getenv('AZURE_SPEECH_REGION', 'westeurope')

# Konfiguracja tłumaczenia
translation_config = speechsdk.translation.SpeechTranslationConfig(
    subscription=SPEECH_KEY,
    region=SPEECH_REGION
)

# Język źródłowy (z którego tłumaczysz)
translation_config.speech_recognition_language = "pl-PL"

# Języki docelowe (na które tłumaczysz)
translation_config.add_target_language("en")  # angielski
translation_config.add_target_language("de")  # niemiecki

# Tłumacz z mikrofonu
recognizer = speechsdk.translation.TranslationRecognizer(
    translation_config=translation_config
)

print("Mów po polsku...")
print("-" * 50)


# Funkcja wywoływana po rozpoznaniu
def recognized(evt):
    print(f"\nPolski: {evt.result.text}")

    # Wyświetl tłumaczenia
    for language, translation in evt.result.translations.items():
        if language == "en":
            print(f"Angielski: {translation}")
        elif language == "de":
            print(f"Niemiecki: {translation}")
    print("-" * 50)


# Podłącz event
recognizer.recognized.connect(recognized)

# Rozpocznij ciągłe rozpoznawanie
recognizer.start_continuous_recognition()

import time

while True:
    time.sleep(1)
