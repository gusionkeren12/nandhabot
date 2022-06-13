from pyrogram import filters
from pyrogram.types import Message

from nandhabot import bot


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.get_chat_members(chat_id, filter="administrators")
    ]


@bot.on_message(filters.command("ban"))
async def ban(_, m: Message):
    reply = m.reply_to_message
    user = m.from_user.id
    chat_id = m.chat.id
    if user not in (await is_admins(chat_id)):
        return await message.reply_text("`You Are Not Admin`")
    if user in (await is_admins(chat_id)):
        await bot.ban_chat_member(m.chat.id, reply.from_user.id)
        await m.reply_text(f"**Bammed!** {reply.from_user.id}")
