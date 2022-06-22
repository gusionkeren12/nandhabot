from nandhabot import bot
from pyrogram import filters


@bot.on_message(filters.command('ban'))
async def ban(_, message):
    chat_id = message.chat.id
    msg = message.reply_to_message
    member = await bot.get_chat_member(chat_id, message.from_user.id)
    if member.status in ("administrator", "creator"):
        txt = message.text.split(" ")[1]
        if msg:
            user_id = msg.from_user.id
            user = await bot.get_users(user_id)
            await bot.ban_chat_member(chat_id, user_id)
            await message.reply_text(f"Banned {user.mention} successfully")
        if txt:
            user = await bot.get_users(txt)
            user_id = user.id
            await bot.ban_chat_member(chat_id, user_id)
            await message.reply_text(f"Banned {user.mention} successfully")
        else:
            await message.reply_text("Reply to someone, or give username or id of them")
    else:
        await message.reply_text("Only Admins Can Ban.")

