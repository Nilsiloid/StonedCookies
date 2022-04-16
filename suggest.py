import os
import discord
import requests
import json
import random
import ast
from discord.ext import commands
import datetime
import nacl
import time
import pytz


IST=pytz.timezone('Asia/Kolkata')

class Suggest(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command()
    async def confess(ctx, *args):
        if ctx.channel.type == discord.ChannelType.private:
            str0 = ' '.join(args)
            channelId = 962016496626831360
            channel = ctx.get_channel(channelId)
            embed = discord.Embed(
                title = "Title",
                description = str0,
                colour = 0x0000ff
                )
            embed.set_footer(text="DM me !confess to post an anonymous confession in this channel.")
            
            
            embed.set_author(name="Anon", icon_url='https://cdn.discordapp.com/attachments/909526973099950112/964870222198767656/images.jpg')
            embed.set_image(url='https://cdn.discordapp.com/attachments/909526973099950112/964871331738959942/download_2.webp')

            await ctx.send("Your confession has been sent!")

            await channel.send(embed = embed)
            

def setup(client):
    client.add_cog(Suggest(client))