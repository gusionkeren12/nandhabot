from nandhabot import bot
from pyrogram import filters 
from pyrogram.types import Message 
import requests 

@bot.on_message(filters.command("angry"))
def waifu(_, m: Message):
    api = request.get("https://api.waifu.pics/sfw/angry").json()
    url = api["url"]
    m.reply_animation(url)
