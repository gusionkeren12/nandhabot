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
     user = m.from_user.id
     chat = m.chat
     if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
     if user in (await is_admins(chat_id)):
         await bot.ban_chat_member(m.chat.id, reply.from_user.id)
         await m.reply_text(f"bammed! {reply.from_user.id}")
