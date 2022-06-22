import io
import sys
import io
import os
import textwrap
from contextlib import redirect_stdout
from telethon.sync import events
import time
import pyrogram
StartTime = time.time()
import traceback
from subprocess import getoutput as run
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from requests import post

from nandhabot import dev_user
from nandhabot.config import OWNER_ID
from nandhabot import bot as app
from nandhabot import bot, tbot


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
                  

@bot.on_message(filters.command('devlist'))
def devlist(_, m):
      if m.from_user.id in dev_user:
         m.reply(str(dev_user))
      else:
          m.reply("only Devs can access this command!")
  
        
@app.on_message(filters.user(OWNER_ID) & filters.command("sh", prefixes=['/', '.', '?', '-']))
def sh(_, m):
    if m.from_user.id in dev_user:
        code = m.text.replace(m.text.split(" ")[0], "")
        x = run(code)
        m.reply(
            f"**SHELL**: `{code}`\n\n**OUTPUT**:\n`{x}`")
    else:
        m.reply("only Devs can access this command!")



def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


@bot.on_message(
    filters.command("logs", prefixes=[".", "/", ";", "," "*"]) & filters.user(dev_user)
)
def sendlogs(_, m: Message):
    logs = run("tail logs.txt")
    x = paste(logs)
    keyb = [
        [
            InlineKeyboardButton("Link", url=x),
            InlineKeyboardButton("File", callback_data="sendfile"),
        ],
    ]
    m.reply(x, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(keyb))



@bot.on_callback_query(filters.regex(r"sendfile"))
def sendfilecallback(_, query: CallbackQuery):
    sender = query.from_user.id
    query.message.chat.id

    if sender in dev_user:
        query.message.edit("`Sending...`")
        query.message.reply_document("logs.txt")

    else:
        query.answer(
            "This Is A Developer's Restricted Command.You Don't Have Access To Use This."
        )
      
@app.on_message(filters.user(dev_user) & filters.command("eval"))
async def eval(client, message):
    status_message = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "<b>EVAL</b>: "
    final_output += f"<code>{cmd}</code>\n\n"
    final_output += "<b>OUTPUT</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code> \n"

    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file, caption=cmd, disable_notification=True
            )
    else:
        await reply_to_.reply_text(final_output)
    await status_message.delete()


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)



@app.on_message(filters.command("leave") & filters.user(dev_user))
async def leave(client, message):
    if len(message.command) == 1:
        try:
            await client.leave_chat(message.chat.id)
        except RPCError as e:
            print(e)
    else:
        cmd = message.text.split(maxsplit=1)[1]
        try:
            await client.leave_chat(int(cmd))
        except RPCError as e:
            print(e)

@app.on_message(filters.command("invitelink"))
async def invitelink(client, message):
    chat_id = message.chat.id
    try:
        grouplink = await client.export_chat_invite_link(chat_id)
        await message.reply_text(f"{grouplink}")
        
    except Exception as e:
        pass

@app.on_message(filters.user(dev_user) & filters.command("ping", prefixes=['/', '.', '?', '-']))
async def ping(_, m):
    start_time = time.time()
    img = "https://telegra.ph/file/fb6a277156b2956f26aa1.jpg"
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = get_readable_time((time.time() - StartTime))
    ping_message = await m.reply_text("Processing ...")
    await m.reply_photo(photo=img, caption=f"**🏓 PONG!!:** `{ping_time} ms`\n**🆙 UPTIME:** `{uptime}`")
    await ping_message.delete()
    
#telethon eval

@tbot.on(events.NewMessage(from_users=[1491497760], pattern="^/teval ?(.*)"))
async def teval(event):
    if event.fwd_from:
        return
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not cmd:
        return
    catevent = await tbot.send_message(event.chat.id, "`Running ...`", reply_to=event)
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = f"**•  Eval : **\n`{cmd}` \n\n**•  Result : **\n`{evaluation}` \n"
    MAX_MESSAGE_SIZE_LIMIT = 4095
    if len(final_output) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await tbot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
            )
    else:
        await catevent.edit(final_output)


async def aexec(code, smessatatus):
    message = event = smessatatus

    def p(_x):
        return print(slitu.yaml_format(_x))

    reply = await event.get_reply_message()
    exec(
        "async def __aexec(message, reply, client, p): "
        + "\n event = smessatatus = message"
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](message, reply, tbot, p)
