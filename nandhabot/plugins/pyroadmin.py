from pyrogram import filters, enums
from nandhabot import bot
from pyrogram.types import *
import os, io, json



   
      
      
@bot.on_message(filters.command("promote"))
async def promoting(_, message):
     global new_admin
     if not message.reply_to_message:
         return await message.reply("**Reply someone To Promoting.**")
     reply = message.reply_to_message
     chat_id = message.chat.id
     new_admin = reply.from_user
     admire = message.from_user
     user_stats = await bot.get_chat_member(chat_id, admire.id)
     bot_stats = await bot.get_chat_member(chat_id, "self")
     if not bot_stats.privileges:
         return await message.reply("**Lol! Make Me Admin When!**")
     elif not user_stats.privileges:
         return await message.reply("**You Needs Admin Rights to Control Me (~_^)!**")
     elif not bot_stats.privileges.can_promote_members:
         return await message.reply("**I'm missing the admin rights `can_promote_members**")
     elif not user_stats.privileges.can_promote_members:
         return await message.reply("**Your missing the admin rights `can_promote_members**")
     elif user_stats.privileges.can_promote_members:
          msg = await message.reply_text("**Promoting Process.**")
          await bot.promote_chat_member(
            chat_id,
            new_admin.id,
            privileges=pyrogram.types.ChatPrivileges(
            can_delete_messages=True,
            can_pin_messages=True,
            can_invite_users=True,
            can_manage_video_chats=True,
            can_restrict_members=True
))
          await msg.edit(f"""**Promoted Admire**:\n**{admire.mention}**
          **New Admire:**\n**{new_admin.mention}** """,
              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Demote", callback_data="demote"),
                                                        InlineKeyboardButton(text="Delete", callback_data="close")]]))
                               
     
                     
@bot.on_callback_query(filters.regex("demote"))
async def demoting(_, query):
         chat_id = query.message.chat.id
         stats = await bot.get_chat_member(query.message.chat.id, query.from_user.id)
         if stats.privileges.can_promote_members:
                  await bot.promote_chat_member(
                     chat_id,
            new_admin.id,
            privileges=pyrogram.types.ChatPrivileges(
            can_delete_messages=False,
            can_pin_messages=False,
            can_invite_users=False,
            can_manage_video_chats=False,
            can_restrict_members=False
))
                  await query.message.edit(f"""**Demote by Admire:**\n** {query.from_user.mention}**
**Demoted Admire:**\n**{new_admin.mention}**""")    
         else:
               await query.answer("You can't Demote!", show_alert=True )
                    
        

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
async def banned(_, message):
         global reply_user
         if not message.reply_to_message:
                   return await message.reply("Reply to Someone to BAN")
         reply_user = message.reply_to_message.from_user
         from_user = message.from_user
         bot_stats = await bot.get_chat_member(message.chat.id, "self")
         from_user_stats = await bot.get_chat_member(message.chat.id, from_user.id)
         reply_user_stats = await bot.get_chat_member(message.chat.id, reply_user.id)
         if not bot_stats.privileges:
                  return await message.reply("Make Me Admin with (`can_restrict_members`) power!")
         elif not from_user_stats.privileges:
                 return await message.reply("Only Admins Can Use This Commands")
         elif not bot_stats.privileges.can_restrict_members:
                 return await message.reply("Give Me (`can_restrict_members`) Permission")
         elif not from_user_stats.privileges.can_restrict_members:
                  return await message.reply("Your missing the rights (`can_restrict_members`)")
         elif reply_user_stats.privileges:
                   return await message.reply("Sorry son I can't ban administrators")
         elif not reply_user_stats.privileges:
                     await bot.ban_chat_member(message.chat.id, reply_user.id)
                     await message.reply_text(f"Admin {from_user.mention} BANNED {reply_user.mention} from {message.chat.title}",
                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Unban", callback_data="unban"),
                                                        InlineKeyboardButton(text="Delete", callback_data="close")]]))
                     
@bot.on_callback_query(filters.regex("unban"))
async def unbaning(_, query):
         stats = await bot.get_chat_member(query.message.chat.id, query.from_user.id)
         if stats.privileges:
                  await bot.unban_chat_member(query.message.chat.id, reply_user.id)
                  await query.message.edit(f"""**Admire: {query.from_user.mention}**
**Unban: {reply_user.mention}**""")    
         else:
               await query.answer("You Not Admin!", show_alert=True )
                    
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
               await m.reply_text("**Successfully group new photo changed!**")

