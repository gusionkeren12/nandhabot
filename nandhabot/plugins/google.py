from googlesearch import search
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from nandhabot import bot

@bot.on_message(filters.command("google"))
def resaults(client, message):
    if not len(message.command):
         return message.reply("**Gimme Query for Search!**")
    query = message.commamd[1]
    m = message.reply("**Searching....**")
    x =  list(search(query, tld="co.in", num=10, stop=10, pause=2))
    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="1",
                        url=x[0],
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="2",
                        url=x[1],
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="3",
                        url=x[2],
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="4",
                        url=x[3],
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="5",
                        url=x[4],
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="6",
                        url=x[5],
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="7",
                        url=x[6],
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="8",
                        url=x[7],
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="9",
                        url=x[8],
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="10",
                        url=x[9],
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="By NandhaBots",
                        url="t.me/nandhabots",
                    ),
                    InlineKeyboardButton(
                        text="TrunksRobot",
                        user_id=5515671520,
                    ),
                ],
            ]
        )
    message.reply(f"-» Resaults for {query} :", reply_markup=keyboard)
    m.delete()
