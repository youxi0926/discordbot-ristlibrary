import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = getenv('DISCORD_BOT_TOKEN) #トークン
CHANNEL_ID = 998859031076675587 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()
# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("毎分投稿するぜー！")
    now = datetime.now().strftime('%H:%M')

    if now == '00:00':
        await channel.send('0:00だよ')  
#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
