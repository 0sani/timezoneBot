import discord
from discord.ext import commands
from datetime import datetime 

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print(f"Bot started at {datetime.now()}")

@client.command()
async def timezone(ctx, tz):
    current = ctx.author.display_name

    if (len(tz) != 3):
        return
    await ctx.author.edit(nick=current[:26]+" ["+tz.upper()+"]")
    await ctx.send("Added timezone")
    print(f"Changed {ctx.author.name}'s timezone to {tz.upper()}")

client.run("TOKEN")
