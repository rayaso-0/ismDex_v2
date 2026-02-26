import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("ismDex Bot Online. Ready for action!") # ready command message by virtue of GroovyIsTrash

async def load():
    for filename in os.listdir("./src/cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(os.getenv("DISCORD_TOKEN"))

asyncio.run(main()) 