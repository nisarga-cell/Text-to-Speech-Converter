from flask import Flask, render_template, request
from gtts import gTTS
import os

app = Flask(__name__)

# Ensure the static directory exists
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    language = request.form['language']
    try:
        tts = gTTS(text=text, lang=language, slow=False)
        audio_path = os.path.join('static', 'welcome.mp3')
        tts.save(audio_path)
        print(f"Audio file saved at: {audio_path}")
        if os.path.exists(audio_path):
            print("File exists and ready to be played.")
        else:
            print("File was not created.")
    except Exception as e:
        print(f"Error generating audio: {e}")
        return render_template('index.html', error=str(e))
    return render_template('index.html', audio_file=audio_path)

if __name__ == '__main__':
    app.run(debug=True)
