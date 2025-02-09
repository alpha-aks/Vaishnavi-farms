import logging
from venv import logger
from telegram import Update
from telegram.ext import Application, CommandHandler

# Replace with your actual bot token from BotFather
TOKEN = "7218648692:AAGujX0YYC3ezH2aC1GGvGf-_dcFnK6Rde0"

async def start(update: Update, context):
    await update.message.reply_text("Hello! I'm your Telegram bot 🤖")

def main():
    logger.info("Starting the bot...")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    logger.info("Bot is now polling...")
    app.run_polling()

if __name__ == "__main__":
    main()