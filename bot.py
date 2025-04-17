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


from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor

# 🔑 Вставь сюда свой токен
BOT_TOKEN = "7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# 🔘 Клавиатура с WebApp кнопкой
webapp_url = "https://andjusyty.github.io/webapp/"  # ← замени на своё!

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton(
    text="📅 Выбрать дату и время",
    web_app=WebAppInfo(url=webapp_url)
))


# 🟢 /start
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет! 👋\nНажми кнопку ниже, чтобы выбрать дату и время:",
        reply_markup=keyboard
    )


# 📩 Обработка данных из WebApp
@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def webapp_handler(message: types.Message):
    try:
        data = message.web_app_data.data
        await message.answer(f"✅ Данные из WebApp:\n<pre>{data}</pre>", parse_mode="HTML")
    except Exception as e:
        await message.answer(f"⚠️ Ошибка при получении данных: {e}")

# 🚀 Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
