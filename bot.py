import telebot
import pandas as pd
import numpy as np
import pickle
import os
from dotenv import load_dotenv

# .env faylni yuklaymiz
load_dotenv()

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi. Railway Environment Variables’ni tekshiring.")

bot = telebot.TeleBot(TOKEN)

# Modelni yuklaymiz
with open('models/aviator_model.pkl', 'rb') as f:
    model = pickle.load(f)

# CSV'dan oxirgi 3 ta koeffitsientni olish funksiyasi
def get_last_3_coefficients():
    try:
        df = pd.read_csv("data/aviator.csv")
        last_row = df.tail(1)
        return float(last_row['k1']), float(last_row['k2']), float(last_row['k3'])
    except:
        return None, None, None

# AI signal funksiyasi
def predict_signal(k1, k2, k3):
    data = pd.DataFrame([[k1, k2, k3]], columns=["k1", "k2", "k3"])
    prediction = model.predict_proba(data)[0][1]
    return prediction

# /start komandasi
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Aviator signal bot ishga tushdi.")

# /signal komandasi
@bot.message_handler(commands=['signal'])
def send_signal(message):
    k1, k2, k3 = get_last_3_coefficients()
    if None in (k1, k2, k3):
        bot.reply_to(message, "Xatolik: oxirgi koeffitsientlar topilmadi.")
        return

    ehtimol = predict_signal(k1, k2, k3)
    bot.send_message(message.chat.id,
        f"✈️ TEST SIGNAL - Aviator\n"
        f"Oxirgi 3 koeffitsiyent: [{round(k1,2)}, {round(k2,2)}, {round(k3,2)}]\n"
        f"Ehtrimol (1.80x+): {round(ehtimol * 100, 1)}%"
    )

# Botni ishga tushuramiz
bot.polling()
