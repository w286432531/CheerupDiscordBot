import os
token=os.environ["token"]
import discord
import zenQuotes
import requests
#import json
import anWeiQuotes
import random
import joke
import saoHua
from keepAlive import keep_alive
client = discord.Client()



@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  messageStart=message.content.startswith
  msg=message.content
  if message.author == client.user:
    return
  if messageStart("-L"):
    await message.channel.send("I love you.")
  if messageStart("-inspire"):
    quote=zenQuotes.get_quote()
    await message.channel.send(quote)
  if "草" in msg or "傻" in msg:
    await message.channel.send("主人消消气。Σ(•̀ω•́ﾉ)ﾉ")
  if any(word in msg for word in anWeiQuotes.sadWord):
    await message.channel.send(random.choice(anWeiQuotes.anWeiWordList))
  if "你爱我吗" in msg:
    await message.channel.send("我爱你，主人。我永远爱你。( ˘ ³˘)♥")
  if any(word in msg for word in anWeiQuotes.lonelyWord):
    await message.channel.send("主人。我会永远陪着你。(♡,,• ₃ •,,♡)")
  if "谢" in msg:
    await message.channel.send("不用这么客气哦。主人˘◡˘")
  if "笑话" in msg:
    await message.channel.send(joke.joke())
  if "骚话" in msg:
    await message.channel.send(random.choice(saoHua.saoHua))

keep_alive()
client.run(token)
