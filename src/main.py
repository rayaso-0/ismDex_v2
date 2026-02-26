import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

class IsmBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".", intents=discord.Intents.all())

    async def setup_hook(self):
        for filename in os.listdir("./src/cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded {filename}")
        
        await self.tree.sync()
        print("Slash commands synced to Discord!")

bot = IsmBot()

@bot.event
async def on_ready():
    print("ismDex Bot Online. Ready for action!") # ready command message by virtue of GroovyIsTrash

async def main():
    async with bot:
        await bot.start(os.getenv("DISCORD_TOKEN"))

asyncio.run(main())