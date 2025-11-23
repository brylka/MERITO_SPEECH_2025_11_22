from flask import Flask, render_template, request, send_file
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os
import io

# Pobranie kluczy Azure Speech
load_dotenv()
SPEECH_KEY = os.getenv('AZURE_SPEECH_KEY', 'twoj-klucz-tutaj')
SPEECH_REGION = os.getenv('AZURE_SPEECH_REGION', 'westeurope')

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('flask1.html')

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.form.get('text')

    # Konfiguracja Azure
    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION
    )

    # Ustaw głos polski (kobieta: Zofia, mężczyzna: Marek)
    speech_config.speech_synthesis_voice_name = "pl-PL-MarekNeural"

    # Syntezator mowy
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=None
    )

    # Zamień tekst na mowę
    result = synthesizer.speak_text_async(text).get()

    return send_file(
        io.BytesIO(result.audio_data),
        mimetype='audio/wav',
        as_attachment=True,
        download_name='speech.wav'
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
