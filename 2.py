import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os

load_dotenv()
SPEECH_KEY = os.getenv('AZURE_SPEECH_KEY')
SPEECH_REGION = os.getenv('AZURE_SPEECH_REGION')

# Konfiguracja
speech_config = speechsdk.SpeechConfig(
    subscription=SPEECH_KEY,
    region=SPEECH_REGION
)
speech_config.speech_recognition_language = "pl-PL"

# Mikrofon jako źródło
recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Powiedz coś...")

# Rozpoznaj jedno zdanie
result = recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print(f"Rozpoznano: {result.text}")
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("Nie rozpoznano mowy")
elif result.reason == speechsdk.ResultReason.Canceled:
    print(f"Błąd: {result.cancellation_details.error_details}")
