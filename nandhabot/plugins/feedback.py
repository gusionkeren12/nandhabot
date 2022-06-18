from nandhabot import bot, dev_user, SUPPORT_CHAT
from pyrogram import filters
from datetime import datetime
from nandhabot.config import OWNER_ID

#made by t.me/nandhaxd

@bot.on_message(filters.command(["feedback","bug"]))
async def feedback(_, m):
         if msg.chat.username:
        chat_username = (f"@{msg.chat.username}")
    else:
        chat_username = ("Private Group")
         if len(m.command) < 2:
               await m.reply_text("gime a feedback!")
               return 
         if m.chat.type == "private":
                await m.reply_text("command work only groups")
                return 
         if m.from_user.id == OWNER_ID:
               await m.reply_text("owner Baka!")
               return 
         text = m.text.split(None, 1)[1]
         user = m.from_user
         datetimes_fmt = "%d-%m-%Y"
         datetimes = datetime.utcnow().strftime(datetimes_fmt)
         feedback = f""" **#NewFeedBack**
FromChat: {chat_username}
user_id: {user.id}
mention: {user.mention}
msg_date: {datetimes}
Feedback: **{text}**
"""      
         await bot.send_message(f"@{SUPPORT_CHAT}", feedback)
    
