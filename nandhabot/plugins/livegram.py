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
async def livgram(client: Client, message: Message):
            if not message.from_user.id == OWNER_ID:
                 await message.forward(OWNER_ID)
            
