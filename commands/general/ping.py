import discord
from discord.ext import commands


def setup(bot: commands.Bot) -> None:
    """Register the ping slash command."""

    @bot.tree.command(name="ping", description="Replies with Pong")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message("Pong!")
