pingdom-twilio-notifier
=======================

Simple Twilio notifier for Pingdom, so you don't have to pay so much for SMS credits.

## Heroku Installation

```
heroku login
heroku create
heroku config:set TWILIO_ACCOUNT_SID=<insert your account sid here>
heroku config:set TWILIO_AUTH_TOKEN=<insert your auth token here>
heroku config:set TWILIO_PHONE_NUM=<insert your Twilio phone number here>
heroku config:set PASSWORD=<insert random string here>
git push heroku master
```

## Pingdom Installation

In your user settings, click "Add Contact Method", select "Webhook/URL", and set the URL to:

```
<your heroku url>/<password>/<recipient phone number>
```

## Environment Variables

- `TWILIO_ACCOUNT_SID` (Twilio account SID)
- `TWILIO_AUTH_TOKEN` (Twilio auth token)
- `TWILIO_PHONE_NUM` (the phone number for Twilio to text you from)
- `PASSWORD` (prevent just anyone from sending messages as you)
- `HOST` (defaults to `0.0.0.0`)
- `PORT` (defaults to `5000`)

## Installation for Developemnt

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
