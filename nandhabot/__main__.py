import logging
import asyncio
from nandhabot import arq, bot, SUPPORT_CHAT
from uvloop import install
from pyrogram import idle
from contextlib import closing, suppress

# enable logging
FORMAT = "[VEGETA ROBOT] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
loop = asyncio.get_event_loop()

async def start_bot():
    restart_data = await clean_restart_stage()
    x = arq.wall("vegeta")
    y = x.result
    try:
        print("Sending online status")
        if restart_data:
            await bot.edit_message_media(
                restart_data["chat_id"],
                restart_data["message_id"],
                media=random.choice(y).url_image,
                caption="**Saiyan Prince Vegeta Successfully Restarted With New Powers**",
            )

        else:
            await bot.send_photo(
                "@VegetaSupport",
                photo=random.choice(y).url_image,
                caption="**Saiyan Prince Vegeta Was Successfully Deployed!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="[► Summon Me ◄]",
                                url=f"https://t.me/VegetaRobot?startgroup=true",
                            )
                        ]
                    ]
                ),
            )
    except Exception as e:
        await bot.send_message("@VegetaSupport", text=f"**ERROR:** `{e}`")
        pass
    await idle()

if __name__ == "__main__":
    install()
    with closing(loop):
        with suppress(asyncio.exceptions.CancelledError):
            loop.run_until_complete(start_bot())
        loop.run_until_complete(asyncio.sleep(3.0))  # task cancel wait
