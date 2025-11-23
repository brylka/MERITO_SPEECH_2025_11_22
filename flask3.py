from flask import Flask, render_template, request, jsonify
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os
import io
from pydub import AudioSegment

load_dotenv()

app = Flask(__name__)

SPEECH_KEY = os.getenv('AZURE_SPEECH_KEY')
SPEECH_REGION = os.getenv('AZURE_SPEECH_REGION')


@app.route('/')
def index():
    return render_template('flask3.html')


@app.route('/recognize', methods=['POST'])
def recognize():
    # Pobierz audio
    audio_file = request.files['audio']
    audio_data = audio_file.read()

    # Konwersja webm -> WAV 16kHz mono
    audio = AudioSegment.from_file(io.BytesIO(audio_data))
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)

    wav_buffer = io.BytesIO()
    audio.export(wav_buffer, format='wav')
    wav_data = wav_buffer.getvalue()

    # Konfiguracja Azure
    speech_config = speechsdk.SpeechConfig(SPEECH_KEY, SPEECH_REGION)
    speech_config.speech_recognition_language = "pl-PL"

    # Rozpoznawanie
    stream = speechsdk.audio.PushAudioInputStream()
    audio_config = speechsdk.audio.AudioConfig(stream=stream)
    recognizer = speechsdk.SpeechRecognizer(speech_config, audio_config)

    stream.write(wav_data)
    stream.close()

    result = recognizer.recognize_once()

    # Zwróć wynik
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return jsonify({'success': True, 'text': result.text})
    else:
        return jsonify({'success': False, 'error': 'Nie rozpoznano mowy'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)