from nandhabot import bot, arq
import logging 
import random
import nandhabot.plugins
from nandhabot.config import SUPPORT_CHAT
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# enable logging
FORMAT = "[VEGETA ROBOT] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)

x = arq.wall("vegeta")
y = x.result

if __name__ == "__main__":
   bot.run()
   with bot:
        bot.send_photo(f"@{SUPPORT_CHAT}",photo=random.choice(y).image_url,caption="Hello there I'm Now online")
