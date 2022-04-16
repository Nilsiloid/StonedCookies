import discord
from discord.ext import commands
import youtube_dl

class Music(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command(name="play", help="plays music by using Youtube URL.")
    async def play(self, ctx, url):
        if(ctx.author.voice):
            ctx.voice_client.stop()     #stops the song.
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YDL_OPTIONS = {'format': "bestaudio"}
            vc=ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2=info['formats'][0]['url']

                source=await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                vc.play(source)
        else: 
            await ctx.send("I am terribly sorry, but I cannot join you as you are not in a voice channel.")

    
    @commands.command(name="pause", help="Pauses currently playing music.")
    async def pause(self, ctx):
        if(ctx.author.voice):
            await ctx.send("Music Paused.")
            await ctx.voice_client.pause()
        else: 
            await ctx.send("I am terribly sorry, but I cannot join you as you are not in a voice channel.")

    @commands.command(name="resume", help="Resumes music.")
    async def resume(self, ctx):
        if(ctx.author.voice):
            await ctx.send("Music resumed.")
            await ctx.voice_client.resume()
        else: 
            await ctx.send("I am terribly sorry, but I cannot join you as you are not in a voice channel.")

    @commands.command(name="stop", help="Stops currently playing music.")
    async def stop(self, ctx):
        if(ctx.author.voice):
            await ctx.send("Music stopped. If you want to listen to more songs, use $play and then add the url of the youtube link to the song..")
            await ctx.voice_client.stop()
        else: 
            await ctx.send("I am terribly sorry, but I cannot join you as you are not in a voice channel.")



def setup(client):
    client.add_cog(Music(client))