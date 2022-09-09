import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "**********" #トークン
CHANNEL_ID = "**********" #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
