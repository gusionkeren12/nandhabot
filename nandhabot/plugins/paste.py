from requests import post, get
import requests 
import socket
from asyncio import get_running_loop
from functools import partial
from nandhabot import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


def spacebin(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


def _netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096).decode("utf-8").strip("\n\x00")
        if not data:
            break
        return data
    s.close()
    
async def ezup(content):
    loop = get_running_loop()
    link = await loop.run_in_executor(
        None, partial(_netcat, "ezup.dev", 9999, content)
    )
    return link

@bot.on_message(filters.command('paste'))
def paste(_, m):
    reply = m.reply_to_message
    if not reply:
           text = m.text.split(None, 1)[1]
           spacebin_url = spacebin(text)
           link = ezup(text)
           m.reply_text(f"{link} +\n{spacebin_url}",disable_web_page_preview=True)
           return 
    text = reply.text or reply.caption
    if reply:
        spacebin_url = spacebin(text)
        link = await ezup(text)
        caption = f"[SPACEBIN]({spacebin_url}) | [ezup.dev]({link})"
        m.reply(text=caption,
                      reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton("SPACEBIN", url=spacebin_url),
                           ],[ InlineKeyboardButton("EZUP.DEV", url=link)]]),disable_web_page_preview=True)




