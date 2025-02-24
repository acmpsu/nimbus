from discord.ext import commands
import discord
from datetime import datetime

class MessageSender(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def m(self, ctx):
    embed = discord.Embed(title="Connect With Us!",
                      description="Use these links to connect with us and learn about upcoming events!\n\n**Discord**\nYou're already here! Use this link to invite friends, too.\nhttps://discord.gg/4Wyja9anhZ\n\n**GroupMe**\nDiscord not your thing? No worries.\nhttps://groupme.com/join_group/105326747/CSj2fp99\n\n**Our Website**\nWeb development really does come in handy. Check us out at: \nhttps://acm.psu.edu/")

    embed.set_author(name="Social Media",
                    icon_url="https://i.ibb.co/BH1QLd4n/acm-logo-transparent.png")

    embed.set_footer(text="Found us on another platform? Be cautious–we do not operate on any other platforms or websites except for those owned by or affiliated with the University.")

    await ctx.send(embed=embed)

  