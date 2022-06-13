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


if __name__ == "__main__":
   bot.run()
   with bot:
        x = await arq.wall("vegeta")
        y = x.result
        bot.send_photo(f"@{SUPPORT_CHAT}",photo=random.choice(y).url_image,caption="Hello there I'm Now online")
