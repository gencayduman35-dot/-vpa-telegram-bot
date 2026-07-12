import os
import requests

TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

# Bu sefer hata varsa bize göstersin diye print ekliyoruz
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
params = {'chat_id': CHAT_ID, 'text': 'Amirim, sistem çalışıyor!'}
response = requests.get(url, params=params)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
