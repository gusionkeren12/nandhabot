from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
from nandhabot import bot
import random
import requests 
        
        
#in this plugins made by @NandhaxD in tg

@bot.on_message(filters.command(["ameme","animememe"]))
async def animememes(_, m):
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
async def memes(_, m):
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
async def memess(_, query: CallbackQuery):
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

@bot.on_message(filters.command(["hmeme","hentaimeme"]))
async def hetaimemes(_, m):
     res = requests.get("https://meme-api.herokuapp.com/gimme/hentaimemes").json()
     url = res['url']
     text = res['title']
     link = res['postLink']
     await m.reply_photo(url,caption=f"[{text}]({link})",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="hentaimeme",
                    ),
                ],
            ],
        ),
    )
        
@bot.on_callback_query(filters.regex("hentaimeme"))
async def hmeme(_, query: CallbackQuery):
                   query = query.message
                   await query.delete()
                   res = requests.get("https://meme-api.herokuapp.com/gimme/hentaimemes").json()
                   url = res['url']
                   text = res['title']
                   link = res['postLink']
                   await query.reply_photo(url,caption=f"[{text}]({link})",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="hentaimeme",
                    ),
                ],
            ],
        ),
    )
