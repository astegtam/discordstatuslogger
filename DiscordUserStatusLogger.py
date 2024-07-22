import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

target_user_id =  # The persons USER ID that u want to check
bot_owner_id =  # The persons USER ID that u want to get messages
target_guild_id =  # The servers ID that the bot is in

@bot.event
async def on_ready():
    print(f'Bot {bot.user} successfully logged in!')
    check_user_status.start()  # Start the loop that checks the user status
    owner = bot.get_user(bot_owner_id)
    await owner.send('Status logger started! ')

@tasks.loop(minutes=1)  # Check every 1 munite
async def check_user_status():
    guild = bot.get_guild(target_guild_id)
    if guild:
        target_member = guild.get_member(target_user_id)
        if target_member:
            if target_member.status != discord.Status.offline:
                owner = bot.get_user(bot_owner_id)
                if owner:
                    await owner.send(f'{target_member.name} now is online!')

bot.run('WRITE BOT TOKEN HERE!')
