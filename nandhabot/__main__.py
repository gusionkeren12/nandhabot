from nandhabot import bot, arq
import logging #aasf
import random
import nandhabot.plugins
from pyrogram import idle
from nandhabot.config import SUPPORT_CHAT
from nandhabot.utils.dbfunctions import clean_restart_stage
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
           bot.send_message("hello! There I'm  Alive")
