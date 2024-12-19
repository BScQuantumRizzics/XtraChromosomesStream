import discord
from discord.ext import commands

TOKEN = 'MTMxOTQ0MjU2NTkxNzA1Mjk3OQ.GbLu7t.3jdyJ79fje1tx3co4br2bw8JcMDn4XmVukyJos'

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
