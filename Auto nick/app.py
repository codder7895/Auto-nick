import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.channel.id == 1189510689849614366:
        member = message.guild.get_member(message.author.id)
        await member.edit(nick=message.content)

    await bot.process_commands(message)

bot.run(config.TOKEN)
