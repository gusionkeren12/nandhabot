from nandhabot import bot
from nandhabot.config import OWNER_ID

from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)

@bot.on_message(filters.private & filters.incoming)
async def livgram(_, m: Message):
            if not m.from_user.id == OWNER_ID:
                 await m.forward(OWNER_ID)
            
