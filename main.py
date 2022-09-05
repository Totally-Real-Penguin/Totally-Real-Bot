from discord import *
from discord.ui import *
from discord.ext import *
from asyncio import *
from youtube_dl import *
from config import *
from os import system

intents = Intents.default()
intents.message_content = True

bot = Bot(guild_ids=GUILDS, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.display_name} Is Alive')

@bot.slash_command(name='suggestion',description='Suggest a new command', guild_ids=GUILDS)
async def command(ctx, suggestion: Option(str,'Suggestion Command',required=True)):
    try:
        await ctx.respond(f'Suggestion Noted')
        await bot.get_channel(SUGGESTION_CHANNEL).send(f'```{ctx.author.display_name} Suggested: \n{suggestion}```')
    except:
        await ctx.respond(f'{ctx.author.display_name} An Error Occured Try Again If It Keeps Happening Report In /bug_report', ephemeral=True)

@bot.slash_command(name='bug_report',description='report a bug', guild_ids=GUILDS)
async def command(ctx, bug: Option(str,'Bug Description',required=True)):
    try:
        await ctx.respond(f'Bug Noted')
        await bot.get_channel(SUGGESTION_CHANNEL).send(f'```{ctx.author.display_name} Suggested: \n{bug}```')
    except:
        await ctx.respond(f'{ctx.author.display_name} An Error Occured Try Again If It Keeps Happening Report In /bug_report', ephemeral=True)

@bot.slash_command(name='ty', description='Just Says Thank You', guild_ids=GUILDS)
async def command(ctx):
    try:
        await ctx.respond(f'Thank You {ctx.author.display_name}', ephemeral=True)
    except:
        await ctx.respond(f'{ctx.author.display_name} An Error Occured Try Again If It Keeps Happening Report In /bug_report', ephemeral=True)

@bot.slash_command(name='connect', description='Connect Bot To A Voice Channel', guild_ids=GUILDS)
async def command(ctx):
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.respond(f'Connected To {channel}')
    except:
        await ctx.respond(f'{ctx.author.display_name} An Error Occured Try Again If It Keeps Happening Report In /bug_report', ephemeral=True)

@bot.slash_command(name='disconnect', description='Disconnects From A Voice Channel', guild_ids=GUILDS)
async def command(ctx):
    try:
        await ctx.respond(f'Disconnected')
        await ctx.voice_client.disconnect()
    except:
        await ctx.respond(f'{ctx.author.display_name} An Error Occured Try Again If It Keeps Happening Report In /bug_report', ephemeral=True)    

try:
    bot.run(TOKEN)
except:
    print('Error Now Rebooting')
    system('kill 1')
    system('python3 restarter.py')
    
