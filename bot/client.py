import asyncio
import logging
import os
import sys
from typing import List

import discord
from cogwatch import watch
from discord.ext import commands
from dotenv import load_dotenv

try:
    import uvloop
except ImportError:
    uvloop = None

logging.basicConfig(level=logging.INFO)

if sys.platform in {'linux', 'macos'}:
    uvloop.install()
    logging.info('Using `uvloop` asyncio event loop.')

load_dotenv()


class BotClient(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=self._check_prefix,
            case_insensitive=True,
            owner_id=os.getenv('OWNER_ID'),
            help_command=None,
        ),

    @staticmethod
    async def _check_prefix(client: commands.Bot, message: discord.Message) -> List[str]:
        if message.guild is None:
            return commands.when_mentioned_or(*[os.getenv('PREFIX'), ''])(client, message)
        else:
            return commands.when_mentioned_or(*[os.getenv('PREFIX')])(client, message)

    @watch(path='bot/commands', preload=True)
    async def on_ready(self):
        logging.info('Bot ready.')

    async def on_message(self, message: discord.Message):
        logging.info(message)

        if message.author.bot:
            return

        await self.process_commands(message)


async def main():
    client = BotClient()
    await client.start(os.getenv('BOT_TOKEN'))


def __poetry_run():
    asyncio.run(main())
