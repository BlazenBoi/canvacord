from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = """[![Discord](https://discord.com/api/guilds/872291125547921459/embed.png)](https://discord.gg/mPU3HybBs9)
[![PyPi](https://img.shields.io/pypi/v/canvacord.svg)](https://pypi.org/project/canvacord)
[![Python](https://img.shields.io/pypi/pyversions/dislash.py.svg)](https://pypi.python.org/pypi/canvacord)

A copy of [canvacord](https://www.npmjs.com/package/canvacord) made in python!



# Table of contents
1. [Installation](#installation)
2. [Examples](#examples)
3. [Creating Images](#creating-images)
4. [Links](#links)
5. [Downloads](#downloads)

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


## Creating-Images

```python
import discord
from discord.ext import commands
import canvacord

client = commands.Bot(command_prefix="!")

@client.command()
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
    
@client.command()
async def triggered(ctx):
    user = ctx.author
    image = await canvacord.trigger(user)
    file = discord.File(filename="triggered.gif", fp=image)
    await ctx.send(file=file)

@client.command()
async def communism(ctx):
    user = ctx.author
    image = await canvacord.communism(user)
    file = discord.File(filename="communism.gif", fp=image)
    await ctx.send(file=file)

@client.command()
async def jail(ctx):
    user = ctx.author
    image = await canvacord.jail(user)
    file = discord.File(filename="jail.png", fp=image)
    await ctx.send(file=file)

@client.command()
async def gay(ctx):
    user = ctx.author
    image = await canvacord.gay(user)
    file = discord.File(filename="gay.png", fp=image)
    await ctx.send(file=file)

@client.command()
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

@client.command()
async def spank(ctx):
    user1 = ctx.author
    user2 = ctx.author
    image = await canvacord.spank(user1, user2)
    file = discord.File(filename="spank.png", fp=image)
    await ctx.send(file=file)

@client.command()
async def bed(ctx):
    user1 = ctx.author
    user2 = ctx.author
    image = await canvacord.bed(user1, user2)
    file = discord.File(filename="bed.png", fp=image)
    await ctx.send(file=file)
    
client.run("BOT_TOKEN")
```


# Links
[![Discord](https://discord.com/api/guilds/872291125547921459/embed.png)](https://discord.gg/mPU3HybBs9)
[![PyPi](https://img.shields.io/pypi/v/canvacord.svg)](https://pypi.org/project/canvacord)


# Downloads


[![Downloads](https://pepy.tech/badge/canvacord)](https://pepy.tech/project/canvacord)
[![Downloads](https://pepy.tech/badge/canvacord/month)](https://pepy.tech/project/canvacord)
![Downloads](https://pepy.tech/badge/canvacord/week)
"""

with open('src/canvacord/__init__.py', 'r') as f:
    version = [line.split('=')[1].strip(" '\"") for line in f.read().splitlines() if line.startswith('__version__')][0]

setup(
    name='canvacord',
    version=version,
    description='A Python Version of Canvacord',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/BlazenBoi/canvacord.py/issues',
    author='Blazen',
    author_email='contact@fireballbot.com',
    keywords='canvacord, rankcard, image manipulation, meme, discord, discordpy, discord-py',
    packages=find_packages(include=['canvacord']),
    python_requires='>=3.6',
    install_requires=[
    "setuptools>=42",
    "wheel",
    "pillow",
    "discord",
    "disnake",
    "datetime",
    "requests",
    "colour"
    ],
    project_urls={
        'Discord Server': 'https://discord.com/invite/mPU3HybBs9',
        'Bug Tracker': 'https://github.com/BlazenBoi/canvacord.py/issues',
        'Source': 'https://github.com/BlazenBoi/canvacord',
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
#© 2021 GitHub, Inc.