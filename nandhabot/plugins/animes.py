from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import requests 
from pyrogram import filters
from nandhabot import bot






@bot.on_message(filters.command("anews"))
async def animenews(_, message):
       global limit
       limit = 1
       api = f"https://api.safone.tech/anime/news?limit={limit}"
       anews = requests.get(api).json() 
       caption = anews["results"][0]['description']
       img = anews["results"][0]["imageUrl"]
       link = anews["results"][0]["link"]
       title = anews["results"][0]["title"] 
       caption = f"""**Title**: `{title}`\n\n**News**: `{caption}`"""
       await message.reply_photo(img,caption=caption,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Source Link", url=link),
             InlineKeyboardButton(text="Next", callback_data="animenews")]]))

@bot.on_callback_query(filters.regex("animenews"))
async def animenews(_, query):
       next = limit+1
       api = f"https://api.safone.tech/anime/news?limit=2"
       anews = requests.get(api).json() 
       caption = anews["results"][0]['description']
       img = anews["results"][0]["imageUrl"]
       link = anews["results"][0]["link"]
       title = anews["results"][0]["title"] 
       caption = f"""**Title**: `{title}`\n\n**News**: `{caption}`"""
       await query.message.edit_media(
          media=InputMediaPhoto(img,caption=caption))
