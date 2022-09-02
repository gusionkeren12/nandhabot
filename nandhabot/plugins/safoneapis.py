from pyrogram import filters
from nandhabot import bot
from SafoneAPI import SafoneAPI
api = SafoneAPI()


@bot.on_message(filters command("webshot"))
async def webshot(_, m):
         if len(message.command) <2:
                return await m.reply("**Give A App Name**\n**- /app telegram**")
         text = m.text.split(None, 1)[1]
         make_shot = await api.webshot(text)
         await m.reply_document(make_shot)

@bot.on_message(filters.command("app"))
async def apps(_, message):
           if len(message.command) <2:
                return await message.reply("**Give A App Name**\n**- /app telegram**")
           text = message.text.split(None, 1)[1]
           apps = await api.apps(text)
           app_text = f"Results of {text}:\n\n"
           for app in apps.results:
                   app_text += f"~ [{app.title}]({app.link})\n"
           await message.reply_text(app_text)
