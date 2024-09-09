import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    # 監視するチャンネルのID
    target_channel_id = 1121209665808781384  # ここにチャンネルのIDを入力

    # メッセージが監視対象のチャンネルで送信された場合
    if message.channel.id == target_channel_id and len(message.content) >= 5:
        # メンバーに「下忍」ロールを付与
        member = message.author
        guild = message.guild
        role = discord.utils.get(guild.roles, name='下忍')
        await member.add_roles(role)

    await bot.process_commands(message)

# Botのトークンを設定
bot.run('MTI4MjYwNjEwMTU4OTkxNzc0OA.GK6ANi.zuA_inkZrCJpXcupENZw42o7g8gO_8HxTD4mS8')
