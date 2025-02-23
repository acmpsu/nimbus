import discord
from discord.ext import commands

JOINABLE_ROLES = ['ai', 'explore']

class RoleNotFound(commands.CommandError):
    pass

class AutoRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def joinrole(self, ctx, role_name: str):
        if role_name not in JOINABLE_ROLES:
            options = [f'`{role}`' for role in JOINABLE_ROLES]
            await ctx.send(f"❌ You can select from: {', '.join(options)}.")
            return
        
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if not role:
            raise RoleNotFound(f'Missing {role_name}')
        
        if role in ctx.author.roles:
            await ctx.send(f"⚠️ You already have the `{role_name}` role.")
        else:
            await ctx.author.add_roles(role)
            await ctx.send(f"✅ You have been added to `{role_name}`!")
    
    @commands.hybrid_command()
    async def leaverole(self, ctx, role_name: str):
        if role_name not in JOINABLE_ROLES:
            options = [f'`{role}`' for role in JOINABLE_ROLES]
            await ctx.send(f"❌ You can select from: {', '.join(options)}.")
            return
        
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if not role:
            raise RoleNotFound(f'Missing {role_name}')

        if role not in ctx.author.roles:
            await ctx.send(f"⚠️ You don't have the `{role_name}` role.")
        else:
            await ctx.author.remove_roles(role)
            await ctx.send(f"✅ You have been removed from `{role_name}`.")
            
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def getroled(self, ctx, role_name: str):
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        
        if not role:
            await ctx.send(f"❌ Role `{role_name}` not found.")
            return

        members_with_role = [f'`{member.name}`' for member in ctx.guild.members if role in member.roles]
   
        if members_with_role:
            await ctx.send(f"**Members with the `{role_name}` role:**\n" + "; ".join(members_with_role))
        else:
            await ctx.send(f"No members have the `{role_name}` role.")