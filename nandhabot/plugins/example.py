from telegram.ext import run_async, CommandHandler,MessageHandler
from nandhabot import dispatcher

import random 

OWO = (
    "*Neko pats {} on the head.",
    "*gently rubs {}'s head*.",
    "*Neko mofumofus {}'s head*",
    "*Neko messes up {}'s head*",
    "*Neko intensly rubs {}'s head*",
    "*{}'s waifu pats their head*",
    "*{}'s got free headpats*",
    "No pats for {}!",
)

def waku(update, context):
      chat = update.effective_chat
      bot = context.bot
      waku = random.choice(OWO)
      bot.sendMessage(chat.id,waku)
      

woku = CommandHandler("waku", waku)
dispatcher.add_handler(woku)
