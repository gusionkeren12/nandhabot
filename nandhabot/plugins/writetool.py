from pyrogram import filters
from pyrogram.types import Message

from nandhabot import bot


@bot.on_message(filters.command("write"))
async def handwriting(_, m : Message):
    if len(m.command) < 2:
        return await m.reply_text("`» Give some text to write...`")
    m = await m.reply_text("`» I writing please wait...`")
    name = (
        m.text.split(None, 1)[1]
        if len(m.command) < 3
        else m.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("`» Uploading...`")
    await m.reply_photo(hand, caption="`🖊 Written by @VegetaRobot`")
