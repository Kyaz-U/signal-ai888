import telebot
from api_client import get_latest_coefficients
from predict_model import predict_signal
from signal_logger import log_signal
from premium import is_premium
from admin_panel import get_statistics
import time
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(msg):
    if msg.chat.id == ADMIN_ID:
        bot.send_message(msg.chat.id, "Assalomu alaykum! Wersal AI signal bot ishga tushdi.")

@bot.message_handler(commands=['signal'])
def manual_signal(msg):
    if not is_premium(msg.chat.id):
        bot.send_message(msg.chat.id, "⚠️ Premium foydalanuvchilar uchun mo‘ljallangan.")
        return
    last_3 = get_latest_coefficients()
    send_signal(last_3)

@bot.message_handler(commands=['stat'])
def admin_stats(msg):
    if msg.chat.id == ADMIN_ID:
        stats = get_statistics()
        bot.send_message(msg.chat.id, stats)

def send_signal(last_3):
    proba = predict_signal(last_3)
    foiz = round(proba * 100, 2)
    if foiz >= 70:
        text = (
            "✈️ YANGI RAUND - Aviator\n"
            f"Signal: EHTIMOLI YUQORI ➜ 1.80x+\n"
            f"Tavsiya: Hozir pul tiking\n"
            f"Ishonchlilik darajasi: {foiz}%\n"
            f"Oxirgi 3 koeffitsiyent: {last_3}"
        )
        bot.send_message(ADMIN_ID, text)
        log_signal(last_3, proba)

# Avtomatik signal loop
import threading

def auto_loop():
    while True:
        last_3 = get_latest_coefficients()
        if is_premium(ADMIN_ID):
            send_signal(last_3)
        time.sleep(10)

threading.Thread(target=auto_loop).start()
bot.polling()
