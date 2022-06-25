from telegram import run_async
from telegram.ext import CommandHandler

def ban(update: Update, context):
    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user

    user_member = chat.get_member(user.id)
    if not user_member.status == 'administrator' or user_member.status == 'creator':
            message.reply_text("Your not admin")
    if user_member.status == 'administrator' or user_member.status == 'creator':
             message.reply_text("yes you can")


BAN_CMD = CommandHandler("ban", ban,run_async=True) 
dispatcher.add_handler(BAN_CMD)
