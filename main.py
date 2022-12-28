import os
import asyncio
import discord
from discord.ext import commands
from boto.s3.connection import S3Connection

bot = commands.Bot(command_prefix="¿", intents=discord.Intents.all())

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

TOKEN = S3Connection(os.environ["TOKEN"])

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

@bot.event
async def on_ready():
    print("Bot is ready.")

asyncio.run(main())
