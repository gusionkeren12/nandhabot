from nandhabot import bot
import os
from nandhabot.utils.sendlog import send_log
from pyrogram import filters
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types import CallbackQuery

async def progress(current, total): 
   print(f"{current * 100 / total:.1f}%") 

@bot.on_message(filters.command('rename'))
def rename(_, message):
    global reply, filename
    try:
        filename = message.text.replace(message.text.split(" ")[0], "")

    except Exception as e:
        message.reply_text(e)
    reply = message.reply_to_message
    if reply:
            buttons = [[ 
                                InlineKeyboardButton("FILE" , callback_data="filetype"),
                                InlineKeyboardButton("VIDEO",  callback_data="videotype"),
                           ],[ InlineKeyboardButton("PHOTO" , callback_data="phototype")]] 
            message.reply_text("Choose the below Button Which Type You Want!",
            reply_markup=InlineKeyboardMarkup(buttons))
    else:
           message.reply_text("reply to document")
        

@bot.on_callback_query(filters.regex("filetype"))
def filtypes(_, query: CallbackQuery):
           a = ".mkv"
           name = filename+a
           dl = reply.download(file_name=name)
           x = query.message.reply_text("uploading now...")
           query.message.reply_document(dl,caption=f"**{name} @Nandhabots**")
           x.delete()

@bot.on_callback_query(filters.regex("videotype"))
def videotypes(_, query: CallbackQuery):
        a = ".mp4"
        name = filename+a
        dl = reply.download(file_name=name)
        x = query.message.reply_text("uploading now...")
        query.message.reply_video(dl,caption=f"**{name} @Nandhabots**")
        x.delete()

@bot.on_callback_query(filters.regex("phototype"))
def phototypes(_, query: CallbackQuery):
        a = ".png"
        name = filename+a
        dl = reply.download(file_name=name)
        x = query.message.reply_text("uploading now...")
        query.message.reply_photo(dl,caption=f"**{name} @Nandhabots**")
        x.delete()
