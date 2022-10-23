"""
client.get_channel(int) not working
"""
import logging
import os
from typing import Any

import discord
from discord import Intents, Message
from dotenv import load_dotenv


class DiscordBot(discord.Client):
    def __init__(self, *, intents: Intents, **options: Any) -> None:
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f"Logged in: {self.user}")

    async def on_message(self, message: Message):
        if message.author == self.user:
            return

        await message.channel.send("Hello World :^)")


def main():
    load_dotenv(".env")

    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise ValueError("Discord Token is not found D:")

    intents = discord.Intents.default()
    client = DiscordBot(intents=intents)

    handler = logging.FileHandler(
        filename="discord.log",
        encoding="utf-8",
        mode="w",
    )

    client.run(
        token,
        log_handler=handler,
        log_level=logging.DEBUG,
    )


if __name__ == "__main__":
    main()
