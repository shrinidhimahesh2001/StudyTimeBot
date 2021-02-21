import discord
import os
import datetime
import requests
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv('.env')

client= commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Hello!')

@client.command()
async def hi(ctx):
    await ctx.channel.send(':nerd: Hello there!') 

@client.command()
async def timenow(ctx):
    timestamp = datetime.datetime.now()
    await ctx.send(f'{ctx.author.name},the time now is {timestamp.strftime(r"%I:%M %p")}')
#@client.command()
#async def stay(ctx):
    #timestamp=datetime.datetime.now().time()
    #if(timestamp>9):
       # await ctx.send(f'{ctx.author.name},you should leave now. Go get some sleep')
   # else:
       # await ctx.send(f'{ctx.author.name},you hang around and study a bit more')

#client.add_command(hi)
client.run(os.getenv('TOKEN'))
