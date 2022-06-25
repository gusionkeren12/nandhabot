from telegram.ext import run_async, CommandHandler,MessageHandler
from nandhabot import dispatcher

import random 


def ban(update, context):
      chat = update.effective_chat
      message = chat = update.effective_message
      bot = context.bot
      user = update.effective_user
      user_id = bot.get_chat(user).id
      user_member = chat.get_member(user_id)
      if not user_member.status == 'administrator' or user_member.status == 'creator':
          message.reply_text("your not admin")
          return 
      if user_member.status == 'administrator' or user_member.status == 'creator':
          chat.kick_member(user_id)
          message.reply_text("banned!")

ban_cmd = CommandHandler("ban", ban)
dispatcher.add_handler(ban_cmd)
