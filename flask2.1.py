from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

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

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": user_prompt}],
        temperature=0.7
    )

    answer = response.choices[0].message.content

    return render_template('flask2.1.html', question=user_prompt, answer=answer)




if __name__ == '__main__':
    app.run(debug=True, port=5005)
