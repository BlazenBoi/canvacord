|Discord| |PyPi| |Python|

A copy of `canvacord <https://www.npmjs.com/package/canvacord>`__ made
in python!

Installation
============

Run any of these commands in terminal:

Mac / Linux

::

    pip install canvacord

Windows

::

    python -m pip install canvacord

Examples
========

💡 This library requires
**`discord.py <https://github.com/Rapptz/discord.py>`__**.

Creating Images
---------------

.. code:: python

    import discord
    from discord.ext import commands
    import canvacord

    client = commands.Bot(command_prefix="!")

    @client.comand()
    async def rankcard(ctx):
        user = ctx.author
        username = ctx.author.name + "#" + ctx.author.discriminator
        currentxp = 1
        lastxp = 0
        nextxp = 2
        current_level = 1
        current_rank = 1
        background = None
        image = await canvacord.rankcard(user=user, username=username, currentxp=currentxp, lastxp=lastxp, nextxp=nextxp, level=current_level, rank=current_rank, background=background)
        file = discord.File(filename="rankcard.png", fp=image)
        await ctx.send(file=file)

    @client.comand()
    async def triggered(ctx):
        user = ctx.author
        image = await canvacord.trigger(user)
        file = discord.File(filename="triggered.gif", fp=image)
        await ctx.send(file=file)

    @client.comand()
    async def communism(ctx):
        user = ctx.author
        image = await canvacord.communism(user)
        file = discord.File(filename="communism.gif", fp=image)
        await ctx.send(file=file)

    @client.comand()
    async def jail(ctx):
        user = ctx.author
        image = await canvacord.jail(user)
        file = discord.File(filename="jail.png", fp=image)
        await ctx.send(file=file)

    @client.comand()
    async def gay(ctx):
        user = ctx.author
        image = await canvacord.gay(user)
        file = discord.File(filename="gay.png", fp=image)
        await ctx.send(file=file)
        
    client.run("BOT_TOKEN")

Links
=====

-  **`PyPi <https://pypi.org/project/canvacord>`__**
-  **`Our Discord <https://discord.gg/mPU3HybBs9>`__**

Downloads
=========

|Downloads| |Downloads| |Downloads|

.. |Discord| image:: https://discord.com/api/guilds/872291125547921459/embed.png
   :target: https://discord.gg/mPU3HybBs9
.. |PyPi| image:: https://img.shields.io/pypi/v/canvacord.svg
   :target: https://pypi.org/project/canvacord
.. |Python| image:: https://img.shields.io/pypi/pyversions/dislash.py.svg
   :target: https://pypi.python.org/pypi/canvacord
.. |Downloads| image:: https://pepy.tech/badge/canvacord
   :target: https://pepy.tech/project/canvacord
.. |Downloads| image:: https://pepy.tech/badge/canvacord/month
   :target: https://pepy.tech/project/canvacord
.. |Downloads| image:: https://pepy.tech/badge/canvacord/week
