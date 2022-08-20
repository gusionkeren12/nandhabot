from pyrogram import filters , __version__ as pyro
import random
import requests 
from telethon import __version__ as telever
from nandhabot import bot

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultAnimation,
    InlineQueryResultPhoto,
)



wish_text = """✨~~ **hey! {}!** ~~🤗
✨ ~~**Your wish**:~~ **{}** 😃
✨ ~~ **Possible to: {}%** ~~
"""

@bot.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.lower()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultPhoto(
                    photo_url="https://telegra.ph/file/c9c62179fef22450bb342.jpg",
                    thumb_url="https://telegra.ph/file/c9c62179fef22450bb342.jpg",
                    caption=f""" Iam At Least Version 
                    Pyrogram Based @TrunksRobot I Can Help And Hope Your Groups ❕❕

Pyrogram Version: {pyro}
Telethon Version: {telever}

Thanks for using and keep support my channels!""",
                    title=f"🤝 Help",
                    description=f" 😎 Alive & About @VegetaRobot",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Support",url="t.me/VegetaSupport", ),
                          InlineKeyboardButton("Updates",url="t.me/VegetaUpdates"),
                            ]
                        ]
                    ))])
    elif string == "wish":
        wish_count = random.randint(1,100)
        api = requests.get("https://nekos.best/api/v2/happy").json()
        url = api["results"][0]['url']
        await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultAnimation(
                animation_url=url,
                thumb_url=url,
                caption=wish_text,
                title="Your Wish 😍",
                description="Chance's of Your Wish")])
