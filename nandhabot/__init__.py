import os
import time
import sys
import glob
import importlib
import logging
from pathlib import Path

from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client, filters
from Python_ARQ import ARQ
from telegraph import Telegraph

StartTime = time.time()

from nandhabot.config import *

# edit yourself nksama/config.py
OWNER_ID = OWNER_ID
LOG_GROUP_ID = LOG_GROUP_ID
BOT_USERNAME = BOT_USERNAME
SUPPORT_CHAT = SUPPORT_CHAT
UPDATES_CHANNEL = UPDATES_CHANNEL
ARQ_API_KEY = ARQ_API_KEY
ARQ_API_URL = ARQ_API_URL
BOT_ID = BOT_ID
MONGO_URL = MONGO_URL


# main vars set your deploying app
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

bot = Client(
    "nandhabot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

bot.run()

aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
telegraph = Telegraph()
telegraph.create_account(short_name=BOT_USERNAME)
print("Initializing MongoDB client")
mongo_client = MongoClient(MONGO_URL)
db = mongo_client.aasf

def load_plugins(plugin_name):
    path = Path(f"nandhabot/plugins/{plugin_name}.py")
    name = "nandhabot.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["nandhabot.plugins." + plugin_name] = load
    print("Imported --> " + plugin_name)

path = "nandhabot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        thepath = Path(a.name)
        plugin_name = thepath.stem
        load_plugins(plugin_name.replace(".py", ""))



dev_user = [1491497760]
