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
import pytz
IST = pytz.timezone('Asia/Kolkata')

load_dotenv()
flag_study=False


class Study(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command(name="join", help="Bot connects to the vc you are in.")
    async def join(self, ctx):
        if (ctx.author.voice):
            voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
            if voice == None:
                channel = ctx.message.author.voice.channel
                await channel.connect()
            
            
        else:
            await ctx.reply("I am terribly sorry, but I cannot join you as you are not in a voice channel.")


    @commands.command(name="study", help="Starts your study session and timer.")
    async def study(self, ctx):
        global start_time
        global flag_study
        global IST
        if (ctx.author.voice):
            #voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
            #if voice == None:
            #    channel = ctx.message.author.voice.channel
            #    await channel.connect()
            flag_study = True
            start_time = datetime.datetime.now(IST)
            print(start_time)
            embed = discord.Embed(
                title = "Study-session",
                description = "Study session started at {0}".format(datetime.datetime.strftime(start_time , "%H:%M:%S")),
                colour = 0x0000ff
            )
            embed.set_footer(text="Happy studying!")
            
            embed.set_author(name="Hackathon_Bot", icon_url='https://cdn.discordapp.com/attachments/909526973099950112/964870222198767656/images.jpg')
                    
            await ctx.reply(embed = embed)
            #await ctx.reply("study session started! {0}".format(datetime.datetime.strftime(start_time , "%H:%M:%S")))
        else: 
            await ctx.send("I am terribly sorry, but I cannot join you as you are not in a voice channel.")


    @commands.command(name="stop_study", help="Ends the study session and reports the amount of time you studied..")
    async def stop_study(self, ctx):
        global start_time
        global end_time
        global flag_study
        global IST
        if (ctx.author.voice):
            end_time = datetime.datetime.now(IST)
            print(end_time)
            delta = end_time-start_time
            #channel = ctx.message.author.voice.channel
            #await ctx.voice_client.disconnect()
        if flag_study:
            flag_study = False
            start_time = 0

        embed = discord.Embed(
            title = "Your study session has ended.",
            description = f"The time spent studying in vc was {delta}s ",
            colour = 0x0000ff
        )
        embed.set_footer(text="!join_vc to join the vc and !study to start the study timer.")

        embed.set_author(name="Hackathon_Bot", icon_url='https://cdn.discordapp.com/attachments/909526973099950112/964870222198767656/images.jpg')
        embed.set_image(url='https://cdn.discordapp.com/attachments/909526973099950112/964882484976295976/download.jpg')

        await ctx.reply(embed = embed)
    
    @commands.command(name="leave", help="Disconnects from the Voice Channel.")
    async def leave(self, ctx):
        global end_time
        global start_time
        global flag_study
        if ctx.guild.voice_client not in self.client.voice_clients:
            await ctx.reply("bot nahi he vc mein madarchod 🤬" , mention_author = True)
            return ; 
        if not flag_study:
            await ctx.voice_client.disconnect()
            return
        else:
            await ctx.voice_client.disconnect()
            return

def setup(client):
    client.add_cog(Study(client))