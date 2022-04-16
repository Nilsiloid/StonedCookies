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

class UrMOM(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command()
    async def urmom(self, ctx):
        res = requests.get("https://api.yomomma.info/")
        data = res.json()
        tmp = discord.Embed(title = data["joke"] , color = 0x696969)
        await ctx.reply(embed = tmp, mention_author = True)

def setup(client):
    client.add_cog(UrMOM(client))