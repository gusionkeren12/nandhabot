from pyrogram import filters , Client
import time, os
from aiohttp import ClientSession
from Python_ARQ import ARQ
from telegraph import Telegraph
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from telethon import TelegramClient
import telegram.ext as tg
import logging

StartTime = time.time()

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

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
MONGO_URL = MONGO_URL
SESSION = "BQA1Ma5Yvta7ZVvARymDBKLgoVo3ut0kS9kfN_fmjmIXxkyKyovmEQ65BnuUFLa4dQ9ADXtg6FHUq3p0AZji8NEgjTYYUfEbaIZt7t88vbyQoNb9hOdpR20x9te0dZo-C8sYq0kDg7_YdlltQLO-BvWJVeUKa0C6Eg30cH6NrW2cdofoJDdEo9q-8tHiIFQp-OUN92E0rge2QBJLqOEGUm9yc0P-iX9MSEUptM2yUwPprzO_ScAEhaFBdysM0bJdh3tManqaSLmXpZn0556nsty4b48TBYn0X_9Z0TRPDwpr1HMkeL8yOPP6gFlyy5UgrC8aUgzQqf8LPrx02pPWlIIDAAAAAUsjUmgA"
TEMP_DOWNLOAD_DIRECTORY = "./" 


#main vars set your deploying app
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
WEBHOOK = bool(os.environ.get('WEBHOOK', False))
PORT = int(os.environ.get('PORT', 5000))
WORKERS = int(os.environ.get('WORKERS', 8))

UB_API_ID = 8658423
UB_API_HASH = "90468210ba43f2c83d01866167602745"

bot = Client("nandhabot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="{}/plugins".format(__name__)))
tbot = TelegramClient("Vegeta", API_ID, API_HASH)
updater = tg.Updater(BOT_TOKEN, workers=WORKERS, use_context=True)
dispatcher = updater.dispatcher
ubot = Client(session_string=SESSION, api_id=UB_API_ID, api_hash=UB_API_HASH, name="nandhabot")

aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
telegraph = Telegraph()
telegraph.create_account(short_name=BOT_USERNAME)
print("Initializing MongoDB client")
mongo_client = MongoClient(MONGO_URL)
db = mongo_client.nandha

dev_user = [1491497760]
