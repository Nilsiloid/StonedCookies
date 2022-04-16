import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
import music_cmds
#import tictactoe
#import study

client=commands.Bot(command_prefix='$')

cogs=["music_cmds", "tictactoe", "study"]

for cog in cogs:
    client.load_extension(cog)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

token=os.getenv("TOKEN")

client.run(token)