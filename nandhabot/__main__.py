import logging

from nandhabot import arq, bot, SUPPORT_CHAT

# enable logging
FORMAT = "[VEGETA ROBOT] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)

if __name__ == "__main__":
    bot.run()
    restart_data = clean_restart_stage()
    x = arq.wall("vegeta")
    y = x.result
    try:
        print("Sending online status")
        if restart_data:
            bot.edit_message_media(
                restart_data["chat_id"],
                restart_data["message_id"],
                media=random.choice(y).url_image,
                caption="**Saiyan Prince Vegeta Successfully Restarted With New Powers**",
            )

        else:
            bot.send_photo(
                f"@VegetaSupport",
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
        bot.send_text("@VegetaSupport", f"**ERROR:** `{e}`")
        pass
