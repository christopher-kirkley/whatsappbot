from flask import Flask, request, send_file
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
from pathlib import Path
import random

from config import *

from app import app

songs = SONGS

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'song' in incoming_msg:
        choice = random.choice(songs)
        print(choice)
        msg.media(choice)
        responded = True
    return str(resp)

