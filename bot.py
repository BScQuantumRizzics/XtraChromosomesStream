import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

bot = dommands.Bot(command_prefix="/")

@bot.event
async def on_ready():
  print(f"Bot is ready! Logged in as {bot.user} (ID: {bot.user.id})")

@bot.command()
async def roast(ctx, user: discord.Member = None):
  if user:
    await ctx.send("Nigger")
  else:
    await ctx.send("Big Black Cock)

bot.run(TOKEN)
