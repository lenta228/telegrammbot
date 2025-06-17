import telebot
import os

TOKEN = os.getenv("7431943285:AAEsgkQ0Bu00kV6eWdsdJPqWsCkvjjk4w3U")  # токен из переменной окружения

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я живой!")

print("✅ Бот запущен")
bot.infinity_polling()  # бот начинает слушать Telegram
