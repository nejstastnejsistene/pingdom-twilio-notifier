#!/usr/bin/env python

import os
import json
from flask import Flask, request, Response
from twilio.rest import TwilioRestClient

app = Flask('pingdom-twilio-notifier')

client = TwilioRestClient()
twilio_phone_num = os.getenv('TWILIO_PHONE_NUM')
password = os.getenv('PASSWORD', '')

@app.route('/'+password+'/<phone_num>')
def notify(phone_num):
  content_type = {'Content-Type': 'text/plain'}
  try:
    message = json.loads(request.args.get('message'))
  except ValueError:
    return 'expecting message query param to be valid json', 400, content_type
  try:
    action, description = message['action'], message['description']
    body = '[Pingdom] action={!r} description={!r}'.format(action, description)
  except KeyError:
    return 'expecting action and description keys', 400, content_type
  client.messages.create(to=phone_num, from_=twilio_phone_num, body=body)
  return '', 200, content_type

host = os.getenv('HOST', '0.0.0.0')
port = os.getenv('PORT', 5000)
app.run(host, port)
