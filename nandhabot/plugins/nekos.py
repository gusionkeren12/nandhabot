import requests
import nekos
from PIL import Image
import os

from nandhabot import bot
from pyrogram import filters
from pyrogram.types import Message





@bot.on_message(filters.command("feed"))
def feed(_,  m: Message):
    target = "feed"
    m.reply_video(nekos.img(target))
    
@bot.on_message(filters.command("neko"))
def neko(_,  m: Message):
    target = "neko"
    m.reply_photo(nekos.img(target))

@bot.on_message(filters.command("wallpaper"))
def wallpaper(_,  m: Message):
    target = "wallpaper"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("ngif"))
def ngif(_,  m: Message):
    target = "ngif"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("tickle"))
def tickle(_,  m: Message):
    target = "tickle"
    m.reply_video(nekos.img(target))

@bot.on_message(filters.command("gasm"))
def gasm(_,  m: Message):
    target = "gasm"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    m.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


@bot.on_message(filters.command("poke"))
def poke(_,  m: Message):
    target = "poke"
    m.reply_animatiom(nekos.img(target))

    
@bot.on_message(filters.command("waifu"))
def waifu(_,  m: Message):
    target = "waifu"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    m.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


@bot.on_message(filters.command("kiss"))
def kiss(_,  m: Message):
    target = "kiss"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("cuddle"))
def cuddle(_,  m: Message):
    target = "cuddle"
    m.reply_video(nekos.img(target))


@bot.on_message(filters.command("foxgirl"))
def foxgirl(_,  m: Message):
    target = "fox_girl"
    m.reply_photo(nekos.img(target))


@bot.on_message(filters.command("smug"))
def smug(_,  m: Message):
    target = "smug"
    m.reply_animation(nekos.img(target))


@bot.on_message(filters.command("8ball"))
def baka(_,  m: Message):
    target = "8ball"
    m.reply_photo(nekos.img(target))

    
