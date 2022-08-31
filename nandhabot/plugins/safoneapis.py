from pyrogram import filters
from nandhabot import bot
from SafoneAPI import SafoneAPI
api = SafoneAPI()



@bot.on_message(filters.command("app"))
async def apps(_, message):
           if len(message.command) <2:
                return await message.reply("**Give A App Name**\n**- /app telegram**")
           text = message.text.split(None, 1)[1]
           apps = await api.apps(text)
           app_text = ""
           for app in apps.results:
                   app_text += f"Results of {text}\n\n~ [{app.title}]({app.link})\n"
           await message.reply_text(app_text,disable_web_page_preview=True)
