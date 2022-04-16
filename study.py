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

    @commands.command()
    async def study(self, ctx):
        global start_time
        global flag_study
        if (ctx.author.voice):
            flag_study = True
            start_time = datetime.datetime.now()
            await ctx.reply("study session started! {0}".format(datetime.datetime.strftime(start_time , "%H:%M:%S")))
        else:
            await ctx.send("I am terribly sorry, but I cannot join you as you are not in a voice channel.")


    @commands.command()
    async def stop_study(self, ctx):
        global start_time
        global end_time
        global flag_study
        if (ctx.author.voice):
            end_time = datetime.datetime.now()
            delta = end_time-start_time
        if flag_study:
            flag_study = False
            start_time = 0
        await ctx.reply(f"study timer stopped, {delta.seconds}s were spent studying.")
    
    @commands.command()
    async def leave(self, ctx):
        global end_time
        global start_time
        global flag_study
        if ctx.guild.voice_client not in ctx.voice_clients:
            await ctx.reply("bot nahi he vc mein madarchod 🤬" , mention_author = True)

        if not flag_study:
            await ctx.send("You left the vc")
            await ctx.voice_client.disconnect()
        
            
            
        else:
            await ctx.send("you need to join one vc b4 leaving one daaaa.") 

def setup(client):
    client.add_cog(Study(client))