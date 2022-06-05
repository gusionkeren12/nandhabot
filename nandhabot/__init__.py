from pyrogram import filters , Client
import os , time
from aiohttp import ClientSession
from Python_ARQ import ARQ
from telegraph import Telegraph

StartTime = time.time()

from nandhabot.config import *

#edit yourself nksama/config.py
OWNER_ID = OWNER_ID
LOG_GROUP_ID = LOG_GROUP_ID
BOT_USERNAME = BOT_USERNAME
SUPPORT_CHAT = SUPPORT_CHAT
UPDATES_CHANNEL = UPDATES_CHANNEL
ARQ_API_KEY = ARQ_API_KEY
ARQ_API_URL = ARQ_API_URL
BOT_ID = BOT_ID



#main vars set your deploying app
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

class Log:
    def __init__(self, save_to_file=False, file_name="wbb.log"):
        self.save_to_file = save_to_file
        self.file_name = file_name

    def info(self, msg):
        print(f"[+]: {msg}")
        if self.save_to_file:
            with open(self.file_name, "a") as f:
                f.write(f"[INFO]({time.ctime(time.time())}): {msg}\n")

    def error(self, msg):
        print(f"[-]: {msg}")
        if self.save_to_file:
            with open(self.file_name, "a") as f:
                f.write(f"[ERROR]({time.ctime(time.time())}): {msg}\n")

log = Log(True, "bot.log")

bot = Client("nandhabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(__name__)))

log.info("Starting bot client")
bot.start()

aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

og.info("telegraph downloading")
telegraph = Telegraph()
telegraph.create_account(short_name=BOT_USERNAME)


dev_user = [1491497760]


