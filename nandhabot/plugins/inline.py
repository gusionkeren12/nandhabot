from pyrogram import filters 
import random

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
    if string == "alive":
        await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultPhoto(
                    input_message_content=InputTextMessageContent(
                        f"<b>🔥I am</b> {random.choice([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])}<b>% Horny!</b>",
                        disable_web_page_preview=True,
                    ),
                    thumb_url="https://telegra.ph/file/fab6e21499ac634c02e00.jpg",
                    title=f"🔥 How horny are U?",
                    description=f"Send Your Current hornyess To This Chat.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "Share your hornyness! 🔥", switch_inline_query="alive"
                                )
                            ]
                        ]
                    ))])
              
