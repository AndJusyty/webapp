# import telebot

# # Вставь сюда свой токен бота
# TOKEN = '7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70'

# # Создаём объект бота
# bot = telebot.TeleBot(TOKEN)

# # Обработчик команды /start
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Привет! Я бот для выбора времени. Нажми кнопку ниже, чтобы выбрать дату и время.")

# # Создание кнопки WebApp для запуска времени
# @bot.message_handler(commands=['timepicker'])
# def send_timepicker(message):
#     from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

#     # Ссылка на твой WebApp
#     webapp_url = "https://andjusyty.github.io/webapp/"  

#     # Кнопка с WebApp
#     markup = InlineKeyboardMarkup()
#     markup.add(
#         InlineKeyboardButton(
#             text="🗓️ Открыть планировщик времени",
#             web_app=WebAppInfo(url=webapp_url)
#         )
#     )

#     # Отправка сообщения с кнопкой
#     bot.send_message(message.chat.id, "Нажми на кнопку, чтобы выбрать время.", reply_markup=markup)

# # Обработка данных, отправленных из WebApp (если нужно)
# @bot.message_handler(content_types=['web_app_data'])
# def handle_webapp_result(message):
#     data = message.web_app_data.data  # Данные, отправленные из WebApp
#     bot.send_message(message.chat.id, f"Вы выбрали: {data}")

# # Запуск бота
# bot.polling(none_stop=True)



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

