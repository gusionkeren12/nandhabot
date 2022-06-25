from telegram import Update
from nandhabot import dispatcher
from telegram.ext import CallbackContext, CommandHadler, run_async

@run_async
def ban(update: Update, context: CallbackContext):
          message = update.effective_message
          chat = update.effective_chat
          member = update.effective_chat.get_member
          if not member(update.effective_user.id).status == ("administrator" or "creator"):
                    message.reply_text("your not admin")
          if member(update.effective_user.id).status == ("administrator" or "creator"):
                       chat.ban_member(message.reply_to_message.from_user.id)
                       message.reply_text("banned!")


ban_cmd = CommandHandler("ban", ban) 

dispatcher.add_handler(ban_cmd)
