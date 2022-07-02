from pyrogram import filters
from nandhabot import ubot

@ubot.on_message(filters.command("userbot"))
async def userbot(_, m):
       await m.reply_text("yep userbot online!")
