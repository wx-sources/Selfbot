import os
import discord
from discord.ext import commands
import asyncio

TOKEN = os.environ.get("Token_do_executor")

bot = commands.Bot(command_prefix=".", self_bot=True)

@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")

@bot.command(name="print")
async def print_command(ctx):
    for _ in range(50):
        await ctx.send("https://discord.gg/vFyYuxNe\n# NOSSA COMUNIDADE VENCEU")
        await asyncio.sleep(1)  # Delay para evitar spam muito rápido

bot.run(TOKEN, bot=False)