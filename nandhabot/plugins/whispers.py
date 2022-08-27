from pyrogram import filters
from pyrogram.types import *

from nandhabot import bot



@bot.on_message(filters.command("whisper"))
async def whisper(_, message):
      global user_id, name, text
      name = message.from_user.first_name
      mention = message.from_user.mention
      if len(message.command) <2:
          return await message.reply("ɢɪᴠᴇ  ᴀ  ᴜsᴇʀɪᴅ  ᴡʜᴏ  ᴡᴀɴᴛ  sᴇᴇ  ʏᴏᴜʀ  ʜɪᴅᴅᴇɴ  ᴍᴇssᴀɢᴇ")
      elif len(message.command) <3:
          return await message.reply("ɢɪᴠᴇ  ᴍᴇssᴀɢᴇ  ᴛᴏ  ᴄʀᴇᴀᴛᴇ  ᴡʜɪsᴘᴇʀ ᴍᴇssᴀɢᴇ!")
      user_id = message.text.split(" ")[1]
      text = message.text.split(" ")[2]
      
      button = [[ InlineKeyboardButton(text="Open Whisper Message!", callback_data="whisper_data")]]
      whisper = f"""** 🕵 New Whisper Message!**
      
**From User:** {mention}
**To UserID:** `{user_id}`

**Note: this Message only can open the: To UserID
Your Not Allow To See Other Personal Messages!**
"""
      await bot.send_message(message.chat.id,whisper,
               reply_markup=InlineKeyboardMarkup(button))
         

@bot.on_callback_query(filters.regex("whisper_data"))
async def whisperdata(_, query):
       user = await bot.get_users(user_id)
       if query.from_user.id == user.id:
          WHISPER = f"""hey! {user.first_name},
          here your message from {name} Message: {text}"""
          await query.answer(WHISPER, show_alert=True)
       else:
           await query.answer("YOUR NOT ALLOWED")
