from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# Pobranie klucza OpenAI
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY_2')

# Inicjalizacja klienta OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Model do użycia
model = "gpt-3.5-turbo"
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('flask2.1.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_prompt = request.form.get('question')

    conversation_history_json = request.form.get('history', '[]')
    conversation_history = json.loads(conversation_history_json)

    conversation_history.append({"role": "user", "content": user_prompt})

    response = client.chat.completions.create(
        model=model,
        messages=conversation_history,
        temperature=0.7
    )

    answer = response.choices[0].message.content

    conversation_history.append({"role": "assistant", "content": answer})

    history_json = json.dumps(conversation_history)

    return render_template('flask2.1.html', question=user_prompt, answer=answer, history=history_json)




if __name__ == '__main__':
    app.run(debug=True, port=5005)
