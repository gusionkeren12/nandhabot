from nandhabot import  bot, arq, tbot,  BOT_TOKEN, updater
import logging 
import random
import nandhabot.plugins
from nandhabot.config import SUPPORT_CHAT
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


if __name__ == "__main__":
   tbot.start(bot_token=BOT_TOKEN)
   bot.run()
   with bot:
        bot.send_message(f"@{SUPPORT_CHAT}", "Hello there I'm Now online")





