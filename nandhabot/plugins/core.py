from nandhabot import tbot
from nandhabot.events import register
from nandhabot.config import OWNER_ID
import os
import asyncio
import os
import time

from datetime import datetime
from nandhabot import dev_users as DEV_USERS
from nandhabot import TEMP_DOWNLOAD_DIRECTORY as path
from datetime import datetime
water = './nandhabot/images/IMG_20220522_180127_083.jpg'
client = tbot

@register(pattern=r"^/pyupload ?(.*)")
async def Prof(event):
    if event.sender_id == OWNER_ID or event.sender_id == DEV_USERS:
        pass
    else:
        return
    thumb = water
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./VegetaRobot/modules/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
     message_id = event.message.id
     await event.client.send_file(
             event.chat_id,
             the_plugin_file,
             force_document=True,
             allow_cache=False,
             thumb=thumb,
             reply_to=message_id,
         )
    else:
        await event.reply("**No File Found!**")
