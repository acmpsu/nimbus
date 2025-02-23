from dotenv import load_dotenv
import os

import discord
from discord.ext import commands
from greetings import Greetings
from auto_role import AutoRole

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='!')


@bot.event
async def on_ready():
    await bot.add_cog(Greetings(bot))
    await bot.add_cog(AutoRole(bot))
    await bot.tree.sync(guild=discord.Object(id=1247395905938653264))


bot.run(os.getenv('BOT_TOKEN'))
