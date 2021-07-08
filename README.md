# WhatsAppBot

A very simply WhatsApp chatbot, using Flask and Twilio to interface with WhatsApp.

## Workflow

The API uses a single POST endpoint:

`/bot`

When user sends a POST request to the endpoint, the Flask app returns a random song, from a publically accessible http link'

## Setup

Requires the creation of config.py file containing a list SONGS, containing public http links to mp3 media files.

