from telegram import Update
from telegram.ext import CommandHandler,run_async
from nandhabot import dispatcher

def ban(update: Update, context):
    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    TEXT= f"""❕ EVENT BANNED:
┏━━━━━━━━━━━━━━━━┓
┃ ➢ : {chat.username}
┃➢ : [{message.from_user.first_name}](tg://user?id={message.from_user.id})
┃➢ : [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}]
┗━━━━━━━━━━━━━━━━┛
"""
    user_member = chat.get_member(user.id)
    if user_member.status == 'administrator' or user_member.status == 'creator':
             chat.ban_member(message.reply_to_message.from_user.id)
             message.reply_text(TEXT)
    else:
             message.reply_text("your not admin")

   
            

 

BAN_CMD = CommandHandler("ban", ban,run_async=True) 
dispatcher.add_handler(BAN_CMD)
