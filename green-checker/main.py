import requests
from bs4 import BeautifulSoup

# معلومات التليجرام
BOT_TOKEN = 'ضع_توكن_البوت_هنا'
CHAT_ID = 'ضع_ChatID_هنا'

# رابط الصفحة
URL = 'ضع_الرابط_هنا'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

def check_green():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    green_elements = soup.find_all(
        lambda tag: tag.has_attr('style') and 'background-color:green' in tag['style'].replace(' ', '')
    )

    if green_elements:
        send_telegram_message("✅ وُجد وقت بلون أخضر! 🚀")

# شغل الفحص الآن
check_green()
