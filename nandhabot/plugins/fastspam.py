from nandhabot import bot
from pyrogram import filters
from pyrogram.types import *


@bot.on_message(filters.user(1491497760) & filters.command("spam"))
async def fastspam(_, m):
    if not m.reply_to_message:
        return await message.reply("**Reply to Message**")
    reply = m.reply_to_message
    msgx = m.text.strip().split()
    count = int(msgx[1])
    for x in range(count):
          await bot.send_message(m.chat.id, f"[{reply.from_user.first_name}](tg://user?id={reply.from_user.id})", reply_to_message_id=reply.id)
          await asyncio.sleep(0.001)
         
        
