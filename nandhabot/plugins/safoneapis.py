from pyrogram import filters
from nandhabot import bot
from SafoneAPI import SafoneAPI
api = SafoneAPI()

@bot.on_message(filters.command("carbon"))
async def carbon(_, message):
        if message.reply_to_message:
           return await message.reply("**Process Your Request.**")
        code = {
  "code": f"{message.reply_to_message.text}",
  "backgroundColor": "green"
}
        carbon = await api.carbon(code)
        await message.reply("**Complete Process.**")
        await message.reply_photo(carbon)


@bot.on_message(filters.command("webshot"))
async def webshot(_, m):
         if len(m.command) <2:
                return await m.reply("**Give A URL to Shot **\n**- /webshot github.com**")
         text = m.text.split(None, 1)[1]
         msg = await m.reply("**Your Request is Processing**")
         make_shot = await api.webshot(text)
         await msg.edit("**Complete Process.**")
         await m.reply_document(make_shot,caption=f"**Request by {m.from_user.mention}**")

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
