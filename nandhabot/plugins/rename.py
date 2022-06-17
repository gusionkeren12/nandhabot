from nandhabot import bot
import os
from nandhabot.utils.sendlog import send_log
from pyrogram import filters


@bot.on_message(filters.command('rename'))
def rename(_, message):

    try:
        filename = message.text.replace(message.text.split(" ")[0], "")

    except Exception as e:
        send_log(e)

    if reply := message.reply_to_message:
        x = message.reply_text("Downloading.....")
        path = reply.download(file_name=filename)
        x.edit("Uploading.....")
        message.reply_document(path)
        os.remove(path)

@bot.on_message(filters.command("s2i"))
async def converttwoimage(_, m):
              reply = m.reply_to_message
              if not reply:
                   return await m.reply("reply to sticker")
              if not reply.sticker:
                    return await m.reply("reply to sticker")
              if reply.sticker:
                   msg = await m.reply("downloading")
                   file_id = reply.sticker.file_id
                   name = "image.png"
                   file = await bot.download_media(file_id, file_name=name)
                   await msg.edit("uploading")
              await m.reply_document(file)
              await msg.delete()
