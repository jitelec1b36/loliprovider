import discord
from discord.ext import commands , tasks
from discord.ext.commands import Bot
import asyncio
import requests
import json
import aiohttp
import urllib.request

client = discord.Client()
bot = commands.Bot(command_prefix="+") 

# class MyClient(discord.Client):
#     def _init_(self, *args,** kwargs):
#         super()._init_(*args,** kwargs)
#         self.bg_task = self.loop.create_task(self.background_loop())
       

@bot.event
async def on_ready():
    print ("I'm ready!!!")
    print ("She's " + bot.user.name)
    print ("My id is : " + str(bot.user.id))
    activity = discord.Game(name = "Posting loli lewds every 5 mins.")
    await bot.change_presence(status=discord.Status.idle,activity=activity)



@bot.event
async def background_loop_kawaii():
    await bot.wait_until_ready()
    channel = bot.get_channel(517359709607428096)
    while not bot.is_closed():
        response = requests.get('https://api.lolis.life/kawaii')
        data = response.json()
        kawaii = json.dumps(data['url'])
        lolikawaii = kawaii.replace('"', '')
        embed = discord.Embed()
        embed.set_image(url=lolikawaii)
        await channel.send(embed = embed)
        await asyncio.sleep(300)

# ---------------------------------------------------------------#


@bot.event
async def background_loop_neko():
    await bot.wait_until_ready()
    channel = bot.get_channel(529701720859607080)
    while not bot.is_closed():
        response = requests.get('https://api.lolis.life/neko')
        data = response.json()
        neko = json.dumps(data['url'])
        lolineko = neko.replace('"', '')
        embed = discord.Embed()
        embed.set_image(url=lolineko)
        await channel.send(embed = embed)
        await asyncio.sleep(300)

# ---------------------------------------------------------------#
@bot.event
async def background_loop_pat():
    await bot.wait_until_ready()
    channel = bot.get_channel(607597361862148259)
    while not bot.is_closed():
        response = requests.get('https://api.lolis.life/pat')
        data = response.json()
        pat = json.dumps(data['url'])
        lolipat = pat.replace('"', '')
        embed = discord.Embed()
        embed.set_image(url=lolipat)
        await channel.send(embed = embed)
        await asyncio.sleep(300)

# ---------------------------------------------------------------#
@bot.event
async def background_loop_slave():
    await bot.wait_until_ready()
    channel = bot.get_channel(607597414018187264)
    while not bot.is_closed():
        response = requests.get('https://api.lolis.life/slave')
        data = response.json()
        slave = json.dumps(data['url'])
        lolislave = slave.replace('"', '')
        embed = discord.Embed()
        embed.set_image(url=lolislave)
        await channel.send(embed = embed)
        await asyncio.sleep(300)

# ---------------------------------------------------------------#
@bot.event
async def background_loop_futa():
    await bot.wait_until_ready()
    channel = bot.get_channel(607597488974856203)
    while not bot.is_closed():
        response = requests.get('https://api.lolis.life/futa')
        data = response.json()
        futa = json.dumps(data['url'])
        lolifuta = futa.replace('"', '')
        embed = discord.Embed()
        embed.set_image(url=lolifuta)
        await channel.send(embed = embed)
        await asyncio.sleep(300)

# ---------------------------------------------------------------#
@bot.event
async def background_loop_monster():
    await bot.wait_until_ready()
    channel = bot.get_channel(607597593559826432)
    while not bot.is_closed():
        response = requests.get('https://api.lolis.life/monster')
        data = response.json()
        monster = json.dumps(data['url'])
        lolimonster = monster.replace('"', '')
        embed = discord.Embed()
        embed.set_image(url=lolimonster)
        await channel.send(embed = embed)
        await asyncio.sleep(300)

# ---------------------------------------------------------------#

@bot.event
async def background_loop_lewd():
    await bot.wait_until_ready()
    channel = bot.get_channel(607597709217628180)
    while not bot.is_closed():
        response = requests.get('https://api.lolis.life/lewd')
        data = response.json()
        lewd = json.dumps(data['url'])
        lolilewd = lewd.replace('"', '')
        embed = discord.Embed()
        embed.set_image(url=lolilewd)
        await channel.send(embed = embed)
        await asyncio.sleep(300)

# ---------------------------------------------------------------#

@bot.command(pass_context = True)
async def ping(ctx):
    response = requests.get('https://api.lolis.life/neko')
    data = response.json()
    neko = json.dumps(data['url'])
    nude = neko.replace('"', '')
    channel = bot.get_channel(517359709607428096)
    await channel.send("test wack")
    # await ctx.send("{}".format(nude))

@bot.command(pass_context= True)
async def say(ctx, *args):
    msg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(msg)

client.loop.create_task(background_loop_kawaii())
client.loop.create_task(background_loop_neko())
client.loop.create_task(background_loop_pat())
client.loop.create_task(background_loop_slave())
client.loop.create_task(background_loop_futa())
client.loop.create_task(background_loop_monster())
client.loop.create_task(background_loop_lewd())

bot.run('NjA3NDc3NDE5MzkzNDE3MjI3.XUbAMQ.SgErB24ibTtUgkSlnKaJ3KNQi7o')
