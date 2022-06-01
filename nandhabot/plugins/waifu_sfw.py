from nandhabot import bot
from pyrogram import filters 
from pyrogram.types import Message 
import requests 

@bot.on_message(filters.command("kill"))
def kill(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = request.get("https://api.waifu.pics/sfw/kill").json()
          url = api["url"]
          reply.reply_animation(url)
      else:
          m.reply_animation(url)
 

@bot.on_message(filters.command("cry"))
def cry(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = request.get("https://api.waifu.pics/sfw/cry").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          m.reply_animation(url)
    
