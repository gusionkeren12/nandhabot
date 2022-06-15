from requests import post, get
from nandhabot import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


@bot.on_message(filters.command('paste'))
def paste(_, m):
    reply = m.reply_to_message
    text = reply.text or reply.caption
    if reply:
        x = paste(text)
        m.reply(x,
                      reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton("Paste Link🔗 ", url=x)]]))

    else:
        m.reply_text("Reply to a message!")
