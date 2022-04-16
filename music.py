import discord
from discord.ext import commands
import youtube_dl

class music(commands.cog):
    def __init__(self, client):
        self.Client=client

    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()

        FFMPEG_OPTIONS={'before-options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc=ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2=info['formats'][0]['url']

            source=await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    async def pause(self, ctx):
        await ctx.send("Music Paused.")
        await ctx.voice_client.pause()

    async def resume(self, ctx):
        await ctx.send("Music resumed.")
        await ctx.voice_client.resume()

    async def stop(self, ctx):
        await ctx.send("Music stopped. If you want to hear more, use $play and then add the url of the youtube link to the song..")
        await ctx.voice_client.stop()



def setup(client):
    client.add_cog(music(client))