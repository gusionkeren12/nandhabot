from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from requests import post

from nandhabot import bot


def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


@bot.on_message(filters.command("paste"))
def pastex(_, message: Message):
    text = message.reply_to_message
    if text:
        x = paste(text.text)
        message.reply(
            x,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Paste Link🔗 ", url=x)]]
            ),
            disable_web_page_preview=True,
        )

    else:
        message.reply_text("Reply to a message!")
