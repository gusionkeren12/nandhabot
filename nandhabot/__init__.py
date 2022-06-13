import os
import time

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
    bot_token=BOT_TOKEN,
    plugins=dict(root="{}/plugins".format(__name__)),
)

aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
telegraph = Telegraph()
telegraph.create_account(short_name=BOT_USERNAME)
print("Initializing MongoDB client")
mongo_client = MongoClient(MONGO_URL)
db = mongo_client.aasf

dev_user = [1491497760]
