from pyrogram import filters
from nandhabot import bot


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in app.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]

@bot.on_message(filters.command("ban"))
async def ban(_, m):
     reply = m.reply_to_message
     if not is_admin:
          await m.reply("your not admin!")
     if m.from_user.id in is_admin:
          await bot.ban_chat_member(m.chat.id, reply.from_user.id)
          await m.reply_text(f"bammed! {reply.from_user.id}")
