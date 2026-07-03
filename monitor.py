import os
import hashlib
import requests
from bs4 import BeautifulSoup

URL = "https://rsahcouncil.org/"

TOKEN = os.getenv("BOT_TOKEN")
CHAT = os.getenv("CHAT_ID")

r = requests.get(URL, timeout=30)
text = BeautifulSoup(r.text, "html.parser").get_text(" ", strip=True)

new_hash = hashlib.sha256(text.encode()).hexdigest()

old_hash = ""
if os.path.exists("state.txt"):
    with open("state.txt", "r") as f:
        old_hash = f.read().strip()

if old_hash != new_hash:
    if old_hash != "":
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={
                "chat_id": CHAT,
                "text": f"🚨 RSAH Council Website Updated!\n\n{URL}"
            }
        )

with open("state.txt", "w") as f:
    f.write(new_hash)
