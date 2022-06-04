from nandhabot import bot
import logging
import nandhabot.plugins
from nandhabot.config import SUPPORT_CHAT

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
        
