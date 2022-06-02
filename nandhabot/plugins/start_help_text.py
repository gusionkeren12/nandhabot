from pyrogram import filters
import random 
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nandhabot import bot, SUPPORT_CHAT
from pyrogram.types import CallbackQuery


           
BOT_IMG = [ "https://telegra.ph/file/b3fbf990e0b67ede241a3.jpg",
           "https://telegra.ph/file/94865dae2576a2fa52732.jpg" ]
text = """
Hello! Dear {}

I'm An Anime themed Smart VegetaRobot make your group's
joyful Using /help commands!!

powered by @PegaBots
"""


@bot.on_message(filters.command(["start"], ["/", ".", "?"]))
async def start(_, m: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "ADD ME", url="t.me/VegetaRobot?startgroup=true"),
            InlineKeyboardButton(
                "HELP", callback_data='help_back'),]]

    await m.reply_photo(
        random.choice(BOT_IMG),
        caption=text.format(m.from_user.mention),
        reply_markup=InlineKeyboardMarkup(buttons),
    )

          
HELP_TEXT = """
**Hello Dear**!
**I'm prince Vegeta I will manage your groups and make your group joyful bellow check my
help and commands!**
"""

HELP_BUTTON = [[
        InlineKeyboardButton('Anime', callback_data='anime_help'),
        InlineKeyboardButton('Admin', callback_data='admin_help'),
        InlineKeyboardButton('SFW', callback_data='sfw_help'),
        ][
        InlineKeyboardButton('NSFW', callback_data='nsfw_help'),
        InlineKeyboardButton('Userinfo', callback_data='userinfo_help')]]

         
@bot.on_message(filters.command(["help"], ["/", ".", "?"]))
async def start(_, m: Message):
   await m.reply_photo(random.choice(BOT_IMG),caption=HELP_TEXT.format(m.from_user.mention),
                      reply_markup=InlineKeyboardMarkup(HELP_BUTTON),)
           
  
@bot.on_callback_query(filters.regex("help_back"))
async def help(_, query: CallbackQuery):
    await query.message.edit_caption(HELP_TEXT,
                                    reply_markup=InlineKeyboardMarkup(HELP_BUTTON),)
               
@bot.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
           query = query.message
           await query.delete()
         
 
ANIME_TEXT = """
anime themed fun & search:

• `/anime {name}` - Search animes in myanimelist.net.

• `/character {name}` - Search Character in myanimelist.net.

• `/upcoming` - details in upcoming animes in myanimelist.net.

• `/quotes` - random anime quotes.
"""

BUTTON = [[InlineKeyboardButton("back 🔙", callback_data="help_back"),
            InlineKeyboardButton("close 🗑", callback_data='close'),]]


@bot.on_callback_query(filters.regex("anime_help"))
async def animehelp(_, query: CallbackQuery):
     await query.message.edit_caption(ANIME_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
USERINFO_TEXT = """
user info chat info:
• /id - userid & chatid.
• /info - userinformation.
• /ginfo - chat information.
• /json - full intention about user & chat.
"""

@bot.on_callback_query(filters.regex("userinfo_help"))
async def userinfohelp(_, query: CallbackQuery):
     await query.message.edit_caption(USERINFO_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

ADMIN_TEXT = """
usage of admin cmds:
• /ban- ban a user.
• /unban - unban a user. 
• /del - delete a message.
• /purge - delete msg multi.
• /pin - pin a message.
• /unpin - unpin a message.
• /unpinall - unpin all msg.
• /setgtitle - set group title.
• /setgpic - set group pic.
• /rgpic - remove group pic.
"""

@bot.on_callback_query(filters.regex("admin_help"))
async def adminhelp(_, query: CallbackQuery):
     await query.message.edit_caption(ADMIN_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
SFW_TEXT = """
anime themed sfw:
**using: waifu.pics**
• /slap - slap a user😠.
• /hug - hug a user🤗.
• /kill - kill a user😈.
• /smile - just smile😊.
• /waifu - waifu images.
• /highfive - high a user🖐.
• /cry - reply to user cry😭.
• /kick - reply to user kick😏.
• /pat - reply to user pat😇.
**using: nekos.py**
/feed - feed react gif.
/neko - nokes img.
/wallpaper - anime wall. 
/ngif - night gif.
/tickle - tickle anime react.
/gasm - gasm anime react. 
/kiss - kiss a user😘.
/poke - poke gif react.
/cuddle - cuddle anime react. 
/smug - smug reacts.
/foxgirl - foxgirl img.
/8ball - 8ball question & answer.
"""

@bot.on_callback_query(filters.regex("sfw_help"))
async def adminhelp(_, query: CallbackQuery):
     await query.message.edit_caption(SFW_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
