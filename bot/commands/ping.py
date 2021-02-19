from discord.ext import commands
from bot.client import BotClient


class Ping(commands.Cog):
    def __init__(self, client: BotClient):
        self.client = client

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.reply('Pong!')


def setup(client: BotClient):
    client.add_cog(Ping(client))
