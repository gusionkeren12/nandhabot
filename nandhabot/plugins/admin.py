from nandhabot import bot
from pyrogram import filters
from nandhabot.utils.admin_check import *

async def admin_filter_f(filt, client, message):
    return await admin_check(message)


admin_fliter = filters.create(
    func=admin_filter_f,
    name="AdminFilter"
)

@bot.on_message(filters.command("ban") & admin_filter)
async def ban(_, m):
          if not m.reply_to_message:
                await m.reply_text("reply to user")
                return 
          if m.reply_to_message:
                 user = m.from_user
                 await bot.ban_chat_member(m.chat.id, user.id)
                 await m.reply_text(f"banned! {user.mention}")
