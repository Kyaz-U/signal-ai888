import telebot
from dotenv import load_dotenv
import os
from predict_model import predict_signal

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Aviator signal bot ishga tushdi.")

@bot.message_handler(commands=['signal'])
def get_signal(message):
    bot.send_message(message.chat.id, "Oxirgi 3 ta koeffitsiyentni vergul bilan kiriting (masalan: 1.8, 2.0, 1.6)")
    bot.register_next_step_handler(message, process_coeffs)

def process_coeffs(message):
    try:
        k1, k2, k3 = map(float, message.text.split(","))
        prediction = predict_signal(k1, k2, k3)
        reply = (
            "✈️ TEST SIGNAL - Aviator\n"
            f"Oxirgi 3 koeffitsiyent: [{round(k1, 2)}, {round(k2, 2)}, {round(k3, 2)}]\n"
            f"Ehtimol (1.80x+): {round(prediction * 100, 1)}%"
        )
        bot.send_message(message.chat.id, reply)
    except:
        bot.send_message(message.chat.id, "Xatolik! Format: 1.8, 2.0, 1.6 — shunday kiriting.")

bot.polling()
