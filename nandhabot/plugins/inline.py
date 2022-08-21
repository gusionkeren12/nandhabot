from pyrogram import filters , __version__ as pyro
import random
import requests 
from telethon import __version__ as telever
from nandhabot import bot
from PyDictionary import PyDictionary
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultAnimation,
    InlineQueryResultPhoto,
)

inlinecmds_text = """ **Here you find moi inline functions commands!**
"""

inlinebuttons = [[InlineKeyboardButton(text="Wish", switch_inline_query_current_chat=".wish")]]

@bot.on_message(filters.command("inlinecmds"))
async def inlinecmds(_, message):
            await message.reply_text(inlinecmds_text,
            reply_markup=InlineKeyboardMarkup(inlinebuttons))


@bot.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.strip().lower()
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
        
    elif string.split()[0] == "ud":
         ud_text = string.split(None, 1)[1].strip()
         search = PyDictionary()
         defin = search.meaning(ud_text)
         await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                        f"Definition of: {text}\nDefinition: {defin}"),
                    thumb_url="https://telegra.ph/file/fab6e21499ac634c02e00.jpg",
                    title=f"🔥 How horny are U?",
                    description=f"Send Your Current hornyess To This Chat.")])
                    
                    
    elif string.split()[0] == "wish":
        wish_text = f"✨~~ **yoo!** ~~🤗 ✨\n~~**Your wish Possible to:  {random.choice([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])}%** ~~"
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
