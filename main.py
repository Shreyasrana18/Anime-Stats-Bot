from http import client
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get('TOKEN')

prefix = '$'
client=commands.Bot(command_prefix=prefix,help_command=None)

cogs=['cogs.stats','cogs.help']

for cog in cogs:
    client.load_extension(cog)


@client.event
async def on_ready():
    print('Bot switched on : {}'.format(client.user.name))
    print('Bot id : {}'.format(client.user.id))

client.run(token)