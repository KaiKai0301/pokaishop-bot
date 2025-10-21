import logging
import os
from telegram.ext import Application, CommandHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv('TOKEN')

async def start(update, context):
    await update.message.reply_text("✅ BOT IS FINALLY WORKING!")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    logger.info("🚀 Starting fixed bot...")
    application.run_polling()

if __name__ == "__main__":
    main()