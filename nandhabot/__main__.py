from nandhabot import bot
from pyrogram import filters, __version__ as pyro
from pyrogram.types import Message 
import logging
import nandhabot.plugins
from nandhabot.config import SUPPORT_CHAT, BOT_USERNAME
from nandhabot import dev_user

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)

if __name__ == "__main__":
    bot.run()
    with bot:
        bot.send_message(f"@{SUPPORT_CHAT}" , "Hello there I'm Now online")
        
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
