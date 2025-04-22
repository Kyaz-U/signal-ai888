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
@bot.message_handler(commands=['signal'])
def send_signal(message):
    try:
        coeffs = get_latest_coefficients()
        prediction = predict_signal(coeffs)

        text = (
            "✈️ TEST SIGNAL - Aviator\n"
            f"Oxirgi 3 koeffitsiyent: {coeffs}\n"
            f"Ehtrimol (1.80x+): {prediction * 100:.1f}%"
        )
        bot.send_message(message.chat.id, text)
    except Exception as e:
        bot.send_message(message.chat.id, f"Xatolik: {e}")

# Botni doimiy ishga tushirish
bot.polling()
