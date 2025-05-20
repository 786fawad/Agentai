import requests

# Replace this with your actual deployed URL
url = "https://agentai-3jnz.onrender.com/send_checklist"

response = requests.post(url, json={"name": "ChecklistTrigger"})

print("Status:", response.status_code)
print("Response:", response.text)
