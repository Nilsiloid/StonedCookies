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

IST=pytz.timezone('Asia/Kolkata')
start_time = 0
end_time = 0
p_1 = ""
p_2 = ""
turn = ""
gameOver = True
global play

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

class TicTacToe(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command(name="tictactoe", help="using this command and pinging 2 people will start a game of tic tac toe..")
    async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member):
        global count
        global p_1
        global p_2
        global turn
        global gameOver

        if gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:"]
            turn = ""
            gameOver = False
            count = 0

            p_1 = p1
            p_2 = p2

            # print the board
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + board[x]

            # determine who goes first
            num = random.randint(1, 2)
            if num == 1:
                turn = p_1
                await ctx.send("It is <@" + str(p_1.id) + ">'s turn.")
            elif num == 2:
                turn = p_2
                await ctx.send("It is <@" + str(p_2.id) + ">'s turn.")
        else:
            await ctx.send("A game is already in progress! Finish it before starting a new one.")

    @commands.command(name="place", help="Places your token(X or O) in the given position.")
    async def place(self, ctx, pos: int):
        global turn
        global p_1
        global p_2
        global board
        global count
        global gameOver

        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == p_1:
                    mark = ":regional_indicator_x:"
                elif turn == p_2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                    board[pos - 1] = mark
                    count += 1

                    # print the board
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x]

                    checkWinner(winningConditions, mark)
                    print(count)
                    if gameOver == True:
                        await ctx.send(mark + " wins!")
                    elif count >= 9:
                        gameOver = True
                        await ctx.send("It's a tie!")

                    # switch turns
                    if turn == p_1:
                        turn = p_2
                    elif turn == p_2:
                        turn = p_1
                else:
                    await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
            else:
                await ctx.send("It is not your turn.")
        else:
            await ctx.send("Please start a new game using the !tictactoe command.")

    @tictactoe.error
    async def tictactoe_error(ctx, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please mention 2 players for this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

    @place.error
    async def place_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter a position you would like to mark.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to enter an integer.")



def checkWinner(winningConditions, mark):
        global gameOver
        for condition in winningConditions:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                gameOver = True

def setup(client):
    client.add_cog(TicTacToe(client))