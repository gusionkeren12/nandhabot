from pyrogram import filters
from pyrogram.types import *
from nandhabot import bot as Bot


CALCULATE_TEXT = "Made by @VegetaRobot"

CALCULATE_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("DEL", callback_data="DEL"),
            InlineKeyboardButton("AC", callback_data="AC"),
            InlineKeyboardButton("(", callback_data="("),
            InlineKeyboardButton(")", callback_data=")")
        ],
        [
            InlineKeyboardButton("7", callback_data="7"),
            InlineKeyboardButton("8", callback_data="8"),
            InlineKeyboardButton("9", callback_data="9"),
            InlineKeyboardButton("÷", callback_data="/")
        ],
        [
            InlineKeyboardButton("4", callback_data="4"),
            InlineKeyboardButton("5", callback_data="5"),
            InlineKeyboardButton("6", callback_data="6"),
            InlineKeyboardButton("×", callback_data="*")
        ],
        [
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
            InlineKeyboardButton("3", callback_data="3"),
            InlineKeyboardButton("-", callback_data="-"),
        ],
        [
            InlineKeyboardButton(".", callback_data="."),
            InlineKeyboardButton("0", callback_data="0"),
            InlineKeyboardButton("=", callback_data="="),
            InlineKeyboardButton("+", callback_data="+"),
        ]
    ]
)


@Bot.on_message(filters.command(["calc", "calculate", "calculator"]))
async def calculate(_, message):
    await message.reply_text(
        text=CALCULATE_TEXT,
        reply_markup=CALCULATE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.text)
async def evaluate(_, message):
    try:
        data = message.text.replace("×", "*").replace("÷", "/")
        result = str(eval(data))
    except:
        return
    await message.reply_text(
        text=result,
        reply_markup=CALCULATE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_callback_query()
async def cb_data(_, message):
        data = message.data
        try:
            message_text = message.message.text.split("\n")[0].strip().split("=")[0].strip()
            text = '' if CALCULATE_TEXT in message_text else message_text
            if data == "=":
                text = str(eval(text))
            elif data == "DEL":
                text = message_text[:-1]
            elif data == "AC":
                text = ""
            else:
                text = message_text + data
            await message.message.edit_text(
                text=f"{text}",
                disable_web_page_preview=True,
                reply_markup=CALCULATE_BUTTONS
            )
        except Exception as error:
            print(error)
