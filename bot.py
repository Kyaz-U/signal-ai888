import telebot
import os
from dotenv import load_dotenv
from api_client import get_latest_coefficients
from predict_model import predict_signal

# .env fayldan tokenni yuklash
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Botni ishga tushirish
bot = telebot.TeleBot(TOKEN)

# Boshlanish komandasi
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Aviator signal bot ishga tushdi.")

# Signal komandasi
from predict_model import predict_signal
import numpy as np

@bot.message_handler(commands=["signal"])
def handle_signal(message):
    # Oxirgi 3 ta qiymat — eng so‘nggi aylanishlar:
    last_coeffs = [5.01, 2.05, 2.25]
    k1, k2, k3 = last_coeffs
    ehtimol = predict_signal(k1, k2, k3)

    msg = (
        "✈️ TEST SIGNAL - Aviator\n"
        f"Oxirgi 3 koeffitsiyent: [{k1}, {k2}, {k3}]\n"
        f"🧠 Ehtimol (1.80x+): {ehtimol}%"
    )
    bot.send_message(message.chat.id, msg)

# Botni doimiy ishga tushirish
bot.polling()
