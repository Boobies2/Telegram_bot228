from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("я сохранять ваше саабщение в редиска о великий гаспадиннн")

async def save_message(update: Update, context: CallbackContext):
    message = update.message.text

    r.lpush('messages', message)

    saved_count = r.llen('messages')

    await update.message.reply_text(f"о преподобный ваше сообщение услышали сами боги! сичас на вашем счету {saved_count} социального рейтинга")


def main():
    application = Application.builder().token("7692941844:AAGCoYupSS65jwAoqSGgUaYx1cxMb755WmQ").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_message))

    application.run_polling()

if __name__ == '__main__':
    main()
