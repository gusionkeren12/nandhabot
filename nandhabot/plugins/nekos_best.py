from nandhabot import bot #nekos.best
from pyrogram import filters 
from pyrogram.types import Message 
import requests 

SLAP_TEXT = (
    "{user2} was killed by magic.",
    "{user2} starved without pats.",
    "{user2} was knocked into the void by {user1}.",
    "{user2} fainted.",
    "{user2} is out of usable Pokemon! {user2} whited out!.",
    "{user2} is out of usable Pokemon! {user2} blacked out!.",
    "{user2} got rekt.",
    "{user2}'s melon was split by {user1}.",
    "{user2} was sliced and diced by {user1}.",
    "{user2} played hot-potato with a grenade.",
    "{user2} was knifed by {user1}.",
    "{user2} ate a grenade.",
    "{user2} is what's for dinner!",
    "{user2} was terminated by {user1}.",
    "{user1} spammed {user2}'s email.",
    "{user1} RSA-encrypted {user2} and deleted the private key.",
    "{user1} put {user2} in the friendzone.",
    "{user1} slaps {user2} with a DMCA takedown request!",
    "{user2} got a house call from Doctor {user1}.",
    "{user1} beheaded {user2}.",
    "{user2} got stoned...by an angry mob.",
    "{user1} sued the pants off {user2}.",
    "{user2} was one-hit KO'd by {user1}.",
    "{user1} sent {user2} down the memory hole.",
    "{user2} was a mistake. - '{user1}' ",
    "{user2} was made redundant.",
    "{user1} {hits} {user2} with a bat!.",
    "{user1} {hits} {user2} with a Taijutsu Kick!.",
    "{user1} {hits} {user2} with X-Gloves!.",
    "{user1} {hits} {user2} with a Jet Punch!.",
    "{user1} {hits} {user2} with a Jet Pistol!.",
    "{user1} {hits} {user2} with a United States of Smash!.",
    "{user1} {hits} {user2} with a Detroit Smash!.",
    "{user1} {hits} {user2} with a Texas Smash!.",
    "{user1} {hits} {user2} with a California Smash!.",
    "{user1} {hits} {user2} with a New Hampshire Smash!.",
    "{user1} {hits} {user2} with a Missouri Smash!.",
    "{user1} {hits} {user2} with a Carolina Smash!.",
    "{user1} {hits} {user2} with a King Kong Gun!.",
    "{user1} {hits} {user2} with a baseball bat - metal one.!.",
    "*Serious punches {user2}*.",
    "*Normal punches {user2}*.",
    "*Consecutive Normal punches {user2}*.",
    "*Two Handed Consecutive Normal Punches {user2}*.",
    "*Ignores {user2} to let them die of embarassment*.",
    "*points at {user2}* What's with this sassy... lost child?.",
    "*Hits {user2} with a Fire Tornado*.",
    "{user1} pokes {user2} in the eye !",
    "{user1} pokes {user2} on the sides!",
    "{user1} pokes {user2}!",
    "{user1} pokes {user2} with a needle!",
    "{user1} pokes {user2} with a pen!",
    "{user1} pokes {user2} with a stun gun!",
    "{user2} is secretly a Furry!",
    "Hey Everybody! {user1} is asking me to be mean!",
    "( ･_･)ﾉ⌒●~* (･.･;) <-{user2}",
    "Take this {user2}\n(ﾉﾟДﾟ)ﾉ ))))●~* ",
    "Here {user2} hold this\n(｀・ω・)つ ●~＊",
    "( ・_・)ノΞ●~*  {user2}\nDieeeee!!.",
    "( ・∀・)ｒ鹵~<≪巛;ﾟДﾟ)ﾉ\n*Bug sprays {user2}*.",
    "( ﾟДﾟ)ﾉ占~<巛巛巛.\n-{user2} You pest!",
    "( う-´)づ︻╦̵̵̿╤── \(˚☐˚”)/ {user2}.",
    "{user1} {hits} {user2} with a {item}.",
    "{user1} {hits} {user2} in the face with a {item}.",
    "{user1} {hits} {user2} around a bit with a {item}.",
    "{user1} {throws} a {item} at {user2}.",
    "{user1} grabs a {item} and {throws} it at {user2}'s face.",
    "{user1} launches a {item} in {user2}'s general direction.",
    "{user1} starts slapping {user2} silly with a {item}.",
    "{user1} pins {user2} down and repeatedly {hits} them with a {item}.",
    "{user1} grabs up a {item} and {hits} {user2} with it.",
    "{user1} ties {user2} to a chair and {throws} a {item} at them.",
    "{user1} gave a friendly push to help {user2} learn to swim in lava.",
    "{user1} bullied {user2}.",
    "Nyaan ate {user2}'s leg. *nomnomnom*",
    "{user1} {throws} a master ball at {user2}, resistance is futile.",
    "{user1} hits {user2} with an action beam...bbbbbb (ง・ω・)ง ====*",
    "{user1} ara ara's {user2}.",
    "{user1} ora ora's {user2}.",
    "{user1} muda muda's {user2}.",
    "{user2} was turned into a Jojo reference!",
    "{user1} hits {user2} with {item}.",
    "Round 2!..Ready? .. FIGHT!!",
    "WhoPixel will oof {user2} to infinity and beyond.",
    "{user2} ate a bat and discovered a new disease.",
    "{user1} folded {user2} into a paper plane",
    "{user1} served {user2} some bat soup.",
    "{user2} was sent to his home, the planet of the apes.",
    "{user1} kicked {user2} out of a moving train.",
    "{user2} just killed John Wick’s dog.",
    "{user1} performed an Avada Kedavra spell on {user2}.",
    "{user1} subjected {user2} to a fiery furnace.",
    "Sakura Haruno just got more useful than {user2}",
    "{user1} unplugged {user2}'s life support.",
    "{user1} subscribed {user2}' to 5 years of bad internet.",
    "You know what’s worse than Dad jokes? {user2}!",
    "{user1} took all of {user2}'s cookies.",
    "{user2} wa mou.......Shindeiru! - {user1}.",
    "{user2} lost his race piece!",  #No game no life reference
    "Shut up {user2}, you are just {user2}.",  #No game no life reference
    "{user1} hits {user2} with Aka si anse!",  #No game no life reference
    "@NeoTheKitty scratches {user2}",  #Pixels pet cat - @NeoTheKitty 
    "Majin buu ate {user2}",  #Dbz
    "Goblin slayer slays {user2}",  #Goblin Slayer
)


@bot.on_message(filters.command("cuddle"))
def cuddle(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/cuddle").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/cuddle").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("shrug"))
def shrug(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/shrug").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/shrug").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

      
@bot.on_message(filters.command("poke"))
def poke(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/poke").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/poke").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("facepalm"))
def facepalm(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/facepalm").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/facepalm").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("stare"))
def stare(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/stare").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/stare").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
      
@bot.on_message(filters.command("pout"))
def pout(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/pout").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/pout").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("handhold"))
def handhold(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/handhold").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/handhold").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("wave"))
def wave(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/wave").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/wave").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("blush"))
def blush(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/blush").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/blush").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("neko"))
def neko(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/neko").json()
          url = api["results"][0]['url']
          reply.reply_photo(url)
      else:
          api = requests.get("https://nekos.best/api/v2/neko").json()
          url = api["results"][0]['url']
          m.reply_photo(url)

@bot.on_message(filters.command("dance"))
def dance(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/dance").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/dance").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("baka"))
def baka(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/baka").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/baka").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("bore"))
def bore(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/bored").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/bored").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)


@bot.on_message(filters.command("laugh"))
def laugh(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/laugh").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/laugh").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("smug"))
def smug(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/smug").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/smug").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("thumbsup"))
def thumbsup(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/thumbsup").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/thumbsup").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("shoot"))
def shoot(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/shoot").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/shoot").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("tickle"))
def tickle(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/tickle").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/tickle").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("feed"))
def feed(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/feed").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/feed").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("think"))
def think(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/think").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/think").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("wink"))
def wink(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/wink").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/wink").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("sleep"))
def sleep(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/sleep").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/sleep").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)

@bot.on_message(filters.command("punch"))
def punch(_, m: Message):
      reply = m.reply_to_message
      if reply:
          api = requests.get("https://nekos.best/api/v2/punch").json()
          url = api["results"][0]['url']
          reply.reply_animation(url)
      else:
          api = requests.get("https://nekos.best/api/v2/punch").json()
          url = api["results"][0]['url']
          m.reply_animation(animation=url)
 


@bot.on_message(filters.command("cry"))
def cry(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/cry").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/cry").json()
          url = api["url"]
          m.reply_animation(animation=url)
      
   
@bot.on_message(filters.command("kill"))
def kill(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/kill").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/kill").json()
          url = api["url"]
          m.reply_animation(animation=url)
      
      
@bot.on_message(filters.command("smile"))
def smile(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/smile").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/smile").json()
          url = api["url"]
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("highfive"))
def highfive(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/highfive").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/highfive").json()
          url = api["url"]      
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("slap"))
def slap(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/slap").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
           api = requests.get("https://api.waifu.pics/sfw/slap").json()
           url = api["url"]
           m.reply_animation(url)      
         
    
@bot.on_message(filters.command("kick"))
def kick(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/kick").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/kick").json()
          url = api["url"]     
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("hug"))
def hug(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/hug").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/hug").json()
          url = api["url"]  
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("pat"))
def pat(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/pat").json()
           url = api["url"]
           reply.reply_animation(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/pat").json()
          url = api["url"]
          m.reply_animation(animation=url)
    
@bot.on_message(filters.command("waifu"))
def waifu(_, m: Message):
       reply = m.reply_to_message
       if reply:
           api = requests.get("https://api.waifu.pics/sfw/waifu").json()
           url = api["url"]
           reply.reply_photo(url)
       else:
          api = requests.get("https://api.waifu.pics/sfw/waifu").json()
          url = api["url"]       
          m.reply_photo(photo=url)
    
