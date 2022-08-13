from pyrogram import filters 
from nandhabot import bot

@bot.on_message(filters.command("save") & filters.user(1491497760))
async def save(_, m):
            try:
                reply = m.reply_to_message
               await bot.copy_message("@Nandha_days", m.chat.id, reply.id)
               await m.reply_text("**Successfully Saved!**\n**@Nandha_Days**")
            except Exception as e:
                  await m.reply_text(f"error: {e}")
