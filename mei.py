import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()

client = commands.Bot(command_prefix = '/', intents=intents)

@client.event
async def on_ready():
    activity = discord.Activity(name="мемуры", type=discord.ActivityType.listening)
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

client.run(TOKEN)