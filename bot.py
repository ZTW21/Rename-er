# bot.py
import os
from datetime import *

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} has connected to Discord!\n'
          f'{guild.name}(id: {guild.id})'
          )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    today = date.today()
    print(f'Today\'s date: {today.strftime("%B %d, %Y")}')

    if:
    elif today.month == 12 and today.day == 25:
        print(f'🎅 !!Merry Christmas!! 🎄')

client.run(TOKEN)
