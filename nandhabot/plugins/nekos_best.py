from nandhabot import bot #nekos.best
from pyrogram import filters 
from pyrogram.types import Message 
import requests 



@bot.on_message(filters.command("cuddle"))
def cuddle(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/cuddle").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/cuddle").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("shrug"))
def shrug(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/shrug").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/shrug").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

      
@bot.on_message(filters.command("poke"))
def poke(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/poke").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/poke").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("facepalm"))
def facepalm(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/facepalm").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/facepalm").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("stare"))
def stare(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/stare").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/stare").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
      
@bot.on_message(filters.command("pout"))
def pout(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/pout").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/pout").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("handhold"))
def handhold(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/handhold").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/handhold").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("wave"))
def wave(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/wave").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/wave").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("blush"))
def blush(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/blush").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/blush").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("neko"))
def neko(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/neko").json()
          url = api["results"][0]['url']
          reply.reply_photo(url)
      else:
          api = requests.get("https://nekos.best/api/v2/neko").json()
          url = api["results"][0]['url']
          m.reply_photo(url)

@bot.on_message(filters.command("dance"))
def dance(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/dance").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/dance").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("baka"))
def baka(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/baka").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/baka").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("bore"))
def bore(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/bored").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/bored").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("laugh"))
def laugh(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/laugh").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/laugh").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("smug"))
def smug(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/smug").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/smug").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("thumbsup"))
def thumbsup(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/thumbsup").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/thumbsup").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("shoot"))
def shoot(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/shoot").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/shoot").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("tickle"))
def tickle(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/tickle").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/tickle").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("feed"))
def feed(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/feed").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/feed").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("think"))
def think(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/think").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/think").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("wink"))
def wink(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/wink").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/wink").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("sleep"))
def sleep(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/sleep").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/sleep").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("punch"))
def punch(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/punch").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/punch").json()
          url = api["results"][0]['url']
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
      
   
@bot.on_message(filters.command("kill"))
def kill(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/kill").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/kill").json()
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
    
