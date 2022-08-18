import os
import asyncio

from pyrogram import filters
from pyrogram.types import Message
from pymongo import MongoClient
from nandhabot import bot
from nandhabot import MONGO_URL as db_url, db



def store_user(chat, user):
    if not db.find_one({'chat' : chat, 'user': user}):
       db.insert_one({'chat': chat,  'user': user})

@bot.on_message(filters.incoming)
async def userdb(_, message):
      store_user(message.chat.id, message.from_user.id)
        
@bot.on_message(filters.command("stats"))
async def stats(_, message):
         await message.reply_text(f"total users\ntotal groups")
