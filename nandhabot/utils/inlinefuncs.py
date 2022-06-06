from nandhabot import bot as app,arq

from pykeyboard import InlineKeyboard

from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineQueryResultArticle, InlineQueryResultPhoto,
                            InputTextMessageContent)

keywords_list = [
    "image",
    "wall",
    "tmdb",
    "lyrics",
    "exec",
    "speedtest",
    "search",
    "ping",
    "tr",
    "ud",
    "yt",
    "info",
    "google",
    "torrent",
    "wiki",
    "music",
    "ytmusic",
]


async def inline_help_func(__HELP__):
    buttons = InlineKeyboard(row_width=4)
    buttons.add(
        *[
            (InlineKeyboardButton(text=i, switch_inline_query_current_chat=i))
            for i in keywords_list
        ]
    )
    answerss = [
        InlineQueryResultArticle(
            title="Inline Commands",
            description="Help Related To Inline Usage.",
            input_message_content=InputTextMessageContent(
                "Click A Button To Get Started."
            ),
            thumb_url="https://hamker.me/cy00x5x.png",
            reply_markup=buttons,
        ),
        InlineQueryResultArticle(
            title="Github Repo",
            description="Get Github Respository Of Bot.",
            input_message_content=InputTextMessageContent(
                "https://github.com/thehamkercat/WilliamButcherBot"
            ),
            thumb_url="https://hamker.me/gjc9fo3.png",
        ),
    ]
    answerss = await alive_function(answerss)
    return answerss
