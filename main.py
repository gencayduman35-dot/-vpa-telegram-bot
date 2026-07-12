import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("TOKEN:", TOKEN)
print("CHAT_ID:", CHAT_ID)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

r = requests.get(url, params={
    "chat_id": CHAT_ID,
    "text": "GitHub bağlantısı başarılı."
})

print(r.status_code)
print(r.text)
