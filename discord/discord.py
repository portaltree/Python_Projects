# -*- coding: utf-8 -*-
# pip install
# discord.py
import nest_asyncio
from discord.ext import commands
import discord
nest_asyncio.apply()

i = 0

bot = commands.Bot(command_prefix='.')

@bot.command()
async def spam(ctx, message, amount:int, *, user: discord.User):
    for i in range(amount):
        await user.send(message)

bot.run('YOUR_DISCORD_TOKEN')
