import os
import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="¿", intents=discord.Intents.all())

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start("ODkxNDI4NDE0ODE1MzQyNjQz.GfECn1._0zI3CaZYzv2eLgvqWpjKRe4RugSV0vaTMujxA")


@bot.event
async def on_ready():
    print("Bot is ready.")

asyncio.run(main())
