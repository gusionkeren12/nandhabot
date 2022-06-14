

from nandhabot import bot
from pyrogram import filters
from requests import get


@bot.on_message(filters.command("logo"))
async def logo(_, m):
             if len(m.command) < 2:
                return await m.reply("<b>Usage:</b>\n<code>/logo nandha</code>")
             text = m.text.split(None, 1)[1]
             msg = await m.reply_text("<b>Creating your logo</b>")
             logo = get((f"https://single-developers.up.railway.app/logo?name={text}").replace(' ','%20')).history[1].url
             await m.reply_photo(logo,caption="Made by @VegetaRobot")
             await msg.delete()
