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


from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
import pandas as pd
import json


app = Flask(__name__)







def questions_from_json(survey_json_string):
    questions = []
    questions_dicts = json.loads(survey_json_string).get('questions')
    for question_dict in questions_dicts:
        body = question_dict['body']
        kind = question_dict['type']



        questions.append({body:})
    return questions





@app.route("/")
def hello():
    return "Hello World!"


@app.route("/sms", methods=['GET', 'POST'])
def sms_webhook():
    """Respond to incoming messages with a friendly SMS."""

    body = request.values.get('Body', None)

    # Start our response
    resp = MessagingResponse()

    # ----------------------------------------------------------
    if body.strip().lower() == 'user':




    # resp.message("Welcome to BayLunch order platform!")
    return str(resp)




















@app.route("/sms1", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""

    body = request.values.get('Body', None)

    # Start our response
    resp = MessagingResponse()

    # Add a text message
    #msg = resp.message("Ahoy! Thanks so much for your message.")
    # Add a picture message
    #msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")

    menu={
    1:'平安虾卷',
    2:'蒲烧鳗鱼',
    3:'卤猪肘',
    4:'红烧牛腩',
    5:'香肠肉燥',
    6:'怀旧排骨',
    7:'卤味三拼',
    8:'黄金虾饼',
    9:'咖喱鸡肉',
    10:'红烧扣肉',
    }



    welcome_str = f'''
    Welcome to BayLunch order system!

    Our menu:
    {str(menu)}
    checkout pictures of the menue, go to www.baylunch.com/menu
    Wanna order? simply reply your dish ID.
    '''

    def return_comfirmamtion(order_ids):

        text=f'''
        You are ordering : {'+'.join([menu[each] for each in order_ids])},
        
        choose closest location with estimated delivery time fits your need:
        1. 1 York  ~ delivered at 11:45 AM
        2. 40 King West ~ 12:00PM
        3. 1 Bloor  ~ 12:30PM

        please reply with this format

        ID;Name;additional request
        example reply:
        3;周杰伦;少菜多肉
        3;Jay Chow;customized pick up location at 365 Bloor.
             
        '''
        return text




    #----------------------------------------------------------
    if body.strip().lower() == 'hi':
        resp.message(welcome_str)
    elif body.strip().isdigit() or '+' in body.strip():
        order_ids = [int(each) for each in body.strip().split('+')]
        resp.message(return_comfirmamtion(order_ids))
    elif ';' in body.strip():
        order =  [ body.strip().split(';')]




    #resp.message("Welcome to BayLunch order platform!")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

