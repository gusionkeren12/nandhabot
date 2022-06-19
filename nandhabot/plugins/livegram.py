from nandhabot import bot
from pyrogram import filters
from nandha.config import OWNER_ID

@bot.on_message(filters.private)
async def livgram(_, m):
            if m.from_user.id == OWNER_ID:
                await message.forward(
                      chat_id=OWNER_ID)
