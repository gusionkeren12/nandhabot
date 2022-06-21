from pyrogram import filters 
from nandhabot import bot
from nandhabot.config import OWNER_ID

def is_admin(group_id: int, user_id: int):
    try:
        user_data = bot.get_chat_member(group_id, user_id)
        if user_data.status == 'administrator' or user_data.status == 'creator':
            # print(f'is admin user_data : {user_data}')
            return True
        else:
            # print('Not admin')
            return False
    except:
        # print('Not admin')
        return False


@bot.on_message(filters.command('ban'))
def ban(_, message):
    # scammer = reply.from_user.id
    reply = message.reply_to_message
    if is_admin(
            message.chat.id, message.from_user.id
    ) and not reply.from_user.id in OWNER_ID:
        bot.chat.ban_member(message.reply_to_message.from_user.id)
        bot.send_message(
            message.chat.id,
            f"Banned! {reply.from_user.username}")
