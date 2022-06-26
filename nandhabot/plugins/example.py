from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler,run_async,CallbackQueryHandler
from nandhabot import dispatcher, dev_user

from cachetools import TTLCache

# stores admemes in memory for 10 min.
ADMIN_CACHE = TTLCache(maxsize=512, ttl=60 * 10, timer=perf_counter)

def refresh_admin(update, _):
    try:
        ADMIN_CACHE.pop(update.effective_chat.id)
    except KeyError:
        pass

    update.effective_message.reply_text("Admins cache refreshed!")
         



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
             message.reply_text(TEXT,reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton(text="❕Unban", callback_data=f"unbanb_unban={message.reply_to_message.from_user.id}")]]),parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True )

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
┃ ➢ : [ᴄʜᴀᴛ](https://t.me/{chat.username})
┃➢ : [ᴀᴅᴍɪɴ](tg://user?id={message.from_user.id})
┃➢ : [ᴜsᴇʀ](tg://user?id={message.reply_to_message.from_user.id})
┗━━━━━━━━┛
"""
    user_member = chat.get_member(user.id)
    if user_member.status == 'administrator' or user_member.status == 'creator' and message.from_user.id in dev_user:
         chat.unban_member(message.reply_to_message.from_user.id)
         message.reply_text(TEXT)
    else:
         message.reply_text(f"[ʏᴏᴜʀ ɴᴏᴛ ᴀᴅᴍɪɴ 🙄](tg://user?id={message.from_user.id})",parse_mode=ParseMode.MARKDOWN)

def unbanb_btn(update: Update, context):
    bot = context.bot
    query = update.callback_query
    chat = update.effective_chat
    user = update.effective_user
    if query.data != "unbanb_del":
        splitter = query.data.split("=")
        query_match = splitter[0]
        if query_match == "unbanb_unban":
            user_id = splitter[1]
        user_member = chat.get_member(user.id)
        if not query.from_user.id in dev_user:
                bot.answer_callback_query(
                    query.id,
                    text="You don't have enough rights to unmute people",
                    show_alert=True,
                )
        if query.from_user.id in dev_user:
               chat.unban_member(user_id)
               TEXT= f"""❕* EVENT UN-BANNED:*
┏━━━━━━━━┓
┃ ➢ : [ᴄʜᴀᴛ](https://t.me/{chat.username})
┃➢ : [ᴀᴅᴍɪɴ](tg://user?id={query.message.from_user.id})
┃➢ : [ᴜsᴇʀ](tg://user?id={query.message.reply_to_message.from_user.id})
┗━━━━━━━━┛
"""
               query.message.edit_text(TEXT,parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

BAN_CMD = CommandHandler("ban", ban,run_async=True) 
dispatcher.add_handler(BAN_CMD)
UNBAN_CMD = CommandHandler("unban", unban,run_async=True) 
dispatcher.add_handler(UNBAN_CMD)
UNBAN_BUTTON_HANDLER = CallbackQueryHandler(unbanb_btn, pattern=r"unbanb_")
dispatcher.add_handler(UNBAN_BUTTON_HANDLER)
refresh_admin_cmd = CommandHandler(["reload","admincache"], refresh_admin,run_async=True)
dispatcher.add_handler(refresh_admin_cmd)
