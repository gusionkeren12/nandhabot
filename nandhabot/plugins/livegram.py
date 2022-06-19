from nandhabot import bot
from pyrogram import filters
from nandhabot.config import OWNER_ID

@bot.on_message(filters.private & filters.incoming)
async def livgram(_, m):
            if not m.from_user.id == OWNER_ID:
                 await m.forward(OWNER_ID)
            await m.reply_text("**⚠ Note!**:\n**Your all Dm Message Well Forward to @NandhaxD**")
            text = m.text
            if m.reply_to_message.forward:
                 await bot.send_message(m.forward.from_user.id, text) 
