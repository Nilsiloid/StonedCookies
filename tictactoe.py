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


class TicTacToe(commands.Cog):
    def __init__(self, client):
        self.client=client

def setup(client):
    client.add_cog(TicTacToe(client))