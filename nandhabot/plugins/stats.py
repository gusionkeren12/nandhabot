#### Powerd by @NandhaBots ####
#### Copyright under - 2022 & 2023 ####
#### by NandhaxD.t.me ####

from nandhabot import bot, mongodb
from pyrogram import filters
from pyrogram.types import *
from pyrogram.enums import ChatType



usersdb = mongodb.users

async def is_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True

async def get_users() -> list:
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list
    
async def add_user(user_id: int):
    is_served = await is_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})   


NEW_USER_TEXT = """**Someone Started Our Bot ヘ(^_^)ヘ**

**🕵 Name: {}**
**🆔 UID: {}**

**🌟 Total UserStats: {}**
"""
START_TEXT = """ **Hey? {}
Do you know I can do anything for you? (๑•́ ₃ •̀๑) check my available commands for /help.**
"""


## Written by @NandhaxD ##

START_BTN = [[ InlineKeyboardButton(text="🆘", callback_data="help_back"),
InlineKeyboardButton(text="📊", url="t.me/Nandha_Network"),],[ InlineKeyboardButton(text="SUPPORT", url="NandhaSupport.t.me"),InlineKeyboardButton(text="UPDATES", url="Nandhabots.t.me")]]


@bot.on_message(filters.command("start",["/","!",".","?","$"]))
async def start(_, message):
     user_id = message.from_user.id
     mention = message.from_user.mention
     if message.chat.type == ChatType.PRIVATE and not await is_user(user_id):
            await add_user(user_id)
            mention = message.from_user.mention
            id = message.from_user.id
            user_stats = len(await get_users())
            await bot.send_message(-1001717881477, text=NEW_USER_TEXT.format(mention, id, user_stats))
            await message.reply_text(START_TEXT.format(mention),reply_markup=InlineKeyboardMarkup(START_BTN))
            return 
         
     elif message.chat.type == ChatType.PRIVATE and await is_user(user_id):

               return await message.reply_text(START_TEXT.format(mention),reply_markup=InlineKeyboardMarkup(START_BTN))
     elif message.chat.type == ChatType.SUPERGROUP or ChatType.GROUP:
            return await message.reply_text("**I'm Already Awake! Nani yo?\n             ¯\_(ツ)_/¯**")

#### by @NandhaBots ###
