# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python

# # Download the helper library from https://www.twilio.com/docs/python/install
# from twilio.rest import Client
#
#
# # Your Account Sid and Auth Token from twilio.com/console
# # DANGER! This is insecure. See http://twil.io/secure
# account_sid = 'ACd6ddda2a57c8e13e28a5e26779f6609e'
# auth_token = '701119ec21417c899874cbd9bfbedb69'
# client = Client(account_sid, auth_token)
#
# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+16479578309',
#                      to='+14163205156'
#                  )
#
# print(message.sid)


from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a text message
    msg = resp.message("Ahoy! Thanks so much for your message.")
    # Add a picture message
    msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

