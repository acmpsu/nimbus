from dotenv import load_dotenv
import os

import discord
from discord.ext import commands
from cogs import setup

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='!')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='puddless form'))
    await setup(bot)
    await bot.tree.sync()


bot.run(os.getenv('BOT_TOKEN'))
