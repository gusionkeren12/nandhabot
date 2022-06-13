from nandhabot import bot, arq
import logging 
import random
import nandhabot.plugins
from nandhabot.config import SUPPORT_CHAT
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# enable logging
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)


if __name__ == "__main__":
   bot.run()
   with bot:
        bot.send_photo(f"@{SUPPORT_CHAT}", "Hello there I'm Now online")
