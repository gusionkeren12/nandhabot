from pyrogram import filters
from pyrogram.types import *

from nandhabot import bot

whisper = """**🕵 New Whisper Message!**
**From User:** {}
**To UserID:** `{}`

**Note: this Message only can open the To UserID
Your Not Allow To See Other Personal Messages!**
"""

@bot.on_message(filters.command("whisper"))
async def whisper(_, message):
      global user_id
      mention = message.from_user.mention
      if len(message.command) <2:
          return await message.reply("ɢɪᴠᴇ  ᴀ  ᴜsᴇʀɪᴅ  ᴡʜᴏ  ᴡᴀɴᴛ  sᴇᴇ  ʏᴏᴜʀ  ʜɪᴅᴅᴇɴ  ᴍᴇssᴀɢᴇ")
      elif len(message.command) <3:
          return await message.reply("ɢɪᴠᴇ  ᴍᴇssᴀɢᴇ  ᴛᴏ  ᴄʀᴇᴀᴛᴇ  ᴡʜɪsᴘᴇʀ ᴍᴇssᴀɢᴇ!")
      user_id = message.text.split(" ")[1]
      text = message.text.split(" ")[2]
      button = [[ InlineKeyboardButton(text="Open Whisper Message!", callback_data="whisper_data")]]
      await bot.send_message(message.chat.id, whisper.format(mention,user_id),reply_markup=InlineKeyboardMarkUp(button))
         
