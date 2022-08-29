from pyrogram import filters
from pyrogram.types import *

from nandhabot import bot



@bot.on_message(filters.command("rename"))
async def rename(_, message):
          try:
             if not message.reply_to_message and not message.reply_to_message.media:
                     return await message.reply("reply to media's")
             elif len(message.command) <2:
                  return await message.reply("provide some text with in extinction!\n for example: `/rename movies.mkv`")
             name = message.text.split(None, 1)[1]
             if message.reply_to_message.media:
                 msg = await message.reply("`now downloading...`")
                 downloads = await message.reply_to_message.download(file_name=name)
                 await msg.edit("`download complete!\n now uploading to telegram")
                 return await message.reply_document(downloads)
                 await msg.delete()
          except Exception as error:
                 await message.reply("**ERROR**: {error}")
             
