import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random

#https://discord.com/oauth2/authorize?client_id=1319442565917052979&permissions=1689917160110144&integration_type=0&scope=applications.commands+bot

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
  print(f"Bot is ready! Logged in as {bot.user} (ID: {bot.user.id})")

@bot.command()
async def roast(ctx, user: discord.Member = None):
  list_of_insults = open("Insults.txt" , "r")
  content = insults.readlines()
  insult = content[random.randint(0, len(content)-1)].strip().upper()
  if user:
    await ctx.send(f"{user.mention}: {insult}")
  else:
    await ctx.send(f"{user.mention}: Erm, what the sigma? You\'re missing a parameter!")

bot.run(TOKEN)
