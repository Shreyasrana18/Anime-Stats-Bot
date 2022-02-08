from http import client
import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, test):
        self.bot = test

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='Anime Stats',
                              description='prefix=$', color=0x1FFF0D)
        embed.add_field(name='1. **Commands**',
                        value='!getanimelist {count}', inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
