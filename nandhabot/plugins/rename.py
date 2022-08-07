from nandhabot import bot
import os
from nandhabot.utils.sendlog import send_log
from pyrogram import filters
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup

@bot.on_message(filters.command('rename'))
def rename(_, message):

    try:
        filename = message.text.replace(message.text.split(" ")[0], "")

    except Exception as e:
        send_log(e)
    reply = message.reply_to_message
    if reply:
            buttons = [[ 
                                InlineKeyboardButton("FILE" , callback_data="videotype"),
                                InlineKeyboardButton("VIDEO",  callback_data="filetype")]] 
            message.reply_text("Choose the below Button Which Type You Want!",
            reply_markup=inlineKeybordMarkup(buttons))
    else:
           message.reply_text("reply to document")
        

@bot.on_message(filters.regex("filetype"))
def filetype(_, m):
        x = message.reply_text("Downloading.....")
        path = reply.download(file_name=filename)
        x.edit("uploading now..... ")
        message.reply_document(path)
        os.remove(path)
