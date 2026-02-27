import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True 
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        print("Starting setup_hook...")
        current_directory = os.path.dirname(os.path.abspath(__file__))
        cogs_folder = os.path.join(current_directory, 'cogs')
        
        if not os.path.exists(cogs_folder):
            print(f"CRITICAL ERROR: Could not find cogs folder at {cogs_folder}")
            return

        for filename in os.listdir(cogs_folder):
            if filename.endswith('.py') and not filename.startswith('__'):
                try:
                    await self.load_extension(f"cogs.{filename[:-3]}")
                    print(f"✅ Successfully loaded cogs.{filename[:-3]}")
                except Exception as e:
                    print(f"❌ Failed to load cogs.{filename[:-3]}: {e}")
        
        await self.tree.sync()
        print("✅ Command tree globally synced to Discord!")

bot = MyBot()

@bot.event
async def on_ready():
    print("ismDex Bot Online. Ready for action!") 
    print("------")

@bot.command(name="sync", description="Manually syncs slash commands (Dev Only)")
@commands.is_owner() 
async def sync(ctx):
    await ctx.send("Syncing command tree to Discord...")
    try:
        synced = await bot.tree.sync()
        await ctx.send(f"Successfully synced {len(synced)} command(s) globally!")
    except Exception as e:
        await ctx.send(f"Failed to sync commands: {e}")

async def main():
    load_dotenv()
    async with bot:
        await bot.start(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())