import telebot
from api_client import get_latest_coefficients
from predict_model import predict_signal
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
        bot.send_message(msg.chat.id, "Assalomu alaykum! Aviator signal bot ishga tushdi.")

@bot.message_handler(commands=['signal'])
def manual_signal(msg):
    if msg.chat.id != ADMIN_ID:
        return
    last_3 = get_latest_coefficients()
    send_signal(last_3)

def send_signal(last_3):
    proba = predict_signal(last_3)
    foiz = round(proba * 100, 2)
    text = (
        "✈️ TEST SIGNAL - Aviator\n"
        f"Oxirgi 3 koeffitsiyent: {last_3}\n"
        f"Ehtimol (1.80x+): {foiz}%"
    )
    bot.send_message(ADMIN_ID, text)

def auto_loop():
    while True:
        last_3 = get_latest_coefficients()
        send_signal(last_3)
        time.sleep(10)

import threading
threading.Thread(target=auto_loop).start()
bot.polling()
