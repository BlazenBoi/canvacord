|Discord| |PyPi| |Python|

A copy of `canvacord <https://www.npmjs.com/package/canvacord>`__ made
in python!

Table of contents
~~~~~~~~~~~~~~~~~

1. `Installation <#installation>`__
2. `Examples <#examples>`__
3. `Creating Images <#creating-images>`__
4. `Downloads <#links>`__

Installation
~~~~~~~~~~~~~~~~~

Run any of these commands in terminal:

Mac / Linux

::

    pip install canvacord

Windows

::

    python -m pip install canvacord

Examples
~~~~~~~~~~~~~~~~~

💡 This library requires
**`discord.py <https://github.com/Rapptz/discord.py>`__**.

Creating-Images
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
        image = await canvacord.rankcard(user=user, username=username, currentxp=currentxp, lastxp=lastxp, nextxp=nextxp, level=current_level, rank=current_rank, background=background, ranklevelsep="|", xpsep="/")
        file = discord.File(filename="rankcard.png", fp=image)
        await ctx.send(file=file)

    @client.command()
    async def welcomecard(ctx):
        image = await canvacord.welcomecard(user=ctx.author, background=None, avatarcolor="white", topcolor="white", bottomcolor="white", backgroundcolor="black", font=None, toptext="Welcome {user_name}!", bottomtext="Enjoy your stay in {server}!")
        file = discord.File(filename="welcomecard.png", fp=image)
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

    @client.comand()
    async def hitler(ctx):
        user = ctx.author
        image = await canvacord.hitler(user)
        file = discord.File(filename="hitler.png", fp=image)
        await ctx.send(file=file)

    @client.command()
    async def aborted(ctx):
        user = ctx.author
        image = await canvacord.aborted(user)
        file = discord.File(filename="aborted.png", fp=image)
        await ctx.send(file=file)

    @client.command()
    async def affect(ctx):
        user = ctx.author
        image = await canvacord.affect(user)
        file = discord.File(filename="affect.png", fp=image)
        await ctx.send(file=file)

    @client.command()
    async def airpods(ctx):
        user = ctx.author
        image = await canvacord.airpods(user)
        file = discord.File(filename="airpods.gif", fp=image)
        await ctx.send(file=file)

    @client.command()
    async def america(ctx):
        user = ctx.author
        image = await canvacord.america(user)
        file = discord.File(filename="america.gif", fp=image)
        await ctx.send(file=file)

    @client.command()
    async def wanted(ctx):
        user = ctx.author
        image = await canvacord.wanted(user)
        file = discord.File(filename="wanted.png", fp=image)
        await ctx.send(file=file)

    @client.command()
    async def joke(ctx):
        user = ctx.author
        image = await canvacord.jokeoverhead(user)
        file = discord.File(filename="jokeoverhead.png", fp=image)
        await ctx.send(file=file)

    @client.comand()
    async def spank(ctx):
        user1 = ctx.author
        user2 = ctx.author
        image = await canvacord.spank(user1, user2)
        file = discord.File(filename="spank.png", fp=image)
        await ctx.send(file=file)

    @client.comand()
    async def bed(ctx):
        user1 = ctx.author
        user2 = ctx.author
        image = await canvacord.bed(user1, user2)
        file = discord.File(filename="bed.png", fp=image)
        await ctx.send(file=file)
        
    client.run("BOT_TOKEN")

Links
~~~~~~~~~~~~~~~~~

|Discord| |PyPi|

Downloads
~~~~~~~~~~~~~~~~~

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
