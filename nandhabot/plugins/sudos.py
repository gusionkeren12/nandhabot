from pyrogram import filters
from nandhabot import bot, db

sudoersdb = db.sudoers


async def add_sudo(user_id: int) -> bool:
    sudoers = await get_sudoers()
    sudoers.append(user_id)
    await sudoersdb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True


async def remove_sudo(user_id: int) -> bool:
    sudoers = await get_sudoers()
    sudoers.remove(user_id)
    await sudoersdb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True

@bot.on_message(filters.command("addsudo"))
async def addsudo(_, m):
         user_id = m.reply_to_message.from_user.id
         added = await add_sudo(user_id)
         if added:
              await m.reply_text("Successfully added sudoers")
