from pyrogram import filters, __version__ as pyro
import random 
import time
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nandhabot import bot, SUPPORT_CHAT, BOT_USERNAME
from pyrogram.types import CallbackQuery


alive = """
BOT - {}
DEV - @NandhaxD
PYRO - {}
"""

@bot.on_message(filters.command("alive"))
async def alive(_, m: Message):
    msg = await m.reply_text("Initialising")
    await msg.edit("Initialising ✪●●●●●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪●●●●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪✪●●●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪✪✪●●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪✪✪✪●")
    time.sleep(1)
    await msg.edit("Initialising ✪✪✪✪✪✪")
    time.sleep(1)
    await msg.edit("✪︎Connection Successful✪")
    await msg.edit(alive.format(BOT_USERNAME, pyro))

           
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
        InlineKeyboardButton('ANIME', callback_data='anime_help'),
        InlineKeyboardButton('ADMIN', callback_data='admin_help'),
        InlineKeyboardButton('NEKOS', callback_data='nekos_help'),
        ],[
        InlineKeyboardButton('NSFW', callback_data='nsfw_help'),
        InlineKeyboardButton('INFO', callback_data='userinfo_help')]]

         
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
NEKOS_TEXT = """
anime themed sfw:
**image:**
neko, waifu

**animation:**
cry, kill, smile, 
highfive, slap, kick, 
hug, pat, punch,
sleep, wink, think, 
feed, tickle, shoot, 
thumbsup, smug, laugh, 
bore, baka, dance,
blush, facepalm, stare, 
pout, handhold, wave, 
cuddle, poke, shrug
"""

@bot.on_callback_query(filters.regex("nekos_help"))
async def sfwhelp(_, query: CallbackQuery):
     await query.message.edit_caption(NEKOS_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

NSFW_TEXT = """
this type of plugins fully Hentai 🔞
so don't use public groups
using: Waifu.pics

• /hneko - hentai nekos img.
• /hwaifu - hentai waifu img.
• /blowjob - hentai blowjob gif.
• /trap - hentai trap img.
"""

@bot.on_callback_query(filters.regex("nsfw_help"))
async def nsfwhelp(_, query: CallbackQuery):
     await query.message.edit_caption(NSFW_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

