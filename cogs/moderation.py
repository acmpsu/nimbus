from discord.ext import commands
import asyncio
import discord

class Moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def clear(self, ctx, amount: str):
    if amount == 'all':
      await ctx.channel.purge(limit=100000)
      await ctx.send(f'Cleared all messages.')
    else:
      await ctx.channel.purge(limit=int(amount))
      await ctx.send(f'Cleared {amount} messages.')
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} got the boot!')

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} got the ban hammer!')

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def unban(self, ctx, *, member):
    await ctx.guild.unban(discord.Object(id=member))
    await ctx.send(f'{member} got unbanned!')
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)
  
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def mute(self, ctx, member: discord.Member, *, reason=None):
    await member.add_roles(discord.utils.get(ctx.guild.roles, name='Muted'))
    await ctx.send(f'{member.mention} got muted!')
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def unmute(self, ctx, member: discord.Member):
    await member.remove_roles(discord.utils.get(ctx.guild.roles, name='Muted'))
    await ctx.send(f'{member.mention} got unmuted!')
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)
    
    
    
    
    
