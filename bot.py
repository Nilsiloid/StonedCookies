import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
import music_cmds
import urmom
import trivia
import tictactoe
import suggest
import study

client=commands.Bot(command_prefix='$', intents = discord.Intents.all())

cogs=["music_cmds", "tictactoe", "study", "urmom", "trivia", "suggest"]

for cog in cogs:
    client.load_extension(cog)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

token=os.getenv("TOKEN")

client.run(token)