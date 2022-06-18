from nandhabot import bot, dev_user, SUPPORT_CHAT
from pyrogram import filters
from datetime import datetime
from nandhabot.config import OWNER_ID

#made by t.me/nandhaxd

@bot.on_message(filters.command(["feedback","bug"]))
async def feedback(_, m):
         if len(m.command) < 2:
            await m.reply_text("gime a feedback!")
            return 
         if m.from_user.id == OWNER_ID:
               await m.reply_text("owner Baka!")
               return 
         if m.chat.type == "private":
                await m.reply_text("command work only groups")
                return 
         text = m.text.split(None, 1)[1]
         user = m.from_user
         chat = m.chat
         datetimes_fmt = "%d-%m-%Y"
         datetimes = datetime.utcnow().strftime(datetimes_fmt)
         feedback = f""" **#NewFeedBack**
FromChat: @{chat.username}
user_id : {user.id}
mention : {user.mention}
from_msg : {datetimes}
Feedback: **{text}**
"""      
         await bot.send_message(f"@{SUPPORT_CHAT}", feedback)
    
