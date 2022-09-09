import discord
from discord.exe import tasks
from datetime import datetime 

TOKEN = "**********" #トークン
CHANNEL_ID = ********** #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '00:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('0:00だよ')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
