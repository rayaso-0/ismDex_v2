import discord
from discord.ext import commands
from discord import app_commands
import random

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} commands online!")

    @app_commands.command(name="hello", description="Greets the user")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello there, {interaction.user.mention}!")

    @app_commands.command(name="goodmorning", description="Wish someone a good morning")
    async def goodmorning(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Good morning, {interaction.user.mention}!")

    @app_commands.command(name="touch", description="Touch Jalen")
    async def touch(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Yes, WE {interaction.user.mention}, are gonna touch jalen :money_mouth:")

    @app_commands.command(name="flip", description="Flips a 50/50 fair coin")
    async def flip(self, interaction: discord.Interaction):
        number = random.randint(1, 2)
        if number == 1:
            await interaction.response.send_message("Heads!")
        else:
            await interaction.response.send_message("Tails!")

    @app_commands.command(name="help", description="List of all commands")
    async def help(self, interaction: discord.Integration):
        await interaction.response.send_message("Here is a list of every current command:\n"
                                                "`/hello`\n"
                                                "`/goodmorning`\n"
                                                "`/github`\n"
                                                "`/tos`\n"
                                                "`/privacypolicy`\n"
                                                "`/touch`\n"
                                                "`/flip`\n"
                                                "`/ping`\n"
                                                "`/groovy_bio`\n"
                                                "`/jalen_bio`\n"
                                                "`/rayaso_bio`\n"
                                                "`/airthyus_bio`\n"
                                                "`/ism_links`\n"
                                                "`/help`\n")
    
    @app_commands.command(name="github", description="Link to our GitHub Repository")
    async def github(self, interaction: discord.Interaction):
        await interaction.response.send_message("Here is the link to my GitHub Repository: https://github.com/rayaso-0/ismDex_v2")
    
    @app_commands.command(name="tos", description="Link to the ismDex discord bot Terms of Service")
    async def github(self, interaction: discord.Interaction):
        await interaction.response.send_message("Here is the link to my Terms of Service: https://github.com/rayaso-0/ismDex_v2/blob/main/TERMS-OF-SERVICE.md")

    @app_commands.command(name="privacypolicy", description="Link to the ismDex discord bot Privacy Policy")
    async def github(self, interaction: discord.Interaction):
        await interaction.response.send_message("Here is the link to my Privacy Policy: https://github.com/rayaso-0/ismDex_v2/blob/main/PRIVACYPOLICY.md")

async def setup(bot):
    await bot.add_cog(Basic(bot))