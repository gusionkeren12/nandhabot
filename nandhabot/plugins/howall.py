
import random
from nandhabot import tbot as asst,bot
from telethon import Button, events
from nandhabot.events import register
from pyrogram import filters

#credits to t.me/nandhaxd
@bot.on_message(filters.command("wish"))
async def wish(_, m):
            reply = m.reply_to_message
            wish_count = random.randint(1,100)
            if not reply:
                if len(m.command) < 2:
                       await m.reply("give a wish 🌠")
                       return 
                       text = m.text.split(None, 1)[1]
                       wish = f""" Hey Dear {m.from_user.mention}
Your Wish: {text}
Possible to Your Wish Cost: {wish_count} 🌠"""
                       await m.reply(wish)
            if reply:
                  text = reply.m.text
                  wish = f""" Hey Dear {m.from_user.mention}
Your Wish: {text}
Possible to Your Wish Cost: {wish_count} 🌠"""
            await m.reply(wish)

BUTTON = [[Button.url("❓ What Is This", "https://t.me/vegetaUpdates/173")]]
HOT = "https://telegra.ph/file/daad931db960ea40c0fca.gif"
SMEXY = "https://telegra.ph/file/a23e9fd851fb6bc771686.gif"
LEZBIAN = "https://telegra.ph/file/5609b87f0bd461fc36acb.gif"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANG = "https://telegra.ph/file/423414459345bf18310f5.gif"
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"

@asst.on(events.NewMessage(pattern="/horny ?(.*)"))
async def horny(e):
         if not e.is_reply:
              user_id = e.sender.id
              user_name = e.sender.first_name
              mention = f"[{user_name}](tg://user?id={str(user_id)})"
              mm = random.randint(1,100)
              HORNY = f"**🔥** {mention} **Is** {mm}**% Horny!**"
              await e.reply(HORNY, buttons=BUTTON, file=HOT)
         if e.is_reply:
               replied = (await e.get_reply_message())
               id = replied.sender.id
               name = replied.sender.first_name
               mention = f"[{name}](tg://user?id={str(id)})"
               mm = random.randint(1,100)
               HORNY = f"**🔥** {mention} **Is** {mm}**% Horny!**"
               await e.reply(HORNY, buttons=BUTTON, file=HOT)

@asst.on(events.NewMessage(pattern="/gay ?(.*)"))
async def gay(e):
         if not e.is_reply:
              user_id = e.sender.id
              user_name = e.sender.first_name
              mention = f"[{user_name}](tg://user?id={str(user_id)})"
              mm = random.randint(1,100)
              GAY = f"**🏳‍🌈** {mention} **Is** {mm}**% Gay!**"
              await e.reply(GAY, buttons=BUTTON, file=SMEXY)
         if e.is_reply:
               replied = (await e.get_reply_message())
               id = replied.sender.id
               name = replied.sender.first_name
               mention = f"[{name}](tg://user?id={str(id)})"
               mm = random.randint(1,100)
               GAY = f"**🏳‍🌈** {mention} **Is** {mm}**% Gay!**"
               await e.reply(GAY, buttons=BUTTON, file=SMEXY)

@asst.on(events.NewMessage(pattern="/lezbian ?(.*)"))
async def lezbian(e):
         if not e.is_reply:
              user_id = e.sender.id
              user_name = e.sender.first_name
              mention = f"[{user_name}](tg://user?id={str(user_id)})"
              mm = random.randint(1,100)
              FEK = f"**💜** {mention} **Is** {mm}**% Lezbian!**"
              await e.reply(FEK, buttons=BUTTON, file=LEZBIAN)
         if e.is_reply:
               replied = (await e.get_reply_message())
               id = replied.sender.id
               name = replied.sender.first_name
               mention = f"[{name}](tg://user?id={str(id)})"
               mm = random.randint(1,100)
               FEK = f"**💜** {mention} **Is** {mm}**% Lezbian!**"
               await e.reply(FEK, buttons=BUTTON, file=LEZBIAN)

@asst.on(events.NewMessage(pattern="/boobs ?(.*)"))
async def boobs(e):
         if not e.is_reply:
              user_id = e.sender.id
              user_name = e.sender.first_name
              mention = f"[{user_name}](tg://user?id={str(user_id)})"
              mm = random.randint(1,100)
              BOOBS = f"**🍒** {mention}**'s Boobs Size Is** {mm}**!**"
              await e.reply(BOOBS, buttons=BUTTON, file=BIGBALL)
         if e.is_reply:
               replied = (await e.get_reply_message())
               id = replied.sender.id
               name = replied.sender.first_name
               mention = f"[{name}](tg://user?id={str(id)})"
               mm = random.randint(1,100)
               BOOBS = f"**🍒** {mention}**'s Boobs Size Is** {mm}**!**"
               await e.reply(BOOBS, buttons=BUTTON, file=BIGBALL)

@asst.on(events.NewMessage(pattern="/cock ?(.*)"))
async def cock(e):
         if not e.is_reply:
              user_id = e.sender.id
              user_name = e.sender.first_name
              mention = f"[{user_name}](tg://user?id={str(user_id)})"
              mm = random.randint(1,100)
              COCK = f"**🍆** {mention}**'s Cock Size Is** {mm}**cm**"
              await e.reply(COCK, buttons=BUTTON, file=LANG)
         if e.is_reply:
               replied = (await e.get_reply_message())
               id = replied.sender.id
               name = replied.sender.first_name
               mention = f"[{name}](tg://user?id={str(id)})"
               mm = random.randint(1,100)
               COCK = f"**🍆** {mention}**'s Cock Size Is** {mm}**cm**"
               await e.reply(COCK, buttons=BUTTON, file=LANG)

@asst.on(events.NewMessage(pattern="/cute ?(.*)"))
async def cute(e):
         if not e.is_reply:
              user_id = e.sender.id
              user_name = e.sender.first_name
              mention = f"[{user_name}](tg://user?id={str(user_id)})"
              mm = random.randint(1,100)
              CUTE = f"**🍑** {mention} {mm}**% Cute**"
              await e.reply(CUTE, buttons=BUTTON, file=CUTIE)
         if e.is_reply:
               replied = (await e.get_reply_message())
               id = replied.sender.id
               name = replied.sender.first_name
               mention = f"[{name}](tg://user?id={str(id)})"
               mm = random.randint(1,100)
               CUTE = f"**🍑** {mention} {mm}**% Cute**"
               await e.reply(CUTE, buttons=BUTTON, file=CUTIE)

