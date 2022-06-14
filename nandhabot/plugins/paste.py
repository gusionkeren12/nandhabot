
  
from requests import post, get
from nandhabot import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

BASE = "https://batbin.me/"


async def paste(content: str):
    resp = await post(f"{BASE}api/paste", data={"content": content})
    if not resp["status"]:
        return
    return BASE + resp["message"]

def pastex(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


@bot.on_message(filters.command("paste"))
async def paste_func(_, message):
    if not message.reply_to_message:
        return await message.reply("Reply To A Message With /paste")
    r = message.reply_to_message

    if not r.text and not r.document:
        return await message.reply(
            "Only text and documents are supported."
        )

    m = await message.reply("Pasting...")

    if r.text:
        content = str(r.text)
    elif r.document:
        if r.document.file_size > 40000:
            return await m.edit(
                "You can only paste files smaller than 40KB."
            )
        if not pattern.search(r.document.mime_type):
            return await m.edit("Only text files can be pasted.")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)

    link = await paste(content)
    x = pastex(r.text)
    try:
        await message.reply_photo(
            photo=link, quote=False, caption=f"{link}"
        )
    except Exception:
        await message.reply(f"Here's your paste {link}")
    await m.delete()
