from discord import *
from discord.ui import *
from discord.ext import *
from asyncio import *
from youtube_dl import *
from os import system

intents = Intents.default()
intents.message_content = True

bot = Bot(guild_ids=GUILDS, intents=intents)

voice_clients = {}

youtube_settings = {'format': 'bestaudio/best'}
ffmpeg_settings = {'options': '-vn'}

youtube = YoutubeDL(youtube_settings)

@bot.event
async def on_ready():
    print(f'{bot.user.display_name} Is Alive')

@bot.slash_command(name='suggestion',description='Suggest a new command', guild_ids=GUILDS)
async def command(ctx, suggestion: Option(str,'Suggestion Command',required=True)):
    try:
        await ctx.respond(f'Suggestion Noted')
        await bot.get_channel(SUGGESTION_CHANNEL).send(f'```{ctx.author.display_name} Suggested: \n{suggestion}```')
    except Exception as err:
        print(err)
        await ctx.respond(f'{ctx.author.display_name} An Error Occured Try Again If It Keeps Happening Report In /bug_report', ephemeral=True)

@bot.slash_command(name='bug_report',description='report a bug', guild_ids=GUILDS)
async def command(ctx, bug: Option(str,'Bug Description',required=True)):
    try:
        await ctx.respond(f'Bug Noted')
        await bot.get_channel(BUG_REPORT).send(f'```{ctx.author.display_name} Suggested: \n{bug}```')
    except Exception as err:
        print(err)
        await ctx.respond(f'{ctx.author.display_name} An Error Occured Try Again If It Keeps Happening Report In /bug_report', ephemeral=True)

@bot.slash_command(name='ty', description='Just Says Thank You', guild_ids=GUILDS)
async def command(ctx):
    try:
        await ctx.respond(f'Thank You {ctx.author.display_name}', ephemeral=True)
    except Exception as err:
        print(err)
        await ctx.respond(f'{ctx.author.display_name} An Error Occured Try Again If It Keeps Happening Report In /bug_report', ephemeral=True)

@bot.slash_command(name='connect', description='Connect Bot To A Voice Channel', guild_ids=GUILDS)
async def command(ctx):
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.respond(f'Connected To {channel}')
    except Exception as err:
        print(err)
        await ctx.respond(f'{ctx.author.display_name} An Error Occured Try Again If It Keeps Happening Report In /bug_report', ephemeral=True)

@bot.slash_command(name='disconnect', description='Disconnects From A Voice Channel', guild_ids=GUILDS)
async def command(ctx):
    try:
        await ctx.respond(f'Disconnected')
        await ctx.voice_client.disconnect()
    except Exception as err:
        print(err)
        await ctx.respond(f'{ctx.author.display_name} An Error Occured Try Again If It Keeps Happening Report In /bug_report', ephemeral=True)    

@bot.slash_command(name='youtube_play', description='Plays A Youtube Url', guild_ids=GUILDS)
async def command(ctx, youtube_link: Option(str,'Youtube Link',required=True)):
    try:
        await ctx.respond(f'{youtube_link} is now playing')

        url = youtube_link.content.split()[1]
        voice_clients[voice_client.guild.id] = voice_client

        loop = get_event_loop()
        data = await loop.run_in_executor(None, lambda: youtube.extract_info(url, download=False))

        song = data['url']
        player = FFmpegPCMAudio(song, **ffmpeg_settings)
        voice_client.play(player)
    except Exception as err:
        await ctx.respond(f'There Might Be A Problem With Your Url {youtube_link} If There Is Not Try Again \nIf It Keeps Happening Use /bug_report')
        print(err)

@bot.slash_command(name='pause',description='Pauses Music',guilds_ids=GUILDS)
async def command(ctx):
    try:
        await ctx.respond(f'Music Paused')
        voice_clients[ctx.guild.id].pause()
    except Exception as err:
        await ctx.send(f'{ctx.author.display_name} Sorry An Error Ocurred',ephemeral=True)
        print(err)

@bot.slash_command(name='resume',description='Pauses Music',guilds_ids=GUILDS)
async def command(ctx):
    try:
        await ctx.respond(f'Music Resumed')
        voice_clients[ctx.guild.id].resume()
    except Exception as err:
        await ctx.send(f'{ctx.author.display_name} Sorry An Error Ocurred',ephemeral=True)
        print(err)

@bot.slash_command(name='stop',description='Stops Music',guilds_ids=GUILDS)
async def command(ctx):
    try:
        await ctx.respond(f'Stopped The Music')
        voice_clients[ctx.guild.id].stop()
    except Exception as err:
        await ctx.send(f'{ctx.author.display_name} Sorry An Error Ocurred',ephemeral=True)
        print(err)

try:
    bot.run(TOKEN)
except:
    print('Error Now Rebooting')
    system('kill 1')
    system('python3 restarter.py')
    
