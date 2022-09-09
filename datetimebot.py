import discord
from discord.ext import tasks
from datetime import datetime
from os import getenv 

TOKEN = getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = 998859031076675587
client = discord.Client()
@tasks.loop(seconds=60)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('毎分投稿するぜー！')
    now = datetime.now().strftime('%H:%M')

    if now == '00:00':
        await channel.send('0:00だよ')
loop.start()
client.run(TOKEN)
