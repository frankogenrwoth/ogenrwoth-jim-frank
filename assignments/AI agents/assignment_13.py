# assignment 13: AI agent to make a gm post on linkedin

from twilio.rest import Client
from dotenv import load_dotenv
import os
import random

load_dotenv()

# good morning whatsapp message
motivational_messages = [
        "Talk is cheap. Show me the code. – Linus Torvalds",
        "First, solve the problem. Then, write the code. – John Johnson",
        "Code is like humor. When you have to explain it, it’s bad. – Cory House",
        "The only way to learn a new programming language is by writing programs in it. – Dennis Ritchie",
        "The best way to predict the future is to invent it. – Alan Kay",
        "The only way to do great work is to love what you do. – Steve Jobs",
]

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

client = Client(account_sid, auth_token)

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:' + os.getenv('TO_NUMBER')

message = client.messages.create(
    body=random.choice(motivational_messages),
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

print(f"Message sent! SID: {message.sid}")
