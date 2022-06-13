from nandhabot import bot
import logging
import nandhabot.plugins
from nandhabot.config import SUPPORT_CHAT
from nandhabot.utils.dbfunctions import clean_restart_stage

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)

if __name__ == "__main__":
    bot.run()
    restart_data = await clean_restart_stage()
    try:
        print("Sending online status")
        if restart_data:
            await bot.edit_message_text(
                restart_data["chat_id"],
                restart_data["message_id"],
                "**Restarted Successfully**",
            )

        else:
            await bot.send_message(f"@{SUPPORT_CHAT}", "Bot started!")
    except Exception:
        pass
 
