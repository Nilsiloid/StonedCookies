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

    @commands.command(name="trivia", help="using this command shows you the different categories and starts a game of trivia.")
    async def trivia(self, ctx):
        desc = "\n".join([f"{i + 1} : {categ}" for i, categ in enumerate(self.category)])
        emb = discord.Embed(
            description=desc,
            colour = 0x0000ff,
            title = "Choose The Trivia Category"
        )
        emb.set_image(url="https://media.discordapp.net/attachments/959752581771583532/964933173882552411/download-1.jpg")
        emb.set_footer(text="Enter the index of the category you want")
        await ctx.send(embed = emb)
        try:
            msg = await self.client.wait_for('message', timeout=20.0, check=lambda x : x.channel == ctx.channel and x.author == ctx.author)
        except asyncio.TimeoutError:
            await ctx.reply("You took too long!")
        else:
            if msg.content[0]=='0' or msg.content[0]=='1' or msg.content[0]=='2' or msg.content[0]=='3' or msg.content[0]=='4' or msg.content[0]=='5' or msg.content[0]=='6' or msg.content[0]=='7' or msg.content[0]=='8' or msg.content[0]=='9':
                index=int(msg.content)
                if index>14 or index<1:
                    await ctx.reply("Please enter a number in the range 1-14.")
                    await self.trivia(ctx)
                await self.quiz(ctx, index-1)

            else:
                await ctx.reply("Please enter a number in the range 1-14.")
                await self.trivia(ctx)

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
            #if isinstance(msg.content, int)==False or (msg.content>14 or msg.content<1):       DOUBT..
            #    await ctx.reply("Please enter a number from 1-14 only.")

        except asyncio.TimeoutError:
            await ctx.reply("You took too long!")

        if msg.content.lower() in answer.lower():
            await ctx.reply("Wow you are absolutely correct!")
        else:
            await ctx.reply(f"Unfortunately, you are wrong, the answer is {answer}")
        


def setup(client):
    client.add_cog(Trivia(client))