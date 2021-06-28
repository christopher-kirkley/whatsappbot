from flask import Flask, request, send_file
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
from pathlib import Path
import random

from config import *

app = Flask(__name__)

songs = SONGS

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'song' in incoming_msg:
        msg.media(random.choice(songs))
        responded = True
    return str(resp)


if __name__ == '__main__':
    app.run()
