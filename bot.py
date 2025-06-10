import discord
from discord.ext import commands

from config.settings import get_token
from commands.general import ping

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


# Register commands
ping.setup(bot)


if __name__ == "__main__":
    bot.run(get_token())
