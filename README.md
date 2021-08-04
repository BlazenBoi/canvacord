[![Discord](https://discord.com/api/guilds/872291125547921459/embed.png)](https://discord.gg/mPU3HybBs9)
[![PyPi](https://img.shields.io/pypi/v/canvacord.svg)](https://pypi.org/project/canvacord)
[![Python](https://img.shields.io/pypi/pyversions/dislash.py.svg)](https://pypi.python.org/pypi/canvacord)

A copy of [canvacord](https://www.npmjs.com/package/canvacord) made in python!


# Installation

Run any of these commands in terminal:

Mac / Linux
```
pip install canvacord
```

Windows
```
python -m pip install canvacord
```

# Examples
💡 This library requires **[discord.py](https://github.com/Rapptz/discord.py)**.


## Creating a Rank Card

```python
import discord
from discord.ext import commands
from canvacord import rankcard

client = commands.Bot(command_prefix="!")

@client.comand()
async def test(ctx):
    user = ctx.author
    username = ctx.author.name + "#" + ctx.author.discriminator
    currentxp = 1
    lastxp = 0
    nextxp = 2
    current_level = 1
    current_rank = 1
    background = None
    image = await rankcard(user=user, username=username, currentxp=currentxp, lastxp=lastxp, nextxp=nextxp, level=current_level, rank=current_rank, background=background)
    file = discord.File(filename="rankcard.png", fp=image)
    await ctx.send(file=file)
    

client.run("BOT_TOKEN")
```


# Links
- **[PyPi](https://pypi.org/project/canvacord)**
- **[Our Discord](https://discord.gg/mPU3HybBs9)**


# Downloads


[![Downloads](https://pepy.tech/badge/canvacord)](https://pepy.tech/project/canvacord)
[![Downloads](https://pepy.tech/badge/canvacord/month)](https://pepy.tech/project/canvacord)
![Downloads](https://pepy.tech/badge/canvacord/week)