from pyrogram import filters 
from pyrogram.types import *
from pyrogram.enums import ChatType

from nandhabot import bot

users = []

@bot.on_message(filters.command("start"))
async def subscription(_, message):
       
       uid = message.from_user.id
       mention = message.from_user.mention
       if ChatType == ChatType.PRIVATE:
           if not uid in users:
                users.append(uid)
                stats = len(users)
           await bot.send_message(-1001717881477,f"""**New User Started Bot**!
**uid: {uid}**
**Name: {mention}**

**Total Users Increased: {stats}**
""")
