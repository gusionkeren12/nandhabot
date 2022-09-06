import asyncio
import requests
import wget
import yt_dlp


from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from pyrogram import filters
from pyrogram.types import *

from nandhabot import bot


@bot.on_message(filters.command("ytvideo"))
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("**Video Process.**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **خطا:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("**Process Complete.\n Now Uploading.**")
    title = ytdl_data["title"]
    await message.reply_video(file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=f"{title}\n**Request by {message.from_user.mention}**")
     
    await msg.delete()
    try:
        os.remove(file_name)
    except Exception as e:
        print(e)                                  
