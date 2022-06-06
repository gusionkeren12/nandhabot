import random
from nandhabot.utils.inlinehelper import *
from nandhabot import bot , SUPPORT_CHAT, UPDATES_CHANNEL
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
)

text = """
Hello! Dear Users
I'm An Anime themed Smart VegetaRobot make your group's joyful bellow Using /help commands!!

Powerd by @PegaBots

"""


@bot.on_inline_query()
async def inline_query_handler(client, query):
    text = query.query.lower()
    if text.split()[0] == "alive":
        await client.answer_inline_query(
            query.id,
            results=[
               InlineQueryResultPhoto(
                    photo_url="https://telegra.ph/file/c9c62179fef22450bb342.jpg",
                    thumb_url="https://telegra.ph/file/c9c62179fef22450bb342.jpg",
                    title=f"🤝 Help",
                    description=f" 😎 About @VegetaRobot",
                    reply_markup=InlineKeyboardMarkup(
                    [[ InlineKeyboardButton("Support", url="t.me/VegetaSupport",),
                       InlineKeyboardButton("Updates",url="t.me/VegetaUpdates"), 
                     ],[InlineKeyboardButton(
                                    "Share any thing! 🤝", switch_inline_query=""
                                ),
                            ]
                        ]
                    ),
                ),
            ],
        )
        
@bot.on_inline_query()
async def inline_query_handler(client, query):
    text = query.query.lower()
    if text.split()[0] == "wall":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    is_gallery=True,
                    switch_pm_text="Wallpapers Search | wall [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await wall_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )
