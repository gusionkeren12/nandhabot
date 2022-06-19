from nandhabot import bot
from pyrogram import filters
from nandhabot.config import OWNER_ID

@bot.on_message(filters.private & filters.incoming)
async def livgram(_, m):
            if not m.from_user.id == OWNER_ID:
                 await m.forward(chat_id=OWNER_ID)
