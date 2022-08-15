
from nandhabot.events import register
from nandhabot import tbot,bot, SUPPORT_CHAT
from telethon import Button
from pyrogram import filters
import requests
import requests
import json


class NotFound(Exception):
    pass



base_url = 'https://9anime.dev'

class client:
    def __init__():
        pass

    def search(anime_name):
        r = requests.get(base_url + '/anime?search=' + anime_name)
        if r.status_code == 404:
            raise exceptions.NotFound('Not Found.')
        elif r.status_code != 200:
            raise Exception(r.content)
        return json.loads(json.dumps(r.json(), indent=4))

__version__ = '1.0.0'

animedev_client = client

@register(pattern='/anilink')
async def animelink(event):
    animename = event.message.message.split()
    if len(animename) <= 1:
        await event.reply('/anilink anime name')
        return
    try:
        anime = animedev_client.search(' '.join(animename[1:]))
        anime['Search_Query'] = anime['Search_Query'].replace(' ', '+')
    except exceptions.NotFound:
        await event.reply('Anime not found.')
        return
    except Exception as e:
        await event.reply(f'*Error*: Contact @{SUPPORT_CHAT}.\nERROR: {e}')
        return
    text = f'''
<b>Anime Title:</b> <code>{anime['AnimeTitle']}</code>
    '''
    button_list = [[Button.url('Download Link', anime['AnimeLink'])], [Button.url('Search Query', anime['Search_Query'])]]
    
    await tbot.send_file(event.chat_id, anime['AnimeImg'], caption=text, buttons=button_list, parse_mode='html', reply_to=event.id)

    

@bot.on_message(filters.command('anilatest'))
def schedule(_, message):
    results = requests.get('https://subsplease.org/api/?f=schedule&h=true&tz=Japan').json()
    text = None
    for result in results['schedule']:
        title = result['title']
        time = result['time']
        aired = bool(result['aired'])
        title = f"**[{title}](https://subsplease.org/shows/{result['page']})**" if not aired else f"**~~[{title}](https://subsplease.org/shows/{result['page']})~~**"
        data = f"{title} - **{time}**"
        
        if text:
            text = f"{text}\n{data}"
        else:
            text = data

    message.reply_text(f"**Today's Schedule:**\nTime-Zone: Tokyo (GMT +9)\n\n{text}")



    
    
    
    
