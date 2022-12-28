from webserver import keep_alive
import os
import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="¿", intents=discord.Intents.all())

my_secret = os.environ['TOKEN']


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(my_secret)


@bot.event
async def on_ready():
    print("Bot is ready.")


keep_alive()

asyncio.run(main())
