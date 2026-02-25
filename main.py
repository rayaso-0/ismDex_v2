import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("ismDex Bot Online. Ready for action!") # ready command by virtue of GroovyIsTrash

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello there, {ctx.author.mention}!")

@bot.command(aliases=["gm", "morning"])
async def goodmorning(ctx):
    await ctx.send(f"Good morning, {ctx.author.mention}!")

# @bot.command()
# async def sendembed(ctx):
#     embeded_msg = discord.Embed(title="Title of embed", description="Description of embed", color=discord.Color.green())
#     embeded_msg.set_thumbnail(url=ctx.author.avatar)
#     embeded_msg.add_field(name="Name of field", value="Value of field", inline=False)
#     embeded_msg.set_image(url=ctx.guild.icon)
#     embeded_msg.set_footer(text="Footer text", icon_url=ctx.author.avatar)
#     await ctx.send(embed=embeded_msg)

@bot.command()
async def groovy_bio(ctx):
    desc = (
        "Groovy is one of the founding members of IsmIsm.\n"
        "He has always been passionate about content creation and the arts including, "
        "streaming, editing, music, and voice acting. To get into specifics of music, He has 7 "
        "years of choral work and is a self-taught percussionist.\n"
        "Groovy started content-creating in 2019 with an unedited Overwatch video, dont "
        "look for it. Since then the quality of their edits has increased but there will always "
        "be room for improvement! When it comes to IsmIsm Groovy does a lot of the "
        "organizing and administrative work."
    )

    embeded_msg = discord.Embed(title="Meet Groovy!", description=desc, color=discord.Color.orange())
    
    embeded_msg.add_field(name="Twitch", value="https://www.twitch.tv/groovykobold", inline=True)
    embeded_msg.add_field(name="Youtube", value="https://www.youtube.com/@GroovyKobold", inline=True)
    
    embeded_msg.set_image(url="https://i.imgur.com/MHP9lmb.jpeg")
    
    await ctx.send(embed=embeded_msg)

@bot.command()
async def jalen_bio(ctx):
    desc = (
        "Jalen is one of the founding members of IsmIsm. With a strong\n"
        "passion in gaming, he wants to go further than that and see where\n"
        "life takes him. He is currently interested in becoming a Voice Actor.\n"
        "But on top of all of this, he is the number one Steph Curry fan on\n"
        "the planet. You cant take the Curry out of Jalen.\n"
        "He leaves with one quote...\"#Feminist\""
    )

    embeded_msg = discord.Embed(title="Meet Jalen!", description=desc, color=discord.Color.dark_grey())
    
    embeded_msg.add_field(name="Instagram", value="https://www.instagram.com/jalen.ex/", inline=True)
    embeded_msg.add_field(name="Twitch", value="https://www.twitch.tv/jalenex", inline=True)
    embeded_msg.add_field(name="Youtube", value="https://www.youtube.com/@JalenEx", inline=True)
    
    embeded_msg.set_image(url="https://i.imgur.com/rNZKe9m.jpeg")
    
    await ctx.send(embed=embeded_msg)

@bot.command()
async def rayaso_bio(ctx):
    desc = (
        "Rayaso is the lead Developer for the ismDex discord bot and one of the Founding\n"
        "Members of IsmIsm. Doing things from recording gameplay with the others or\n"
        "working behind the scenes like editing videos or coding this very bot!\n"
        "He is very excited for the future is IsmIsm and cant wait to create a community of\n"
        "like-minded people who like all things gaming.\n"
        "Dont hesitate to reach out for anything!"
    )

    embeded_msg = discord.Embed(title="Meet Rayaso!", description=desc, color=discord.Color.purple())
    
    embeded_msg.add_field(name="LinkedIn Profile:", value="https://www.linkedin.com/in/kristoefb/", inline=True)
    embeded_msg.add_field(name="Youtube:", value="https://www.youtube.com/@rayaso6036", inline=True)
    embeded_msg.add_field(name="Twitch Channel:", value="https://www.twitch.tv/rayaso_0", inline=True)
    
    embeded_msg.set_image(url="https://i.imgur.com/5PmuFLR.png")
    
    await ctx.send(embed=embeded_msg)

@bot.command()
async def airthyus_bio(ctx):
    desc = (
        "Airthyus is one of the founding members of IsmIsm.\n"
        "With a strong passion in gaming and math, he wants to go further than that and\n"
        "see where life takes him. He is currently interested in fighter games such as\n"
        "Tekken, MK and brawlhalla. He mainly plays apex and overwatch. He does a\n"
        "lot behind the scenes for Ism so be on the lookout for him!\n" \
        "I LIKE PHONK"
    )

    embeded_msg = discord.Embed(title="Meet Airthyus!", description=desc, color=discord.Color.red())
    
    embeded_msg.add_field(name="Youtube", value="https://www.youtube.com/@Airthyus", inline=True)
    embeded_msg.add_field(name="Twitch", value="https://www.twitch.tv/airthyus", inline=True)
    
    await ctx.send(embed=embeded_msg)

bot.run(os.getenv("DISCORD_TOKEN"))