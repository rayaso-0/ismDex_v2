import discord
from discord.ext import commands, tasks
import feedparser
import aiohttp

class YouTubeAnnouncer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.announce_channel_id = 1269594252103520338
        
        self.youtube_channels = {
            "IsmIsm": "UCmBOzDLXqz8elPkUPIU1hPA"
        }
        
        self.latest_videos = {} 
        
        self.check_uploads.start()

    def cog_unload(self):
        self.check_uploads.cancel()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} background task online!")

    @tasks.loop(minutes=15)
    async def check_uploads(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(self.announce_channel_id)
        
        if not channel:
            return

        async with aiohttp.ClientSession() as session:
            for name, yt_id in self.youtube_channels.items():
                feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={yt_id}"
                
                async with session.get(feed_url) as response:
                    if response.status != 200:
                        continue
                    
                    text_data = await response.text()
                    feed = feedparser.parse(text_data)
                    
                    if not feed.entries:
                        continue
                        
                    latest_video = feed.entries[0]
                    video_id = latest_video.yt_videoid
                    video_link = latest_video.link
                    
                    if name not in self.latest_videos:
                        self.latest_videos[name] = video_id
                        continue
                        
                    if self.latest_videos[name] != video_id:
                        self.latest_videos[name] = video_id
                        await channel.send(f"🚨 New vid drop!!! \n{video_link} @Grunt")

async def setup(bot):
    await bot.add_cog(YouTubeAnnouncer(bot))