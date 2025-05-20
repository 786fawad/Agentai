
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class WebhookData(BaseModel):
    trigger: str

@app.post("/zapier-hook")
async def zapier_webhook(data: WebhookData):
    response_message = {
        "message": "*Good morning, Fawad! Here’s your Dynamic Daily Power Start Checklist:*\n\n"
                   "1. *Workout Visual:* https://yourserver.com/images/today.jpg\n"
                   "2. *Job Alerts:* EA, Cloud, Strategy (Live links can be embedded)\n"
                   "3. *Stock Snapshot:* LOAR $86.04 | AMZN $202.06 | BTC $123.21\n"
                   "4. *Crypto Trend:* BTC +2.3%, SUI -1.1%, AERO -3.7%\n"
                   "5. *Karachi Flights:* Deals from Dec 21 – Jan 14 under $1500\n"
                   "6. *Energy Tip:* Warm lemon-honey water 20 mins pre-gym\n\n"
                   "Let’s win the day!"
    }
    return response_message

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
