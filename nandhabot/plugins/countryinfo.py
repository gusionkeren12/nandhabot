


from countryinfo import CountryInfo
from nandhabot import bot
from pyrogram import filters

@bot.on_message(filters.command(["ci", "countryinfo"]))
async def countryinfo(_, m):
                  search = m.text.split(None, 1)[1]
                  country = CountryInfo(search)
                  a = country.info()
                  name = a.get("name")
                  capital = a.get("capital")
                  languages = a.get("languages")
                  lMAO = ""
                  for lmao in languages:
                      lMAO += lmao + ",  "


caption = """
**Country**: `{}`
**Capital**: `{}`
