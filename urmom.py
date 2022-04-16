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

class urmom(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command(name="urmom", help="Generates a random Your Mom joke.")
    async def urmom(self, ctx):
        res = requests.get("https://api.yomomma.info/")
        data = res.json()
        tmp = discord.Embed(title = data["joke"] , color = 0x696969)
        await ctx.reply(embed = tmp, mention_author = True)

    @commands.command(name="kick", help="Kicks the mentioned user from the server.")
    async def kick(self, ctx, member: discord.Member, *, reason=None):

        await member.kick(reason=reason)

        await ctx.send(f'User {member} has kicked.')

def setup(client):
    client.add_cog(urmom(client))