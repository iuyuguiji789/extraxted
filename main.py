import os
from config import Config
from pyrogram import Client, idle
import asyncio, logging
import tgcrypto
from pyromod import listen
from logging.handlers import RotatingFileHandler
from flask import Flask
from threading import Thread

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

# Auth Users
AUTH_USERS = [int(chat) for chat in Config.AUTH_USERS.split(",") if chat != '']

# Prefixes
prefixes = ["/", "~", "?", "!"]

plugins = dict(root="plugins")

# Flask Web Server for Koyeb Health Check
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host="0.0.0.0", port=8080)  # Ensure Koyeb detects the app

if __name__ == "__main__":
    bot = Client(
        "StarkBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=20,
        plugins=plugins,
        workers=50
    )

    async def run_bot():
        await bot.start()
        bot_info = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) STARKBOT --->")
        await idle()

    # Start Flask Web Server in a Separate Thread
    Thread(target=run_web).start()

    # Run Bot
    asyncio.get_event_loop().run_until_complete(run_bot())
    LOGGER.info(f"<---Bot Stopped--->")
