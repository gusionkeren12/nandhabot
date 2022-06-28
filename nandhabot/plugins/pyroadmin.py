from pyrogram import filters
from nandhabot import bot
from pyrogram.types import *
import os

@bot.on_message(filters.command("del"))
async def delete(_, m):
     reply = m.reply_to_message
     chat = m.chat
     user = m.from_user
     user_stats = await bot.get_chat_member(chat.id, user.id)
     bot_stats = await bot.get_chat_member(chat.id, "self")
     if not bot_stats.privileges:
            await m.reply_text("Make Me Admin REEE!!")
            return 
     if not user_stats.privileges:
            await m.reply_text("Only Admins are allowed to use this command!")
            return 
     if not reply:
             await m.reply_text("reply to msg for deleting")
             return 
     if not bot_stats.privileges.can_delete_messages:
               await m.reply_text("**I'm missing the permission of**:\n`can_delete_messages`")
               return 
     if not user_stats.privileges.can_delete_messages:
               await m.reply_text("**your are missing the permission of**:\n`can_delete_messages`")
               return 
     if user_stats.privileges.can_delete_messages:
               await reply.delete()
               await m.delete()
      
@bot.on_message(filters.command("ban"))
async def banned(_, m):
     reply = m.reply_to_message
     chat = m.chat
     user = m.from_user
     bot_stats = await bot.get_chat_member(chat.id, "self")
     if not bot_stats.privileges:
            await m.reply_text("Make Me Admin REEE!!")
            return 
     user_stats = await bot.get_chat_member(chat.id, user.id)
     if not user_stats.privileges:
            await m.reply_text("Only Admins are allowed to use this command!")
            return 
     if not reply:
             await m.reply_text("reply to user or channel")
             return 
     if not bot_stats.privileges.can_restrict_members:
               await m.reply_text("**I'm missing the permission of**:\n`can_restrict_members`")
               return 
     if not user_stats.privileges.can_restrict_members:
               await m.reply_text("**your don't having the permission of**:\n`can_restrict_members`")
               return 
     if user_stats.privileges.can_restrict_members:
             ban = reply.from_user or reply.sender_chat
             chat_name = m.chat.title
             if ban:
                    await bot.ban_chat_member(chat.id, ban.id)
                    await m.reply_text(f"[banned](tg://user?id={ban.id}) successfully from {chat_name}")

                    
@bot.on_message(filters.command(["setgtitle","setchattitle"]))
async def setgrouptitle(_, m):
     reply = m.reply_to_message
     user = m.from_user
     chat = m.chat
     new_title = m.text.split(None, 1)[1]
     user_stats = await bot.get_chat_member(chat.id, user.id)
     bot_stats = await bot.get_chat_member(chat.id, "self")
     if not bot_stats.privileges:
            await m.reply_text("Make Me Admin REEE!!")
            return 
     if not user_stats.privileges:
            await m.reply_text("Only Admins are allowed to use this command!")
            return 
     if not bot_stats.privileges.can_manage_chat:
               await m.reply_text("**I'm missing the permission of**:\n`can_manage_chat`")
               return 
     if not user_stats.privileges.can_manage_chat:
               await m.reply_text("**your are missing the permission of**:\n`can_manage_chat`")
               return 
     if user_stats.privileges.can_manage_chat:
               await m.chat.set_title(new_title)
               await m.reply_text(f"Successfully set {new_title} as new chat title!")

@bot.on_message(filters.command(["setgpic","setchatpic"]))
async def setgrouptitle(_, m):
     reply = m.reply_to_message
     user = m.from_user
     chat = m.chat
     user_stats = await bot.get_chat_member(chat.id, user.id)
     bot_stats = await bot.get_chat_member(chat.id, "self")
     if not bot_stats.privileges:
            await m.reply_text("Make Me Admin REEE!!")
            return 
     if not user_stats.privileges:
            await m.reply_text("Only Admins are allowed to use this command!")
            return 
     if not bot_stats.privileges.can_manage_chat:
               await m.reply_text("**I'm missing the permission of**:\n`can_manage_chat`")
               return 
     if not user_stats.privileges.can_manage_chat:
               await m.reply_text("**your are missing the permission of**:\n`can_manage_chat`")
               return 
     if not reply:
                await m.reply_text("reply only document or photo")
                return 
     file = reply.document or reply.photo
     if not file:
               await m.reply_text("reply only document or photo")
               return 
     if user_stats.privileges.can_manage_chat:
               photo = await bot.download_media(file)
               await bot.set_chat_photo(chat.id, photo=photo)
               await m.reply_text("*Successfully group new photo changed!")

