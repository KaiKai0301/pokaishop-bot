from flask import Flask
import threading
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    return "PokaiShop Bot is running!"

@app.route('/health')
def health():
    return "OK"

def run_bot():
    try:
        logger.info("Starting Telegram bot...")
        # Import and run your bot
        from claim_sales_bot import main
        main()
    except Exception as e:
        logger.error(f"Error running bot: {e}")

if __name__ == "__main__":
    # Start bot in a separate thread
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Start web server
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting web server on port {port}")
    app.run(host='0.0.0.0', port=port)