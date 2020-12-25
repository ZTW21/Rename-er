# bot.py
import os
import threading
from datetime import *
import discord
from dotenv import load_dotenv
import holidays

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()
today = date.today()
date_str = today.strftime("%d/%m/%Y")
us_holidays = holidays.US()


def change_channel_name():
    if today.month == 1 and today.day == 1:
        new_name = '🧨Happy New Years🎍'
    elif today.month == 2 and today.day == 14:
        new_name = '💝Happy Valentines day💌'
    elif today.month == 7 and today.day == 4:
        new_name = '🧨Forth_of_July🧨'
    elif today.month == 12 and today.day == 24:
        new_name = '🎄Christmas_Eve🎄'
    elif today.month == 12 and today.day == 25:
        new_name = '🎅Merry_Christmas🎄'
    elif today.month == 12 and today.day == 31:
        new_name = '🧨New_Years_Eve🧨'
    else:
        if date(date_str) in us_holidays:
            new_name = us_holidays.get(date_str)
        else:
            new_name = date_str

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
