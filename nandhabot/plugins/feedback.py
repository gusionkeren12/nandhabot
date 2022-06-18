from nandhabot import bot, dev_user, SUPPORT_CHAT
from pyrogram import filters
from datetime import datetime
from pyrogram.types import *
from nandhabot.config import OWNER_ID

#made by t.me/nandhaxd

@bot.on_message(filters.command(["feedback","bug"]))
async def feedback(_, m):
         if m.chat.type == "private":
                await m.reply_text("**Command work only groups!**")
                return 
         if len(m.command) < 2:
               await m.reply_text("**Gime a Feedback!**")
               return 
         if m.from_user.id == OWNER_ID:
               await m.reply_text("**Owner Baka!**")
               return 
         text = m.text.split(None, 1)[1]
         user = m.from_user
         chat = m.chat
         datetimes_fmt = "%d-%m-%Y"
         datetimes = datetime.utcnow().strftime(datetimes_fmt)
         feedback = f""" **#NewFeedBack**
FromChat: {chat.username}
user_id: {user.id}
mention: {user.mention}
msg_date: {datetimes}
Feedback: **{text}**
"""      
         await m.reply_text("Your feedback Successfully Reported On SupportChat!")
         await bot.send_message(f"@{SUPPORT_CHAT}", feedback,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "➡ View Bug", url=f"{m.link}"),
                            InlineKeyboardButton(
                                "❌ Close", callback_data="close")
                        ]
                    ]
                )
            )
    
