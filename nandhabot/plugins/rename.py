from pyrogram import filters
from pyrogram.types import *

from nandhabot import bot


@bot.on_message(filters.command("rename"))
async def rename(_, message):
             if not message.repy_to_message and not message.reply_to_message.media:
                     return await message.reply("reply to media's")
             elif len(message.command) <2:
                  return await message.reply("`provide some text with in extinction!\n for example: '/rename movies.mkv`")
              name = message.text.split(None, 1)[1]
              elif message.reply_to_message.media:
                 downloads = await message.reply_to_message.download(file_name=name)
                 await message.reply_document(downloads)
           
