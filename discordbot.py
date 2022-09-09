from discord.ext import commands
from os import getenv
import traceback
import discord
from discord.ext import tasks
from datetime import datetime
from os import getenv 

bot = commands.Bot(command_prefix='/')
client = discord.Client()


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')



CHANNEL_ID = 998859031076675587

@tasks.loop(seconds=60)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('毎分投稿するぜー！')
    now = datetime.now().strftime('%H:%M')

    if now == '00:00':
        await channel.send('0:00だよ')
loop.start()


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
