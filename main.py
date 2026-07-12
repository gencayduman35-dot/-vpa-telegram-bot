import os
import requests

# GitHub Secrets'tan bilgileri al
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': text}
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    # Test mesajı
    result = send_message("Bot başarıyla başlatıldı ve çalışıyor!")
    print(result)
