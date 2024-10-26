import os

from dotenv import load_dotenv
from telegram import ForceReply, Update
from telegram.ext import ContextTypes, CommandHandler, Application, MessageHandler, filters

load_dotenv()

TOKEN=os.getenv('BOT_TOKEN')

async def start(update:Update,context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

async def upload_file(update:Update,context:ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    file = await update.message.document.get_file()
    reply_text = f"File {file.file_unique_id} received from {user.mention_markdown_v2()}!\n Download Path: {file.file_path}"
    await update.message.reply_text(reply_text)

async def echo(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def init_bot():
    application=Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start',start))
    application.add_handler(MessageHandler(filters.Document.ALL,upload_file))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)