import telebot
import os
from predict_model import predict_signal
from signal_logger import log_signal

# Railway uchun tokenni o‘qish
TOKEN = os.getenv("BOT_TOKEN")
if TOKEN is None:
    raise ValueError("BOT_TOKEN topilmadi. Railway Environment Variables’ni tekshiring.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Aviator signal bot ishga tushdi.")

@bot.message_handler(commands=['signal'])
def send_signal(message):
    try:
        prediction, last_coeffs = predict_signal()
        reply = (
            "✈️ TEST SIGNAL - Aviator\n"
            f"Oxirgi 3 koeffitsiyent: {last_coeffs}\n"
            f"Ehtimol (1.80x+): {prediction * 100:.1f}%"
        )
        log_signal(last_coeffs, prediction)
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"Xato: {e}")

bot.polling()
