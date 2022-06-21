from nandhabot import bot
from pyrogram import filters

@bot.on_message(filters.command("ban"))
async def ban(_, m):
