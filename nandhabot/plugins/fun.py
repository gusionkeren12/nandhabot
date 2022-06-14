from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
from nandhabot import bot, BOT_ID
import random
import requests 
import secureme

@bot.on_message(filters.command("encrypt"))
async def encrypt(_, m):
           reply = m.reply_to_message
           if not reply:
                return await m.reply_text("reply to message encrypt")
           if reply:
                   rtext = m.reply_to_message.text
                   encrypt = secureme.encrypt(rtext)
                   text = await m.reply_text("encrypting....")
                   await text.edit(encrypt)

@bot.on_message(filters.command("decrypt"))
async def decrypt(_, m):
           reply = m.reply_to_message
           if not reply:
                return await m.reply_text("reply to message decrypt")
           if reply:
                   rtext = m.reply_to_message.text
                   decrypt = secureme.decrypt(rtext)
                   text = await m.reply_text("decrypting....")
                   await text.edit(decrypt)

@bot.on_message(filters.command("truth"))
async def truth(_, m):
         reply = m.reply_to_message
         if reply:
               get = requests.get("https://api.truthordarebot.xyz/v1/truth").json
               text = get["question"]
               await m.reply_text(text)
         else:
               get = requests.get("https://api.truthordarebot.xyz/v1/truth").json
               text = get["question"]
               await m.reply_text(text)
                      
@bot.on_message(filters.command("dare"))
async def dare(_, m):
         reply = m.reply_to_message
         if reply:
               get = requests.get("https://api.truthordarebot.xyz/v1/dare").json
               text = get["question"]
               dare = f"""
               Hey! {reply.from_user.mention}
               {m.from_user.mention} give you a dare!
               <bDare</b>: <code>{text}</code>
               """"
               await m.reply_text(dare)
         else:
               get = requests.get("https://api.truthordarebot.xyz/v1/dare").json
               text = get["question"]
               dare = f"""
               Hey! {m.from_user.mention} your dare here!
               <bDare</b>: <code>{text}</code>
               """"
               await m.reply_text(text)

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
      if len(m.command) < 2:
          return await m.reply("add a reason to gban")
      if reply.from_user.id == BOT_ID:
          return await m.reply_text("nigga I can't gban myself")
      if reply:
          user1 = m.from_user
          reason = m.text.split(None, 1)[1]
          count = random.randint(10,30)
          user2 = reply.from_user
          chat = m.chat
          gbam = await m.reply_photo(gban_img,caption="Gbaning...")
          await gbam.edit_caption(gbam_text.format(chat.username,user1.mention,
                                            user2.mention,reason,count))
       
      
@bot.on_message(filters.command("joke"))
def joke(_, message: Message):
        res = requests.get('https://some-random-api.ml/joke').json()
        text = res['joke']
        message.reply_text(text)
        
