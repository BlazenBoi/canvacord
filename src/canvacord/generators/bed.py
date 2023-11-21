from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageColor
import asyncio
import aiohttp
from random import randint
from io import BytesIO
import discord
from typing import Union

async def getavatar(user: Union[discord.User, discord.Member]) -> bytes:
    session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
    disver = str(discord.__version__)
    if disver.startswith("1"):
        async with session.get(str(user.avatar_url)) as response:
            avatarbytes = await response.read()
        await session.close()
    elif disver.startswith("2"):
        async with session.get(str(user.display_avatar.url)) as response:
            avatarbytes = await response.read()
        await session.close()
    return avatarbytes

async def getbackground(background):
    session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
    async with session.get("https://cdn.glitch.com/dff50ce1-3805-4fdb-a7a5-8cabd5e53756%2Fbed.bmp?v=1628443911219") as response:
        backgroundbytes = await response.read()
    await session.close()
    return backgroundbytes

async def bed(user1, user2):
        avatar = Image.open(BytesIO(await getavatar(user1))).resize((100, 100)).convert('RGBA')
        avatar2 = Image.open(BytesIO(await getavatar(user2))).resize((70, 70)).convert('RGBA')
        base = Image.open(BytesIO(await getbackground("bed"))).convert('RGBA')
        avatar_small = avatar.copy().resize((70, 70))
        base.paste(avatar, (25, 100), avatar)
        base.paste(avatar, (25, 300), avatar)
        base.paste(avatar_small, (53, 450), avatar_small)
        base.paste(avatar2, (53, 575), avatar2)
        base = base.convert('RGBA')

        b = BytesIO()
        base.save(b, format='png')
        b.seek(0)
        return b