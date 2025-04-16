import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = '7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'webapp'])
def send_webapp(message):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text="📅 Открыть планировщик",
            web_app=WebAppInfo(url="https://andjusyty.github.io/webapp/")  # замени на своё
        )
    )
    bot.send_message(message.chat.id, "Нажми кнопку ниже для выбора даты/времени:", reply_markup=markup)

bot.polling()

