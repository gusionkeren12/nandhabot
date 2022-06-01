from nandhabot import bot
from pyrogram import filters
from pyrogram.types import Message
import requests 

@bot.on_message(filtees.command("hneko"))
def hneko(_, m: Message):
    api = requests.get("https://api.waifu.pics/nsfw/neko").json()
    url = api["url"]
    m.reply_photo(photo=url)
    
