from nandhabot import bot, dev_user, SUPPORT_CHAT
from pyrogram import filters
from nandhabot.config import OWNER_ID

#made by t.me/nandhaxd

@bot.on_message(filters.command(["feedback","bug"]))
async def feedback(_, m):
         if len(m.command) < 2:
            return await m.reply_text("gime a feedback!")
         text = m.text.split(None, 1)[1]
         user = m.from_user
         chat = m.chat
         feedback = f""" **#NewFeedBack**
FromChat: @{chat.username}
user_id : {user.id}
mention : {user.mention}
Feedback: **{text}**
"""      
         await bot.send_message(f"@{SUPPORT_CHAT}", feedback)
    
