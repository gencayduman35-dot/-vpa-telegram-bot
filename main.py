import os
import requests
import time

TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

def send_message(text):
    requests.get(BASE_URL + "sendMessage", params={'chat_id': CHAT_ID, 'text': text})

# Botu ilk açılışta selamla
send_message("Amirim, bot aktif ve emirlerini bekliyor!")

# Basit bir mesaj dinleme döngüsü (polling)
last_update_id = 0
while True:
    response = requests.get(BASE_URL + "getUpdates", params={'offset': last_update_id + 1})
    data = response.json()
    
    if data['ok'] and data['result']:
        for update in data['result']:
            last_update_id = update['update_id']
            msg = update.get('message', {}).get('text', '')
            if msg:
                send_message(f"Amirim, '{msg}' dedin, emrin başım üstüne!")
    
    time.sleep(2) # Sistemi yormamak için 2 saniye bekle
