from pyrogram import filters , version as pyro
import random
from telethon import version as telever
from nandhabot import bot

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
)


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
                    caption = f""" Iam At Least Version 
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
    elif string == "info":
        user_id = query.inline_query.query.split(None, 2)[2]
        await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultArticle(
                input_message_content=InputTextMessageContent(
                        f"{user_id}"),
                    thumb_url="https://telegra.ph/file/fab6e21499ac634c02e00.jpg",
                    title=f"userinfo!",
                    description=f"Userinformatiom searcher")])