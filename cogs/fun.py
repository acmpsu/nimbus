import requests
import os
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def cat(self, ctx):
        response = requests.get(
            'https://api.thecatapi.com/v1/images/search', params='api_key='+os.getenv('CAT_API_KEY'))
        if response.status_code == 200:
            cat_url = response.json()[0]["url"]
            await ctx.send(cat_url)
        else:
            await ctx.send("Sorry! Looks like they ran away. Try again later.")
