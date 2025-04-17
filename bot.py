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
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup, Message
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from json import loads

BOT_TOKEN = "7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70"
WEBAPP_URL = "https://andjusyty.github.io/webapp/"  

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(
            text="📅 Выбрать дату и время",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(
        "Привет! 👋\nНажми кнопку ниже, чтобы выбрать дату и время:",
        reply_markup=keyboard
    )

@dp.message()
async def handle_webapp_data(message: Message):
    if message.web_app_data:
        try:
            data = loads(message.web_app_data.data)
            date = data.get("date")
            time = data.get("time")
            timezone = data.get("timezone")
            text = f"🗓 Дата: <b>{date}</b>\n⏰ Время: <b>{time}</b>\n🌍 Таймзона: <b>{timezone}</b>"
        except Exception as e:
            text = f"⚠️ Ошибка разбора данных: {e}"

        await message.answer(text)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())