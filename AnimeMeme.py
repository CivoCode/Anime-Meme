from http import client
import discord
import random
import aiohttp
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.command()
async def animememe(ctx):
    async with aiohttp.ClientSession() as cd:
        async with cd.get("https://www.reddit.com/r/animememes.json") as r:
            animememes = await r.json()
            embed = discord.Embed(color=discord.Color.random())
            embed.set_image(url=animememes["data"]["children"][random.randint(0, 30)]["data"]["url"])
            embed.set_footer(text=f"Meme sent by {ctx.author}")

            await ctx.send(embed=embed)
