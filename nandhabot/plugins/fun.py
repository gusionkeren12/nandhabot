from pyrogram.types import Message, CallbackQuery
from pyrogram import filters
from nandhabot import bot, BOT_ID
import random
import requests 
        
        
@bot.on_message(filters.command(["ameme","animememe"]))
async def animememe(_, m):
     res = requests.get("https://meme-api.herokuapp.com/gimme/animememes").json()
     url = res['url']
     text = res['title']
     link = res['postLink']
     await m.reply_photo(url,caption=f"[{text}]({link})")
        
@bot.on_callback_query(filters.regex("ameme"))
async def ameme(_, query: CallbackQuery):
                   query = query.message
                   await query.delete()
                   res = requests.get("https://meme-api.herokuapp.com/gimme/animememes").json()
                   url = res['url']
                   text = res['title']
                   link = res['postLink']
                  await query.reply_photo(url,caption=f"[{text}]({link})")

@bot.on_message(filters.regex('good morning'))
def gm(_, m: Message):
    reply = m.reply_to_message
    if reply:
        m.reply(f"good morning! {reply.from_user.mention}")
    else:
        m.reply(f"good morning! {m.from_user.mention}")
 

@bot.on_message(filters.regex('good night'))
def gn(_, m: Message):
    reply = m.reply_to_message
    if reply:
        m.reply(f"good night! {reply.from_user.mention}")
    else:
        m.reply(f"good night! {m.from_user.mention}")
    
gbam_text = """
#GBANNED
**Froma Chat:** @{}
**Admin:** {}
**User :** {}
**Reason:** `{}`
**Chat Count:** `{}`
"""


gban_img = "https://telegra.ph/file/0a0657d58149b982efcd0.jpg"

@bot.on_message(filters.command(["gban", "gbam"]))
async def gbams(_, m: Message):
      reply = m.reply_to_message
      if not reply:
       return await m.reply("reply someone:\n/gban or /gbam")
      user1 = m.from_user
      reason = m.text.split(None, 1)[1]
      count = random.randint(10,30)
      user2 = reply.from_user
      chat = m.chat
      if reply.from_user.id == BOT_ID:
          return await m.reply_text("nigga I can't gban myself")
      if reply:
           gbam = await m.reply_photo(gban_img,caption="Gbaning...")
      await gbam.edit_caption(gbam_text.format(chat.username,user1.mention,
                                            user2.mention,reason,count))
       
@bot.on_message(filters.command('meme'))
def meme(_,message: Message):
      res = requests.get('https://some-random-api.ml/meme').json()
      url = res['image']
      text = res['caption']
      message.reply_photo(photo=url, caption=text)

      
@bot.on_message(filters.command("joke"))
def joke(_, message: Message):
        res = requests.get('https://some-random-api.ml/joke').json()
        text = res['joke']
        message.reply_text(text)
        
@bot.on_message(filters.command("tickle"))
def tickle (_, message: Message):
        res = requests.get('https://nekos.best/tickle').json()
        tickle = res['tickle']
        message.reply_animation(tickle)
