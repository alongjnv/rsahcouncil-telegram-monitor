
import os,hashlib,requests
from bs4 import BeautifulSoup
URL=os.getenv("URL","https://rsahcouncil.org/")
TOKEN=os.getenv("BOT_TOKEN")
CHAT=os.getenv("CHAT_ID")
r=requests.get(URL,timeout=30)
text=BeautifulSoup(r.text,"html.parser").get_text(" ",strip=True)
h=hashlib.sha256(text.encode()).hexdigest()
old=""
if os.path.exists("state.txt"): old=open("state.txt").read().strip()
if h!=old:
    if old:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id":CHAT,"text":"RSAH Council website updated: "+URL})
    open("state.txt","w").write(h)
