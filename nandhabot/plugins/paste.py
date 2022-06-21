from requests import post, get
from nandhabot import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"



@bot.on_message(filters.command('paste'))
def pastex(_, m):
    reply = m.reply_to_message
    text = reply.text or reply.caption
    key = requests.post(
        'https://nekobin.com/api/documents', json={
            "content": text
        }).json().get('result').get('key')
    nekobin = f"https://nekobin.com/{key}"
    if reply:
        x = paste(text)
        caption = f"[NEKOBIN]({nekobin}) | [SPACEBIN]({x})"
        m.reply(text=caption,
                      reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton("SPACEBIN", url=x),
                             InlineKeyboardButton("NEKOBIN", url=nekobin)]]))

    else:
        m.reply_text("Reply to a message!")
