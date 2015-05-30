#!/usr/bin/env python

import os
import json
from flask import Flask, request, Response
from twilio.rest import TwilioRestClient

app = Flask('pingdom-twilio-notifier')

if os.environ.get('DEBUG'):
    app.debug = True

client = TwilioRestClient()
twilio_phone_num = os.environ['TWILIO_PHONE_NUM']
password = os.environ['PASSWORD']

@app.route('/'+password+'/<phone_num>')
def notify(phone_num):
    content_type = {'Content-Type': 'text/plain'}
    try:
      message = json.loads(request.args.get('message'))
    except ValueError:
      return 'expecting message query param to be valid json', 400, content_type
    try:
      checkname = message['checkname']
      host = message['host']
      description = message['description']
      body = '[Pingdom] {}: {} is {}.'.format(checkname, host, description)
    except KeyError:
      return 'expecting checkname, host, and description keys', 400, content_type
    client.messages.create(to=phone_num, from_=twilio_phone_num, body=body)
    return '', 200, content_type

host = os.getenv('HOST', '0.0.0.0')
port = os.getenv('PORT', 5000)
app.run(host, port)
