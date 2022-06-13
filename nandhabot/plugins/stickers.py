import os
from asyncio import gather

from pyrogram import filters
from pyrogram.types import Message

from nandhabot import bot as app
from nandhabot.utils.errors import capture_err

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
