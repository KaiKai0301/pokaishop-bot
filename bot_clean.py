import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv('TOKEN', '8456466564:AAFtPxI6RX_lR0AWYuv_8Gp0M61cPduE0Ps')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the command /start is issued."""
    await update.message.reply_text("🤖 Bot is WORKING! Hello from the CLEAN version!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all messages."""
    await update.message.reply_text(f"I received: {update.message.text}")

def main():
    """Start the bot - CLEAN VERSION"""
    try:
        # Create the Application (MODERN v20.7 WAY)
        application = Application.builder().token(TOKEN).build()
        
        logger.info("🤖 CLEAN Bot starting...")
        
        # Add basic handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        # Start the Bot
        logger.info("✅ CLEAN Bot starting polling...")
        application.run_polling()
        
    except Exception as e:
        logger.error(f"❌ CLEAN Bot failed to start: {e}")

if __name__ == "__main__":
    main()