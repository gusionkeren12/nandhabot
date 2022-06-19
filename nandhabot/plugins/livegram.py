from nandhabot import bot
from pyrogram import filters
from nandhabot.config import OWNER_ID

@bot.on_message(filters.private & filters.incoming)
async def livgram(_, m):
            if not m.from_user.id == OWNER_ID:
                 await m.forward(OWNER_ID)
            text = m.text
            if m.reply_to_message.forward:
                 await bot.send_message(m.reply_to_message.forward_from.id, text) 
