from nandhabot import bot
from pyrogram import filters
from pyrogram.types import Message
import requests 

@bot.on_message(filters.command("hneko") & filters.private)
def hneko(_, m: Message):
    api = requests.get("https://api.waifu.pics/nsfw/neko").json()
    url = api["url"]
    m.reply_photo(url)
    
@bot.on_message(filters.command("hwaifu") & filters.private)
def hwaifu(_, m: Message):
    api = requests.get("https://api.waifu.pics/nsfw/waifu").json()
    url = api["url"]
    m.reply_photo(url)
   

@bot.on_message(filters.command("trap") & filters.private)
def trap(_, m: Message):
    api = requests.get("https://api.waifu.pics/nsfw/trap").json()
    url = api["url"]
    m.reply_photo(url)
    

@bot.on_message(filters.command("blowjob") & filters.private)
def blowjob(_, m: Message):
    api = requests.get("https://api.waifu.pics/nsfw/blowjob").json()
    url = api["url"]
    m.reply_animation(url)

@bot.on_message(filters.command("lewd") & filters.private)
def lewd(_, m):
           api = requests.get("https://meme-api.herokuapp.com/gimme/lewdanime").json()
           url = api["url"]
           title = api["title"]
           m.reply_photo(url,caption=title)
    
@bot.on_message(filters.command("pussy") & filters.private)
def pussy(_, m):
           api = requests.get("https://meme-api.herokuapp.com/gimme/animepussy").json()
           url = api["url"]
           title = api["title"]
           m.reply_photo(url,caption=title)
         
@bot.on_message(filters.command("ero") & filters.private)
def ero(_, m):
           api = requests.get("https://meme-api.herokuapp.com/gimme/eroanime").json()
           url = api["url"]
           title = api["title"]
           m.reply_photo(url,caption=title)
         
