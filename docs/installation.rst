============
Installation
============

Install the package with pip::

.. code-block:: python

    from discord.ext import commands
    from dislash import *

    bot = commands.Bot(command_prefix="!")
    slash = SlashClient(bot)

    @slash.command(description="Sends Hello")
    async def hello(interaction):
        await interaction.reply("Hello!")
    
    bot.run("BOT_TOKEN")

    $ pip install read-the-docs-template
