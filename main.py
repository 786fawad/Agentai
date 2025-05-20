from fastapi import FastAPI
from pydantic import BaseModel
from twilio.rest import Client
import openai
import os

app = FastAPI()

# ENV VARS
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
TWILIO_TO = os.getenv("TWILIO_WHATSAPP_TO")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = Client(TWILIO_SID, TWILIO_TOKEN)
openai.api_key = OPENAI_API_KEY

class TriggerRequest(BaseModel):
    name: str = "ChecklistTrigger"

def get_openai_message():
    prompt = (
        "Generate a 5:30 a.m. WhatsApp checklist message with these:\n"
        "1. Daily motivational workout image link (say: [Image] and give dummy link)\n"
        "2. Robinhood buy/sell recommendation (assume $100 invested)\n"
        "3. Stock & crypto quick summary\n"
        "4. Flight price NJ to Karachi for Dec 21 – Jan 14 under $1500 with max 6h layover\n"
        "5. Job listings (Director/VP, EA/Cloud, $180K–$250K, remote/NJ/ATL/CHI)\n"
        "Use line breaks \n for formatting. Include emojis and friendly tone."
    )

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content

@app.post("/send_checklist")
def send_checklist(data: TriggerRequest):
    message_body = get_openai_message()

    try:
        message = client.messages.create(
            body=message_body,
            from_=f'whatsapp:{TWILIO_FROM}',
            to=f'whatsapp:{TWILIO_TO}'
        )
        return {"status": "sent", "sid": message.sid}
    except Exception as e:
        return {"status": "failed", "error": str(e)}