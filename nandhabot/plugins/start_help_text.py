from pyrogram import filters, __version__ as pyrogram_version
import random 
from telethon import __version__ as telethon_version

import time
StartTime = time.time()
from pyrogram import enums 
from pyrogram.enums import ChatType
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nandhabot import bot, SUPPORT_CHAT, BOT_USERNAME
from nandhabot.plugins.dev_user import get_readable_time
from pyrogram.types import CallbackQuery


@bot.on_message(filters.command("alive"))
async def alive(_, m: Message):
    user = m.from_user
    uptime = get_readable_time((time.time() - StartTime))
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
    pm_caption = f"** ♡ Hey [{user.first_name}](tg://user?id={user.id}) \nI,m Vegeta ✨ **\n\n"
    pm_caption += f"**♡ My Uptime :** `{uptime}`\n\n"
    pm_caption += f"**♡ Telethon Version :** `{telethon_version}`\n\n"
    pm_caption += f"**♡ Pyrogram Version :** `{pyrogram_version}`\n\n"
    pm_caption += "**♡ My Master :** [Nandha](https://t.me/nandhaxd) "
    await msg.edit_text(text=(pm_caption),disable_web_page_preview=True)

           
BOT_IMG = [ "https://telegra.ph/file/b3fbf990e0b67ede241a3.jpg",
           "https://telegra.ph/file/94865dae2576a2fa52732.jpg" ]
pm_text = """
Hello! Dear {}

I'm An Anime themed Smart VegetaRobot make your group's
joyful Using /help commands!!

powered by @NandhaBots
"""

buttons = [
        [
            InlineKeyboardButton(
                "ADD ME", url="t.me/VegetaRobot?startgroup=true"),
            InlineKeyboardButton(
                "HELP", callback_data='help_back'),]]

users = []

@bot.on_message(filters.command(["start"], ["/", ".", "?"]))
async def start(_, message):
        uid = message.from_user.id
        mention = message.from_user.mention
        if message.chat.type == ChatType.PRIVATE and not uid in users:
                await users.append(uid)
                await bot.send_message(-1001717881477, f"**Someone Started Our Bot ^o^**\n**Name: {mention}**\n**uid: {uid}**\n**total users {len(stats)}**")
                await message.reply_photo(
            random.choice(BOT_IMG),
            caption=pm_text.format(message.from_user.mention),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        else: 
              await message.reply_photo(
            random.choice(BOT_IMG),
            caption=pm_text.format(message.from_user.mention),
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
        InlineKeyboardButton('MISC', callback_data='misc_help'),
        InlineKeyboardButton('INFO', callback_data='userinfo_help'),
        ],[
        InlineKeyboardButton('MEME', callback_data='meme_help'),
        InlineKeyboardButton('FUN', callback_data='fun_help'),
        InlineKeyboardButton('SG', callback_data='sticker_help'),
        ],[
        InlineKeyboardButton('DEV', callback_data='dev_help'),
        InlineKeyboardButton('TOOLS', callback_data='tools_help')]]

         
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
• /lewd - get anime lewd img.
• /ero - get anime ero img. 
• /pussy - get smile pussy img.
"""

@bot.on_callback_query(filters.regex("nsfw_help"))
async def nsfwhelp(_, query: CallbackQuery):
     await query.message.edit_caption(NSFW_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

MISC_TEXT = """
**random misc tools:**

/font {text}: for style fonts.
/tm: reply to media for upload telegraph.
/txt {pagename}: reply to text for upload telegraph.
/pastet: reply to msg paste.
/rename: rename files.
/encrypt: reply to msg encrypt.
/decrypt: reply to msg decrypt.
/spell: reply to msg convert correct spelling.
/wall {text}: get awesome wallpaper.
/tr {code}: reply to msg translate.
/lang: translate language codes.
/reddit {text}: search on reddit.
/ud {text}: ward definition.
/share: reply to msg get share link.
"""

@bot.on_callback_query(filters.regex("misc_help"))
async def mischelp(_, query: CallbackQuery):
     await query.message.edit_caption(MISC_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
MEME_TEXT = """
**Memes & jokes:**
/ameme: read a random anime memes.
/meme: read a random memes.
/hmeme: read a hentai based memes.
/joke: read some random jokes.
"""

@bot.on_callback_query(filters.regex("meme_help"))
async def memehelp(_, query: CallbackQuery):
     await query.message.edit_caption(MEME_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

STICKER_TEXT = """
/getsticker: reply to sticker for get photo document type. 
/stickers {text}: for search stickers.
/stickerid: reply to sticker to get I'd.
/gifid: reply to gif for get gif I'd 
"""
@bot.on_callback_query(filters.regex("sticker_help"))
async def stickerhelp(_, query: CallbackQuery):
     await query.message.edit_caption(STICKER_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
FUN_TEXT = """
**Fun commands:**
/react: reply to msg react.
/gban: fake gban for fun.
`good morning`: regex cmd tell good morning.
`good night`: regex cmd tell good night.
/dare: reply to user give dare.
/truth: reply to user give truth. 
/write {text}: note written photo type.
/hack: reply to user hack.
/love: animation love story. 
"""

@bot.on_callback_query(filters.regex("fun_help"))
async def funhelp(_, query: CallbackQuery):
     await query.message.edit_caption(FUN_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

DEV_TEXT = """
/logs: get bot logs.
/eval: run codes.
/ping: bot server start time & end time.
/sh: run codes.
/leave: bot left the chat. 
/pyupload: get plugins document type.
/devlist: list of developer.
"""
@bot.on_callback_query(filters.regex("dev_help"))
async def devhelp(_, query: CallbackQuery):
     await query.message.edit_caption(DEV_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

TOOLS_TEXT = """
/feedback {text}: give feedback about bot.
/img {text}: download img to google.
/logo {text}: random logo generate.
/logohq {text}: hight quality logo generate. 
/reverse: reply to image for search on google.  
/wiki {text}: Wikipedia search.
/song {text: download songs with high quality.
/countryinfo {text}: generate country information.
/github {text}: github user profile information.
"""
@bot.on_callback_query(filters.regex("tools_help"))
async def toolshelp(_, query: CallbackQuery):
     await query.message.edit_caption(TOOLS_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
