from flask import Flask, request
from twilio.twiml.voice_response import Gather, VoiceResponse
from twilio_helper import handle_voice_call

app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def voice():
    return handle_voice_call(request.form['RecordingUrl'])

if __name__ == '__main__':
    app.run(debug=True)
