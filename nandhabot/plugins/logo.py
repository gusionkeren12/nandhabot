

from nandhabot import bot
from pyrogram import filters
import requests 


@bot.on_message(filters.command("logo"))
async def logo(_, m):
             text = m.text.split(None, 1)[1]
             logo = get((f"https://single-developers.up.railway.app/logo?name={text}").replace(' ','%20')).history[1].url
             await m.reply_photo(logo,caption="Made by @VegetaRobot")
