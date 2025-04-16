# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Application, CommandHandler, ContextTypes

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [
#         [InlineKeyboardButton("Открыть WebApp", web_app={"url": "https://andjusyty.github.io/webapp/"})]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     await update.message.reply_text("Нажми кнопку, чтобы открыть WebApp:", reply_markup=reply_markup)

# app = Application.builder().token("7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70").build()
# app.add_handler(CommandHandler("start", start))
# app.run_polling()


from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "7979211167:AAEt9T-0LmzXVoqe7xw4AWKfVrKErYm2D70"
WEBAPP_URL = "https://andjusyty.github.io/webapp/" 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть WebApp", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Нажми на кнопку ниже 👇", reply_markup=reply_markup)

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

