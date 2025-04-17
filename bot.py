# import telebot
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# TOKEN = '7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70'
# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start', 'webapp'])
# def send_webapp(message):
#     markup = InlineKeyboardMarkup()
#     markup.add(
#         InlineKeyboardButton(
#             text="📅 Открыть планировщик",
#             web_app=WebAppInfo(url="https://andjusyty.github.io/webapp/")
#         )
#     )
#     bot.send_message(message.chat.id, "Нажми кнопку ниже для выбора даты/времени:", reply_markup=markup)

# bot.polling()


import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties

# 🔑 Твой токен и WebApp URL
BOT_TOKEN = "7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70"
WEBAPP_URL = "https://andjusyty.github.io/webapp/"

# ✅ Новая схема: parse_mode через DefaultBotProperties
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

# ⌨️ Клавиатура с кнопкой
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton(
    text="📅 Выбрать дату и время",
    web_app=WebAppInfo(url=WEBAPP_URL)
))


# /start — показать кнопку
@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(
        "Привет! 👋\nНажми кнопку ниже, чтобы выбрать дату и время:",
        reply_markup=keyboard
    )


# Обработка данных из WebApp
@dp.message()
async def handle_webapp_data(message: Message):
    if message.web_app_data:
        await message.answer(
            f"✅ Получено из WebApp:\n<pre>{message.web_app_data.data}</pre>"
        )


# Запуск бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
