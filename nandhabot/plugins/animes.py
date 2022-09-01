from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests 
from pyrogram import filters
from nandhabot import bot

anews = requests.get("https://api.safone.tech/anime/news").json() 


@bot.on_message(filters.command("anews"))
async def animenews(_, message):
       caption = anews["results"][0]['description']
       img = anews["results"][0]["imageUrl"]
       link = anews["results"][0]["link"]
       title = anews["results"][0]["title"] 
       caption = f"""**Title**: `{title}`\n\n**News**: `{caption}`
       await message.reply_photo(img,caption=caption,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Source Link", url=link)]]))
