from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('flask1.html')

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.form.get('text')
    print(f"Przyszły dane {text}")
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
