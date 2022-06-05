from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
from nandhabot import bot
import random
import requests 
        
        
@bot.on_message(filters.command(["ameme","animememe"]))
async def animememe(_, m):
     res = requests.get("https://meme-api.herokuapp.com/gimme/animememes").json()
     url = res['url']
     text = res['title']
     link = res['postLink']
     await m.reply_photo(url,caption=f"[{text}]({link})",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="ameme",
                    ),
                ],
            ],
        ),
    )
        
@bot.on_callback_query(filters.regex("ameme"))
async def ameme(_, query: CallbackQuery):
                   query = query.message
                   await query.delete()
                   res = requests.get("https://meme-api.herokuapp.com/gimme/animememes").json()
                   url = res['url']
                   text = res['title']
                   link = res['postLink']
                   await query.reply_photo(url,caption=f"[{text}]({link})",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="ameme",
                    ),
                ],
            ],
        ),
    )
                
@bot.on_message(filters.command("meme"))
async def meme(_, m):
     res = requests.get("https://meme-api.herokuapp.com/gimme/memes").json()
     url = res['url']
     text = res['title']
     link = res['postLink']
     await m.reply_photo(url,caption=f"[{text}]({link})",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="meme",
                    ),
                ],
            ],
        ),
    )
        
@bot.on_callback_query(filters.regex("meme"))
async def nmeme(_, query: CallbackQuery):
                   query = query.message
                   await query.delete()
                   res = requests.get("https://meme-api.herokuapp.com/gimme/memes").json()
                   url = res['url']
                   text = res['title']
                   link = res['postLink']
                   await query.reply_photo(url,caption=f"[{text}]({link})",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="meme",
                    ),
                ],
            ],
        ),
    )

