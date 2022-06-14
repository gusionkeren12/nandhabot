
import imghdr
import os
from bs4 import BeautifulSoup as bs
import requests 
from asyncio import gather
from traceback import format_exc

from pyrogram import filters
from pyrogram.errors import (PeerIdInvalid, ShortnameOccupyFailed,
                             StickerEmojiInvalid, StickerPngDimensions,
                             StickerPngNopng, UserIsBlocked)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from nandhabot import BOT_USERNAME, bot as app, bot
from nandhabot.utils.errors import capture_err
from nandhabot.utils.files import (get_document_from_file_id,
                             resize_file_to_sticker_size, upload_document)

combot_stickers_url = "https://combot.org/telegram/stickers?q="

MAX_STICKERS = (
    120  # would be better if we could fetch this limit directly from telegram
)
SUPPORTED_TYPES = ["jpeg", "png", "webp"]


@app.on_message(filters.command("stickerid"))
@capture_err
async def sticker_id(_, message: Message):
    reply = message.reply_to_message

    if not reply:
        return await message.reply("Reply to a sticker.")

    if not reply.sticker:
        return await message.reply("Reply to a sticker.")

    await message.reply_text(f"`{reply.sticker.file_id}`")


@app.on_message(filters.command("getsticker"))
@capture_err
async def sticker_image(_, message: Message):
    r = message.reply_to_message

    if not r:
        return await message.reply("Reply to a sticker.")

    if not r.sticker:
        return await message.reply("Reply to a sticker.")

    m = await message.reply("Sending..")
    f = await r.download(f"{r.sticker.file_unique_id}.png")

    await gather(
        *[
            message.reply_photo(f),
            message.reply_document(f),
        ]
    )

    await m.delete()
    os.remove(f)

@bot.on_message(filters.command("stickers"))
async def stickers(_, m):
               mrtm = m.reply_to_message
               if len(m.command) < 2:
                   return await m.reply("Gime a text baka!")
               search = m.text.split(None, 1)[1]
               requests.get(combot_stickers_url + search).text
               soup = bs(text, "lxml")
               results = soup.find_all("a", {"class": "sticker-pack__btn"})
               titles = soup.find_all("div", "sticker-pack__title")
               if not results:
                       await m.reply_text("No results found :(.")
                       return
               reply = f"Stickers for *{search}*:"
               for result, title in zip(results, titles):
                    link = result["href"]
                    reply += f"\n• [{title.get_text()}]({link})"
               m.reply_text(reply)

