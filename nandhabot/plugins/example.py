from telegram import Update, ParseMode
from telegram.ext import CommandHandler,run_async
from nandhabot import dispatcher, dev_user

def ban(update: Update, context):
    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    if not message.reply_to_message:
           message.reply_text("reply to someone!")
           return 
    TEXT= f"""❕* EVENT BANNED:*
┏━━━━━━━━┓
┃ ➢ : [ᴄʜᴀᴛ](https://t.me/c/{chat.id})
┃➢ : [ᴀᴅᴍɪɴ](tg://user?id={message.from_user.id})
┃➢ : [ᴜsᴇʀ](tg://user?id={message.reply_to_message.from_user.id})
┗━━━━━━━━┛
"""
    user_member = chat.get_member(user.id)
    if user_member.status == 'administrator' or user_member.status == 'creator':
             chat.ban_member(message.reply_to_message.from_user.id)
             message.reply_text(TEXT,parse_mode=ParseMode.MARKDOWN)
    if message.reply_to_message.from_user.id in dev_user:
             message.reply_text("that's my developer nigga!")
             return 
    else:
             message.reply_text(f"[ʏᴏᴜʀ ɴᴏᴛ ᴀᴅᴍɪɴ 🙄](tg://user?id={message.from_user.id}),parse_mode=ParseMode.MARKDOWN")

   
            

 

BAN_CMD = CommandHandler("ban", ban,run_async=True) 
dispatcher.add_handler(BAN_CMD)
