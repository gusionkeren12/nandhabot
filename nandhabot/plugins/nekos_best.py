from nandhabot import bot #nekos.best
from pyrogram import filters 
from pyrogram.types import Message 
import requests 

@bot.on_message(filters.command("kill"))
def kill(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/kill").json()
          url = api["url"]
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/kill").json()
          url = api["url"]
          m.reply_animation(animation=url)
 

@bot.on_message(filters.command("cry"))
def cry(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/cry").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/cry").json()
          url = api["url"]
          m.reply_animation(animation=url)
      
    
@bot.on_message(filters.command("smile"))
def smile(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/smile").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/smile").json()
          url = api["url"]
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("highfive"))
def highfive(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/highfive").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/highfive").json()
          url = api["url"]      
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("slap"))
def slap(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/slap").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
           api = requests.get("https://api.waifu.pics/sfw/slap").json()
           url = api["url"]
           m.reply_animation(url)      
         
    
@bot.on_message(filters.command("kick"))
def kick(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/kick").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/kick").json()
          url = api["url"]     
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("hug"))
def hug(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/hug").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/hug").json()
          url = api["url"]  
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("pat"))
def pat(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/pat").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/pat").json()
          url = api["url"]
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("waifu"))
def waifu(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/waifu").json()
           url = api["url"]
           reply.reply_photo(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/waifu").json()
          url = api["url"]       
          m.reply_photo(photo=url)
    
