from pyrogram import filters
from nandhabot import bot

@bot.on_message(filters.command("pdel"))
async def (_, m):
     reply = m.reply_to_message
     chat = m.chat
     user = m.from_user
     user_stats = await bot.get_chat_member(chat.id, user.id)
     it user_stats.privileges.can_delete_messages == "false":
            await message.reply_text("You don't having a deleting permission")
            return 
     it user_stats.privileges.can_delete_messages == "true":
               await reply.delete()
               await message.reply_text("deleted!")
