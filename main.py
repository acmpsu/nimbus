from dotenv import load_dotenv
import os

import discord
from discord.ext import commands
from greetings import Greetings
from auto_role import AutoRole
from fun import Fun

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='!')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='puddles form'))
    await bot.add_cog(Greetings(bot))
    await bot.add_cog(AutoRole(bot))
    await bot.add_cog(Fun(bot))
    await bot.tree.sync()


bot.run(os.getenv('BOT_TOKEN'))
