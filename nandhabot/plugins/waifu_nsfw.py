from nandhabot import bot
from pyrogram import filters
from pyrogram.types import Message
import requests 

@bot.on_message(filters.command("hneko"))
def hneko(_, m: Message):
    api = requests.get("https://api.waifu.pics/nsfw/neko").json()
    url = api["url"]
    m.reply_animation(url)
    
@bot.on_message(filters.command("hwaifu"))
def hwaifu(_, m: Message):
    api = requests.get("https://api.waifu.pics/nsfw/waifu").json()
    url = api["url"]
    m.reply_animation(animation=url)
   

@bot.on_message(filters.command("trap"))
def trap(_, m: Message):
    api = requests.get("https://api.waifu.pics/nsfw/trap").json()
    url = api["url"]
    m.reply_animation(url)
    

@bot.on_message(filters.command("blowjob"))
def blowjob(_, m: Message):
    api = requests.get("https://api.waifu.pics/nsfw/blowjob").json()
    url = api["url"]
    m.reply_animation(url)
    
