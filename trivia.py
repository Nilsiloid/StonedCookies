from email import message
from nis import cat
from unicodedata import category
import discord
from discord.ext import commands
import os
import requests
import json
import random
from dotenv import load_dotenv
load_dotenv()
import asyncio

#from keep_alive import keep_alive

class Trivia(commands.Cog):
    def __init__(self, client):
        self.client=client

    category=[
        "artliterature",
        "language",
        "sciencenature",
        "general",
        "fooddrink",
        "peopleplaces",
        "geography",
        "historyholidays",
        "entertainment",
        "toysgames",
        "music",
        "mathematics",
        "religionmythology",
        "sportsleisure"
    ]

    @commands.command()
    async def trivia(self, ctx):
        desc = "\n".join([f"{i + 1} : {categ}" for i, categ in enumerate(self.category)])
        emb = discord.Embed(description=desc)
        emb.set_footer(text="Enter the index of the category you want")
        await ctx.send(embed = emb)
        try:
            msg = await self.client.wait_for('message', timeout=20.0, check=lambda x : x.channel == ctx.channel and x.author == ctx.author)
        except asyncio.TimeoutError:
            await ctx.reply("You took too long!")
        else:
            index=int(msg.content)
            await self.quiz(ctx, index-1)

    async def quiz(self, ctx, index):
        #print("Hello")
        api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(self.category[index])
        #print("Hello")
        response = requests.get(api_url, headers={'X-Api-Key': 'thNqwveg8T9uywiyTE6FvA==Hvq6Go3pVLi2t1xd'})
        if response.status_code == requests.codes.ok:
            data=json.loads(response.text)
            answer=(data[0])['answer']
            if 'question' in data[0].keys():
                await ctx.reply((data[0])['question'])
        else:
            print("Error:", response.status_code, response.text)

        try:
            msg = await self.client.wait_for('message', timeout=100.0, check=lambda x : x.channel == ctx.channel and x.author == ctx.author)
            print(msg.content)
        except asyncio.TimeoutError:
            await ctx.reply("You took too long!")

        if answer.lower() == msg.content.lower():
            await ctx.reply("Wow you are absolutely correct!")
        else:
            await ctx.reply(f"Unfortunately, you are wrong, the answer is {answer}")
        


def setup(client):
    client.add_cog(Trivia(client))