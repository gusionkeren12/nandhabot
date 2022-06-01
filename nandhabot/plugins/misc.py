import os
import requests
from pyrogram import filters
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types import Message
from gpytranslate import Translator
from nandhabot import bot, SUPPORT_CHAT
from urllib.parse import quote



@bot.on_message(filters.command(["lang", "langs"]))
def language(_, m: Message):
       #langs codes
        m.reply_text("Click on the button below to see the list of supported language codes.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Language codes",
                        url="https://telegra.ph/Lang-Codes-03-19-3",
                    ),
                ],
            ],
        ),
    )


trans = Translator()


@bot.on_message(filters.command(["tl", "tr"]))
async def translate(_, message: Message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("Reply to a message to translate it!\n Use: /langs for translation codes")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"**Translated from {source} to {dest}**:\n"
        f"`{translation.text}`"
    )

    await message.reply_text(reply)




@bot.on_message(filters.command('json'))
async def jsonify(_, message):
    the_real_message = None
    reply_to_id = None

    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message

    try:
        await message.reply_text(f"<code>{the_real_message}</code>")
    except Exception as e:
        with open("json.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        await message.reply_document(
            document="json.text",
            caption=str(e),
            disable_notification=True,
            reply_to_message_id=reply_to_id,
        )
        os.remove("json.text")
       
       
@bot.on_message(filters.command("ud"))
async def ud(_, message: Message):
       if len(message.command) < 2:
        return await message.reply_text("» Give some text")
        text = message.text.split(None, 1)[1]
        results = requests.get(
        f'https://api.urbandictionary.com/v0/define?term={text}').json()
        reply_text = f'**results: {text}**\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
        ud = await message.reply_text("finding.. define.")
        await ud.edit_text(reply_text)

  
def share_link(text: str) -> str:
    return "**Here is Your Sharing Text:**\nhttps://t.me/share/url?url=" + quote(text)

@bot.on_message(filters.command("share"))
async def share_text(_, message: Message):
    reply = message.reply_to_message
    reply_id = message.reply_to_message.id if message.reply_to_message else message.id
    input_split = message.text.split(None, 1)
    if len(input_split) == 2:
        input_text = input_split[1]
    elif reply and (reply.text or reply.caption):
        input_text = reply.text or reply.caption
    else:
        await message.reply_text(
            text=f"**Notice:**\n\n1. Reply Any Messages.\n2. No Media Support\n\n**Any Question Join Support Chat**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Support Chat", url=f"https://t.me/vegetasupport")
                    ]                
                ]
            ),
        )
        return
    await message.reply_text(share_link(input_text))
