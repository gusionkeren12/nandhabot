import wikipedia
from pyrogram import filters
from pyrogram.types import Message

from nandhabot import bot


@bot.on_message(filters.command(["wiki", "Wikipedia"]))
async def wikipediasearch(_, m: Message):
    query = m.text.split(None, 1)[1]
    if not query:
        await m.reply_text(
            "`Invalid Syntax See Help Menu To Know How To Use This Command`"
        )
        return
    results = wikipedia.search(query)
    result = ""
    for s in results:
        try:
            page = wikipedia.page(s)
            url = page.url
            result += f"> [{s}]({url}) \n"
        except BaseException:
            pass
    await m.reply_text(
        "`WikiPedia Search:` {} \n\n Result: \n\n{}".format(query, result)
    )
