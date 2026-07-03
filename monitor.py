import os
import requests

TOKEN = os.getenv("BOT_TOKEN")
CHAT = os.getenv("CHAT_ID")

response = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT,
        "text": "✅ GitHub Actions is connected successfully!"
    }
)

print(response.status_code)
print(response.text)
