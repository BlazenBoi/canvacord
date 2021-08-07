============
Installation
============

Install the package with pip::

Mac / Linux

    $ pip install canvacord


Windows

    $ python -m pip install canvacord

.. code-block:: python

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

.. seealso::
