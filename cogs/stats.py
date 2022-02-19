import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import asyncio


class AnimeStats(commands.Cog):
    def __init__(self, test):
        self.bot = test

    @commands.command()
    async def getanimelist(self, ctx, count):
        embed = discord.Embed(title='Choose one from the following:',
                              description='Input the corresponding number', color=0x1FFF0D)
        embed.add_field(name='1. **Top Airing Animes**',
                        value='Gets a list of top airing animes', inline=False)
        embed.add_field(name='2. **Most Popular Animes**',
                        value='Gets a list of most popular animes', inline=False)
        embed.add_field(name='3. **Top Upcoming Animes**',
                        value='Gets a list of top upcoming animes', inline=False)
        embed.add_field(name='4. **Top Movies**',
                        value='Gets a list of top movies', inline=False)
        embed.add_field(name='5. **Top OVAs**',
                        value='Gets a list of top OVAs(original video animation)', inline=False)
        embed.add_field(name='6. **Most Favourited**',
                        value='Gets a list of most favourite animes', inline=False)
        await ctx.send(embed=embed)

        def check(reply_user):
            return reply_user.author == ctx.author and reply_user.channel == ctx.channel

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=10)
        except asyncio.TimeoutError:
            await ctx.send('Sorry, you didn\'t reply in time!')
            return

        a = ['airing', 'bypopularity', 'upcoming','movie','ova','favorite']
        x = int(msg.content)-1
        search_filter = a[x]

        url = f'https://myanimelist.net/topanime.php?type={search_filter}'
        # print(url)
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            tags = soup('tr', class_="ranking-list")
            rank = 0
            count = int(count)
            # always remember to convert string to int
            i = 0
            if count < 51 and count > 0:
                embed = discord.Embed(
                    title='Anime List', description='Here is your anime list', color=0x1FFF0D)
                for tag in tags:
                    if count < 51 and i < count:
                        i = i+1
                        s = tag.find('h3')
                        # finds the all the h3 tag
                        anime_name = s.get_text()
                        # print(anime_name)
                        # gets all text from h3 tags

                        a = s.find('a')
                        # finds a tag in h3 tag
                        anime_link = a.get('href')
                        # gets the link from a tag

                        rank = rank+1
                        embed.add_field(
                            name=f'{rank}. **{anime_name}**', value=anime_link, inline=False)
                    else:
                        break
                await ctx.send(embed=embed)
            else:
                await ctx.send('```Enter a number between 1-50```')

        except:
            await ctx.send('site is down for now !!!! Try later')


def setup(client):
    client.add_cog(AnimeStats(client))
