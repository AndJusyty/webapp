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

BOT_TOKEN = "7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70"
WEBAPP_URL = "https://andjusyty.github.io/webapp/"  # Замени на свою ссылку

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
@dp.message()
async def handle_webapp_data(message: Message):
    if message.web_app_data:
        # message.web_app_data.data — это строка JSON
        from json import loads
        try:
            data = loads(message.web_app_data.data)
            date = data.get("date")
            time = data.get("time")
            timezone = data.get("timezone")
            text = f"🗓 Дата: <b>{date}</b>\n⏰ Время: <b>{time}</b>\n🌍 Таймзона: <b>{timezone}</b>"
        except Exception as e:
            text = f"⚠️ Ошибка разбора данных: {e}"

        await message.answer(text)


from aiogram.filters import WebAppData

@dp.message(WebAppData())
async def handle_webapp_data(message: Message):
    data = message.web_app_data.data
    await message.answer(
        f"✅ Вы выбрали:\n<pre>{data}</pre>",
        parse_mode="HTML"
    )


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())