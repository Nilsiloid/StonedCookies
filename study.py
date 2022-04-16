import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests
import random
import datetime
import ast
import nacl
import time

load_dotenv()


class Study(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command()
    async def join(self, ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.reply("I am terribly sorry, but I cannot join you as you are not in a voice channel.")

def setup(client):
    client.add_cog(Study(client))