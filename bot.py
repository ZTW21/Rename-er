# bot.py
import os
import threading
from datetime import *
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()
today = date.today()


def change_channel_name():
    if today.month == 1 and today.day == 1:
        new_name = '🧨 Happy New Years 🎍'
    elif today.month == 2 and today.day == 14:
        new_name = '💝 Happy Valentines day 💌'
    elif today.month == 7 and today.day == 4:
        new_name = '🧨 Forth of July 🧨'
    elif today.month == 12 and today.day == 24:
        new_name = '🎄 Christmas Eve 🎄'
    elif today.month == 12 and today.day == 25:
        new_name = '🎅 Merry Christmas 🎄'
    elif today.month == 12 and today.day == 31:
        new_name = '🧨 New Years Eve 🧨'
    else:
        new_name = today.strftime("%B %d, %Y")

    return new_name


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} has connected to Discord!')

    threading.Timer(1, change_channel_name).start()

    print(f'Today\'s date: {today.strftime("%B %d, %Y")}')

    channel_id = client.get_channel(181483365155864588)
    await channel_id.edit(name=change_channel_name())


client.run(TOKEN)
