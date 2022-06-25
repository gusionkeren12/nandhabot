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
┃ ➢ : [ᴄʜᴀᴛ](https://t.me/{chat.username})
┃➢ : [ᴀᴅᴍɪɴ](tg://user?id={message.from_user.id})
┃➢ : [ᴜsᴇʀ](tg://user?id={message.reply_to_message.from_user.id})
┗━━━━━━━━┛
"""
    user_member = chat.get_member(user.id)
    if user_member.status == 'administrator' or user_member.status == 'creator' and message.from_user.id in dev_user:
             chat.ban_member(message.reply_to_message.from_user.id)
             message.reply_text(TEXT,parse_mode=ParseMode.MARKDOWN)
    if message.reply_to_message.from_user.id in dev_user:
              message.reply_text("that's my developer nigga!")
              return ""
    else:
             message.reply_text(f"[ʏᴏᴜʀ ɴᴏᴛ ᴀᴅᴍɪɴ 🙄](tg://user?id={message.from_user.id})",parse_mode=ParseMode.MARKDOWN)

   
def unban(update: Update, context):
    message = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    if not message.reply_to_message:
           message.reply_text("reply to someone!")
           return 
    TEXT= f"""❕* EVENT UN-BANNED:*
┏━━━━━━━━┓
┃ ➢ : [ᴄʜᴀᴛ](https://t.me/{chat.usernme})
┃➢ : [ᴀᴅᴍɪɴ](tg://user?id={message.from_user.id})
┃➢ : [ᴜsᴇʀ](tg://user?id={message.reply_to_message.from_user.id})
┗━━━━━━━━┛
"""
    user_member = chat.get_member(user.id)
    if user_member.status == 'administrator' or user_member.status == 'creator' and message.from_user.id in dev_user:
             chat.unban_member(message.reply_to_message.from_user.id)
             message.reply_text(TEXT,reply_msg,
            reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton(text="❕Unban", callback_data=f"unbanb_unban={message.reply_to_message.from_user.id}"
                        )]],parse_mode=ParseMode.MARKDOWN)
    else:
             message.reply_text(f"[ʏᴏᴜʀ ɴᴏᴛ ᴀᴅᴍɪɴ 🙄](tg://user?id={message.from_user.id})",parse_mode=ParseMode.MARKDOWN)

def unban_btn(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    query = update.callback_query
    chat = update.effective_chat
    user = update.effective_user
    if query.data != "unbanb_del":
        splitter = query.data.split("=")
        query_match = splitter[0]
        if query_match == "unbanb_unban":
            user_id = splitter[1]
            chat.unban_member(user_id)
            TEXT= f"""❕* EVENT UN-BANNED:*
┏━━━━━━━━┓
┃ ➢ : [ᴄʜᴀᴛ](https://t.me/{chat.usernme})
┃➢ : [ᴀᴅᴍɪɴ](tg://user?id={message.from_user.id})
┃➢ : [ᴜsᴇʀ](tg://user?id={message.reply_to_message.from_user.id})
┗━━━━━━━━┛
"""
            query.message.edit(TEXT)

BAN_CMD = CommandHandler("ban", ban,run_async=True) 
dispatcher.add_handler(BAN_CMD)
UNBAN_CMD = CommandHandler("unban", unban,run_async=True) 
dispatcher.add_handler(UNBAN_CMD)
