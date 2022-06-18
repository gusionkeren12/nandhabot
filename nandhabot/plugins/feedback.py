from nandhabot import bot, dev_user, SUPPORT_CHAT
from pyrogram import filters
from nandhabot.config import OWNER_ID

#made by t.me/nandhaxd

@bot.on_message(filters.command(["feedback","bug"]))
async def(_, m):
      if not len(m.command) <2:
          return await m.reply_text("gime a feedback!")
      if m.from_user.id in OWNER_ID or dev_user:
          return await m.rely_text("hey! baka this is your bot!")
      text = m.text.split("", 1)
      user = m.from_user
      chat = m.chat
      caption = f"""
**#NewFeedBack**
FromChat:{chat.title}
user_id : {user.id}
mention : {user.mention}
Feedback: **{text}**
"""   await bot.send_message(f"@{SUPPORT_CHAT}", caption=caption)
    
