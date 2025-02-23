import requests
import os
from discord.ext import commands


WHITELISTED_CHANNELS = [1343099049473212559, 1326585585741074514]


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def whitelisted_channel():
        def predicate(ctx):
            return ctx.channel.id in WHITELISTED_CHANNELS
        return commands.check(predicate)

    @commands.hybrid_command()
    @commands.check_any(whitelisted_channel(), commands.has_permissions(administrator=True))
    async def cat(self, ctx):
        response = requests.get(
            'https://api.thecatapi.com/v1/images/search', params='api_key='+os.getenv('CAT_API_KEY'))
        if response.status_code == 200:
            cat_url = response.json()[0]["url"]
            await ctx.send(cat_url)
        else:
            await ctx.send("Sorry! Looks like they ran away. Try again later.")
