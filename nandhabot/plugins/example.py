from telegram.ext import run_async, CommandHandler,MessageHandler
from nandhabot import dispatcher

import random 


def ban(update, context):
      chat = update.effective_chat
      message = update.effective_message
      bot = context.bot
      user_id = message.reply_to_message.from_user.id
      user_member = chat.get_member(user_id)
      if not message.reply_to_message:
           message.reply_text("reply to someone ban")
           return 
      if not user_member.status == 'administrator' or user_member.status == 'creator':
          message.reply_text("your not admin")
          return 
      if user_member.status == 'administrator' or user_member.status == 'creator':
          chat.ban_member(user_id)
          message.reply_text("banned!")
            

ban_cmd = CommandHandler("ban", ban)
dispatcher.add_handler(ban_cmd)
