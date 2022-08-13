from pyrogram import filters 
from nandhabot import bot

@bot.on_message(filters.command("save") & filters.user(1491497760))
async def save(_, m):
            reply = m.reply_to_message
            await bot.copy_message("@Nandha_days", message.chat.id, reply.id)
            await m.reply_text("**Successfully Saved!**\n**@Nandha_Days**")
            
