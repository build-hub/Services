from configuration import client
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from twilio.rest import Client

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Sms(BaseModel):
    recipient : str
    body : str

def configure():
    account_sid = "AC2f827ef415611e1421e24d55ee785f28"
    auth_token = "23859e1389e898307aa08d09570593de"
    client = Client(account_sid, auth_token)
    return client

@app.post("/sms")
def send_sms(sms:Sms):
    recipient = sms.recipient
    body = sms.body
    if recipient[0] == "0":
        recipient = recipient.replace("0","+234",1)

    configure().messages.create(
            body=body,
            from_='+17608402657',
            to=recipient
        )
    return("Success")


