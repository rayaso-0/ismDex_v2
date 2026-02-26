import discord
from discord.ext import commands
import random

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} commands online!")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello there, {ctx.author.mention}!")

    @commands.command(aliases=["gm", "morning"])
    async def goodmorning(self, ctx):
        await ctx.send(f"Good morning, {ctx.author.mention}!")

    @commands.command()
    async def github(self, ctx):
        await ctx.send("Here is the link to our GitHub Repository: https://github.com/rayaso-0/ismDex_v2")

    @commands.command()
    async def touch(self, ctx):
        await ctx.send(f"Yes, WE {ctx.author.mention}, are gonna touch jalen :money_mouth:")

    @commands.command()
    async def flip(self, ctx):
        number = random.randint(1, 2)
        if number == 1:
            await ctx.send("Heads!")
        else:
            await ctx.send("Tails!")

async def setup(bot):
    await bot.add_cog(Basic(bot))