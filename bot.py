

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть WebApp", web_app={"url": "https://andjusyty.github.io/webapp/"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Нажми кнопку, чтобы открыть WebApp:", reply_markup=reply_markup)

app = Application.builder().token("7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

