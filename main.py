from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class WebhookData(BaseModel):
    trigger: str

@app.post("/zapier-hook")
async def zapier_webhook(data: WebhookData):
    return {
        "message": "*Good morning, Fawad! Here's your Dynamic Daily Power Start Checklist:*\n\n"
                   "1. *Workout Visual:*\n"
                   "https://files.chatgpt.com/file_000000002fbc6230b303cb7783506f30\n\n"
                   "2. *Job Alerts:*\n"
                   "- EA Director (Remote): https://bit.ly/job1\n"
                   "- VP Cloud Strategy (Atlanta): https://bit.ly/job2\n"
                   "- Digital Transformation Lead (NJ): https://bit.ly/job3\n\n"
                   "3. *Stock Snapshot:*\n"
                   "LOAR $86.04 | AMZN $202.06 | LCID $2.82 | WMT $97.17\n\n"
                   "4. *Crypto Wallet:*\n"
                   "BTC: $123.21 | SUI: $27.66 | AERO: $0.93\n\n"
                   "5. *Karachi Flights (Dec 21 – Jan 14):*\n"
                   "- Turkish: $1,388 (4h) → Book: https://turkishairlines.com/deal\n"
                   "- Qatar: $1,423 (5h) → Book: https://qatar.com/deal\n"
                   "- Etihad: $1,460 (6h) → Book: https://etihad.com/deal\n\n"
                   "6. *Energy Tip:*\n"
                   "Warm lemon-honey water 20 mins pre-gym\n\n"
                   "Let's win the day!"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
