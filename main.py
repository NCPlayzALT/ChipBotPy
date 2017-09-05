import discord
from discord.ext import commands
import random
import os

description = '''---CHIPBOT COMMANDS---'''
bot = commands.Bot(command_prefix='-', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if "luna" in message.content or "Luna" in message.content:
        await bot.send_message(message.channel, 'Luna? \U0001f440')
    if "Hello ChipBot!" in message.content:
        await bot.send_message(message.channel, 'Beep! Boop! I am ChipBot!')
    await bot.process_commands(message)

token = os.environ["TOKEN"]
bot.run(token)