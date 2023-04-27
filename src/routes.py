from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from twilio_settings import account_sid, account_token, phone
from .directions import get_directions

proxy_client = TwilioHttpClient()

client = Client(account_sid, account_token, http_client=proxy_client)

question = 1
starting = ""

@app.route("/sms", methods=["POST"])
def sms_reply():
    global question, starting
    content = request.values.get("Body", None)
    contact = request.values.get("From", None)
    resp = MessagingResponse()

    if question == 1:
        response = "Welcome to MapMe, Where are you right now?"
        question += 1
        client.messages.create(to=contact, from_=phone, body=response)
    elif question == 2:
        starting = content
        response = "Cool! Now tell me, Where would you like to go?"
        question += 1
        client.messages.create(to=contact, from_=phone, body=response)
    elif question == 3:
        destination = content
        tempresponse = "Great! Let me calculate the fastest route for you"
        client.messages.create(to=contact, from_=phone, body=tempresponse)
        response = str(get_directions(starting, destination))
        result_list = response.split("\n")
        if len(result_list) > 20:
            third = int(len(result_list) / 3)
            twoThird = third * 2
            response1 = "\n".join(result_list[0:third])
            response2 = "\n".join(result_list[third:twoThird])
            response3 = "\n".join(result_list[twoThird : len(result_list)])
            client.messages.create(to=contact, from_=phone, body=response1)
            client.messages.create(to=contact, from_=phone, body=response2)
            client.messages.create(to=contact, from_=phone, body=response3)
        else:
            client.messages.create(to=contact, from_=phone, body=response)
    else:
        response = "Resetting"
        client.messages.create(to=contact, from_=phone, body=response)
        question = 1

    return "Worked"
