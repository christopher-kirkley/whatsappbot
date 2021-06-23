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
    # if 'listen' in incoming_msg:
    #     msg.body("What would you like to listen to?\n" +
    #             "1: Etran de L'Air\n" +
    #             "2: Oumou Diabate & Kara Show\n" + 
    #             "3: Alkibar Gignor\n")
    #     responded = True
    if 'song' in incoming_msg:
        msg.media(random.choice(songs))
        responded = True
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    # if not responded:
    #     msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()
