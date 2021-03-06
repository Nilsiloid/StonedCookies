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
channelID=0
set=False

class Suggest(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command(name="setconfess", help="displays the channels to whom you can set the id.")
    #@commands.has_permissions(administrator=True)
    async def setconfess(self, ctx):
        if ctx.message.author.guild_permissions.administrator:
            global set
            global j
            set = True
            global text_channel_list
            text_channel_list = []
            for server in self.client.guilds:
                if server.id == ctx.message.guild.id:
                    for channel in server.channels:
                        if str(channel.type) == 'text':
                            text_channel_list.append(channel)
            #print(text_channel_list)
            for j in range(len(text_channel_list)):
                await ctx.send(f"{j+1}. {text_channel_list[j]}")
            await ctx.reply("Type '$setid <number>', where number stands for the channel number in the given list which you'd like to set as your suggestion channel.")
            return

        
            
        else:
            await ctx.reply("You aren't an admin noob HAHAHAHAH JAJAJAJA. It's an admin only command, cope.")
            return

    @commands.command(name="setid", help="Sets channel to which confessions will be submitted.")
    @commands.has_permissions(administrator=True)
    async def setid(self, ctx, *args):
        global set
        
        global channelId
        global text_channel_list
        
        if set:
            str0 = ' '.join(args)
            if (int(str0)-1)<=len(text_channel_list) and (int(str0)-1)>=1:
                channelId = text_channel_list[int(str0)-1].id
                await ctx.reply(f"{text_channel_list[int(str0)-1]} has been set as the new confession channel.")
            else:
                await ctx.reply("Error! the number should be in the given range. Try again!")
                return
            
        else:
            await ctx.reply("you need to initialize the $setconfess command first in your server.")
            return

        set = False

    @commands.command(name="confess", help="DM the bot and you can drop a complaint/suggestion regarding the bot or the server anonymously here.")
    async def confess(self, ctx, *args):
        if ctx.channel.type == discord.ChannelType.private:
            str0 = ' '.join(args)
            global channelId
            if channelId == 0:
                await ctx.reply("you need to set the confession channel first, use $setconfess to set a confession channel.")
                return
                
            channel = self.client.get_channel(channelId)
            embed = discord.Embed(
                description = str0,
                colour = 0x0000ff
            )
            embed.set_footer(text="DM me $confess to post an anonymous confession in this channel.")
            
            
            embed.set_author(name="Anon", icon_url='https://cdn.discordapp.com/attachments/909526973099950112/964870222198767656/images.jpg')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/909526973099950112/964871331738959942/download_2.webp')

            await ctx.send("Your confession has been sent!")


            await channel.send(embed = embed)

def setup(client):
    client.add_cog(Suggest(client))