
import os
import re

import aiofiles
  
from requests import post, get
from nandhabot import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"

@bot.on_message(filters.command("paste"))
async def paste(_, m):
         if not m.reply_to_message:
              return await m.reply("Reply To A Message With /paste")
         reply = m.reply_to_message
         if not reply.text and not reply.document:
               return await m.reply_text("Only work text and document")
         msg = await m.reply_text("Pasting...")
         if reply.text:
               content = str(r.text)
      elif r.document:
         if r.document.file_size > 40000:
                 return await m.edit("You can only paste files smaller than 40KB.")
         if not pattern.search(reply.document.mime_type):
              return await m.edit("Only text files can be pasted.")
         doc = await m.reply_to_message.download()
         async with aiofiles.open(doc, mode="r") as f:
               content = await f.read()
         os.remove(doc)
         link = await paste(reply.text)
         await reply_text(f"{link})
